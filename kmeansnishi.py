#!/
# kmeansnishi.py v 1.0

import sys
import numpy as np
from optparse import OptionParser

##### FOR KMEANS CLUSTERING
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

############ argument ##############
parser = OptionParser

def get_options():
   p = OptionParser()
   p.add_option('--i-data2d', dest='fn_data2d',
                help="file name for 2d data")
   p.add_option('--o-cluster', dest='fn_cluster',
                help="file name for result of clustering")
   opts, args = p.parse_args()
   print "----------------------------"
   p.print_help()
   print "----------------------------"
   return opts, args

############ main ##############
print "kmeansnishi.py"

##### READING SECTION
opts, args = get_options()

fn_data2d = 'data2d.dat'
if opts.fn_data2d:         
   fn_data2d = opts.fn_data2d
f = open(fn_data2d,'r')
#c1 = np.array(f.readline().split(),dtype=float)
c1 = []
for line in f:
    c1.append(line.split()[0])
    c1.append(line.split()[1])
f.close()

c1 = np.array(c1,dtype=float)
c1 = c1.reshape(len(c1)/2,2)

print c1

##### KMEANS CLUSTERING
y_pred = KMeans(n_clusters=2).fit_predict(c1)
print y_pred

##### OUTPUT PC COORDINATES OF ALL STRUCTURES  
fn_cluster = 'cluster.dat'
if opts.fn_cluster:
   fn_cluster = opts.fn_cluster
output = open(fn_cluster,'w')
for i, j in enumerate(c1):
   print >> output, j[0], j[1], y_pred[i]
output.close()

