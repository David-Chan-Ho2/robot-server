from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from uuid import UUID
from sqlalchemy.orm import Session

from schemas.robots import RobotCreate, RobotResponse, RobotUpdate
from crud import robots as crud
from config.database import get_db

router = APIRouter()

@router.get("", response_model=List[RobotResponse], status_code=status.HTTP_200_OK)
def read_robots(
    limit: int = 10,
    offset: int = 0,
    db: Session = Depends(get_db)
):
    if limit:
        return crud.get_robots(db, limit, offset)
    
    return crud.get_robots_all(db)

@router.get("/{robot_id}", response_model=RobotResponse, status_code=status.HTTP_200_OK)
def read_robot(
    robot_id: UUID,
    db: Session = Depends(get_db)
):
    robot = crud.get_robot(db, robot_id)
    if not robot:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Robot not found")
    return robot

@router.post("", response_model=RobotResponse, status_code=status.HTTP_201_CREATED)
def create_robot(
    payload: RobotCreate, 
    db: Session = Depends(get_db)
):
    return crud.create_robot(db, payload)

@router.patch("/{robot_id}", response_model=RobotResponse, status_code=status.HTTP_200_OK)
def update_robot(
    robot_id: UUID,
    payload: RobotUpdate, 
    db: Session = Depends(get_db)
):
    robot = crud.update_robot(db, robot_id, payload)
    if not robot:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Robot not found")
    return robot

@router.delete("/{robot_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_robot(
    robot_id: UUID,
    db: Session = Depends(get_db)
):
    robot = crud.delete_robot(db, robot_id)
    if not robot:
        raise HTTPException(status.HTTP_304_NOT_MODIFIED, detail="Robot was not deleted")
    return {"message": "robot removed"}
