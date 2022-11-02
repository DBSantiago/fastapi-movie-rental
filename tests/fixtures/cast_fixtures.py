import pytest

from api.apps.cast.models import GenderModel, RoleModel, MemberModel
from api.apps.cast.schemas import GenderResponse, RoleResponse, MemberResponse


@pytest.fixture
def cast_gender(client, session):
    gender = GenderModel(
        gender="Female"
    )

    session.add(gender)
    session.commit()
    session.refresh(gender)

    return GenderResponse.from_orm(gender)


@pytest.fixture
def cast_role(client, session):
    role = RoleModel(
        role="Director"
    )

    session.add(role)
    session.commit()
    session.refresh(role)

    return RoleResponse.from_orm(role)


@pytest.fixture
def cast_member(client, session, cast_gender, cast_role):
    member = MemberModel(
        name="Jane",
        last_name="Doe",
        gender_id=cast_gender.id,
        role_id=cast_role.id
    )

    session.add(member)
    session.commit()
    session.refresh(member)

    return MemberResponse.from_orm(member)
