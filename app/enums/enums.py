import enum

class TableName:
    ROLE = "role"
    PERMISSION = "permission"
    USER = "user"
    PRODUCT = "product"
    ORDERS = "orders"
    ORDERITEMS = "orderitems"

class Stock(str, enum.Enum):
    AVAILABLE = "available"
    UNAVAILABLE = "unavailable"

class Status(str, enum.Enum):
    CONFIRMED = "confirmed"
    FAILED = "failed"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    PENDING = "pending"


class UserRoleEnum(str, enum.Enum):
    ADMIN = "Admin"
    MANAGER = "Manager"
    CUSTOMER = "Customer"


class Category(str, enum.Enum):
    HOME = "home"