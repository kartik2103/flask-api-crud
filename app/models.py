from pydantic import BaseModel

class Profile(BaseModel):
    name: str
    age: int
    email: str
    callback_url: str
