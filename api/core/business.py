from decimal import Decimal


class Business:
    MAX_RENT_DAYS = 15
    DATE_FORMAT = "%Y-%m-%d"
    PENALTY_PER_DAY = Decimal("2.00")
    ADMIN_ROLE = "ADMIN"
    ADMIN_PERMISSION = 100
    EMPLOYEE_ROLE = "EMPLOYEE"
    EMPLOYEE_PERMISSION = 10
    ANON_ROLE = "ANON"
