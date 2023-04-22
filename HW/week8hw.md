## Homework 8     
#### 1) 请阐述 RNA-seq 中归一化基因表达值的几种基本计算方法。         
首先设N=map到某基因上的reads数，T=所有reads的总数。则：         
CPM/RPM:  $\frac{N}{\frac{T}{10^6}}$      
RPKM: $\frac{N}{\frac{T}{10^6} * gene\quad length\quad in\quad Kbp}$        
FPKM: RPKM/2      
TPM: $\frac{RPKM}{\sum (RPKM)} * 10^6$     
TMM counts: 首先选择参考样本r和参考gene set G，对每个基因g计算权重 $w_g(j,r)$，对每个样本计算归一因子 $C_j$，最后即可得到 $\frac{C_{raw}(g)}{C_j}$。            
RLE: 首先计算基因原始数据的几何均值，再用gene除以几何均值，对每个样本计算归一因子 $C_j$，最后同TMM类似地，得到 $\frac{C_{raw}(g)}{C_j}$。     
     
#### 2) 根据下述图片描述，填出对应选项:    
![image](https://user-images.githubusercontent.com/126166219/233662385-dd3a3aad-66d3-40e6-b3ce-e5915a0dd62b.png)    
**Standard Illumina:** E.13     
**Ligation Method:** D.9    
**dUTPs Method:** A.4    
    
#### 3) 通过软件计算，判断给出文件shape02数据是来自哪一种sequencing protocols （strand nonspecific, strand specific - forward, strand specific - reverse)，并选择合适的参数计算shape02的read count matrix，给出AT1G09530基因(PIF3基因)上的counts数目。         
判断shape02数据来源:       
```
cd /home/test
/usr/local/bin/infer_experiment.py -r GTF/Arabidopsis_thaliana.TAIR10.34.bed -i bam/Shape02.bam
```
结果：   
```
Reading reference gene model GTF/Arabidopsis_thaliana.TAIR10.34.bed ... Done
Loading SAM/BAM file ...  Total 200000 usable reads were sampled


This is PairEnd Data
Fraction of reads failed to determine: 0.0315
Fraction of reads explained by "1++,1--,2+-,2-+": 0.4769
Fraction of reads explained by "1+-,1-+,2++,2--": 0.4916
```
由于"1++,1--,2+-,2-+" 和"1+-,1-+,2++,2--" 的数值相差不大且都接近0.5，故认为采用的是Non-Strand-specific的方法。           
        
计算shape02的read count matrix:        
```
/home/software/subread-2.0.3-source/bin/featureCounts -s 0 -p -t exon -g gene_id -a GTF/Arabidopsis_thaliana.TAIR10.34.gtf -o result/Shape02.featurecounts.exon.txt bam/Shape02.bam
```
输出Shape02.featurecounts.exon.txt和Shape02.featurecounts.exon.txt.summary文件（见作业压缩包）。                   
```
Status  bam/Shape02.bam
Assigned        2559170
Unassigned_Unmapped     0
Unassigned_Read_Type    0
Unassigned_Singleton    0
Unassigned_MappingQuality       0
Unassigned_Chimera      0
Unassigned_FragmentLength       0
Unassigned_Duplicate    0
Unassigned_MultiMapping 0
Unassigned_Secondary    0
Unassigned_NonSplit     0
Unassigned_NoFeatures   59487
Unassigned_Overlapping_Length   0
Unassigned_Ambiguity    111786
```
      
找到AT1G09530基因的raw reads count:          
```
cat Shape02.featurecounts.exon.txt | grep AT1G09530 | awk '{print $1,$7}'
```
结果：        
```
AT1G09530 86
```
即得到AT1G09530基因(PIF3基因)上的counts数目为86。       
         
#### 4) tumor-transcriptome-demo.tar.gz提供了结肠癌(COAD)，直肠癌(READ)和食道癌(ESCA)三种癌症各50个样本的bam文件用featureCount计算产生的结果。请大家编写脚本将这些文件中的counts合并到一个矩阵中(行为基因，列为样本), 计算logCPM的Z-score，并用 heatmap 展示，提供代码和heatmap。根据heatmap可视化的结果，你认为这三种癌症中哪两种癌症的转录组是最相似的?        
脚本文件如下：     
```
library(pheatmap)
setwd('C:/Users/Sumts/Desktop/tumor-transcriptome-demo')

gettype=function(s){
  t=strsplit(s,split='/')[[1]][1]
  return(t)
}
# 只读取第一列和第七列
classes=c("character",rep("NULL",5),"integer")
# 批量读取所有文件，并整合到一个数据框rawm中
path=c("COAD","ESCA","READ")
samplelist=list.files(path,pattern="*.txt$",full.names=TRUE)
n=length(samplelist)
rawm=read.table(samplelist[1],colClasses=classes,skip=2)
colnames(rawm)=c("GeneId",1)
for (i in c(2:length(samplelist))){
  temp=read.table(samplelist[i],colClasses=classes,skip=2)
  colnames(temp)=c("GeneId",i)
  rawm=merge(rawm,temp,by="GeneId",suffixes=NULL)
}
rownames(rawm)=rawm$GeneId
rawm$GeneId=NULL

# 计算z score
log10.CPM.matrix=log10(t(1000000*t(rawm)/colSums(rawm))+1)
z.scores=(log10.CPM.matrix - rowMeans(log10.CPM.matrix))/apply(log10.CPM.matrix,1,sd)

# 处理数据
z.scores=z.scores[apply(z.scores, 1, function(y) any(!is.na(y))),]
z.scores[is.na(z.scores)]=0
z.scores[z.scores>2]=4
z.scores[z.scores <= -2] = -4
# 注释癌症类型
anno_col = data.frame(TumorType=factor(sapply(samplelist,gettype)))
rownames(anno_col) = colnames(z.scores)

# 绘制Heatmap
pheatmap(z.scores,
         color = colorRampPalette(c("red", "white", "yellow"))(50),
         cutree_col = 3,
         show_colnames=FALSE, cluster_cols=TRUE,
         annotation_col = anno_col,
         annotation_colors = list(TumorType = c(COAD = "red", ESCA = "yellow", READ = "blue")))

```
作Heatmap如下（部分基因行为NaN，被聚为一类）    
由图可看出绝大部分COAD和ESCA被分为同一类，即得出结论，结肠癌和直肠癌转录组最接近。     
![clus](https://user-images.githubusercontent.com/126166219/233792220-1d3a6e59-25cc-4300-832f-3b1f20ab13c8.png)
