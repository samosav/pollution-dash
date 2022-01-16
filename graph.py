import dash
from dash import html
import dash_core_components as dcc
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('test.csv', header=None)
print(df)

app = dash.Dash(__name__)
fig = go.Figure()
fig.add_scatter(x=df[0].to_list(), y=df[1].to_list())

app.layout = html.Div([

    dcc.Graph(
        figure=fig

    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
