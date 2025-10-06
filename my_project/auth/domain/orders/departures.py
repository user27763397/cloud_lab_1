from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Departures(db.Model, IDto):
    __tablename__ = "departures"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    route_id = db.Column(db.Integer, db.ForeignKey("routes.id"), nullable=False)
    routes = db.relationship("Routes", backref="departures")
    departure_date = db.Column(db.Date, nullable=False)

    def __repr__(self) -> str:
        return f"'{self.id}', {self.route_id}, {self.depature_date}"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "route_id": self.route_id,
            "departure_date": self.departure_date
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Departures:
        obj = Departures(**dto_dict)
        return obj
