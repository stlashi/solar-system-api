from flask import Blueprint
from app import db 
from app.models.planet import planet 

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods = ["POST","GET"])
def handle_planets():
    if request.method == "POST":
        request_body = request.get_json()
        new_planet = Planet(name = request_body["name"],
            description = request_body["description"],
            order_from_sun = request_body["order_from_sun"]) 
        
        db.session.add(new_planet) 
        db.session.commit()
        
        return make_response(f"Planet {new_planet.name} successfully created", 201)

    #elif request.method == "GET":
         
