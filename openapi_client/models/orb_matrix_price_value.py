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


from typing import List, Optional
from pydantic import BaseModel, StrictStr, conlist

class OrbMatrixPriceValue(BaseModel):
    """
    OrbMatrixPriceValue
    """
    dimension_values: Optional[conlist(StrictStr)] = None
    unit_amount: Optional[StrictStr] = None
    __properties = ["dimension_values", "unit_amount"]

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
    def from_json(cls, json_str: str) -> OrbMatrixPriceValue:
        """Create an instance of OrbMatrixPriceValue from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OrbMatrixPriceValue:
        """Create an instance of OrbMatrixPriceValue from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OrbMatrixPriceValue.parse_obj(obj)

        _obj = OrbMatrixPriceValue.parse_obj({
            "dimension_values": obj.get("dimension_values"),
            "unit_amount": obj.get("unit_amount")
        })
        return _obj


