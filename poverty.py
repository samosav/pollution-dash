import dash
from dash import html

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('Poverty And Equity Database',
            style={'color':'blue',
                   'fontSize':'40px'}),
    html.H2('The World Bank'),
    html.P('Key facts'),
    html.Ul([
        html.Li('Number of Economies: 170'),
        html.Li('Temporal Coverage: 1974 - 2019'),
        html.Li('Update Frequency: Quaterly'),
        html.Li('Last Updates: March 18, 2020'),
        html.Li([
            'Source: ',
          html.A(children='https://datacatalog.worldbank.org/dataset/poverty-and-equity-database',
                 href='https://datacatalog.worldbank.org/dataset/poverty-and-equity-database'),
    html.H2('Test Me')
        ])
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)
    
    
