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
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr, conlist, validator
from openapi_client.models.azure_marketplace_price import AzureMarketplacePrice

class AzureMarketplacePriceAndAvailabilityCorePrice(BaseModel):
    """
    AzureMarketplacePriceAndAvailabilityCorePrice
    """
    price: Optional[Union[StrictFloat, StrictInt]] = None
    price_input_option: Optional[StrictStr] = Field(None, alias="priceInputOption")
    price_per_core: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="pricePerCore")
    price_per_core_size: Optional[Dict[str, Any]] = Field(None, alias="pricePerCoreSize")
    prices: Optional[conlist(AzureMarketplacePrice)] = None
    __properties = ["price", "priceInputOption", "pricePerCore", "pricePerCoreSize", "prices"]

    @validator('price_input_option')
    def price_input_option_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('free', 'flat', 'perCore', 'perCoreSize', 'perMarketAndCoreSize'):
            raise ValueError("must be one of enum values ('free', 'flat', 'perCore', 'perCoreSize', 'perMarketAndCoreSize')")
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
    def from_json(cls, json_str: str) -> AzureMarketplacePriceAndAvailabilityCorePrice:
        """Create an instance of AzureMarketplacePriceAndAvailabilityCorePrice from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in prices (list)
        _items = []
        if self.prices:
            for _item in self.prices:
                if _item:
                    _items.append(_item.to_dict())
            _dict['prices'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AzureMarketplacePriceAndAvailabilityCorePrice:
        """Create an instance of AzureMarketplacePriceAndAvailabilityCorePrice from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AzureMarketplacePriceAndAvailabilityCorePrice.parse_obj(obj)

        _obj = AzureMarketplacePriceAndAvailabilityCorePrice.parse_obj({
            "price": obj.get("price"),
            "price_input_option": obj.get("priceInputOption"),
            "price_per_core": obj.get("pricePerCore"),
            "price_per_core_size": obj.get("pricePerCoreSize"),
            "prices": [AzureMarketplacePrice.from_dict(_item) for _item in obj.get("prices")] if obj.get("prices") is not None else None
        })
        return _obj


