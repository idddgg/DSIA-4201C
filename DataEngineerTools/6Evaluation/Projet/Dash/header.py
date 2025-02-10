from dash import html
from database import get_logo_urls  # Importer la fonction de récupération des logos depuis la DB

# Récupérer les URLs des logos depuis MongoDB
logos = get_logo_urls()  # Cette fonction retourne une liste de 4 URLs

# Initialiser les variables
logo_left = ""
logo_center1 = ""
logo_center2 = ""
logo_right = ""

# Assigner chaque logo en fonction de son nom de fichier
for logo in logos:
    if "Logo_BMW_GROUP.svg" in logo:
        logo_left = logo  # BMW Group (gauche)
    elif "Logo_MINI.svg" in logo or "Logo_BMW.svg" in logo:
        if not logo_center1:
            logo_center1 = logo  # Centre-gauche
        else:
            logo_center2 = logo  # Centre-droit
    elif "Logo_Rolls-Royce.svg" in logo:
        logo_right = logo  # Rolls-Royce (droite)

# Fonction pour créer l'en-tête
def create_header():
    return html.Div(
        children=[
            # Logo tout à gauche
            html.Div(
                html.Img(src=logo_left, style={"height": "150px", "objectFit": "contain"}),
                style={"flex": "1", "textAlign": "left"}
            ),
            # Logo centre gauche
            html.Div(
                html.Img(src=logo_center1, style={"height": "150px", "objectFit": "contain"}),
                style={"flex": "1", "textAlign": "center"}
            ),
            # Logo centre droit
            html.Div(
                html.Img(src=logo_center2, style={"height": "150px", "objectFit": "contain"}),
                style={"flex": "1", "textAlign": "center"}
            ),
            # Logo tout à droite
            html.Div(
                html.Img(src=logo_right, style={"height": "150px", "objectFit": "contain"}),
                style={"flex": "1", "textAlign": "right"})
        ],
        style={
            "display": "flex",
            "alignItems": "center",
            "padding": "10px",
            "borderBottom": "1px solid #ccc"
        }
    )
