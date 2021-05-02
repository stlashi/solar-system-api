from app import db 
from flask import Blueprint, request, make_response, jsonify
from app.models.planet import Planet 

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods = ["POST","GET"], strict_slashes=False)
def handle_planets():
    if request.method == "POST":
        request_body = request.get_json()
        new_planet = Planet(name = request_body["name"],
            description = request_body["description"],
            order_from_sun = request_body["order_from_sun"]) 
        
        db.session.add(new_planet) 
        db.session.commit()
        
        return make_response(f"Planet {new_planet.name} successfully created", 201)
    elif request.method == "GET":
        planets = Planet.query.all()
        planets_response = []
        for p in planets:
            planets_response.append({
                "id": p.id,
                "name": p.name,
                "description": p.description,
                "order_from_sun": p.order_from_sun,
            })
        return jsonify(planets_response)
    
@planets_bp.route("/<planet_id>", methods = ["GET"], strict_slashes=False)
def handle_planet_id(planet_id):
    planet = Planet.query.get(planet_id)

    return {
        "id":planet.id,
        "name":planet.name,
        "description":planet.description,
        "order_from_sun": planet.order_from_sun 
    }
