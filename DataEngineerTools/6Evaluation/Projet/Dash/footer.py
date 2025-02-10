from dash import html, dcc

def create_footer():
    return html.Footer(
        children=[
            dcc.Link(
                html.Button(
                    "Retour à l'accueil",
                    style={
                        "backgroundColor": "#0078d7",
                        "color": "white",
                        "border": "none",
                        "borderRadius": "8px",
                        "padding": "16px 30px",
                        "fontSize": "18px",
                        "cursor": "pointer",
                        "boxShadow": "0px 4px 6px rgba(0, 0, 0, 0.1)",
                        "margin": "10px auto",
                        "display": "block",
                        "transition": "transform 0.2s ease",
                    },
                ),
                href="/",
                style={  # ✅ Style ajouté pour supprimer la décoration du lien
                    "textDecoration": "none"  # Supprime le soulignement
                },
            )
        ],
        style={
            "position": "fixed",  # Toujours fixé en bas
            "bottom": "0",
            "width": "100%",
            "backgroundColor": "#f9f9f9",
            "padding": "10px 0",
            "textAlign": "center",
            "boxShadow": "0px -2px 5px rgba(0, 0, 0, 0.1)",
        }
    )
