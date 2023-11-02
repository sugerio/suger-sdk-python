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
from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr
from openapi_client.models.gcp_period_duration import GcpPeriodDuration

class GcpMarketplacePrivateOfferTerm(BaseModel):
    """
    GcpMarketplacePrivateOfferTerm
    """
    enable_scheduled_start_times: Optional[StrictBool] = Field(None, alias="enableScheduledStartTimes")
    end_time: Optional[datetime] = Field(None, alias="endTime")
    start_policy: Optional[StrictStr] = Field(None, alias="startPolicy", description="such as \"OFFER_START_POLICY_IMMEDIATE\"")
    start_time: Optional[datetime] = Field(None, alias="startTime")
    term_duration: Optional[GcpPeriodDuration] = Field(None, alias="termDuration")
    __properties = ["enableScheduledStartTimes", "endTime", "startPolicy", "startTime", "termDuration"]

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
    def from_json(cls, json_str: str) -> GcpMarketplacePrivateOfferTerm:
        """Create an instance of GcpMarketplacePrivateOfferTerm from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of term_duration
        if self.term_duration:
            _dict['termDuration'] = self.term_duration.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GcpMarketplacePrivateOfferTerm:
        """Create an instance of GcpMarketplacePrivateOfferTerm from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GcpMarketplacePrivateOfferTerm.parse_obj(obj)

        _obj = GcpMarketplacePrivateOfferTerm.parse_obj({
            "enable_scheduled_start_times": obj.get("enableScheduledStartTimes"),
            "end_time": obj.get("endTime"),
            "start_policy": obj.get("startPolicy"),
            "start_time": obj.get("startTime"),
            "term_duration": GcpPeriodDuration.from_dict(obj.get("termDuration")) if obj.get("termDuration") is not None else None
        })
        return _obj


