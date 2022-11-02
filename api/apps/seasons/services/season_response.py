from api.core.security.permissions import MethodPermissions
from api.db.managers.query_manager import QueryManager
from api.utils.responses.response_manager import ResponseManager


class SeasonResponseManager(ResponseManager):
    query_manager = QueryManager
    method_permissions = MethodPermissions.ADMIN_OR_READ
