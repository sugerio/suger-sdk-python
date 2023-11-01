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
from pydantic import BaseModel, Field, StrictInt, StrictStr


class GcpPriceValue(BaseModel):
    """
    GcpPriceValue
    """

    currency_code: Optional[StrictStr] = Field(
        None, alias="currencyCode", description='such as "USD"'
    )
    nanos: Optional[StrictInt] = Field(
        None, description="for the decimal part, such as 30000000 = $0.03"
    )
    units: Optional[StrictStr] = Field(
        None, description='for the integer part, such as "500000" = $50K'
    )
    __properties = ["currencyCode", "nanos", "units"]

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
    def from_json(cls, json_str: str) -> GcpPriceValue:
        """Create an instance of GcpPriceValue from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GcpPriceValue:
        """Create an instance of GcpPriceValue from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GcpPriceValue.parse_obj(obj)

        _obj = GcpPriceValue.parse_obj(
            {
                "currency_code": obj.get("currencyCode"),
                "nanos": obj.get("nanos"),
                "units": obj.get("units"),
            }
        )
        return _obj
