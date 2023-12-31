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

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, StrictStr

class AwsMarketplaceEventBridgeEventOffer(BaseModel):
    """
    AwsMarketplaceEventBridgeEventOffer
    """
    arn: Optional[StrictStr] = None
    expiration_date: Optional[datetime] = Field(None, alias="expirationDate")
    id: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    __properties = ["arn", "expirationDate", "id", "name"]

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
    def from_json(cls, json_str: str) -> AwsMarketplaceEventBridgeEventOffer:
        """Create an instance of AwsMarketplaceEventBridgeEventOffer from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AwsMarketplaceEventBridgeEventOffer:
        """Create an instance of AwsMarketplaceEventBridgeEventOffer from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AwsMarketplaceEventBridgeEventOffer.parse_obj(obj)

        _obj = AwsMarketplaceEventBridgeEventOffer.parse_obj({
            "arn": obj.get("arn"),
            "expiration_date": obj.get("expirationDate"),
            "id": obj.get("id"),
            "name": obj.get("name")
        })
        return _obj


