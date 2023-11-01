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


from typing import Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr, validator


class AzureMarketplaceTerm(BaseModel):
    """
    AzureMarketplaceTerm
    """

    type: Optional[StrictStr] = None
    value: Optional[Union[StrictFloat, StrictInt]] = Field(
        None, description="default 0"
    )
    __properties = ["type", "value"]

    @validator("type")
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ("day", "week", "month", "year"):
            raise ValueError(
                "must be one of enum values ('day', 'week', 'month', 'year')"
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
    def from_json(cls, json_str: str) -> AzureMarketplaceTerm:
        """Create an instance of AzureMarketplaceTerm from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AzureMarketplaceTerm:
        """Create an instance of AzureMarketplaceTerm from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AzureMarketplaceTerm.parse_obj(obj)

        _obj = AzureMarketplaceTerm.parse_obj(
            {"type": obj.get("type"), "value": obj.get("value")}
        )
        return _obj
