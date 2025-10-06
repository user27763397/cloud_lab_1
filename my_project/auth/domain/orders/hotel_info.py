from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class HotelInfo(db.Model, IDto):
    __tablename__ = "hotel_info"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    route_id = db.Column(db.Integer, db.ForeignKey("routes.id"), nullable=False)
    routes = db.relationship("Routes", backref="hotel_info")
    hotel_name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    amenities = db.Column(db.String(100), nullable=False)

    def __repr__(self) -> str:
        return f"'{self.id}', {self.route_id}, {self.hotel_name}, {self.address}, {self.amenities}"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "route_id": self.route_id,
            "hotel_name": self.hotel_name,
            "address": self.address,
            "amenities": self.amenities
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> HotelInfo:
        obj = HotelInfo(**dto_dict)
        return obj
