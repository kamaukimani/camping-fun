from flask import Blueprint,make_response 
from app.models import Camper

camper_bp=Blueprint("camper",__name__)

@camper_bp.route('/',methods=["GET"])
def campers():
    campers=[camper.to_dict(rules=("-signups",)) for camper in Camper.query.all()]

    return make_response(
        campers,200
    )

@camper_bp.route('/<int:id>',methods=["GET"])
def camper_by_id(id):
    camper=Camper.query.filter(Camper.id == id).first()

    if camper:
        response=camper.to_dict()
        return make_response(
            response,200
        )
    return {"error": "Camper not found"},404