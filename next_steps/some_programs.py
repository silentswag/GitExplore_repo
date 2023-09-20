from dash import Dash, html

app = Dash(__name__)

app.layout = html.Div([
    html.Div(children='Hello World'),
    html.Div(children=" my first access and explore to git gitlab git bash")
])

if __name__ == '__main__':
    app.run(debug=True)
