import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc
import pandas as pd


data = pd.read_csv('BreastCancer_predict.txt', sep='\t').replace('benign', 0).replace('malignant', 1)
y_true = data['y_true'].values
pred_p = data['prediction_probability'].values


fpr, tpr, thresholds = roc_curve(y_true, pred_p)
roc_auc = auc(fpr, tpr)

# 画ROC曲线
plt.plot(fpr, tpr, '-', color='r', label='ROC', lw=2)
plt.plot([0, 1], [0, 1], '--', color=(0.6, 0.6, 0.6), label='Random Chance')
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.title('ROC curve')
plt.xlabel('FPR')
plt.ylabel('TPR')
plt.legend()
plt.show()
plt.close()


