import dash
from dash import dcc, html
import plotly.graph_objects as go
import numpy as np

app = dash.Dash(__name__)

steps = np.arange(0, 100, 10)
sword_qty = np.array([0, 1, 1, 2, 2, 3, 3, 4, 4, 5])
potion_qty = np.array([0, 0, 2, 2, 4, 4, 6, 6, 8, 8])
shield_qty = np.array([0, 0, 0, 1, 1, 1, 2, 2, 2, 3])

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=steps, y=sword_qty + 20, 
    mode='lines', line_shape='hv', name='Iron Sword',
    line=dict(color='#00ff00', width=2)
))

fig.add_trace(go.Scatter(
    x=steps, y=potion_qty + 10, 
    mode='lines', line_shape='hv', name='Health Potion',
    line=dict(color='#00ff00', width=2)
))

fig.add_trace(go.Scatter(
    x=steps, y=shield_qty, 
    mode='lines', line_shape='hv', name='Knight Shield',
    line=dict(color='#00ff00', width=2)
))

fig.update_layout(
    plot_bgcolor='#000000',
    paper_bgcolor='#2e2e2e',
    font=dict(color='#ffffff'),
    xaxis=dict(showgrid=True, gridcolor='#444444', title="Gold Budget Timeline"),
    yaxis=dict(showgrid=True, gridcolor='#444444', showticklabels=False),
    margin=dict(l=20, r=20, t=40, b=40),
    showlegend=True,
    legend=dict(
        yanchor="top",
        y=0.99,
        xanchor="left",
        x=0.01,
        bgcolor="#1e1e1e"
    )
)

app.layout = html.Div(style={'backgroundColor': '#2e2e2e', 'height': '100vh', 'fontFamily': 'monospace'}, children=[
    html.Div("GTKWave-Style RPG Build Visualizer", style={'color': '#00ff00', 'padding': '15px', 'fontSize': '20px', 'backgroundColor': '#1e1e1e', 'borderBottom': '1px solid #444'}),
    dcc.Graph(figure=fig, style={'height': '85vh'})
])

if __name__ == '__main__':
    app.run_server(debug=True, port=8050)