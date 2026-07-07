import uuid

from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID

from config.database import Base

class Robot(Base):
    __tablename__ = "robots"
    
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        index=True,
        default=uuid.uuid4
    )
    name = Column(
        String,
        index=True,
        unique=True,
        nullable=False
    )
    