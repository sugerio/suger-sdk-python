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


from typing import Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr
from openapi_client.models.github_com_sugerio_marketplace_service_azure_sdk_marketplacemeteringv1_usage_event_conflict_response import (
    GithubComSugerioMarketplaceServiceAzureSdkMarketplacemeteringv1UsageEventConflictResponse,
)
from openapi_client.models.github_com_sugerio_marketplace_service_azure_sdk_marketplacemeteringv1_usage_event_status_enum import (
    GithubComSugerioMarketplaceServiceAzureSdkMarketplacemeteringv1UsageEventStatusEnum,
)


class GithubComSugerioMarketplaceServiceAzureSdkMarketplacemeteringv1UsageBatchEventOkMessage(
    BaseModel
):
    """
    GithubComSugerioMarketplaceServiceAzureSdkMarketplacemeteringv1UsageBatchEventOkMessage
    """

    dimension: Optional[StrictStr] = Field(None, description="Dimension identifier")
    effective_start_time: Optional[StrictStr] = Field(
        None,
        alias="effectiveStartTime",
        description="Time in UTC when the usage event occurred",
    )
    error: Optional[
        GithubComSugerioMarketplaceServiceAzureSdkMarketplacemeteringv1UsageEventConflictResponse
    ] = None
    message_time: Optional[StrictStr] = Field(
        None, alias="messageTime", description="Time this message was created in UTC"
    )
    plan_id: Optional[StrictStr] = Field(
        None, alias="planId", description="Plan associated with the purchased offer"
    )
    quantity: Optional[Union[StrictFloat, StrictInt]] = Field(
        None, description="Number of units consumed"
    )
    resource_id: Optional[StrictStr] = Field(
        None,
        alias="resourceId",
        description="Identifier of the resource against which usage is emitted",
    )
    resource_uri: Optional[StrictStr] = Field(
        None,
        alias="resourceUri",
        description="Identifier of the managed app resource against which usage is emitted",
    )
    status: Optional[
        GithubComSugerioMarketplaceServiceAzureSdkMarketplacemeteringv1UsageEventStatusEnum
    ] = None
    usage_event_id: Optional[StrictStr] = Field(
        None,
        alias="usageEventId",
        description="Unique identifier associated with the usage event",
    )
    __properties = [
        "dimension",
        "effectiveStartTime",
        "error",
        "messageTime",
        "planId",
        "quantity",
        "resourceId",
        "resourceUri",
        "status",
        "usageEventId",
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
    def from_json(
        cls, json_str: str
    ) -> GithubComSugerioMarketplaceServiceAzureSdkMarketplacemeteringv1UsageBatchEventOkMessage:
        """Create an instance of GithubComSugerioMarketplaceServiceAzureSdkMarketplacemeteringv1UsageBatchEventOkMessage from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of error
        if self.error:
            _dict["error"] = self.error.to_dict()
        return _dict

    @classmethod
    def from_dict(
        cls, obj: dict
    ) -> GithubComSugerioMarketplaceServiceAzureSdkMarketplacemeteringv1UsageBatchEventOkMessage:
        """Create an instance of GithubComSugerioMarketplaceServiceAzureSdkMarketplacemeteringv1UsageBatchEventOkMessage from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GithubComSugerioMarketplaceServiceAzureSdkMarketplacemeteringv1UsageBatchEventOkMessage.parse_obj(
                obj
            )

        _obj = GithubComSugerioMarketplaceServiceAzureSdkMarketplacemeteringv1UsageBatchEventOkMessage.parse_obj(
            {
                "dimension": obj.get("dimension"),
                "effective_start_time": obj.get("effectiveStartTime"),
                "error": GithubComSugerioMarketplaceServiceAzureSdkMarketplacemeteringv1UsageEventConflictResponse.from_dict(
                    obj.get("error")
                )
                if obj.get("error") is not None
                else None,
                "message_time": obj.get("messageTime"),
                "plan_id": obj.get("planId"),
                "quantity": obj.get("quantity"),
                "resource_id": obj.get("resourceId"),
                "resource_uri": obj.get("resourceUri"),
                "status": obj.get("status"),
                "usage_event_id": obj.get("usageEventId"),
            }
        )
        return _obj