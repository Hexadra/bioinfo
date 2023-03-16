## 脚本文件     
```
#!/bin/bash 
dir="./bash_homework" 
echo -e "\c" > dirname.txt 
echo -e "\c" > filenames.txt 
for temp in $(ls $dir | cat)  
do 
	Path=$(echo "${dir}/${temp}") 
	# 指向目标文件夹下文件
	if [ -d $Path ] 
	then 
		echo "$temp" >> dirname.txt 
	elif [ -f $Path ] 
	then 
		echo "$temp" >> filenames.txt 
	fi 
done 
exit 1 
```

## filename    
```
a1.txt
a.txt
b1.txt
bam_wig.sh
b.filter_random.pl
c1.txt
chrom.size
c.txt
d1.txt
dir.txt
e1.txt
f1.txt
human_geneExp.txt
if.sh
image
insitiue.txt
mouse_geneExp.txt
name.txt
number.sh
out.bw
random.sh
read.sh
test3.sh
test4.sh
test.sh
test.txt
wigToBigWig
```


## dirname    
```
a-docker
app
backup
bin
biosoft
c1-RBPanno
datatable
db
download
e-annotation
exRNA
genome
git
highcharts
home
hub29
ibme
l-lwl
map2
mljs
module
mogproject
node_modules
perl5
postar2
postar_app
postar.docker
RBP_map
rout
script
script_backup
software
tcga
test
tmp
tmp_script
var
x-rbp
```
