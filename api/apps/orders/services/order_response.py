from api.apps.orders.services.order_manager import OrderManager
from api.core.security.permissions import MethodPermissions
from api.utils.responses.response_manager import ResponseManager


class OrderResponseManager(ResponseManager):
    query_manager = OrderManager
    method_permissions = MethodPermissions.EMPLOYEE
