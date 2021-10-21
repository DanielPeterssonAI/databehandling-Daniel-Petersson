import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

def barplot_with_missing_data(dataframe):
    df_to_plot = pd.DataFrame({"Missing values": dataframe.isnull().sum()})
    df_to_plot["Column name"] = dataframe.columns

    fig, ax = plt.subplots(1, 1, figsize = (12,4), dpi = 100)
    plt.xticks(rotation = 90)
    
    sns.barplot(data = df_to_plot, x = df_to_plot["Column name"], y = df_to_plot["Missing values"])
