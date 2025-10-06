from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class CruiseInfo(db.Model, IDto):
    __tablename__ = "cruise_info"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    route_id = db.Column(db.Integer, db.ForeignKey("routes.id"), nullable=False)
    routes = db.relationship("Routes", backref="cruise_info")
    ship_name = db.Column(db.String(100), nullable=False)
    port_of_departure = db.Column(db.String(100), nullable=False)
    port_of_arrival = db.Column(db.String(100), nullable=False)

    def __repr__(self) -> str:
        return f"'{self.id}', {self.route_id}, {self.ship_name}, {self.port_of_departure}, {self.port_of_arrival}"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "route_id": self.route_id,
            "ship_name": self.ship_name,
            "port_of_departure": self.port_of_departure,
            "port_of_arrival": self.port_of_arrival
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> CruiseInfo:
        obj = CruiseInfo(**dto_dict)
        return obj
