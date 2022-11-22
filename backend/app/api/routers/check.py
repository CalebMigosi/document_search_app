import os
import sys

SCRIPT_DIR = os.path.dirname(__file__)
SCRIPT_DIR = os.path.join(SCRIPT_DIR, os.pardir, os.pardir, os.pardir)
sys.path.append(os.path.abspath(SCRIPT_DIR))

from models.check import MatchedEntity, MatchedEntities # noqa
from api.dependencies.es_conn import search_user_in_es, update_matching_rule # noqa

# import logging
from fastapi import APIRouter, Depends, Form # noqa
from typing import Union, List, Dict # noqa

check = APIRouter()


@check.post("/check", tags=["check"])
async def check_user(result: Union[MatchedEntity, MatchedEntities] = Depends(search_user_in_es)): # noqa
    return result


@check.post("/check/update_matching_rule", tags=["check"])
async def update_matching_rule(result: dict = Depends(update_matching_rule)):
    return result
