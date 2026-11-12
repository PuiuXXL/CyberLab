from typing import Annotated

from pydantic import BaseModel, ConfigDict, StringConstraints


class LoginRequest(BaseModel):
    username: Annotated[
        str,
        StringConstraints(strip_whitespace=True, min_length=1, max_length=100),
    ]


class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    username: str