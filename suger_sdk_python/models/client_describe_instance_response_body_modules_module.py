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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from suger_sdk_python.models.client_describe_instance_response_body_modules_module_properties import ClientDescribeInstanceResponseBodyModulesModuleProperties
from typing import Optional, Set
from typing_extensions import Self

class ClientDescribeInstanceResponseBodyModulesModule(BaseModel):
    """
    ClientDescribeInstanceResponseBodyModulesModule
    """ # noqa: E501
    code: Optional[StrictStr] = Field(default=None, alias="Code")
    id: Optional[StrictStr] = Field(default=None, alias="Id")
    name: Optional[StrictStr] = Field(default=None, alias="Name")
    properties: Optional[ClientDescribeInstanceResponseBodyModulesModuleProperties] = Field(default=None, alias="Properties")
    __properties: ClassVar[List[str]] = ["Code", "Id", "Name", "Properties"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ClientDescribeInstanceResponseBodyModulesModule from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of properties
        if self.properties:
            _dict['Properties'] = self.properties.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ClientDescribeInstanceResponseBodyModulesModule from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "Code": obj.get("Code"),
            "Id": obj.get("Id"),
            "Name": obj.get("Name"),
            "Properties": ClientDescribeInstanceResponseBodyModulesModuleProperties.from_dict(obj["Properties"]) if obj.get("Properties") is not None else None
        })
        return _obj


