## Homework 10        
### III.3.ChIP-seq             
作业副本另见[my Github homework 10](https://github.com/Hexadra/bioinfo/blob/main/HW/week10%20hw.md)
1. 请解释在ChIP-seq实验中为什么一般都要平行做一个 control （通常叫 input）的实验。      



2. 请解释 findPeaks 和 findMotifsGenome.pl 主要参数的含义。       
在findPeaks中，命令为：``findPeaks <tag directory> -style factor -o auto -i <input tag directory>``          
主要参数的含义分别为：     
-F 为筛选归一化后peaks的fold change     
-P 为筛选设定符合泊松分布的peaks数的p value      
-inputSize 可以设定peaks的倍数以适应不同对照组        
-style 指定寻找peaks的方法     
        
在findMotifGenome.pl中，命令为：``findMotifsGenome.pl <peak/BED file> -size``          
peak/BED file是peak文件的路径，作为输入。    
genome是参考基因组名称，如人的hg19、小鼠的mm10等。     
output directory是结果的输出路径    
主要参数的含义分别为：      
-size 指定了软件用多长的序列寻找motif，默认200。建议对转录因子设置为50（若寻找临近的共富集motif可增加至200），组蛋白设置为500-1000。       
-len 指定motif长度，提供多个值时软件会分别寻找对应长度的motif，默认8,10,12。        
-bg 指定了作背景的序列，软件在初步计算出motif后会计算样本中每个motif相对于背景的丰度，据此检验motif的显著性。不指定时软件会随机选择2×peak数或50000个区域作背景，并保证其GC含量的分布与样本一致。      
-S 指定了输出的motif数量，默认25。       
-mis 指定了软件寻找motif过程中允许的碱基错配数，值越低则越保守，默认2。     
     
     
3. 我们在容器的/home/test/chip-seq/homework目录中提供了酵母Snf1蛋白CHIP-seq的bam文件，ip.chrom_part.bam为IP实验数据，input.chrom\_part.bam为背景数据。请大家从这两个文件出发，用homer重复本章中介绍的peak calling和motif finding分析。请大家提交找到的motif的截图，以及Fold Change (vs Control) >=8且p-value (vs Control) < `的peaks(建议放在同一个文件中提交)。                            


```
cd /home/test/chip-seq/homework
mkdir output
makeTagDirectory input/ip ip.chrom_part.bam
makeTagDirectory input/input input.chrom_part.bam
# 不过滤
findPeaks input/ip/ -style factor -o output/part.peak -i input/input/
findMotifsGenome.pl output/part.peak sacCer2 output/part.motif.output -len 8
# 过滤
findPeaks input/ip/ -style factor -o output/f_part.peak -i input/input/ -F 8 -P 1e-8
findMotifsGenome.pl output/f_part.peak sacCer2 output/f_part.motif.output -len 8
```
