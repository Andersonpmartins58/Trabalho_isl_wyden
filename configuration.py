from routes.home import home_route
from routes.autor import autor_route
from database.database import db 
from database.models.autor import Autor 

def configure_all(app): 
    configure_routes(app)
    configure_db()


def configure_routes(app): 
    app.register_blueprint(home_route)
    app.register_blueprint(autor_route, url_prefix='/autores')

def configure_db(): 
    db.connect()
    db.create_tables([Autor])
