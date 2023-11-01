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
from pydantic import BaseModel, Field
from openapi_client.models.github_com_sugerio_marketplace_service_azure_sdk_marketplacemeteringv1_usage_event_ok_response import (
    GithubComSugerioMarketplaceServiceAzureSdkMarketplacemeteringv1UsageEventOkResponse,
)


class GithubComSugerioMarketplaceServiceAzureSdkMarketplacemeteringv1UsageEventConflictResponseAdditionalInfo(
    BaseModel
):
    """
    GithubComSugerioMarketplaceServiceAzureSdkMarketplacemeteringv1UsageEventConflictResponseAdditionalInfo
    """

    accepted_message: Optional[
        GithubComSugerioMarketplaceServiceAzureSdkMarketplacemeteringv1UsageEventOkResponse
    ] = Field(None, alias="acceptedMessage")
    __properties = ["acceptedMessage"]

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
    ) -> GithubComSugerioMarketplaceServiceAzureSdkMarketplacemeteringv1UsageEventConflictResponseAdditionalInfo:
        """Create an instance of GithubComSugerioMarketplaceServiceAzureSdkMarketplacemeteringv1UsageEventConflictResponseAdditionalInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of accepted_message
        if self.accepted_message:
            _dict["acceptedMessage"] = self.accepted_message.to_dict()
        return _dict

    @classmethod
    def from_dict(
        cls, obj: dict
    ) -> GithubComSugerioMarketplaceServiceAzureSdkMarketplacemeteringv1UsageEventConflictResponseAdditionalInfo:
        """Create an instance of GithubComSugerioMarketplaceServiceAzureSdkMarketplacemeteringv1UsageEventConflictResponseAdditionalInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GithubComSugerioMarketplaceServiceAzureSdkMarketplacemeteringv1UsageEventConflictResponseAdditionalInfo.parse_obj(
                obj
            )

        _obj = GithubComSugerioMarketplaceServiceAzureSdkMarketplacemeteringv1UsageEventConflictResponseAdditionalInfo.parse_obj(
            {
                "accepted_message": GithubComSugerioMarketplaceServiceAzureSdkMarketplacemeteringv1UsageEventOkResponse.from_dict(
                    obj.get("acceptedMessage")
                )
                if obj.get("acceptedMessage") is not None
                else None
            }
        )
        return _obj
