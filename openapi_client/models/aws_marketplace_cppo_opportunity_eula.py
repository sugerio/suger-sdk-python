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
from pydantic import BaseModel, Field, StrictStr

class AwsMarketplaceCppoOpportunityEula(BaseModel):
    """
    AwsMarketplaceCppoOpportunityEula
    """
    access_url: Optional[StrictStr] = Field(None, alias="accessUrl", description="The S3 signed URL of the EULA file.")
    key: Optional[StrictStr] = None
    object_url: Optional[StrictStr] = Field(None, alias="objectUrl")
    __properties = ["accessUrl", "key", "objectUrl"]

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
    def from_json(cls, json_str: str) -> AwsMarketplaceCppoOpportunityEula:
        """Create an instance of AwsMarketplaceCppoOpportunityEula from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AwsMarketplaceCppoOpportunityEula:
        """Create an instance of AwsMarketplaceCppoOpportunityEula from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AwsMarketplaceCppoOpportunityEula.parse_obj(obj)

        _obj = AwsMarketplaceCppoOpportunityEula.parse_obj({
            "access_url": obj.get("accessUrl"),
            "key": obj.get("key"),
            "object_url": obj.get("objectUrl")
        })
        return _obj


