from typing import Optional, List
from pydantic import BaseModel


class SingleIndividualAttributes(BaseModel):
    '''
        Strict implementation of the version in check
    '''
    first_name: str
    last_name: str
    birthdate: str
    identification: str


class BulkIndividualAttributes(BaseModel):
    entries: List[SingleIndividualAttributes]