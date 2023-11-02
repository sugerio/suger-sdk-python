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
from pydantic import BaseModel, conlist
from openapi_client.models.orb_price_tier import OrbPriceTier

class OrbPriceModelConfigBULKBPS(BaseModel):
    """
    OrbPriceModelConfigBULKBPS
    """
    tiers: Optional[conlist(OrbPriceTier)] = None
    __properties = ["tiers"]

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
    def from_json(cls, json_str: str) -> OrbPriceModelConfigBULKBPS:
        """Create an instance of OrbPriceModelConfigBULKBPS from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in tiers (list)
        _items = []
        if self.tiers:
            for _item in self.tiers:
                if _item:
                    _items.append(_item.to_dict())
            _dict['tiers'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OrbPriceModelConfigBULKBPS:
        """Create an instance of OrbPriceModelConfigBULKBPS from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OrbPriceModelConfigBULKBPS.parse_obj(obj)

        _obj = OrbPriceModelConfigBULKBPS.parse_obj({
            "tiers": [OrbPriceTier.from_dict(_item) for _item in obj.get("tiers")] if obj.get("tiers") is not None else None
        })
        return _obj


