from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class BusInfo(db.Model, IDto):
    __tablename__ = "bus_info"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    route_id = db.Column(db.Integer, db.ForeignKey("routes.id"), nullable=False)
    routes = db.relationship("Routes", backref="bus_info")
    bus_company = db.Column(db.String(100), nullable=False)
    vehicle_type = db.Column(db.String(100), nullable=False)

    def __repr__(self) -> str:
        return f"'{self.id}', {self.route_id}, {self.bus_company}, {self.vehicle_type}"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "route_id": self.route_id,
            "bus_company": self.bus_company,
            "vehicle_type": self.vehicle_type
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> BusInfo:
        obj = BusInfo(**dto_dict)
        return obj
