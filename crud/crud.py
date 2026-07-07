from sqlalchemy.orm import Session
from uuid import UUID
from fastapi import Depends

from config.database import get_db

class Crud:
    
    def __init__(self, session):
        self.db = session
        
    def set_model(self, model):
        self.model = model
    
    def get_all(self, limit: int, offset: int):
        items = self.db.query(self.model)
        if limit:
            return items.offset(offset).limit(limit)
        return items.all()
    
    def get_one(self, uid: UUID):
        return self.db.query(self.model).where(self.model.id == uid).first()
    
    def create(self, payload):
        new_item = self.model(**payload.model_dump())
        self.db.add(new_item)
        self.db.commit()
        self.db.refresh(new_item)
        return new_item
    
    def update(self, uid, payload):
        item = self.get_one(uid)
        if not item:
            return None
        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(item, k, v)
        self.db.commit()
        self.db.refresh(item)
        return item

    
    def delete(self, uid):
        item = self.get_one(uid)
        if item:
            self.db.delete(item)
            self.db.commit()
        return item

crud = Crud(Depends(get_db))