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
from openapi_client.models.orb_external_connection import OrbExternalConnection

class OrbItem(BaseModel):
    """
    OrbItem
    """
    created_at: Optional[StrictStr] = None
    external_connections: Optional[conlist(OrbExternalConnection)] = None
    id: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    __properties = ["created_at", "external_connections", "id", "name"]

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
    def from_json(cls, json_str: str) -> OrbItem:
        """Create an instance of OrbItem from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in external_connections (list)
        _items = []
        if self.external_connections:
            for _item in self.external_connections:
                if _item:
                    _items.append(_item.to_dict())
            _dict['external_connections'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OrbItem:
        """Create an instance of OrbItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OrbItem.parse_obj(obj)

        _obj = OrbItem.parse_obj({
            "created_at": obj.get("created_at"),
            "external_connections": [OrbExternalConnection.from_dict(_item) for _item in obj.get("external_connections")] if obj.get("external_connections") is not None else None,
            "id": obj.get("id"),
            "name": obj.get("name")
        })
        return _obj


