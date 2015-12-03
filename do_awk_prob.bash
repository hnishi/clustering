#!/bin/bash

#awk '{if($4>0){print $1,$2}}' $1 |less
awk '{if($4>0){print $1,$2,$3}}' prob.dat > file_3_ext.dat
