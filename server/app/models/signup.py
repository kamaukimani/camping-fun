from sqlalchemy.orm import Mapped,mapped_column,relationship 
from sqlalchemy import ForeignKey 
from app.db import db 
from sqlalchemy_serializer import SerializerMixin 
from sqlalchemy import CheckConstraint

class Signup(db.Model,SerializerMixin):
    __tablename__="signups"

    serialize_rules=("-activity.signups","-camper.signups",)

    id:Mapped[int]=mapped_column(primary_key=True)
    time:Mapped[int]=mapped_column(CheckConstraint('0 <= time <= 23'))
    camper_id:Mapped[int]=mapped_column(ForeignKey("campers.id"))
    activity_id:Mapped[int]=mapped_column(ForeignKey("activities.id"))

    activity:Mapped["Activity"]=relationship(back_populates="signups")
    camper:Mapped["Camper"]=relationship(back_populates="signups")

    def __repr__(self):

        return f"<Signup {self.id} {self.time}>"