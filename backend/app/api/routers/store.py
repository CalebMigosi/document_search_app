import os
import sys

SCRIPT_DIR = os.path.dirname(__file__)
SCRIPT_DIR = os.path.join(SCRIPT_DIR, os.pardir, os.pardir, os.pardir)
sys.path.append(os.path.abspath(SCRIPT_DIR))

from models.check import MatchedEntity, MatchedEntities # noqa
from api.dependencies.es_conn import update_single_entry, update_bulk_entries # noqa

# import logging
from fastapi import APIRouter, Depends, Form # noqa
from typing import Union, List, Dict # noqa

store = APIRouter()


@store.post("/store", tags=["store"])
async def store_single_entry(result: Dict = Depends(update_single_entry)):
    return result


@store.post("/store_bulk", tags=["store"])
async def store_bulk_entries(result: Dict = Depends(update_bulk_entries)):
    return result
