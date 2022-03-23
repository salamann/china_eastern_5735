#!/usr/bin/env python
# coding: utf-8


import pandas
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import timedelta


df = pandas.read_csv("MU5735-Flightradar24-Granular-Data.csv")
df['time'] = [_.split("Z")[0] for _ in df['time']]
df["time"] = pandas.to_datetime(df["time"], format='%Y-%m-%d %H:%M:%S')
df = df.set_index("time")
df = df[df.index > df.index[-1]-timedelta(minutes=3)]


fig = make_subplots(rows=4)
fig.update_layout(width=800, height=600, title="#MU5735 Last 3 minutes")
fig.add_trace(go.Scatter(
    x=df.index, y=df['altitude'], name="Altitude ft"), row=1, col=1)
fig.add_trace(go.Scatter(
    x=df.index, y=df['speed'], name="GPS speed kt"), row=2, col=1)
fig.add_trace(go.Scatter(
    x=df.index, y=df['vspeed'], name="VV ft/min"), row=3, col=1)
fig.add_trace(go.Scatter(
    x=df.index, y=df['track'], name="Track angle deg"), row=4, col=1)
fig.write_html("mu5735.html")
