import sys, os
sys.path.insert(0, os.path.abspath('..'))

from fastapi import APIRouter, Depends, status, HTTPException
from blog import schemas, database, models
from blog.hashing import Hash
from sqlalchemy.orm import Session

router = APIRouter(
    prefix='/user',
    tags=['Users']
)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowUser)
async def get_user(id: int, db: Session = Depends(database.get_db)):
    user = db.query(models.User).get(id)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail={'message': f'User with id {id} doesnt exist'}
        )

    return user


@router.post('/create', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser)
async def create_user(request: schemas.User, db: Session = Depends(database.get_db)):
    new_user = models.User(
        username=request.username, email=request.email, password=Hash.bcrypt(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
