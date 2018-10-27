from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import file_html
from bokeh.models import HoverTool, PolySelectTool, LassoSelectTool
from bokeh.models import TapTool, UndoTool, RedoTool, ResetTool, ZoomInTool, ZoomOutTool, CrosshairTool
import pandas as pd


sp500_df = pd.read_csv('c:/tmp/sp500.csv', 
        sep=",", 
        skiprows=1, 
        header=None, 
        names = ["Date","Open","High","Low","Close","Volume"],
        parse_dates=["Date"],
        dayfirst=True,
        infer_datetime_format=True)


p = figure(plot_height = 600, plot_width = 1200, 
           title = 'S&P 500',
          x_axis_label = 'Date', 
           y_axis_label = 'Close (in USD)')
p.line(sp500_df['Date'], sp500_df['Close'], color='blue', legend='')

# Hover tool with vline mode
hover = HoverTool(tooltips=[('Close', '$@{Close}{%0.2f}'), 
                            ('Date', '@date{%F}')],
                    formatters={
                        'date'      : 'datetime', # use 'datetime' formatter for 'date' field
                        'Close' : 'printf',   # use 'printf' formatter for 'adj close' field
                                                # use default 'numeral' formatter for other fields
                    },
                    mode='vline')

p.add_tools(hover)
p.add_tools(LassoSelectTool())
p.add_tools(PolySelectTool())
p.add_tools(TapTool ())
p.add_tools(UndoTool())
p.add_tools(RedoTool())
p.add_tools(ResetTool())
p.add_tools(ZoomInTool())
p.add_tools(ZoomOutTool())
p.add_tools(CrosshairTool())

html = file_html(p, CDN, "my plot")

with open("./test_bokeh.html", "w") as html_file:
    html_file.write(html)