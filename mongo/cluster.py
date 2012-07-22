import random
import math
from collections import defaultdict
import common as c

def _get_centroid(events):
	lats = [lat for uid, (lat, lon) in events]
	lons = [lon for uid, (lat, lon) in events]
	average = lambda l : sum(l) / len(l)
	return ((average(lats), average(lons)))


def _dist((lat1, lon1), (lat2, lon2)):
	return math.sqrt((lat1 - lat2) ** 2 + (lon1 - lon2) ** 2)

def _iterate_k_means(nearby, k, means):
	clusters_dict = defaultdict(set)
	for uid, loc in nearby:
		closest_mean = None
		for mean in means:
			dist = _dist(loc, mean)
			if not closest_mean:
				closest_mean = mean
			elif _dist(loc, closest_mean) > _dist(loc, mean):
				closest_mean = mean
		clusters_dict[closest_mean].add((uid, tuple(loc)))
	clusters = set([frozenset(cluster) for cluster in clusters_dict.values()])
	new_means = [_get_centroid(cluster) for cluster in clusters]
	return new_means, clusters

def kmeans(nearby, k):
	''' Runs full kmeans on nearby with the given k. Returns the clusters. '''
	# Choose k random initial means
	lats = [lat for uid, (lat, lon) in nearby]
	lons = [lon for uid, (lat, lon) in nearby]
	pick_rand = lambda l : random.random() * (max(l) - min(l)) + min(l)
	means = [(pick_rand(lats), pick_rand(lons)) for i in range(k)]
	clusters = None
	# repeatedly cluster until convergence
	for i in range(c.MAX_K_MEANS_ITERATIONS):
		new_means, new_clusters = _iterate_k_means(nearby, k, means)
		if new_clusters != clusters:
			means = new_means
			clusters = new_clusters
		else:
			break
	return clusters

def cross_validate(clusters, k):
	''' Reclusters a subset of the points in clusters and compares the
		memberships to the full clustering. Retuns a score proportional
		to the changes in clustering found. '''
	clusters_copy = list(clusters)
	subset_size = len(clusters) / 2
	subset = []
	while len(subset) < subset_size:
		rand_index = random.randint(0, len(clusters_copy) - 1)
		cluster = clusters_copy[rand_index]
		subset.append(cluster)
		del clusters_copy[rand_index]
	print subset
	subset_clusters = kmeans(subset, k)
	min_diff = lambda c : min([len(c.symmetric_difference(c2)) for c2 in subset_clusters])
	return sum([min_diff(c) for c in clusters])

def get_cluster(nearby):
	''' Takes a a list of (uid, (lat, lon)) pairs sorted in increasing
		distance from the target user (the first uid).
		Returns the cluster that the target user belongs to. '''
	if len(nearby) < c.MIN_SIZE_TO_CLUSTER:
		best_clustering = (None, 99999999)
		for k in range(2, c.MAX_CLUSTERS):
			clusters = kmeans(nearby, k)
			score = cross_validate(clusters, k)
			if score < best_cluster[1]:
				best_clustering = (cluster, score)
		target_user = nearby[0]
		for cluster in best_clustering[1]:
			if cluster and target_user in cluster:
				return cluster
	#fall back to showing everyone
	return nearby