from enum import Enum


class Permission(str, Enum):
    # ===== USERS =====
    CREATE_USER = "create_user"
    VIEW_USERS = "view_users"

    # ===== INVOICES =====
    CREATE_INVOICE = "create_invoice"
    CANCEL_INVOICE = "cancel_invoice"
    VIEW_INVOICES = "view_invoices"

    # ===== REPORTS =====
    VIEW_REPORTS = "view_reports"
