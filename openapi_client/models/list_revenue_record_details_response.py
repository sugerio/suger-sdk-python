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
from openapi_client.models.revenue_record_detail import RevenueRecordDetail

class ListRevenueRecordDetailsResponse(BaseModel):
    """
    ListRevenueRecordDetailsResponse
    """
    next_offset: Optional[StrictInt] = Field(None, alias="nextOffset")
    revenue_record_details: Optional[conlist(RevenueRecordDetail)] = Field(None, alias="revenueRecordDetails")
    __properties = ["nextOffset", "revenueRecordDetails"]

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
    def from_json(cls, json_str: str) -> ListRevenueRecordDetailsResponse:
        """Create an instance of ListRevenueRecordDetailsResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in revenue_record_details (list)
        _items = []
        if self.revenue_record_details:
            for _item in self.revenue_record_details:
                if _item:
                    _items.append(_item.to_dict())
            _dict['revenueRecordDetails'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ListRevenueRecordDetailsResponse:
        """Create an instance of ListRevenueRecordDetailsResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ListRevenueRecordDetailsResponse.parse_obj(obj)

        _obj = ListRevenueRecordDetailsResponse.parse_obj({
            "next_offset": obj.get("nextOffset"),
            "revenue_record_details": [RevenueRecordDetail.from_dict(_item) for _item in obj.get("revenueRecordDetails")] if obj.get("revenueRecordDetails") is not None else None
        })
        return _obj


