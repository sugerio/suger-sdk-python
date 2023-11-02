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

class PaymentInstallment(BaseModel):
    """
    PaymentInstallment
    """
    amount: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="The amount the buyer has paid for this installment. If there is a discount off the original price, the amount is the discounted price.")
    charge_on: Optional[datetime] = Field(None, alias="chargeOn", description="When the buyer will be charged for this installment. If it is null, the buyer will be charged on the effective date of the entitlement.")
    charge_on_str: Optional[StrictStr] = Field(None, alias="chargeOnStr", description="The charge on date in string format. It is used for front-end display only.")
    credit: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="Used in GCP Marketplace private offer as one-time credit. Default as zero if there is no credit.")
    discount_percentage: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="discountPercentage", description="The discount percentage off the original price. For GCP Marketplace, it can be discount off the commitment amount or discount off the usage price. The value is between 0 to 100. For example, 20 means 20% off. Default as zero if there is no discount.")
    original_amount: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="originalAmount", description="The original amount before discount if there is a discount off the original price. nil if there is no discount.")
    __properties = ["amount", "chargeOn", "chargeOnStr", "credit", "discountPercentage", "originalAmount"]

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
    def from_json(cls, json_str: str) -> PaymentInstallment:
        """Create an instance of PaymentInstallment from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PaymentInstallment:
        """Create an instance of PaymentInstallment from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PaymentInstallment.parse_obj(obj)

        _obj = PaymentInstallment.parse_obj({
            "amount": obj.get("amount"),
            "charge_on": obj.get("chargeOn"),
            "charge_on_str": obj.get("chargeOnStr"),
            "credit": obj.get("credit"),
            "discount_percentage": obj.get("discountPercentage"),
            "original_amount": obj.get("originalAmount")
        })
        return _obj


