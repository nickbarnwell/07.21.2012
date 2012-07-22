def _get_centroid(points):
	pass

def kmeans(nearby, k):
	''' Runs full kmeans on nearby with the given k. Returns the clusters. '''
	#Choose k random initial means
	points = [loc for loc in ]

def cross_validate(clusters):
	''' Reclusters a subset of the point in clusters and compares the
		memberships to the full clustering. The 1 - the fraction of
		points that changed membership is the returned score. '''



def main(nearby):
	''' Takes a a list of (uid, (lat, lon)) pairs sorted in increasing
		distance from the target user (the first uid).
		Returns the cluster that the target user belongs to. '''
	if len(nearby) < c.MIN_SIZE_TO_CLUSTER:
		best_clustering = (None, 0)
		for k in range(2, c.MAX_CLUSTERS):
			clusters = kmeans(nearby, k)
			score = cross_validate(clusters)
			if score > best_cluster[1]:
				best_clustering = (cluster, score)
		target_user = nearby[0]
		for cluster in best_clustering[1]:
			if target_user in cluster:
				return cluster
	#fall back to showing everyone
	return nearby