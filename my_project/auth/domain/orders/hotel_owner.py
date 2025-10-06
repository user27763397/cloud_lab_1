from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class HotelOwner(db.Model, IDto):
    __tablename__ = "hotel_owner"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    hotel_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(255), nullable=False)

    def __repr__(self) -> str:
        return f"'{self.id}', {self.hotel_id}, {self.name}"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "hotel_id": self.hotel_id,
            "name": self.name,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> HotelOwner:
        obj = HotelOwner(**dto_dict)
        return obj
