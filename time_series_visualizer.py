import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
import numpy as np
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# Clean data
df = df[(df['value'] > df['value'].quantile(0.025)) & (df['value'] < df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig = df.plot.line(figsize=(16,6), title='Daily freeCodeCamp Forum Page Views 5/2016-12/2019', xlabel='Date', ylabel='Page Views').figure 

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
      df_bar = df.copy(deep=True)
      df_bar['year'] = df_bar.index.year
      months = ["January", "February", "March", "April", "May", "June", "July", "August","September", "October", "November", "December"]
      df_bar['month'] = df_bar.index.month_name()
      df_bar['month'] = pd.Categorical(df_bar['month'], categories=months)
      df_bar_pivot = pd.pivot_table(
          df_bar,
          values="value",
          index="year",
          columns="month",
          aggfunc=np.mean
    )
  
    
      # Draw bar plot using seaborn
      fig = df_bar_pivot.plot(kind='bar').get_figure()
      fig.set_figheight(6)
      fig.set_figwidth(8)
      plt.xlabel('Years')
      plt.ylabel('Average Page Views')
      plt.legend(title='Months')
      # Save image and return fig (don't change this part)
      fig.savefig('bar_plot.png')
      return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(1, 2, figsize=(16,6))
    sns.boxplot(x = 'year', y = 'value', data = df_box, ax = ax[0]).set(title = 'Year-wise Box Plot (Trend)', xlabel = 'Year', ylabel = 'Page Views')
    sns.boxplot(x = 'month', y = 'value', data = df_box, ax = ax[1], order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']).set(title = 'Month-wise Box Plot (Seasonality)', xlabel = 'Month', ylabel = 'Page Views')
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
