from typing import Optional, List
from pydantic import BaseModel


class MatchedEntity(BaseModel):
    first_name: str
    last_name: str
    probability: str


class MatchedEntities(BaseModel):
    matches: List[MatchedEntity]


class IndividualAttributes(BaseModel):
    first_name: str
    last_name: str
    birthdate: Optional[str] = "0000-01-01"
    identification: Optional[str] = "MISSING"


class MatchingRule(BaseModel):
    first_name: Optional[dict]
    last_name: Optional[dict]
    birthdate: Optional[dict]
    identification: Optional[dict]