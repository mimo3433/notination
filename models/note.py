from pydantic import BaseModel


class Note(BaseModel):
    Title: str
    Description: str
    highpriority: bool = False