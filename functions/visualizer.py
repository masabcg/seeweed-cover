import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import itertools


def hist_graph_visualizer(df, hue_col_name=None, graph_size=4, c=3, bins=10, facecolor='lightblue'):
    '''
    概要：データフレームに含まれる数値データ全てのヒストグラムを出力する
    
    '''
    df = df.select_dtypes(include='number')  # 数値型のみ可視化
    col_list = list(df.columns)
    num_col_list = len(col_list)

    fig, ax = plt.subplots((num_col_list//c)+1, c, 
                           figsize=(graph_size*c, graph_size*(num_col_list//c)+1), 
                           facecolor=facecolor
                          )

    if hue_col_name:
        list_hue_unique = sorted(list(df[hue_col_name].unique()))   # 分けて表示するカラムの一意な値をリストに格納
        list_hue_df = [df[df[hue_col_name] == i] for i in list_hue_unique]   # 分けて表示するカラムの値ごとにデータフレームを分割し、リストに格納
        for i, col in enumerate(col_list):
            ax[i//3, i%3].set_title(col)
            for df_hue in list_hue_df:
                ax[i//3, i%3].hist(df_hue[col], bins=bins, 
                                   alpha=1 / len(list_hue_unique),
                                   label=str(df_hue[hue_col_name].unique())
                                  )
                ax[i//3, i%3].legend()
        
            
    else:
        for i, col in enumerate(col_list):
            ax[i//3, i%3].hist(df[col], bins=bins)
            ax[i//3, i%3].set_title(col)

    fig.tight_layout()
    plt.show()
    
    
def scatter_all_comb_visualizer(df, graph_size=4, c=3, facecolor='lightblue', alpha=0.1):
    '''
    概要：データフレームに含まれる全ての数値データの全組み合わせの散布図を出力する
    '''
    df = df.select_dtypes(include='number')  # 数値型のみ可視化
    
    list_col = list(df.columns)
    list_pair_col = [pair for pair in itertools.combinations(list_col, 2)]  # カラム名の全組み合わせをリストに格納
    num_graph = len(list_pair_col)
    
    # 可視化
    fig, ax = plt.subplots((num_graph//c)+1, c, 
                       figsize=(graph_size*c, graph_size*(num_graph//c)+1), 
                       facecolor=facecolor
                      )

    for i, pair in enumerate(list_pair_col):
        x = pair[0]
        y = pair[1]
        ax[i//3, i%3].scatter(df[x], df[y], alpha=alpha)
        ax[i//3, i%3].set_xlabel(x)
        ax[i//3, i%3].set_ylabel(y)

    fig.tight_layout()
    plt.show()
    