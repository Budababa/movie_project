from pydantic import BaseModel, Field

class MovieBase(BaseModel):
    title: str = Field(..., example="Inception")
    year: int = Field(..., example=2010)
    genre: str = Field(..., example="Sci-Fi")
    rating: float = Field(..., example=8.8)

class MovieCreate(MovieBase):
    pass

class MovieRead(MovieBase):
    id: int

    class Config:
        from_attributes = True
