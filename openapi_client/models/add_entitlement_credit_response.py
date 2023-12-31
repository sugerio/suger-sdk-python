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

class AddEntitlementCreditResponse(BaseModel):
    """
    AddEntitlementCreditResponse
    """
    credit_amount_increment: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="creditAmountIncrement", description="The amount to be added to the credit amount.")
    entitlement_id: Optional[StrictStr] = Field(None, alias="entitlementID")
    entitlement_term_id: Optional[StrictStr] = Field(None, alias="entitlementTermID")
    new_credit_amount: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="newCreditAmount", description="The new credit amount after the increment.")
    organization_id: Optional[StrictStr] = Field(None, alias="organizationID")
    __properties = ["creditAmountIncrement", "entitlementID", "entitlementTermID", "newCreditAmount", "organizationID"]

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
    def from_json(cls, json_str: str) -> AddEntitlementCreditResponse:
        """Create an instance of AddEntitlementCreditResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AddEntitlementCreditResponse:
        """Create an instance of AddEntitlementCreditResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AddEntitlementCreditResponse.parse_obj(obj)

        _obj = AddEntitlementCreditResponse.parse_obj({
            "credit_amount_increment": obj.get("creditAmountIncrement"),
            "entitlement_id": obj.get("entitlementID"),
            "entitlement_term_id": obj.get("entitlementTermID"),
            "new_credit_amount": obj.get("newCreditAmount"),
            "organization_id": obj.get("organizationID")
        })
        return _obj


