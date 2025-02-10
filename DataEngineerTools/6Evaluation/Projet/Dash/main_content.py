from dash import html, dcc
from database import get_video_url  # Import de la fonction pour récupérer la vidéo depuis MongoDB

# Récupération de l'URL de la vidéo depuis MongoDB
video_path = get_video_url()

# Fonction pour créer le contenu principal
def create_main_content():
    return html.Div(
        children=[
            # Vidéo récupérée dynamiquement depuis MongoDB
            html.Div(
                html.Video(
                    src=video_path,       # URL dynamique de la vidéo
                    autoPlay=True,        # Lecture automatique
                    loop=True,            # Lecture en boucle
                    muted=True,           # Muet pour éviter les restrictions des navigateurs
                    controls=True,        # Affiche les contrôles
                    style={
                        "width": "100%",  # Occupe toute la largeur de la page
                        "height": "auto", # Maintient le ratio d'aspect
                        "display": "block",
                        "margin": "0 auto",  # Centre la vidéo
                        "maxHeight": "90vh"  # Limite la hauteur maximale pour éviter qu'elle soit trop grande
                    }
                )
            ),
            # Boutons de navigation
            html.Div(
                children=[
                    dcc.Link(html.Button("Hybride", style={
                        "backgroundColor": "#0078d7",
                        "color": "white",
                        "border": "none",
                        "borderRadius": "8px",
                        "padding": "16px 30px",  # Taille augmentée
                        "fontSize": "18px",      # Police plus grande
                        "cursor": "pointer",
                        "boxShadow": "0px 4px 6px rgba(0, 0, 0, 0.1)",
                        "margin": "12px",
                        "transition": "transform 0.2s ease",
                    }), href="/hybride"),
                    dcc.Link(html.Button("Essence", style={
                        "backgroundColor": "#0078d7",
                        "color": "white",
                        "border": "none",
                        "borderRadius": "8px",
                        "padding": "16px 30px",
                        "fontSize": "18px",
                        "cursor": "pointer",
                        "boxShadow": "0px 4px 6px rgba(0, 0, 0, 0.1)",
                        "margin": "12px",
                        "transition": "transform 0.2s ease",
                    }), href="/essence"),
                    dcc.Link(html.Button("Électrique", style={
                        "backgroundColor": "#0078d7",
                        "color": "white",
                        "border": "none",
                        "borderRadius": "8px",
                        "padding": "16px 30px",
                        "fontSize": "18px",
                        "cursor": "pointer",
                        "boxShadow": "0px 4px 6px rgba(0, 0, 0, 0.1)",
                        "margin": "12px",
                        "transition": "transform 0.2s ease",
                    }), href="/electrique"),
                    dcc.Link(html.Button("Diesel", style={
                        "backgroundColor": "#0078d7",
                        "color": "white",
                        "border": "none",
                        "borderRadius": "8px",
                        "padding": "16px 30px",
                        "fontSize": "18px",
                        "cursor": "pointer",
                        "boxShadow": "0px 4px 6px rgba(0, 0, 0, 0.1)",
                        "margin": "12px",
                        "transition": "transform 0.2s ease",
                    }), href="/diesel"),
                ],
                style={"textAlign": "center", "marginTop": "30px"}
            )
        ],
        style={
            "padding": "0px"
        }
    )
