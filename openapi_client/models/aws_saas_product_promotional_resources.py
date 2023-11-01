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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist
from openapi_client.models.aws_saas_product_additional_resource import (
    AwsSaasProductAdditionalResource,
)


class AwsSaasProductPromotionalResources(BaseModel):
    """
    AwsSaasProductPromotionalResources
    """

    additional_resources: Optional[conlist(AwsSaasProductAdditionalResource)] = Field(
        None, alias="AdditionalResources"
    )
    logo_url: Optional[StrictStr] = Field(None, alias="LogoUrl")
    video_urls: Optional[conlist(StrictStr)] = Field(
        None,
        alias="VideoUrls",
        description="Currently, AWS only support 1 url in the array.",
    )
    __properties = ["AdditionalResources", "LogoUrl", "VideoUrls"]

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
    def from_json(cls, json_str: str) -> AwsSaasProductPromotionalResources:
        """Create an instance of AwsSaasProductPromotionalResources from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in additional_resources (list)
        _items = []
        if self.additional_resources:
            for _item in self.additional_resources:
                if _item:
                    _items.append(_item.to_dict())
            _dict["AdditionalResources"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AwsSaasProductPromotionalResources:
        """Create an instance of AwsSaasProductPromotionalResources from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AwsSaasProductPromotionalResources.parse_obj(obj)

        _obj = AwsSaasProductPromotionalResources.parse_obj(
            {
                "additional_resources": [
                    AwsSaasProductAdditionalResource.from_dict(_item)
                    for _item in obj.get("AdditionalResources")
                ]
                if obj.get("AdditionalResources") is not None
                else None,
                "logo_url": obj.get("LogoUrl"),
                "video_urls": obj.get("VideoUrls"),
            }
        )
        return _obj