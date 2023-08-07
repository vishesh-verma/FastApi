# Use this as a controller where database operation are done
from sqlalchemy.orm import Session

from . import models, schemas


def create_file(db: Session, file: schemas.UserIdCreate):
    db_user = models.File(filename=file.filename,user_ids=file.userids,content=file.content )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


