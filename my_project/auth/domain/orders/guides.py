from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Guides(db.Model, IDto):
    __tablename__ = "guides"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    contact_info = db.Column(db.String(100), nullable=False)

    def __repr__(self) -> str:
        return f"'{self.id}', {self.first_name}, {self.last_name}, {self.contact_info}"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "contact_info": self.contact_info
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Guides:
        obj = Guides(**dto_dict)
        return obj
