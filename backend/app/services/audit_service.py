from sqlalchemy.orm import Session

from app.repositories.audit_repository import AuditRepository
from app.db.models.user import User


class AuditService:
    def __init__(self) -> None:
        self._repo = AuditRepository()

    def log_action(
        self,
        db: Session,
        *,
        user: User | None,
        action: str,
        entity: str,
        entity_id: int | None = None,
        extra_data: dict | None = None,
    ) -> None:
        self._repo.log(
            db,
            user_id=user.id if user else None,
            action=action,
            entity=entity,
            entity_id=entity_id,
            extra_data=extra_data,
        )
