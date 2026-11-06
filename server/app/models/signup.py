from sqlalchemy.orm import Mapped,mapped_column,relationship 
from sqlalchemy import ForeignKey 
from app.db import db 
from sqlalchemy_serializer import SerializerMixin 
from sqlalchemy import CheckConstraint

class Signup(db.Model,SerializerMixin):
    __tablename__="signups"

    serialize_rules=("-activity.signups","-camper.signups",)

    id:Mapped[int]=mapped_column(primary_key=True)
    time:Mapped[int]
    camper_id:Mapped[int]=mapped_column(ForeignKey("campers.id"))
    activity_id:Mapped[int]=mapped_column(ForeignKey("activities.id"))

    activity:Mapped["Activity"]=relationship(back_populates="signups")
    camper:Mapped["Camper"]=relationship(back_populates="signups")

    __table_args__=(
        CheckConstraint('time >=0 AND time <=23'),
    )

    def __repr__(self):

        return f"<Signup {self.id} {self.time}>"