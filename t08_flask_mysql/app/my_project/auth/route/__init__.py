from .error_handler import err_handler_bp

from flask import Flask

def register_routes(app: Flask) -> None:
    """
    Registers all necessary Blueprint routes
    :param app: Flask application object
    """
    from .orders.media_route import media_bp
    from .orders.owners_route import owners_bp
    from .orders.places_route import places_bp
    from .orders.place_owners_route import place_owners_bp
    from .orders.place_amenities_route import place_amenity_bp
    from .orders.amenities_route import amenity_bp
    from .orders.ratings_route import ratings_bp
    from .orders.reviews_route import reviews_bp
    from .orders.users_route import users_bp

    app.register_blueprint(media_bp)
    app.register_blueprint(owners_bp)
    app.register_blueprint(places_bp)
    app.register_blueprint(place_owners_bp)
    app.register_blueprint(place_amenity_bp)
    app.register_blueprint(amenity_bp)
    app.register_blueprint(ratings_bp)
    app.register_blueprint(reviews_bp)
    app.register_blueprint(users_bp)
