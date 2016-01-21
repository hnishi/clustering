#!/
# kmeansnishi3d.py 
print "kmeansnishi3d.py v1.0"

import sys
import numpy as np
from optparse import OptionParser

##### FOR KMEANS CLUSTERING
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.cluster import MeanShift
from sklearn.datasets import make_blobs

############ argument ##############
parser = OptionParser

def get_options():
   p = OptionParser()
   p.add_option('--i-data3d', dest='fn_data3d',
                help="file name for 3d data")
   p.add_option('--o-cluster', dest='fn_cluster',
                help="file name for result of clustering")
   p.add_option('--p-num', dest='prm_num',
                help="parameter for the number of cluster")
   opts, args = p.parse_args()
   print "----------------------------"
   p.print_help()
   print "----------------------------"
   return opts, args

############ main ##############

##### READING SECTION
opts, args = get_options()

fn_data3d = 'data3d.dat'
if opts.fn_data3d:         
   fn_data3d = opts.fn_data3d
f = open(fn_data3d,'r')

prm_num = int(2)
if opts.prm_num:         
   prm_num = int(opts.prm_num)

c1 = []
pot = []
for line in f:
    c1.append(line.split()[0])
    c1.append(line.split()[1])
    c1.append(line.split()[2])
    pot.append(line.split()[3])
f.close()

c1 = np.array(c1,dtype=float)
c1 = c1.reshape(len(c1)/3,3)

print c1

##### KMEANS CLUSTERING
y_pred = KMeans(n_clusters=prm_num).fit_predict(c1)
print y_pred

##### OUTPUT PC COORDINATES OF ALL STRUCTURES  
fn_cluster = 'cluster.dat'
if opts.fn_cluster:
   fn_cluster = opts.fn_cluster
output = open(fn_cluster,'w')
for i, j in enumerate(c1):
   print >> output, j[0], j[1],j[2],pot[i], y_pred[i]
output.close()

