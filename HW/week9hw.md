## Homework 9     
### III.2.3.Differential Expression with DEseq2 and edgeR         
1. 什么是Multiple test correction? 并解释 q value(很多时候也叫FDR) 和 p value 的差别。     
 
3. 请结合上课时所讲的知识阐述DESeq2和edgeR中如何对数据进行 normalization，列出并解释具体的公式 。     
 
5. 利用我们以上介绍的方法和数据，分别使用DESeq2和edgeR找出uvr8突变型（uvr8）在光照前后的差异基因，保存为文本文件     
 
7. 对于uvr8突变型的差异基因，定义|log2FC|>1，FDR<0.05的基因为差异表达基因。比较两个软件得到的差异基因有多少是重合的，有多少是不同的，用venn图的形式展示     

9. 对于edgeR找出的FDR<0.05的基因，选出log2FoldChange最大的10个基因和最小的10个基因，计算表达量log10CPM的Z-score并作热图（heatmap）    

    
    
### II.3.1 GO       
1. 从wt.light.vs.dark.all.txt(这是我们在差异表达一节获得的野生型的结果)中选取显著上调的(FDR<0.05, logFC>1)的基因进行GO分析。     

3. 请问上面的例子中， Fold Enrichment和P value是如何计算的? 请写出公式，并解释原理。此外，在定义显著富集的 GO terms 时为什么一般不是参考P value的大小，而是要计算一个 FDR来做为参考？       



### II.3.2 KEGG     
1. 请用 KEGG enrichment 分析上一章(GO enrichment analysis)中的基因集，比较两章的结果，总结两种方法得到的生物学意义有哪些异同。     



