from sqlalchemy.orm import Session

from app.db.models.audit_log import AuditLog


class AuditRepository:
    """
    Repositorio encargado de registrar acciones de auditoría.
    """

    def log(
        self,
        db: Session,
        *,
        user_id: int | None,
        action: str,
        entity: str,
        entity_id: int | None = None,
        extra_data: dict | None = None,
    ) -> None:
        audit = AuditLog(
            user_id=user_id,
            action=action,
            entity=entity,
            entity_id=entity_id,
            extra_data=extra_data,
        )

        db.add(audit)
        db.commit()
