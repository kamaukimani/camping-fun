from flask import Blueprint,make_response 
from app.models import Camper

camper_bp=Blueprint("camper",__name__)

@camper_bp.route('/',methods=["GET"])
def campers():
    campers=[camper.to_dict(rules=("-signups",)) for camper in Camper.query.all()]

    return make_response(
        campers,200
    )