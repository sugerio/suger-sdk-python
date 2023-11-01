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


from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr, conlist

class AzureMarketplacePrice(BaseModel):
    """
    AzureMarketplacePrice
    """
    currency: Optional[StrictStr] = Field(None, description="ISO 4217 currency code")
    markets: Optional[conlist(StrictStr)] = None
    price: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="default 0")
    prices: Optional[Dict[str, Any]] = None
    __properties = ["currency", "markets", "price", "prices"]

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
    def from_json(cls, json_str: str) -> AzureMarketplacePrice:
        """Create an instance of AzureMarketplacePrice from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AzureMarketplacePrice:
        """Create an instance of AzureMarketplacePrice from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AzureMarketplacePrice.parse_obj(obj)

        _obj = AzureMarketplacePrice.parse_obj({
            "currency": obj.get("currency"),
            "markets": obj.get("markets"),
            "price": obj.get("price"),
            "prices": obj.get("prices")
        })
        return _obj


