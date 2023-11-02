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
from pydantic import BaseModel, Field, conlist
from openapi_client.models.alibaba_marketplace_product_extra import AlibabaMarketplaceProductExtra

class AlibabaMarketplaceProductExtras(BaseModel):
    """
    AlibabaMarketplaceProductExtras
    """
    product_extra: Optional[conlist(AlibabaMarketplaceProductExtra)] = Field(None, alias="ProductExtra")
    __properties = ["ProductExtra"]

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
    def from_json(cls, json_str: str) -> AlibabaMarketplaceProductExtras:
        """Create an instance of AlibabaMarketplaceProductExtras from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in product_extra (list)
        _items = []
        if self.product_extra:
            for _item in self.product_extra:
                if _item:
                    _items.append(_item.to_dict())
            _dict['ProductExtra'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AlibabaMarketplaceProductExtras:
        """Create an instance of AlibabaMarketplaceProductExtras from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AlibabaMarketplaceProductExtras.parse_obj(obj)

        _obj = AlibabaMarketplaceProductExtras.parse_obj({
            "product_extra": [AlibabaMarketplaceProductExtra.from_dict(_item) for _item in obj.get("ProductExtra")] if obj.get("ProductExtra") is not None else None
        })
        return _obj


