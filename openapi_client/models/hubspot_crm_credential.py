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
from pydantic import BaseModel, Field, StrictInt, StrictStr

class HubspotCrmCredential(BaseModel):
    """
    HubspotCrmCredential
    """
    access_token: Optional[StrictStr] = Field(None, alias="accessToken")
    acquired_on: Optional[StrictInt] = Field(None, alias="acquiredOn", description="UTC timestamp on receiving the auth response")
    expires_in: Optional[StrictInt] = Field(None, alias="expiresIn")
    refresh_token: Optional[StrictStr] = Field(None, alias="refreshToken")
    __properties = ["accessToken", "acquiredOn", "expiresIn", "refreshToken"]

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
    def from_json(cls, json_str: str) -> HubspotCrmCredential:
        """Create an instance of HubspotCrmCredential from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> HubspotCrmCredential:
        """Create an instance of HubspotCrmCredential from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return HubspotCrmCredential.parse_obj(obj)

        _obj = HubspotCrmCredential.parse_obj({
            "access_token": obj.get("accessToken"),
            "acquired_on": obj.get("acquiredOn"),
            "expires_in": obj.get("expiresIn"),
            "refresh_token": obj.get("refreshToken")
        })
        return _obj


