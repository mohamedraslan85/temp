# -*- coding: utf-8 -*-
"""crypto_scanner_classuse.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rQobovjubPoNa49ZzloSGQ5FQiC242t9
"""

# Commented out IPython magic to ensure Python compatibility.
# %cd /

##pip install django-toolbelt bokeh numpy

# Commented out IPython magic to ensure Python compatibility.
# %cd content/drive/MyDrive/crypto_scanner/

pip install -r requirements.txt



from crypto import crypto

a=crypto('binance',1,'USDT')

a.scanner()

ask_filtered,bid_filtered=a.get_bidask(10,0)

time_tuple=(2021, 3, 20, 00, 00, 00, 0, 00, 0)

OHLCV=a.get_OHLCV(time_tuple,'1h')
df=OHLCV[OHLCV['symbol']=='BTC/USDT']

start='2021-04-03 18:00:00'
end='2021-04-02 20:00:00'
a.BTC_drop_change(start,end,-30,10)

a.get_tweets()
a.group_tweets('BTC','1h')

a.into.reset_index()

a.draw_bidask('BTC/USDT',['binance'])

df

from bokeh.plotting import figure, show, output_file
from bokeh.models import ColumnDataSource, Range1d, LabelSet, Label
from bokeh.plotting import ColumnDataSource, figure, output_file, show

output_file("toolbar.html")
TOOLTIPS = [
    #("Date", "$x"),
    ("Number of bitcoints :", "@count"),
    ("Price", "@price{0.0 }"),
     ("Close", "@close{0.0 }"),

]

_tools_to_show = 'box_zoom,pan,save,hover,reset,tap,wheel_zoom'        

p = figure(width=1000, height=750 ,x_axis_type="datetime", tools=_tools_to_show,tooltips=TOOLTIPS)

#z=outfrom.drop(['destination','source','amount_USD'],axis=1)

w=1*60*60*1000
df_ = df.copy()
symbol=df['symbol'].unique()[0]
inc = df_.Close > df_.Open
dec = df_.Open > df_.Close
source1 = ColumnDataSource(data=dict(
    x=df_.Date[inc],
    close=df_.Close[inc],
    open= df_.Open[inc],
    desc=df.symbol[inc],
))
source2= ColumnDataSource(data=dict(
    x=df_.Date[dec],
    close=df_.Close[dec],
    open= df_.Open[dec],
    desc=df.symbol[dec],
))

#p = figure(plot_width=400, plot_height=400, ,title="Mouse over the dots")
#p.scatter(x='time', y='coin_price', size=10, source=source)
p.segment(df_.index, df_.High, df_.index, df_.Low, color="black")
p.vbar('x', w, 'open', 'close', source=source1,fill_color="green", line_color="red")
p.vbar('x', w, 'open', 'close', source=source2,fill_color="red", line_color="green")
#p.triangle(outfrom.index, outfrom.coin_price,name="mycircle",angle =3.14,fill_alpha=0.5,color='green',size=5*outfrom.coin_count/average_out)
#a.into.reset_index(inplace=True)
#a.outfrom.reset_index(inplace=True)  
#labels = LabelSet(x='time', y='coin_price', text='coin_count', level='glyph', x_offset=5, y_offset=5, source=source, render_mode='canvas')
source_into_tweet=ColumnDataSource(data=dict(
    x=a.into.time,
    price=a.into.coin_price,
    size=a.into.coin_count/150,
    count=a.into.coin_count,
))
source_outfrom_tweet=ColumnDataSource(data=dict(
    x=a.outfrom.time,
    price=a.outfrom.coin_price,
    size=a.outfrom.coin_count/150,
    count=a.outfrom.coin_count,
))
average_in=a.into.coin_count.mean()
average_out=a.outfrom.coin_count.mean()
p.triangle('x', 'price',name="mycircle",source=source_outfrom_tweet ,angle =3.14,fill_alpha=0.5,color='green',size='size')
p.triangle('x', 'price',name="mycircle",source=source_into_tweet, fill_alpha=0.5 ,color='red',size='size')
#p.circle('x', 'y', size=20, source=source)

#p.add_layout(labels)

show(p)

a.plot_bokeh(df)

from flask import Flask
from flask_ngrok import run_with_ngrok
from flask import Response
import io
import base64
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import matplotlib.pyplot as plt
import numpy as np 
from flask import Flask, request, render_template, abort, Response
from bokeh.plotting import figure
from bokeh.embed import components



import numpy as np 
from flask import Flask, request, render_template, abort, Response
from bokeh.plotting import figure
from bokeh.embed import components



#pip install flask_ngrok

a.get_tweets()
a.group_tweets()