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
from typing import Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr
from openapi_client.models.partner import Partner


class UsageMeteringDailyRecord(BaseModel):
    """
    UsageMeteringDailyRecord
    """

    amount: Optional[Union[StrictFloat, StrictInt]] = None
    var_date: Optional[datetime] = Field(None, alias="date")
    key: Optional[StrictStr] = Field(
        None, description="The dimension key of the usage metering."
    )
    partner: Optional[Partner] = None
    quantity: Optional[Union[StrictFloat, StrictInt]] = None
    __properties = ["amount", "date", "key", "partner", "quantity"]

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
    def from_json(cls, json_str: str) -> UsageMeteringDailyRecord:
        """Create an instance of UsageMeteringDailyRecord from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UsageMeteringDailyRecord:
        """Create an instance of UsageMeteringDailyRecord from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UsageMeteringDailyRecord.parse_obj(obj)

        _obj = UsageMeteringDailyRecord.parse_obj(
            {
                "amount": obj.get("amount"),
                "var_date": obj.get("date"),
                "key": obj.get("key"),
                "partner": obj.get("partner"),
                "quantity": obj.get("quantity"),
            }
        )
        return _obj
