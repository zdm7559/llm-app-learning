from pydantic import BaseModel, constr, conint, confloat

class StudentCreate(BaseModel):
    name: constr(strip_whitespace=True, min_length=1, max_length=20) # type: ignore
    age: conint(ge=0, le=150) # type: ignore
    score: confloat(ge=0, le=100) # type: ignore