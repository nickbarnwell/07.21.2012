import random
import math
import defaultdict

def _get_centroid(points):
	pass

def _dist(lat1, lon1, lat2, lon2):
	return math.sqrt((lat1 - lat2) ** 2 + (lon1 - lon2) ** 2)

def _iterate_k_means(nearby, k, means, last_clusters):
	for uid, loc in nearby:
		closest_mean = None
		for mean in means:
			dist = _dist(loc, mean)
			if not closest_mean:
				closest_mean = mean
			elif _dist(loc, closest_mean) > _dist(loc, mean):
				closest_mean = mean
		clusters[closest_mean].add((uid, loc))
	new_means = [_get_centroid(cluster) for cluster in clusters.values()]
	return new_means, clusters.values()

def kmeans(nearby, k):
	''' Runs full kmeans on nearby with the given k. Returns the clusters. '''
	# Choose k random initial means
	lats = [lat for uid, (lat, lon) in nearby]
	lons = [lon for uid, (lat, lon) in nearby]
	pick_rand = lambda l : random.random * (max(l) - min(l)) + min(l)
	means = [(pick_rand(lats), pick_rand(lons)) for i in range(k)]
	clusters = defaultdict(set)
	# repeatedly cluster until convergence
	for i in range(c.MAX_K_MEANS_ITERATIONS):
		new_means, new_clusters = _iterate_k_means(nearby, k, means, clusters)
		if new_clusters != clusters:
			means = new_means
			clusters = new_clusters
		else:
			break
	return clusters

def cross_validate(clusters, k):
	''' Reclusters a subset of the point in clusters and compares the
		memberships to the full clustering. The 1 - the fraction of
		points that changed membership is the returned score. '''
	clusters_copy = list(clusters)
	subset_size = len(clusters) / 2
	subset = []
	while len(subset) < subset_size:
		rand_index = random.randint(0, len(clusters_copy) - 1)
		cluster = clusters_copy[rand_index]
		subset.append(cluster)
		del clusters_copy[rand_index]
	subset_clusters = kmeans(subset, k)
	


def main(nearby):
	''' Takes a a list of (uid, (lat, lon)) pairs sorted in increasing
		distance from the target user (the first uid).
		Returns the cluster that the target user belongs to. '''
	if len(nearby) < c.MIN_SIZE_TO_CLUSTER:
		best_clustering = (None, 0)
		for k in range(2, c.MAX_CLUSTERS):
			clusters = kmeans(nearby, k)
			score = cross_validate(clusters, k)
			if score > best_cluster[1]:
				best_clustering = (cluster, score)
		target_user = nearby[0]
		for cluster in best_clustering[1]:
			if target_user in cluster:
				return cluster
	#fall back to showing everyone
	return nearby