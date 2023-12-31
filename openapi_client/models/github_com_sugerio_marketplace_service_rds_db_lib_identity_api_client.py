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

class GithubComSugerioMarketplaceServiceRdsDbLibIdentityApiClient(BaseModel):
    """
    GithubComSugerioMarketplaceServiceRdsDbLibIdentityApiClient
    """
    api_key_hash: Optional[StrictStr] = Field(None, alias="apiKeyHash")
    creation_time: Optional[StrictStr] = Field(None, alias="creationTime")
    id: Optional[StrictStr] = None
    info: Optional[StrictStr] = None
    last_update_time: Optional[StrictStr] = Field(None, alias="lastUpdateTime")
    organization_id: Optional[StrictStr] = Field(None, alias="organizationID")
    provider: Optional[StrictStr] = None
    role: Optional[StrictStr] = None
    secret: Optional[StrictStr] = None
    type: Optional[StrictStr] = None
    __properties = ["apiKeyHash", "creationTime", "id", "info", "lastUpdateTime", "organizationID", "provider", "role", "secret", "type"]

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
    def from_json(cls, json_str: str) -> GithubComSugerioMarketplaceServiceRdsDbLibIdentityApiClient:
        """Create an instance of GithubComSugerioMarketplaceServiceRdsDbLibIdentityApiClient from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GithubComSugerioMarketplaceServiceRdsDbLibIdentityApiClient:
        """Create an instance of GithubComSugerioMarketplaceServiceRdsDbLibIdentityApiClient from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GithubComSugerioMarketplaceServiceRdsDbLibIdentityApiClient.parse_obj(obj)

        _obj = GithubComSugerioMarketplaceServiceRdsDbLibIdentityApiClient.parse_obj({
            "api_key_hash": obj.get("apiKeyHash"),
            "creation_time": obj.get("creationTime"),
            "id": obj.get("id"),
            "info": obj.get("info"),
            "last_update_time": obj.get("lastUpdateTime"),
            "organization_id": obj.get("organizationID"),
            "provider": obj.get("provider"),
            "role": obj.get("role"),
            "secret": obj.get("secret"),
            "type": obj.get("type")
        })
        return _obj


