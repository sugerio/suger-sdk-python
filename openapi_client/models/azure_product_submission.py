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

from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conlist, validator
from openapi_client.models.azure_pending_update_info import AzurePendingUpdateInfo
from openapi_client.models.azure_type_value import AzureTypeValue
from openapi_client.models.azure_variant_resource import AzureVariantResource

class AzureProductSubmission(BaseModel):
    """
    AzureProductSubmission
    """
    are_resources_ready: Optional[StrictBool] = Field(None, alias="areResourcesReady")
    friendly_name: Optional[StrictStr] = Field(None, alias="friendlyName")
    id: Optional[StrictStr] = None
    pending_update_info: Optional[AzurePendingUpdateInfo] = Field(None, alias="pendingUpdateInfo")
    published_time_in_utc: Optional[datetime] = Field(None, alias="publishedTimeInUtc")
    release_number: Optional[StrictInt] = Field(None, alias="releaseNumber")
    resource_type: Optional[StrictStr] = Field(None, alias="resourceType")
    resources: Optional[conlist(AzureTypeValue)] = None
    state: Optional[StrictStr] = None
    sub_state: Optional[StrictStr] = Field(None, alias="subState")
    targets: Optional[conlist(AzureTypeValue)] = None
    variant_resources: Optional[conlist(AzureVariantResource)] = Field(None, alias="variantResources")
    __properties = ["areResourcesReady", "friendlyName", "id", "pendingUpdateInfo", "publishedTimeInUtc", "releaseNumber", "resourceType", "resources", "state", "subState", "targets", "variantResources"]

    @validator('resource_type')
    def resource_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Submission'):
            raise ValueError("must be one of enum values ('Submission')")
        return value

    @validator('state')
    def state_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Inprogress', 'Published'):
            raise ValueError("must be one of enum values ('Inprogress', 'Published')")
        return value

    @validator('sub_state')
    def sub_state_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('InDraft', 'Submitted', 'Failed', 'FailedInCertification', 'ReadyToPublish', 'Publishing', 'Published', 'InStore'):
            raise ValueError("must be one of enum values ('InDraft', 'Submitted', 'Failed', 'FailedInCertification', 'ReadyToPublish', 'Publishing', 'Published', 'InStore')")
        return value

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
    def from_json(cls, json_str: str) -> AzureProductSubmission:
        """Create an instance of AzureProductSubmission from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of pending_update_info
        if self.pending_update_info:
            _dict['pendingUpdateInfo'] = self.pending_update_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in resources (list)
        _items = []
        if self.resources:
            for _item in self.resources:
                if _item:
                    _items.append(_item.to_dict())
            _dict['resources'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in targets (list)
        _items = []
        if self.targets:
            for _item in self.targets:
                if _item:
                    _items.append(_item.to_dict())
            _dict['targets'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in variant_resources (list)
        _items = []
        if self.variant_resources:
            for _item in self.variant_resources:
                if _item:
                    _items.append(_item.to_dict())
            _dict['variantResources'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AzureProductSubmission:
        """Create an instance of AzureProductSubmission from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AzureProductSubmission.parse_obj(obj)

        _obj = AzureProductSubmission.parse_obj({
            "are_resources_ready": obj.get("areResourcesReady"),
            "friendly_name": obj.get("friendlyName"),
            "id": obj.get("id"),
            "pending_update_info": AzurePendingUpdateInfo.from_dict(obj.get("pendingUpdateInfo")) if obj.get("pendingUpdateInfo") is not None else None,
            "published_time_in_utc": obj.get("publishedTimeInUtc"),
            "release_number": obj.get("releaseNumber"),
            "resource_type": obj.get("resourceType"),
            "resources": [AzureTypeValue.from_dict(_item) for _item in obj.get("resources")] if obj.get("resources") is not None else None,
            "state": obj.get("state"),
            "sub_state": obj.get("subState"),
            "targets": [AzureTypeValue.from_dict(_item) for _item in obj.get("targets")] if obj.get("targets") is not None else None,
            "variant_resources": [AzureVariantResource.from_dict(_item) for _item in obj.get("variantResources")] if obj.get("variantResources") is not None else None
        })
        return _obj


