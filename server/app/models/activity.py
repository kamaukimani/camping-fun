from sqlalchemy.orm import Mapped,mapped_column,relationship
from app.db import db 
from sqlalchemy_serializer import SerializerMixin 
from typing import List
from sqlalchemy.ext.associationproxy import association_proxy

class Activity(db.Model,SerializerMixin):
    __tablename__="activities"

    serialize_rules=("-signups.activity",)

    id:Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]
    difficulty:Mapped[int]

    signups:Mapped[List["Signup"]]=relationship(back_populates="activity",cascade="all,delete-orphan")
    campers=association_proxy("signups","camper",creator=lambda camper_obj:Signup(camper=camper_obj))

    def __repr__(self):
        return f"<Activity {self.id} {self.name}>"