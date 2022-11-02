import random
from typing import Any

from faker import Faker

from api.apps.users.models import UserModel, UserRoleModel
from api.core.security.hasher import Hasher
from api.db.session import SessionLocal

from api.utils.commands.faker_gen import FakerBase

fake = Faker()


class FakerUser(FakerBase):
    """Class for generating User records on the database."""
    model = UserModel

    @staticmethod
    def generate_admin_user():
        with SessionLocal() as db:
            if db.query(UserModel).filter(
                    UserModel.username == "admincito").first():
                return None

            data = {
                "username": "admincito",
                "password": Hasher.hash_password("admincito"),
                "email": "email@email.com",
                "role": db.query(UserRoleModel).filter(
                    UserRoleModel.role == "ADMIN").first()
            }

            admin = UserModel(**data)
            db.add(admin)
            db.commit()
            db.refresh(admin)

    @classmethod
    def generate_roles(cls):
        with SessionLocal() as db:
            all_roles = {role.role for role in db.query(UserRoleModel).all()}
            roles = {
                'ADMIN': 100,
                'EMPLOYEE': 10,
            }

            for role in set(roles.keys()).difference(all_roles):
                obj = UserRoleModel(
                    role=role, permission_level=roles.get(role))
                db.add(obj)
                db.commit()
                db.refresh(obj)

    @classmethod
    def set_up(cls) -> dict[str, Any]:
        name = fake.name().split()
        username = name[0][:3].lower() + name[1].lower()
        password = fake.password()
        email = fake.safe_email()

        return {
            "username": username,
            "password": Hasher.hash_password(password),
            "email": email,
        }

    @classmethod
    def generate_records(cls):
        cls.generate_roles()
        cls.generate_admin_user()
        with SessionLocal() as db:
            roles = db.query(UserRoleModel).all()

        for _ in range(cls.records):
            role = random.choice(roles)
            cls.generate_single_record(role=role)
