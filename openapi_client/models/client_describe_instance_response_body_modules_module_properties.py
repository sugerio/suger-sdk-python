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
from openapi_client.models.client_describe_instance_response_body_modules_module_properties_property import (
    ClientDescribeInstanceResponseBodyModulesModulePropertiesProperty,
)


class ClientDescribeInstanceResponseBodyModulesModuleProperties(BaseModel):
    """
    ClientDescribeInstanceResponseBodyModulesModuleProperties
    """

    var_property: Optional[
        conlist(ClientDescribeInstanceResponseBodyModulesModulePropertiesProperty)
    ] = Field(None, alias="Property")
    __properties = ["Property"]

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
    def from_json(
        cls, json_str: str
    ) -> ClientDescribeInstanceResponseBodyModulesModuleProperties:
        """Create an instance of ClientDescribeInstanceResponseBodyModulesModuleProperties from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in var_property (list)
        _items = []
        if self.var_property:
            for _item in self.var_property:
                if _item:
                    _items.append(_item.to_dict())
            _dict["Property"] = _items
        return _dict

    @classmethod
    def from_dict(
        cls, obj: dict
    ) -> ClientDescribeInstanceResponseBodyModulesModuleProperties:
        """Create an instance of ClientDescribeInstanceResponseBodyModulesModuleProperties from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ClientDescribeInstanceResponseBodyModulesModuleProperties.parse_obj(
                obj
            )

        _obj = ClientDescribeInstanceResponseBodyModulesModuleProperties.parse_obj(
            {
                "var_property": [
                    ClientDescribeInstanceResponseBodyModulesModulePropertiesProperty.from_dict(
                        _item
                    )
                    for _item in obj.get("Property")
                ]
                if obj.get("Property") is not None
                else None
            }
        )
        return _obj
