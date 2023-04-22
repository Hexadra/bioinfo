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




#### 4) tumor-transcriptome-demo.tar.gz提供了结肠癌(COAD)，直肠癌(READ)和食道癌(ESCA)三种癌症各50个样本的bam文件用featureCount计算产生的结果。请大家编写脚本将这些文件中的counts合并到一个矩阵中(行为基因，列为样本), 计算logCPM的Z-score，并用 heatmap 展示，提供代码和heatmap。根据heatmap可视化的结果，你认为这三种癌症中哪两种癌症的转录组是最相似的?        
脚本文件如下     
```







```
