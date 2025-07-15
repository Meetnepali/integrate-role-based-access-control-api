from pydantic import BaseModel

class UserProfileResponse(BaseModel):
    id: int
    username: str
    email: str
    role: str
