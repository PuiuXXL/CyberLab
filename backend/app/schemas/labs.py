from pydantic import BaseModel, ConfigDict


class LabResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id : int
    name : str
    category: str | None
    description: str | None
