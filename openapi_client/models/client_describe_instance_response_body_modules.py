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
from openapi_client.models.client_describe_instance_response_body_modules_module import (
    ClientDescribeInstanceResponseBodyModulesModule,
)


class ClientDescribeInstanceResponseBodyModules(BaseModel):
    """
    ClientDescribeInstanceResponseBodyModules
    """

    module: Optional[conlist(ClientDescribeInstanceResponseBodyModulesModule)] = Field(
        None, alias="Module"
    )
    __properties = ["Module"]

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
    def from_json(cls, json_str: str) -> ClientDescribeInstanceResponseBodyModules:
        """Create an instance of ClientDescribeInstanceResponseBodyModules from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in module (list)
        _items = []
        if self.module:
            for _item in self.module:
                if _item:
                    _items.append(_item.to_dict())
            _dict["Module"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ClientDescribeInstanceResponseBodyModules:
        """Create an instance of ClientDescribeInstanceResponseBodyModules from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ClientDescribeInstanceResponseBodyModules.parse_obj(obj)

        _obj = ClientDescribeInstanceResponseBodyModules.parse_obj(
            {
                "module": [
                    ClientDescribeInstanceResponseBodyModulesModule.from_dict(_item)
                    for _item in obj.get("Module")
                ]
                if obj.get("Module") is not None
                else None
            }
        )
        return _obj