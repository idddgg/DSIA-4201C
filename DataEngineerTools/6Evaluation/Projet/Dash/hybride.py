from dash import html, dcc, Input, Output, State, callback_context
from database import get_all_cars, get_specific_image  # Ajout de la récupération d'image spécifique
from footer import create_footer  # Import du footer global

# Charger les voitures hybrides
cars = [car for car in get_all_cars() if "hybride" in car.get("fuel_type", "").lower()]
specific_image_url = get_specific_image()  # Récupération de l'image spécifique

def create_hybride_layout():
    """Retourne le layout de la page hybride avec 3 images dans le carrousel."""

    if not cars:
        return html.Div(
            "Aucune voiture hybride trouvée.",
            style={"textAlign": "center", "fontSize": "20px", "margin": "50px"},
        )

    return html.Div(
        children=[
            html.H1(
                "BMW - Voitures Hybrides",
                style={"textAlign": "center", "marginBottom": "20px", "color": "#0078d7", "fontSize": "32px"},
            ),
            dcc.Store(id="hybride-current-image-index", data=0),

            # Carrousel avec 3 images
            html.Div(
                style={
                    "position": "relative",
                    "width": "100%",
                    "margin": "0 auto",
                    "padding": "20px",
                    "display": "flex",
                    "justifyContent": "space-between",
                    "alignItems": "center",
                    "boxShadow": "0px 4px 8px rgba(0, 0, 0, 0.1)",
                    "background": "linear-gradient(to right, #f9f9f9, #ffffff)",
                    "borderRadius": "10px",
                },
                children=[
                    html.Button(
                        "❮",
                        id="hybride-prev-button",
                        n_clicks=0,
                        style={
                            "fontSize": "24px",
                            "backgroundColor": "#0078d7",
                            "color": "white",
                            "border": "none",
                            "borderRadius": "50%",
                            "width": "50px",
                            "height": "50px",
                            "cursor": "pointer",
                            "boxShadow": "0px 4px 8px rgba(0, 0, 0, 0.2)",
                        },
                    ),
                    html.Div(
                        id="hybride-images-container",
                        style={
                            "display": "flex",
                            "justifyContent": "space-around",
                            "alignItems": "center",
                            "width": "90%",
                        },
                    ),
                    html.Button(
                        "❯",
                        id="hybride-next-button",
                        n_clicks=0,
                        style={
                            "fontSize": "24px",
                            "backgroundColor": "#0078d7",
                            "color": "white",
                            "border": "none",
                            "borderRadius": "50%",
                            "width": "50px",
                            "height": "50px",
                            "cursor": "pointer",
                            "boxShadow": "0px 4px 8px rgba(0, 0, 0, 0.2)",
                        },
                    ),
                ],
            ),

            # Image spécifique en bas
            html.Div(
                children=[
                    html.Img(
                        src=specific_image_url,
                        style={
                            "width": "100%",
                            "height": "auto",
                            "marginTop": "20px",
                            "borderRadius": "10px",
                            "boxShadow": "0px 4px 8px rgba(0, 0, 0, 0.1)",
                        },
                    ),
                ],
                style={"textAlign": "center"},
            ),

            # Footer avec le bouton "Retour à l'accueil"
            create_footer(),
        ]
    )

def register_hybride_callbacks(app):
    """Enregistre les callbacks de la page hybride."""

    @app.callback(
        [Output("hybride-images-container", "children"), Output("hybride-current-image-index", "data")],
        [Input("hybride-prev-button", "n_clicks"), Input("hybride-next-button", "n_clicks")],
        State("hybride-current-image-index", "data"),
    )
    def update_images(prev_clicks, next_clicks, current_index):
        total_images = len(cars)

        # Vérification si des voitures sont disponibles
        if total_images == 0:
            return [], 0

        # Identifier quel bouton a été cliqué
        changed_id = [p["prop_id"] for p in callback_context.triggered][0]
        if "hybride-prev-button" in changed_id:
            current_index = (current_index - 1) % total_images  # Boucle circulaire vers l'arrière
        elif "hybride-next-button" in changed_id:
            current_index = (current_index + 1) % total_images  # Boucle circulaire vers l'avant

        # Générer les indices pour afficher les 3 images suivantes
        indices = [
            current_index % total_images,
            (current_index + 1) % total_images,
            (current_index + 2) % total_images,
        ]
        images = [
            html.Div(
                children=[
                    html.Img(
                        src=cars[i]["image_url"],
                        style={
                            "width": "100%",
                            "height": "auto",
                            "objectFit": "contain",
                            "borderRadius": "10px",
                            "boxShadow": "0px 4px 8px rgba(0, 0, 0, 0.1)",
                        },
                        className="car-image",
                    ),
                    html.Div(
                        children=[
                            html.H3(
                                cars[i].get("model", "Modèle inconnu"),
                                style={"textAlign": "center", "marginTop": "10px"},
                            ),
                            html.P(
                                f"Prix : {cars[i].get('price', 'N/A')} €",
                                style={"textAlign": "center", "fontSize": "16px", "marginTop": "5px", "color": "#555"},
                            ),
                        ],
                    ),
                ],
                style={"position": "relative", "width": "30%", "margin": "10px", "cursor": "pointer"},
                className="car-card",
            )
            for i in indices
        ]

        return images, current_index
