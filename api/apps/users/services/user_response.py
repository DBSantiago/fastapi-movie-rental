from api.apps.users.services import UserManager
from api.core.security.permissions import MethodPermissions
from api.utils.responses.response_manager import ResponseManager


class UserResponseManager(ResponseManager):
    query_manager = UserManager
    method_permissions = MethodPermissions.ADMIN
