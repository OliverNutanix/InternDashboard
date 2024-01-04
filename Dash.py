import dash
from dash import html

# FRONTEND Section + the css sheet in styles.css
# Initialize the Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Add stuff here", className="header"), # classname is referencing the class "header" in assets/styles.css
    # Add HTML and frontend stuff here
])

# Used to start the app, no need to change this
if __name__ == '__main__':
    app.run_server(debug=True)
