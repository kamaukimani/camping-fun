from sqlalchemy.orm import Mapped,mapped_column,relationship
from app.db import db 
from sqlalchemy_serializer import SerializerMixin 
from typing import List
from sqlalchemy import CheckConstraint
from sqlalchemy.ext.associationproxy import association_proxy

class Camper(db.Model,SerializerMixin):
    __tablename__="campers"

    serialize_rules=("-signups.camper",)

    id:Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]=mapped_column(nullable=False)
    age:Mapped[int]

    signups:Mapped[List["Signup"]]=relationship(back_populates="camper",cascade="all,delete-orphan")
    activities=association_proxy("signups","activity",creator=lambda activity_obj:Signup(activity=activity_obj))

    __table_args__=(
        CheckConstraint('age >=8 AND age <=18'),
    )
    
    def __repr__(self):
        return f"<Camper {self.id} {self.name}>"