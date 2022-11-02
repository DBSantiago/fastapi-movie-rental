import random
from typing import Any

from faker import Faker

from api.apps.cast.models import RoleModel, MemberModel, GenderModel
from api.db.session import SessionLocal
from api.utils.commands.faker_gen import FakerBase

fake = Faker()


class FakerRole(FakerBase):
    """Class for generating cast Role records on the database."""
    model = RoleModel

    @classmethod
    def set_up(cls) -> dict[str, Any]:
        role = fake.job()

        return {
            "role": role,
        }


class FakerCast(FakerBase):
    """Class for generating cast Member records on the database."""
    model = MemberModel

    @classmethod
    def generate_genders(cls) -> None:
        with SessionLocal() as db:
            all_genders = {gender.gender for gender
                           in db.query(GenderModel).all()}
            genders = {"Male", "Female", "Not Specified"}
            for gender in genders.difference(all_genders):
                obj = GenderModel(gender=gender)
                db.add(obj)
                db.commit()
                db.refresh(obj)

    @classmethod
    def generate_roles(cls) -> None:
        FakerRole.generate_records()

    @classmethod
    def set_up(cls) -> dict[str, Any]:
        with SessionLocal() as db:
            roles = db.query(RoleModel).all()
            genders = db.query(GenderModel).all()

            role = random.choice(roles)
            gender = random.choice(genders)

            full_name = fake.name().split()
            name = full_name[0]
            last_name = full_name[1]

        return {
            "name": name,
            "last_name": last_name,
            "role": role,
            "gender": gender,
        }

    @classmethod
    def generate_records(cls) -> None:
        cls.generate_genders()
        cls.generate_roles()
        super().generate_records()
