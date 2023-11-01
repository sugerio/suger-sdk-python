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
from pydantic import BaseModel, Field, StrictFloat, StrictInt

class UsageCount(BaseModel):
    """
    UsageCount
    """
    credit_count: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="creditCount", description="The count of this dimension usage records that are handled as credit.")
    included_count: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="includedCount", description="The count of this dimension usage records that are handled as included in IncludedBaseQuantity")
    reported_count: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="reportedCount", description="The count of this dimension usage records that are reported to cloud vendors.")
    __properties = ["creditCount", "includedCount", "reportedCount"]

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
    def from_json(cls, json_str: str) -> UsageCount:
        """Create an instance of UsageCount from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UsageCount:
        """Create an instance of UsageCount from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UsageCount.parse_obj(obj)

        _obj = UsageCount.parse_obj({
            "credit_count": obj.get("creditCount"),
            "included_count": obj.get("includedCount"),
            "reported_count": obj.get("reportedCount")
        })
        return _obj


