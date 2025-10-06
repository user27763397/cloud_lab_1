from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Routes(db.Model, IDto):
    __tablename__ = "routes"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    route_type_id = db.Column(db.Integer, db.ForeignKey("route_types.id"), nullable=False)
    route_types = db.relationship("RouteTypes", backref="routes")
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    duration_days = db.Column(db.Integer, nullable=False)
    price_per_person = db.Column(db.Float, nullable=False)
    next_departure_date = db.Column(db.Date)

    def __repr__(self) -> str:
        return f"'{self.id}', {self.route_type_id}, {self.name}, {self.description}, {self.duration_days}, {self.price_per_person}, {self.next_departure_date}"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "route_type_id": self.route_type_id,
            "name": self.name,
            "description": self.description,
            "duration_days": self.duration_days,
            "price_per_person": self.price_per_person,
            "next_departure_date": self.next_departure_date
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Routes:
        obj = Routes(**dto_dict)
        return obj
