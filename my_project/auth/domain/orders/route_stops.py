from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class RouteStops(db.Model, IDto):
    __tablename__ = "route_stops"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    route_id = db.Column(db.Integer, db.ForeignKey("routes.id"), nullable=False)
    routes = db.relationship("Routes", backref="route_stops")
    stop_id = db.Column(db.Integer, db.ForeignKey("stops.id"), nullable=False)
    stops = db.relationship("Stops", backref="route_stops")
    stop_order = db.Column(db.Integer, nullable=False)

    def __repr__(self) -> str:
        return f"'{self.id}', {self.route_id}, {self.stop_id}, {self.stop_order}"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "route_id": self.route_id,
            "stop_id": self.stop_id,
            "stop_order": self.stop_order
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> RouteStops:
        obj = RouteStops(**dto_dict)
        return obj
