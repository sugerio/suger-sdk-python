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
from pydantic import BaseModel, StrictInt, StrictStr


class SlackOAuthV2ResponseAuthedUser(BaseModel):
    """
    SlackOAuthV2ResponseAuthedUser
    """

    access_token: Optional[StrictStr] = None
    expires_in: Optional[StrictInt] = None
    id: Optional[StrictStr] = None
    refresh_token: Optional[StrictStr] = None
    scope: Optional[StrictStr] = None
    token_type: Optional[StrictStr] = None
    __properties = [
        "access_token",
        "expires_in",
        "id",
        "refresh_token",
        "scope",
        "token_type",
    ]

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
    def from_json(cls, json_str: str) -> SlackOAuthV2ResponseAuthedUser:
        """Create an instance of SlackOAuthV2ResponseAuthedUser from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SlackOAuthV2ResponseAuthedUser:
        """Create an instance of SlackOAuthV2ResponseAuthedUser from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SlackOAuthV2ResponseAuthedUser.parse_obj(obj)

        _obj = SlackOAuthV2ResponseAuthedUser.parse_obj(
            {
                "access_token": obj.get("access_token"),
                "expires_in": obj.get("expires_in"),
                "id": obj.get("id"),
                "refresh_token": obj.get("refresh_token"),
                "scope": obj.get("scope"),
                "token_type": obj.get("token_type"),
            }
        )
        return _obj