from app.core.permissions import Permission


ROLE_PERMISSIONS: dict[str, set[Permission]] = {
    "admin": {
        Permission.CREATE_USER,
        Permission.VIEW_USERS,
        Permission.CREATE_INVOICE,
        Permission.CANCEL_INVOICE,
        Permission.VIEW_INVOICES,
        Permission.VIEW_REPORTS,
    },
    "user": {
        Permission.CREATE_INVOICE,
        Permission.VIEW_INVOICES,
    },
}
