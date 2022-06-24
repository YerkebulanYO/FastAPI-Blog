from fastapi import FastAPI
from database import Base, engine
from routers import blog, user, authentication


app = FastAPI()

Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)

#
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


# @app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED, tags=['blogs'])
# async def update_blog(id, request: schemas.Blog, db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id)
#     if not blog.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id "{id}" doesnt exist')
#
#     blog.update(request.dict())
#     db.commit()
#     return 'updated succesfully'


# @app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=['blogs'])
# async def delete_blog(id, db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id)
#     if not blog:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id "{id}" doesnt exist')
#
#     blog.delete(synchronize_session=False)
#     db.commit()
#     return {'Blog is deleted succesfully'}

#
# @app.get('/blog/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog, tags=['blogs'])
# async def get_blog(id: int, response: Response, db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id).first()
#
#     if not blog:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={'message': 'Blog with id doesnt exist'})
#         # response.status_code = status.HTTP_404_NOT_FOUND
#         # return {'detail': f'Blog with id "{id}" is not found'}
#     return blog

#
# @app.get('/', status_code=status.HTTP_200_OK, response_model=List[schemas.ShowBlog], tags=['blogs'])
# async def get_all_blogs(db: Session = Depends(get_db)):
#     blogs = db.query(models.Blog.title, models.Blog.id).all()
#     return blogs

#
# @app.post('/blog', status_code=status.HTTP_201_CREATED, tags=['blogs'])
# async def create_blog(request: schemas.Blog, db: Session = Depends(get_db)):
#     new_blog = models.Blog(title=request.title, description=request.description, user_id=1)
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#
#     return new_blog

#
# @app.post('/create-user', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser, tags=['users'])
# async def create_user(request: schemas.User, db: Session = Depends(get_db)):
#     new_user = models.User(
#         username=request.username, email=request.email, password=Hash.bcrypt(request.password)
#     )
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#
#     return new_user
#

# @app.get('/users/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowUser, tags=['users'])
# async def get_user(id: int, db: Session = Depends(get_db)):
#     user = db.query(models.User).get(id)
#
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND, detail={'message': f'User with id {id} doesnt exist'}
#         )
#
#     return user
