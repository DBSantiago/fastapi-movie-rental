from api.apps.films.services import FilmManager
from api.core.security.permissions import MethodPermissions
from api.utils.responses.response_manager import ResponseManager


class FilmResponseManager(ResponseManager):
    query_manager = FilmManager
    method_permissions = MethodPermissions.ADMIN_OR_READ
