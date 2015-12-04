#!/bin/bash

python kmeansnishi.py \
   --i-data2d file_3_ext.dat \
   --p-num 2 \
   --o-cluster cluster.dat

exit

for i in {1..2}
do
   python prjnishi.py \
      --i-trj coord.dat \
      --i-ave aveq.dat \
      --i-egv e${i}.dat \
      --o-pcc c${i}.dat
done

paste c1.dat c2.dat > out.dat
