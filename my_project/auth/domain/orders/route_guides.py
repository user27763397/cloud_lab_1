from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class RouteGuides(db.Model, IDto):
    __tablename__ = "route_guides"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    route_id = db.Column(db.Integer, db.ForeignKey("routes.id"), nullable=False)
    routes = db.relationship("Routes", backref="route_guides")
    guide_id = db.Column(db.Integer, db.ForeignKey("guides.id"), nullable=False)
    guides = db.relationship("Guides", backref="route_guides")
    work_date = db.Column(db.Date, nullable=False)

    def __repr__(self) -> str:
        return f"'{self.id}', {self.route_id}, {self.guide_id}, {self.work_date}"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "route_id": self.route_id,
            "guide_id": self.guide_id,
            "work_date": self.work_date
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> RouteGuides:
        obj = RouteGuides(**dto_dict)
        return obj
