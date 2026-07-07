from sqlalchemy.orm import Session
from uuid import UUID

from models.Robot import Robot
from schemas.robots import RobotCreate, RobotUpdate

def get_robots(
    db: Session, 
    limit: int, 
    offset: int
):
    robots = db.query(Robot).order_by(Robot.name)
    if limit:
        return robots.offset(offset).limit(limit)
    return robots.all()

def get_robots_all(
    db: Session
):
    robots = db.query(Robot).order_by(Robot.name)
    return robots.all()

def get_robot(
    db: Session, 
    Robot_id: UUID
):
    return db.query(Robot).where(Robot.id == Robot_id).first()

def create_robot(
    db: Session, 
    payload: RobotCreate
):
    robot = Robot(**payload.model_dump())
    db.add(robot)
    db.commit()
    db.refresh(robot)
    return robot

def update_robot(
    db: Session,
    Robot_id: UUID,
    payload: RobotUpdate,
):
    robot = get_robot(db, Robot_id)
    if not robot:
        return None
    data = payload.model_dump(exclude_unset=True)
    for k, v in data.items():
        setattr(robot, k, v)
    db.commit()
    db.refresh(robot)
    return robot

def delete_robot(
    db: Session, 
    Robot_id: UUID
):
    robot = get_robot(db, Robot_id)
    if robot:
        db.delete(robot)
        db.commit()
    return robot