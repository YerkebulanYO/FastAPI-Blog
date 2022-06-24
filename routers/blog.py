import sys, os
sys.path.insert(0, os.path.abspath('..'))

from fastapi import APIRouter, Depends, status, Response, HTTPException
from blog import database, models, schemas

from typing import List
from sqlalchemy.orm import Session


router = APIRouter(
    prefix='/blog',
    tags=['Blogs']
)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
async def get_blog(id: int, response: Response, db: Session = Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()

    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={'message': 'Blog with id doesnt exist'})
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail': f'Blog with id "{id}" is not found'}
    return blog


@router.post('/create', status_code=status.HTTP_201_CREATED)
async def create_blog(request: schemas.Blog, db: Session = Depends(database.get_db)):
    new_blog = models.Blog(title=request.title, description=request.description, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)

    return new_blog


@router.get('/', status_code=status.HTTP_200_OK, response_model=List[schemas.ShowBlog])
async def get_all_blogs(db: Session = Depends(database.get_db)):
    blogs = db.query(models.Blog.title, models.Blog.id).all()
    return blogs


@router.delete('/delete/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_blog(id: int, db: Session = Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id "{id}" doesnt exist')

    blog.delete(synchronize_session=False)
    db.commit()
    return {'Blog is deleted succesfully'}


@router.put('/update/{id}', status_code=status.HTTP_202_ACCEPTED)
async def update_blog(id, request: schemas.Blog, db: Session = Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id "{id}" doesnt exist')

    blog.update(request.dict())
    db.commit()
    return 'updated succesfully'
