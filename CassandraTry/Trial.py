from cassandra.cluster import Cluster
__author__ = 'f'


cluster = Cluster()
session = cluster.connect('mykeyspace')