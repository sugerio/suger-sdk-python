# coding: utf-8

"""
    Suger API

    CRUD operations on a set of resources, including organizations, products, offers, entitlements, usage record groups for meterting, etc.

    The version of the OpenAPI document: 1.0
    Contact: support@suger.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, validator


class AzurePricingUnit(BaseModel):
    """
    AzurePricingUnit
    """

    is_unlimited_unit: Optional[StrictBool] = Field(None, alias="isUnlimitedUnit")
    lower_unit: Optional[StrictInt] = Field(None, alias="lowerUnit")
    name: Optional[StrictStr] = None
    unit_type: Optional[StrictStr] = Field(None, alias="unitType")
    upper_unit: Optional[StrictInt] = Field(None, alias="upperUnit")
    __properties = ["isUnlimitedUnit", "lowerUnit", "name", "unitType", "upperUnit"]

    @validator("name")
    def name_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ("sharedcore", "transactions"):
            raise ValueError(
                "must be one of enum values ('sharedcore', 'transactions')"
            )
        return value

    class Config:
        """Pydantic configuration"""

        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> AzurePricingUnit:
        """Create an instance of AzurePricingUnit from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AzurePricingUnit:
        """Create an instance of AzurePricingUnit from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AzurePricingUnit.parse_obj(obj)

        _obj = AzurePricingUnit.parse_obj(
            {
                "is_unlimited_unit": obj.get("isUnlimitedUnit"),
                "lower_unit": obj.get("lowerUnit"),
                "name": obj.get("name"),
                "unit_type": obj.get("unitType"),
                "upper_unit": obj.get("upperUnit"),
            }
        )
        return _obj