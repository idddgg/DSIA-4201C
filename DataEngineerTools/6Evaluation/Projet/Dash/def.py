from dash import html, dcc, Input, Output
import dash_bootstrap_components as dbc
from database import get_all_cars

# Fonction pour récupérer les voitures en fonction du type de carburant
def get_cars_by_fuel_type(fuel_type):
    all_cars = get_all_cars()
    return [car for car in all_cars if car["fuel_type"].lower() == fuel_type.lower()]

# Fonction pour créer le carrousel des voitures
def create_carousel(fuel_type):
    cars = get_cars_by_fuel_type(fuel_type)
    
    if not cars:
        return html.P("Aucune voiture disponible pour ce type de carburant.", style={"textAlign": "center", "fontSize": "18px"})
    
    return html.Div([
        dcc.Store(id='current-image-index', data=0),
        
        html.Div(
            style={
                'position': 'relative',
                'width': '800px',
                'height': '450px',
                'margin': '0 auto',
                'borderRadius': '10px',
                'overflow': 'hidden',
                'boxShadow': '0px 4px 8px rgba(0, 0, 0, 0.2)'
            },
            children=[
                html.Img(
                    id='displayed-image',
                    src=cars[0]['image_url'],
                    style={'width': '100%', 'height': '100%', 'objectFit': 'cover', 'borderRadius': '10px'}
                ),
                
                html.Button(
                    "❮",
                    id='prev-button',
                    n_clicks=0,
                    style={
                        'position': 'absolute',
                        'top': '50%',
                        'left': '10px',
                        'transform': 'translateY(-50%)',
                        'fontSize': '24px',
                        'backgroundColor': 'white',
                        'border': 'none',
                        'borderRadius': '50%',
                        'width': '40px',
                        'height': '40px',
                        'cursor': 'pointer',
                        'opacity': '0.8'
                    }
                ),
                
                html.Button(
                    "❯",
                    id='next-button',
                    n_clicks=0,
                    style={
                        'position': 'absolute',
                        'top': '50%',
                        'right': '10px',
                        'transform': 'translateY(-50%)',
                        'fontSize': '24px',
                        'backgroundColor': 'white',
                        'border': 'none',
                        'borderRadius': '50%',
                        'width': '40px',
                        'height': '40px',
                        'cursor': 'pointer',
                        'opacity': '0.8'
                    }
                ),
            ]
        ),
    ], style={'textAlign': 'center'})

# Callback pour gérer la navigation dans le carrousel

def register_callbacks(app, fuel_type):
    @app.callback(
        Output('current-image-index', 'data'),
        Input('prev-button', 'n_clicks'),
        Input('next-button', 'n_clicks'),
        prevent_initial_call=True
    )
    def update_image_index(prev_clicks, next_clicks):
        cars = get_cars_by_fuel_type(fuel_type)
        total_images = len(cars)
        changed_id = [p['prop_id'] for p in app.callback_context.triggered][0]
        
        if 'prev-button' in changed_id:
            return (prev_clicks - 1) % total_images
        elif 'next-button' in changed_id:
            return (next_clicks + 1) % total_images
        return 0
    
    @app.callback(
        Output('displayed-image', 'src'),
        Input('current-image-index', 'data')
    )
    def display_current_image(image_index):
        cars = get_cars_by_fuel_type(fuel_type)
        return cars[image_index]['image_url']
