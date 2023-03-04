## HW2   

**1. 列出1.gtf文件中 XI 号染色体上的后 10 个 CDS （按照每个CDS终止位置的基因组坐标进行sort）。**            

grep -v '^#' 1.gtf |awk '$1 == "XI" && $3 =="CDS" {name=$10;gsub("\"", "", name);print name, $4, $5}'| sort -nk 5 | tail -n 10   

**2. 统计 IV 号染色体上各类 feature （1.gtf文件的第3列，有些注释文件中还应同时考虑第2列） 的数目，并按升序排列。**         

grep -v '^#' 1.gtf |awk '$1 == "IV"{print $3}'| sort | uniq -c | sort -nk 1     

**3. 寻找不在 IV 号染色体上的所有负链上的基因中最长的2条 CDS 序列，输出他们的长度。**             

grep -v '^#' 1.gtf |awk '$1 != "IV" && $3 =="CDS" && $7 == "-"{name=$10;gsub("\"", "", name);print name, $5 - $4 + 1}'| sort -rnk 2 | head -n 2    

**4. 寻找 XV 号染色体上长度最长的5条基因，并输出基因 id 及对应的长度。**            

grep -v '^#' 1.gtf |awk '$1 == "XV" && $3 =="gene" {name=$10;gsub("\"", "", name);print name, $5-$4 + 1}'| sort -r | head -n 5   

**5. 统计1.gtf列数**                  

awk -F '\t' 'BEGIN {to=0}NF>to{to=NF}END{print NF}' 1.gtf   



2023.3.4
