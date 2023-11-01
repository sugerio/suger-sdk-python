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
from openapi_client.models.alibaba_marketplace_product_sku import (
    AlibabaMarketplaceProductSku,
)


class AlibabaMarketplaceProductSkus(BaseModel):
    """
    AlibabaMarketplaceProductSkus
    """

    product_sku: Optional[conlist(AlibabaMarketplaceProductSku)] = Field(
        None, alias="ProductSku"
    )
    __properties = ["ProductSku"]

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
    def from_json(cls, json_str: str) -> AlibabaMarketplaceProductSkus:
        """Create an instance of AlibabaMarketplaceProductSkus from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in product_sku (list)
        _items = []
        if self.product_sku:
            for _item in self.product_sku:
                if _item:
                    _items.append(_item.to_dict())
            _dict["ProductSku"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AlibabaMarketplaceProductSkus:
        """Create an instance of AlibabaMarketplaceProductSkus from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AlibabaMarketplaceProductSkus.parse_obj(obj)

        _obj = AlibabaMarketplaceProductSkus.parse_obj(
            {
                "product_sku": [
                    AlibabaMarketplaceProductSku.from_dict(_item)
                    for _item in obj.get("ProductSku")
                ]
                if obj.get("ProductSku") is not None
                else None
            }
        )
        return _obj
