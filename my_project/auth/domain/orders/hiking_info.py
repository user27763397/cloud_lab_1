from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class HikingInfo(db.Model, IDto):
    __tablename__ = "hiking_info"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    route_id = db.Column(db.Integer, db.ForeignKey("routes.id"), nullable=False)
    routes = db.relationship("Routes", backref="hiking_info")
    difficulty_level =  db.Column(db.String(100), nullable=False)
    distance_km = db.Column(db.Float, nullable=False)
    elevation_gain_m = db.Column(db.Integer, nullable=False)

    def __repr__(self) -> str:
        return f"'{self.id}', {self.route_id}, {self.difficulty_level}, {self.distance_km}, {self.elevation_gain_m}"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "route_id": self.route_id,
            "difficulty_level": self.difficulty_level,
            "distance_km": self.distance_km,
            "elevation_gain_m": self.elevation_gain_m
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> HikingInfo:
        obj = HikingInfo(**dto_dict)
        return obj
