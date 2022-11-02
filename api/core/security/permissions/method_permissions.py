from api.core.business import Business


class MethodPermissions:
    ADMIN = {
        "GET": Business.ADMIN_ROLE,
        "POST": Business.ADMIN_ROLE,
        "PUT": Business.ADMIN_ROLE,
        "DELETE": Business.ADMIN_ROLE,
    }
    ADMIN_OR_READ = {
        "GET": Business.ANON_ROLE,
        "POST": Business.ADMIN_ROLE,
        "PUT": Business.ADMIN_ROLE,
        "DELETE": Business.ADMIN_ROLE,
    }
    EMPLOYEE = {
        "GET": Business.EMPLOYEE_ROLE,
        "POST": Business.EMPLOYEE_ROLE,
        "PUT": Business.EMPLOYEE_ROLE,
        "DELETE": Business.EMPLOYEE_ROLE,
    }
    EMPLOYEE_OR_READ = {
        "GET": Business.ANON_ROLE,
        "POST": Business.EMPLOYEE_ROLE,
        "PUT": Business.EMPLOYEE_ROLE,
        "DELETE": Business.EMPLOYEE_ROLE,
    }
    ANON = {
        "GET": Business.ANON_ROLE,
        "POST": Business.ANON_ROLE,
        "PUT": Business.ANON_ROLE,
        "DELETE": Business.ANON_ROLE,
    }
