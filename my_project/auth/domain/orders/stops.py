from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Stops(db.Model, IDto):
    __tablename__ = "stops"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(150), nullable=False)

    def __repr__(self) -> str:
        return f"'{self.id}', {self.name}, {self.location}"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "location": self.location
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Stops:
        obj = Stops(**dto_dict)
        return obj
