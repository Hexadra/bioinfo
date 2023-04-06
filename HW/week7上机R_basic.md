## 上机任务：    
iris是R语言自带的一个数据集，它默认会作为一个数据框加载到R环境中，请对iris数据做如下分析：   
### 1. iris数据集有几列？每列的数据类型是什么?    
有5列，分别为 Sepal.Length，Sepal.Width，Petal.Length，Petal.Width 和 Species。      
第1,2,3,4列都是"numeric"，第5列为"factor"。    
### 2. 按Species列将数据分成3组，分别计算Sepal.Length的均值和标准差，保存为一个csv文件，提供代码和csv文件的内容。    
```
aa <- aggregate(Sepal.Length ~ Species, iris, mean)
bb <- aggregate(Sepal.Length ~ Species, iris, sd)
cc <- cbind(aa,bb)
write.csv(cc,"output2.csv",quote=F)
```
csv文件内容（左侧是均值，右侧是标准差）：     
![image](https://user-images.githubusercontent.com/126166219/230256716-2f31dff3-c149-4409-852e-ce786dda6cc8.png)


### 3. 对不同Species的Sepal.Width进行One way ANOVA分析，提供代码和输出的结果。    
```
summary(aov(Sepal.Width~Species,data=iris))
```     
   
|         |  Df |Sum Sq |Mean Sq| F value| Pr(>F) ||
|  -- |  -- |---|------- |----| ----- |---|
|Species   |    2 | 11.35 |  5.672 |  49.16| <2e-16| ***     
|Residuals  | 147 | 16.96  | 0.115                      
