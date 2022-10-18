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


def boxplot(dataframe, figsize_rows, figsize_cols, x, y, title):
    sns.set_style('darkgrid')
    plt.figure(figsize=(figsize_rows, figsize_cols))
    sns.boxplot(data=dataframe, x=x, y=y)
    plt.xticks(rotation=90)
    plt.title(title, fontdict={'fontsize': 18, 'verticalalignment': 'bottom'}, weight='bold')