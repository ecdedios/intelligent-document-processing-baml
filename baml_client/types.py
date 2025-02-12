###############################################################################
#
#  Welcome to Baml! To use this generated code, please run the following:
#
#  $ pip install baml
#
###############################################################################

# This file was generated by BAML: please do not edit it. Instead, edit the
# BAML files and re-generate this code.
#
# ruff: noqa: E501,F401
# flake8: noqa: E501,F401
# pylint: disable=unused-import,line-too-long
# fmt: off
import baml_py
from enum import Enum
from pydantic import BaseModel, ConfigDict
from typing import Dict, Generic, List, Literal, Optional, TypeVar, Union, TypeAlias


T = TypeVar('T')
CheckName = TypeVar('CheckName', bound=str)

class Check(BaseModel):
    name: str
    expression: str
    status: str

class Checked(BaseModel, Generic[T,CheckName]):
    value: T
    checks: Dict[CheckName, Check]

def get_checks(checks: Dict[CheckName, Check]) -> List[Check]:
    return list(checks.values())

def all_succeeded(checks: Dict[CheckName, Check]) -> bool:
    return all(check.status == "succeeded" for check in get_checks(checks))



class Appointment(BaseModel):
    day_of_week: str
    month: str
    date: int
    year: int
    hour: int
    minute: int
    ampm: str

class DropOffPackageReceipt(BaseModel):
    line_item: List["ReceiptItem"]
    location: str
    address: str
    day_of_week: str
    day: int
    month: str
    year: int
    hour: int
    minute: int
    ampm: str
    total_packages: int
    total_packages_ui: str

class NutritionLabel(BaseModel):
    product: str
    description: str
    calories: int
    fat: int
    fat_ui: str
    fat_dv: float
    sodium: int
    sodium_ui: str
    sodium_dv: float
    carb: int
    carb_ui: str
    carb_dv: float
    protein: int
    protein_ui: str
    protein_dv: Optional[float] = None

class ReceiptItem(BaseModel):
    tracking_number: str
    weight: float
    weight_ui: str
