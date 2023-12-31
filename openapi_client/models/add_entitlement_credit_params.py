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


from typing import Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr

class AddEntitlementCreditParams(BaseModel):
    """
    AddEntitlementCreditParams
    """
    credit_amount_increment: Union[StrictFloat, StrictInt] = Field(..., alias="creditAmountIncrement", description="The amount to be added to the credit amount.")
    entitlement_id: StrictStr = Field(..., alias="entitlementID")
    organization_id: StrictStr = Field(..., alias="organizationID")
    __properties = ["creditAmountIncrement", "entitlementID", "organizationID"]

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
    def from_json(cls, json_str: str) -> AddEntitlementCreditParams:
        """Create an instance of AddEntitlementCreditParams from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AddEntitlementCreditParams:
        """Create an instance of AddEntitlementCreditParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AddEntitlementCreditParams.parse_obj(obj)

        _obj = AddEntitlementCreditParams.parse_obj({
            "credit_amount_increment": obj.get("creditAmountIncrement"),
            "entitlement_id": obj.get("entitlementID"),
            "organization_id": obj.get("organizationID")
        })
        return _obj


