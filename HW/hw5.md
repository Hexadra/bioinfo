## Homework 4    

### 1. 请阐述bowtie中利用了 BWT 的什么性质提高了运算速度？并通过哪些策略优化了对内存的需求？  
利用BWT变换后的保序性    
通过间隔记录索引的方式减小了存储索引占用空间。   

### 2. 用bowtie将 THA2.fa mapping 到 BowtieIndex/YeastGenome 上，得到 THA2.sam，统计mapping到不同染色体上的reads数量(即统计每条染色体都map上了多少条reads)。

```  
# 将fasta文件中THA1.fa的reads mapping到酵母基因组上  
bowtie -v 2 -m 10 --best --strata BowtieIndex/YeastGenome -f THA1.fa -S THA1.sam
# -v 2: 最多容许2个mismatch
# -m 10: 只输出可以map到不超过10个位置的reads mapping的结果
# --best --strata: 只汇报最好的一个hit,两个参数需要同时指定
# BowtieIndex/YeastGenome: 酵母的bowtie index,可以从https://bowtie-bio.sourceforge.net/manual.shtml下载，也可以用bowtie-build从基因组文件自己建立
# -f THA1.fa: 输入为fasta文件，路径为THA1.fa
# -S THA1.sam: 输出文件名为THA1.sam，格式为sam文件
```  


### 3. 查阅资料，回答以下问题:     
（3.1）什么是sam/bam文件中的"CIGAR string"? 它包含了什么信息?    
CIGAR string 的作用是记录该序列和参考序列相比对时，匹配、插入、删除的数量及位置等情况。    
（3.2）"soft clip"的含义是什么，在CIGAR string中如何表示？   
"soft clip"的含义是在序列两侧比对不上参考序列，但是仍然保存在SAM文件的reads中的片段；在CIGAR string中用S加数字表示。     
（3.3）什么是reads的mapping quality? 它反映了什么样的信息?   
mapping quality等于-10 * log10{mapping位置出错的概率}，它反映了mapping到该位置的可信度。       
（3.4）仅根据sam/bam文件的信息，能否推断出read mapping到的区域对应的参考基因组序列? (提示:参考https://samtools.github.io/hts-specs/SAMtags.pdf中对于MD tag的介绍)       
可以推断出来。根据MD tag 记录的插入、删除等信息和CIGAR的信息可以在query序列的基础上重建出参考序列。      

### 4. 软件安装和资源文件的下载也是生物信息学实践中的重要步骤。请自行安装教程中未涉及的bwa软件，从UCSC Genome Browser下载Yeast (S. cerevisiae, sacCer3)基因组序列。使用bwa对Yeast基因组sacCer3.fa建立索引，并利用bwa将THA2.fa，mapping到Yeast参考基因组上，并进一步转化输出得到THA2-bwa.sam文件。   

```
# Download the bwa-0.7.11 binary package (download link may change)
wget -O- http://sourceforge.net/projects/bio-bwa/files/bwakit/bwakit-0.7.12_x64-linux.tar.bz2/download \
  | gzip -dc | tar xf -
# Generate the GRCh38+ALT+decoy+HLA and create the BWA index
bwa.kit/run-gen-ref hs38DH   # download GRCh38 and write hs38DH.fa
bwa.kit/bwa index hs38DH.fa  # create BWA index
# mapping
bwa.kit/run-bwamem -o out -H hs38DH.fa read1.fq read2.fq | sh
```
### 5. 利用Genome Browser浏览 1.Mapping的 Homework 得到的sam/bam文件，并仿照上文中的 examples截图展示一个 gene的区域。   





参考：   
1. [孟浩巍 - 知乎](https://www.zhihu.com/people/meng_howard)

