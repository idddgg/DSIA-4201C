from dash import Dash, html, dcc, Input, Output
from header import create_header
from main_content import create_main_content
from hybride import create_hybride_layout, register_hybride_callbacks
from essence import create_essence_layout, register_essence_callbacks
from electrique import create_electrique_layout, register_electrique_callbacks
from diesel import create_diesel_layout, register_diesel_callbacks

# Initialisation de l'application Dash
app = Dash(__name__, suppress_callback_exceptions=True)
server = app.server

# Enregistrer les callbacks pour chaque page
register_hybride_callbacks(app)
register_essence_callbacks(app)
register_electrique_callbacks(app)
register_diesel_callbacks(app)

# Définition du layout global
app.layout = html.Div(
    children=[
        dcc.Location(id="url", refresh=False),  # Gestion de l'URL
        create_header(),                        # Header global
        html.Div(id="page-content")             # Contenu dynamique de chaque page
    ]
)

# Callback pour changer de page selon l'URL
@app.callback(
    Output("page-content", "children"),
    Input("url", "pathname")
)
def display_page(pathname):
    """Affiche le contenu en fonction de l'URL."""
    if pathname == "/electrique":
        return create_electrique_layout()
    elif pathname == "/hybride":
        return create_hybride_layout()
    elif pathname == "/essence":
        return create_essence_layout()
    elif pathname == "/diesel":
        return create_diesel_layout()
    else:
        return create_main_content()

if __name__ == "__main__":
    # Lancer le serveur avec le reloader désactivé (évite des démarrages multiples)
    app.run_server(debug=False, use_reloader=False, host="0.0.0.0", port=8050)
