import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns


def countplot(dataframe, column, title):
    g = sns.countplot(data=dataframe, y=column, palette="rainbow", order=dataframe[column].value_counts().index);
    g.axes.set_ylim(10)
    g.set_title(title, fontdict={'fontsize': 20, 'verticalalignment': 'bottom'}, weight='bold')
    sns.set(rc={"figure.figsize": (8, 5)})


def heatmap(dataframe, columns, title, rows, cols):
    f, ax = plt.subplots(figsize=(rows, cols))
    i = sns.heatmap(dataframe[columns].corr(), annot=True, cmap="PiYG")
    i.set_xticklabels(i.get_xmajorticklabels(), fontsize=12)
    i.set_yticklabels(i.get_ymajorticklabels(), fontsize=12)
    i.set_title(title, fontdict={'fontsize': 14, 'verticalalignment': 'bottom'}, weight='bold')


def scatter(dataframe, x, y ):
    sns.scatterplot(data=dataframe, x=x, y=y)


def boxplot(dataframe, x):
    sns.set_style('darkgrid')
    plt.figure(figsize=(6, 4))
    sns.boxplot(data=dataframe, x=x)
    plt.xticks(rotation=90)
    plt.title(f'Boxplot - {x}', fontdict={'fontsize': 18, 'verticalalignment': 'bottom'}, weight='bold')


def box_y_hist_plot(dataframe, col):
    fig, ax = plt.subplots(2, 1, figsize=(6, 4))

    ax[0].set_title(f"Distribucion de {col}")
    sns.histplot(data=dataframe, x=f"{col}", kde=True, ax=ax[0])

    ax[1].set_title(f"Boxplot de{col}")
    sns.boxplot(data=dataframe, x=f"{col}", ax=ax[1])


def plot_roc_curve(y_test, y_pred):
    from sklearn.metrics import roc_auc_score
    from sklearn.metrics import roc_curve

    logit_roc_auc = roc_auc_score(y_test, y_pred)
    fpr, tpr, thresholds = roc_curve(y_test, y_pred)

    plt.figure()
    plt.plot(fpr, tpr, label='Logistic Regression (area=%0.2f)' % logit_roc_auc)
    plt.plot([0, 1], [0, 1], 'r--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC Curve')
    plt.legend(loc='lower right')
    plt.show()