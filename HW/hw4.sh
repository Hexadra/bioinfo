#!/bin/bash
# input
file=hw4_2_seq.fa
touch ${file}
s="MSTRSVSSSSYRRMFGGPGTASRPSSSRSYVTTSTRTYSLGSALRPSTSRSLYASSPGGVYATRSSAVRL"

init=0
len=${#s}
ter=${len-1}

# Shuffle
for i in {1..10}
do
	shuffled=""
	# Generate random seq of num
	for j in `seq $init $ter | shuf`;
	do
		shuffled=$shuffled${s:$j:1}
	done
	echo '>shuffled'$i >> ${file}
	echo $shuffled >> ${file}
done
blastp -query ${file} -subject ${file} -out hw4_result
