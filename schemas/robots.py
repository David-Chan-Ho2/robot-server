from pydantic import BaseModel, ConfigDict, Field
from typing import Optional, Annotated
from uuid import UUID

class RobotBase(BaseModel):
    name: Annotated[str, Field(min_length=3, max_length=20)]

class RobotCreate(RobotBase):
    pass
    
class RobotUpdate(BaseModel):
    name: Optional[str] = None
    
class RobotResponse(RobotBase):
    id: UUID
    
    model_config = ConfigDict(from_attributes=True)
