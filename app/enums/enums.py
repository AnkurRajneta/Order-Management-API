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


class Permission(str, enum.Enum):
    CREATE_USER_CONTROLLER = "create_user_controller"
    UPDATE_USER_BY_ID_CONTROLLER = "update_user_by_id_controller"
    DELETE_USER_BY_ID_CONTROLLER = "delete_user_by_id_controller"
    CREATE_ROLE_CONTROLLER = "create_role_controller"
    UPDATE_ROLE_BY_CONTROLLER = "update_role_by_controller"
    DELETE_ROLE_BY_ID_CONTROLLER = "delete_role_by_id_controller"
    CREATE_PRODUCT_CONTROLLER = "create_product_controller"
    UPDATE_PRODUCT_BY_ID_CONTROLLER = "update_product_by_id_controller"
    DELETE_PRODUCT_BY_ID_CONTROLLER = "delete_product_by_id_controller"
    GET_ALL_ORDER_CONTROLLER = "get_all_order_controller"
    UPDATE_ORDER_BY_ID = "update_order_by_id"
    GET_PRODUCT_ALL_CONTROLLER = "get_product_all_controller"
    CREATE_ORDER_CONTROLLER = "create_order_controller"
    GET_ORDER_BY_ID_CONTROLLER = "get_order_by_id_controller"