from flask import Blueprint,make_response,request
from app.models import Camper
from app.db import db

camper_bp=Blueprint("camper",__name__)

@camper_bp.route('',methods=["GET","POST"])
@camper_bp.route('/',methods=["GET","POST"])
def campers():
    if request.method == "GET":
        campers=[camper.to_dict(rules=("-signups",)) for camper in Camper.query.all()]

        return make_response(
            campers,200
        )
    elif request.method == "POST":       

        data=request.get_json()
        allowed_fields=["name","age"]
        age=data.get("age")

        camper=Camper()

        if "name" in data and "age" in data:

            if not (8 <= age <= 18):

                return {"error":"Age must be between 8 and 18"},422

            for attr,value in data.items():

                if attr in allowed_fields:

                    setattr(camper,attr,value)
                    
            db.session.add(camper)
            db.session.commit()

            response= camper.to_dict(rules=("-signups",))
            return make_response(
                response,
                200
            )

        return{"errors": ["validation errors"]},422


@camper_bp.route('/<int:id>',methods=["GET","PATCH"])
def camper_by_id(id):
    camper=Camper.query.filter(Camper.id == id).first()
    if camper is None:
        return {"error": "Camper not found"},404
    if request.method == "GET":

        response=camper.to_dict()
        return make_response(
                response,
                200
            )
        
    elif request.method == "PATCH":
        data=request.get_json()
        allowed_fields=["name","age"]
        age=data.get("age")        

        if "name" in data and "age" in data:
            if not (8 <= age <= 18):
                return {"error":"Age must be between 8 and 18"},422
            for attr,value in data.items():
                if attr in allowed_fields:
                    setattr(camper,attr,value)
            db.session.commit()

            response= camper.to_dict(rules=("-signups",))
            return make_response(
                response,
                200
            )
        return{"errors": ["validation errors"]},422
