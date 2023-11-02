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

class CompanyInfo(BaseModel):
    """
    CompanyInfo
    """
    address_line1: Optional[StrictStr] = Field(None, alias="addressLine1")
    address_line2: Optional[StrictStr] = Field(None, alias="addressLine2")
    city: Optional[StrictStr] = None
    country: Optional[StrictStr] = None
    email_domain: Optional[StrictStr] = Field(None, alias="emailDomain")
    name: Optional[StrictStr] = None
    postal_code: Optional[StrictStr] = Field(None, alias="postalCode")
    state: Optional[StrictStr] = None
    __properties = ["addressLine1", "addressLine2", "city", "country", "emailDomain", "name", "postalCode", "state"]

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
    def from_json(cls, json_str: str) -> CompanyInfo:
        """Create an instance of CompanyInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CompanyInfo:
        """Create an instance of CompanyInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CompanyInfo.parse_obj(obj)

        _obj = CompanyInfo.parse_obj({
            "address_line1": obj.get("addressLine1"),
            "address_line2": obj.get("addressLine2"),
            "city": obj.get("city"),
            "country": obj.get("country"),
            "email_domain": obj.get("emailDomain"),
            "name": obj.get("name"),
            "postal_code": obj.get("postalCode"),
            "state": obj.get("state")
        })
        return _obj


