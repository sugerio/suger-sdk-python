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
from pydantic import BaseModel, Field, StrictInt, conlist
from openapi_client.models.metering_usage_record_report import MeteringUsageRecordReport

class ListUsageRecordReportsResponse(BaseModel):
    """
    ListUsageRecordReportsResponse
    """
    next_offset: Optional[StrictInt] = Field(None, alias="nextOffset")
    usage_record_reports: Optional[conlist(MeteringUsageRecordReport)] = Field(None, alias="usageRecordReports")
    __properties = ["nextOffset", "usageRecordReports"]

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
    def from_json(cls, json_str: str) -> ListUsageRecordReportsResponse:
        """Create an instance of ListUsageRecordReportsResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in usage_record_reports (list)
        _items = []
        if self.usage_record_reports:
            for _item in self.usage_record_reports:
                if _item:
                    _items.append(_item.to_dict())
            _dict['usageRecordReports'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ListUsageRecordReportsResponse:
        """Create an instance of ListUsageRecordReportsResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ListUsageRecordReportsResponse.parse_obj(obj)

        _obj = ListUsageRecordReportsResponse.parse_obj({
            "next_offset": obj.get("nextOffset"),
            "usage_record_reports": [MeteringUsageRecordReport.from_dict(_item) for _item in obj.get("usageRecordReports")] if obj.get("usageRecordReports") is not None else None
        })
        return _obj


