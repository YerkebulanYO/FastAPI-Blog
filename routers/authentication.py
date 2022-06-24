import sys, os
sys.path.insert(0, os.path.abspath('..'))

from fastapi import APIRouter, Depends, status, HTTPException
from blog import database, models, schemas
from blog.hashing import Hash

from sqlalchemy.orm import Session


router = APIRouter(
    tags=['Authentication']
)


@router.post('/login')
async def login(request: schemas.Login, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.email).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User with this email doesnt exist')

    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Incorrect password')

    return user