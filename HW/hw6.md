## Homework 6    

### 请大家查阅网络资源（如NCBI和ENSEMBL）以及文献等资料回答以下问题:      
#### 1）人类基因组的大小是多少?基本组成是怎样的？    
GRCh38.p13 (Genome Reference Consortium Human Build 38)碱基对数量为 3,096,649,726    
基本组成包括编码基因、非编码基因、转录调控序列及其他序列。   
   
#### 2）人类基因组中有多大的比例可以被转录成非编码RNA？请列举出主要非编码RNA的类型，并用1-2句话对它们的功能进行解释。 注：请说明数字的来源     
在总共252913个转录本中有163502条，即约64.6%转录本属于非编码RNA     
>来源：[GENCODE](https://www.gencodegenes.org/human/stats.html)   

主要非编码RNA有：
rRNA: 是核糖体的组成成分   
tRNA: 翻译中运载氨基酸    
snRNA: 参与mRNA剪接   
snoRNA: 介导其它RNA的化学修饰   
miRNA: 抑制并降解匹配的mRNA    
lncRNA: 参与多种生物学过程，包括DNA甲基化、组蛋白修饰、RNA转录后调控和蛋白质翻译调控等       
>来源：[ENSEMBL](https://www.ensembl.org/Homo_sapiens/Info/Annotation)     

### Bedtools and Samtools
#### 1）我们提供的bam文件COAD.ACTB.bam是单端测序分析的结果还是双端测序分析的结果？为什么？(提示：可以使用samtools flagstat）      
命令： `samtools flagstat COAD.ACTB.bam`  
输出结果：    
```
185650 + 0 in total (QC-passed reads + QC-failed reads)
4923 + 0 secondary
0 + 0 supplementary
0 + 0 duplicates
185650 + 0 mapped (100.00% : N/A)
0 + 0 paired in sequencing
0 + 0 read1
0 + 0 read2
0 + 0 properly paired (N/A : N/A)
0 + 0 with itself and mate mapped
0 + 0 singletons (N/A : N/A)
0 + 0 with mate mapped to a different chr
0 + 0 with mate mapped to a different chr (mapQ>=5)
```
该bam文件是单端测序的结果，因为paired in sequencing为0+0，显示reads没有配对。    

#### 2）查阅资料回答什么叫做"secondary alignment"？并统计提供的bam文件中，有多少条记录属于"secondary alignment?" （提示：可以使用samtools view -f 获得对应secondary alignment的records进行统计）     
当一条read可被map到多个位置时，其中一个会被标记为primary，而选择哪个是primary的依据可能是随机的，也可能依赖某个指标。其它的alignment都会被标记为secondary。    
>来源: [Linear, Chimeric, Supplementary, Primary and Secondary Alignments](https://yulijia.net/en/bioinformatics/2015/12/21/Linear-Chimeric-Supplementary-Primary-and-Secondary-Alignments.html#:~:text=Supplementary%20Alignment%3A%20A%20chimeric%20reads%20but%20not%20a,other%20alignments%20have%20the%20secondary%20alignment%20flag.%205.)       

Secondary alignment对应的FLAG为256，故使用：`samtools view -f 256 COAD.ACTB.bam | wc -l`   
输出`4923`     

#### 3）请根据hg38.ACTB.gff计算出在ACTB基因的每一条转录本中都被注释成intron的区域，以bed格式输出。并提取COAD.ACTB.bam中比对到ACTB基因intron区域的bam信息，后将bam转换为fastq文件。      
>提示：   
写脚本把ACTB在gff中第三列为"gene"的interval放在一个bed文件中，第三列为"exon"的intervals放在另外一个bed文件中，再使用bedtools subtract。   
请注意bed文件使用的是0-based coordinate，gff文件使用的是1-based coordinate。    
鼓励其他实现方法，描述清楚过程即可    
1）     
```
#!/bin/bash
#读取文件
file="hg38.ACTB.gff"
# 将gene和exon以bed输出
cat $file | awk -v OFS="\t" '$3=="gene" {print $1,$4-1,$5,".",".",$7}' > gene.bed
cat $file | awk -v OFS="\t" '$3=="exon" {print $1,$4-1,$5,".",".",$7}' > exon.bed
# 得到intron
bedtools subtract -a gene.bed -b exon.bed > intron.bed
exit 0
```
2）     
```
samtools sort COAD.ACTB.bam > COAD.ACTB_sorted.bam
samtools index COAD.ACTB_sorted.bam
# 选出COAD.ACTB_sorted.bam中与intron.bed有交集的片段
bedtools intersect -a COAD.ACTB_sorted.bam -b intron.bed -wa > intersect.bam
# 转换为fastq
samtools bam2fq intersect.bam > intersect.fastq
```

#### 4) 利用COAD.ACTB.bam计算出reads在ACTB基因对应的genomic interval上的coverage，以bedgraph格式输出。 （提示：对于真核生物转录组测序向基因组mapping得到的bam文件，bedtools genomecov有必要加-split参数。）        
计算reads在ACTB基因对应的genomic interval上的coverage，即：    
`bedtools genomecov -ibam COAD.ACTB.bam -split -bg >  COAD.coverage.bedgraph`     




