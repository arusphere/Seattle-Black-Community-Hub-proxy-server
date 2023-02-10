from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()
load_dotenv()


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
        "SQLALCHEMY_DATABASE_URI")

    app.config["LOCATION_KEY"] = os.environ.get("LOCATION_KEY")


    # Import models here for Alembic setup
    # from app.models.ExampleModel import ExampleModel
    from app.models.historical_sites import Sites
    from app.models.restaurants import Restaurants 
    from app.models.services import Services 
    from app.models.stores import Stores

    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints here
    # from .routes import example_bp
    # app.register_blueprint(example_bp)
    
    from .routes import restaurants_bp
    app.register_blueprint(restaurants_bp)

    from .routes import historicalsites_bp
    app.register_blueprint(historicalsites_bp)

    from .routes import stores_bp
    app.register_blueprint(stores_bp)

    from .routes import services_bp
    app.register_blueprint(services_bp)

    from .routes import location_bp
    app.register_blueprint(location_bp)


    CORS(app)
    return app