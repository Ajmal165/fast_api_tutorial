from pydantic import BaseModel


class Notes(BaseModel):
    title: str
    desc: str
    important: bool = None