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
from openapi_client.models.client_describe_instance_response_body_modules_module_properties_property_property_values import ClientDescribeInstanceResponseBodyModulesModulePropertiesPropertyPropertyValues

class ClientDescribeInstanceResponseBodyModulesModulePropertiesProperty(BaseModel):
    """
    ClientDescribeInstanceResponseBodyModulesModulePropertiesProperty
    """
    display_unit: Optional[StrictStr] = Field(None, alias="DisplayUnit")
    key: Optional[StrictStr] = Field(None, alias="Key")
    name: Optional[StrictStr] = Field(None, alias="Name")
    property_values: Optional[ClientDescribeInstanceResponseBodyModulesModulePropertiesPropertyPropertyValues] = Field(None, alias="PropertyValues")
    show_type: Optional[StrictStr] = Field(None, alias="ShowType")
    __properties = ["DisplayUnit", "Key", "Name", "PropertyValues", "ShowType"]

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
    def from_json(cls, json_str: str) -> ClientDescribeInstanceResponseBodyModulesModulePropertiesProperty:
        """Create an instance of ClientDescribeInstanceResponseBodyModulesModulePropertiesProperty from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of property_values
        if self.property_values:
            _dict['PropertyValues'] = self.property_values.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ClientDescribeInstanceResponseBodyModulesModulePropertiesProperty:
        """Create an instance of ClientDescribeInstanceResponseBodyModulesModulePropertiesProperty from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ClientDescribeInstanceResponseBodyModulesModulePropertiesProperty.parse_obj(obj)

        _obj = ClientDescribeInstanceResponseBodyModulesModulePropertiesProperty.parse_obj({
            "display_unit": obj.get("DisplayUnit"),
            "key": obj.get("Key"),
            "name": obj.get("Name"),
            "property_values": ClientDescribeInstanceResponseBodyModulesModulePropertiesPropertyPropertyValues.from_dict(obj.get("PropertyValues")) if obj.get("PropertyValues") is not None else None,
            "show_type": obj.get("ShowType")
        })
        return _obj


