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
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from openapi_client.models.partner import Partner

class UsageMeteringDailyVerification(BaseModel):
    """
    UsageMeteringDailyVerification
    """
    billed_amount: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="billedAmount", description="The amount of the usage metering billed by the cloud marketplace metering service.")
    billed_date: Optional[datetime] = Field(None, alias="billedDate", description="The date when the usage metering is billed by the cloud marketplace metering service.")
    billed_quantity: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="billedQuantity", description="The quantity of the usage metering billed by the cloud marketplace metering service.")
    is_amount_matched: Optional[StrictBool] = Field(None, alias="isAmountMatched", description="Whether the amount is matched between reported & billed usage metering.")
    is_quantity_matched: Optional[StrictBool] = Field(None, alias="isQuantityMatched", description="Whether the quantity is matched between reported & billed usage metering.")
    key: Optional[StrictStr] = Field(None, description="The dimension key of the usage metering.")
    partner: Optional[Partner] = None
    reported_amount: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="reportedAmount", description="The amount of the usage metering reported to the cloud marketplace.")
    reported_date: Optional[datetime] = Field(None, alias="reportedDate", description="The date when the usage metering is reported to the cloud marketplace.")
    reported_quantity: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="reportedQuantity", description="The quantity of the usage metering reported to the cloud marketplace.")
    __properties = ["billedAmount", "billedDate", "billedQuantity", "isAmountMatched", "isQuantityMatched", "key", "partner", "reportedAmount", "reportedDate", "reportedQuantity"]

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
    def from_json(cls, json_str: str) -> UsageMeteringDailyVerification:
        """Create an instance of UsageMeteringDailyVerification from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UsageMeteringDailyVerification:
        """Create an instance of UsageMeteringDailyVerification from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UsageMeteringDailyVerification.parse_obj(obj)

        _obj = UsageMeteringDailyVerification.parse_obj({
            "billed_amount": obj.get("billedAmount"),
            "billed_date": obj.get("billedDate"),
            "billed_quantity": obj.get("billedQuantity"),
            "is_amount_matched": obj.get("isAmountMatched"),
            "is_quantity_matched": obj.get("isQuantityMatched"),
            "key": obj.get("key"),
            "partner": obj.get("partner"),
            "reported_amount": obj.get("reportedAmount"),
            "reported_date": obj.get("reportedDate"),
            "reported_quantity": obj.get("reportedQuantity")
        })
        return _obj


