from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class RouteTypes(db.Model, IDto):
    __tablename__ = "route_types"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    type_name = db.Column(db.String(100), nullable=False)

    def __repr__(self) -> str:
        return f"'{self.id}', {self.type_name}"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "type_name": self.type_name
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> RouteTypes:
        obj = RouteTypes(**dto_dict)
        return obj
