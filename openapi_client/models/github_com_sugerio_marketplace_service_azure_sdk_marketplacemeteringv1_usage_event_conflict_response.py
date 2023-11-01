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
from openapi_client.models.github_com_sugerio_marketplace_service_azure_sdk_marketplacemeteringv1_usage_event_conflict_response_additional_info import GithubComSugerioMarketplaceServiceAzureSdkMarketplacemeteringv1UsageEventConflictResponseAdditionalInfo

class GithubComSugerioMarketplaceServiceAzureSdkMarketplacemeteringv1UsageEventConflictResponse(BaseModel):
    """
    GithubComSugerioMarketplaceServiceAzureSdkMarketplacemeteringv1UsageEventConflictResponse
    """
    additional_info: Optional[GithubComSugerioMarketplaceServiceAzureSdkMarketplacemeteringv1UsageEventConflictResponseAdditionalInfo] = Field(None, alias="additionalInfo")
    code: Optional[StrictStr] = None
    message: Optional[StrictStr] = None
    __properties = ["additionalInfo", "code", "message"]

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
    def from_json(cls, json_str: str) -> GithubComSugerioMarketplaceServiceAzureSdkMarketplacemeteringv1UsageEventConflictResponse:
        """Create an instance of GithubComSugerioMarketplaceServiceAzureSdkMarketplacemeteringv1UsageEventConflictResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of additional_info
        if self.additional_info:
            _dict['additionalInfo'] = self.additional_info.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GithubComSugerioMarketplaceServiceAzureSdkMarketplacemeteringv1UsageEventConflictResponse:
        """Create an instance of GithubComSugerioMarketplaceServiceAzureSdkMarketplacemeteringv1UsageEventConflictResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GithubComSugerioMarketplaceServiceAzureSdkMarketplacemeteringv1UsageEventConflictResponse.parse_obj(obj)

        _obj = GithubComSugerioMarketplaceServiceAzureSdkMarketplacemeteringv1UsageEventConflictResponse.parse_obj({
            "additional_info": GithubComSugerioMarketplaceServiceAzureSdkMarketplacemeteringv1UsageEventConflictResponseAdditionalInfo.from_dict(obj.get("additionalInfo")) if obj.get("additionalInfo") is not None else None,
            "code": obj.get("code"),
            "message": obj.get("message")
        })
        return _obj


