from flask import Blueprint,make_response,request
from app.models import Signup
from app.db import db

signup_bp=Blueprint("signup",__name__)


@signup_bp.route('', methods=["GET", "POST"])
@signup_bp.route('/',methods=["GET","POST"])
def signups():
    if request.method == "GET":
        signups=[signup.to_dict() for signup in Signup.query.all()]

        return make_response(
            signups,
            200
        )
    elif request.method == "POST":
        data=request.get_json()
        allowed_fields=["camper_id","activity_id","time"]
        
        signup=Signup()

        if "camper_id" in data and "activity_id" in data and "time" in data:

            if not (0 <= data.get("time") <=23):
                return {"error":"Time must be between 0 and 23"},422

            for attr,value in data.items():
                if attr in allowed_fields:
                    setattr(signup,attr,value)
            db.session.add(signup)
            db.session.commit()

            response=signup.to_dict()

            return make_response(
                response,
                200
            )
        return {"errors": ["validation errors"]},422