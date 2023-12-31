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


from typing import Dict, List, Optional, Union
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr, conlist
from openapi_client.models.entitlement_term_type import EntitlementTermType

class EntitlementTermInfo(BaseModel):
    """
    EntitlementTermInfo
    """
    dimension_quantity_decimal_parts: Optional[Dict[str, Union[StrictFloat, StrictInt]]] = Field(None, alias="dimensionQuantityDecimalParts", description="The decimal part of the dimension quantity, in format of <dimensionKey, decimalPart> It is used to save the decimal part of the dimension quantity for AWS Marketplace only. Because AWS Marketplace only accepts integer for dimension quantity. If the dimension quantity is a decimal number, we need to save the decimal part for future use.")
    is_commit_divided: Optional[StrictBool] = Field(None, alias="isCommitDivided", description="Whether the commit is divided into multiple sub entitlement terms. If true, it has subEntitlementTermIds.")
    parent_entitlement_term_id: Optional[StrictStr] = Field(None, alias="parentEntitlementTermId", description="The partner's entitlement term ID. It stands for the partner's entitlement term. Applicable to the sub entitlement term only.")
    sub_entitlement_term_ids: Optional[conlist(StrictStr)] = Field(None, alias="subEntitlementTermIds", description="All sub entitlement terms id of this entitlement term if it is commit divided.")
    type: Optional[EntitlementTermType] = None
    __properties = ["dimensionQuantityDecimalParts", "isCommitDivided", "parentEntitlementTermId", "subEntitlementTermIds", "type"]

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
    def from_json(cls, json_str: str) -> EntitlementTermInfo:
        """Create an instance of EntitlementTermInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EntitlementTermInfo:
        """Create an instance of EntitlementTermInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EntitlementTermInfo.parse_obj(obj)

        _obj = EntitlementTermInfo.parse_obj({
            "dimension_quantity_decimal_parts": obj.get("dimensionQuantityDecimalParts"),
            "is_commit_divided": obj.get("isCommitDivided"),
            "parent_entitlement_term_id": obj.get("parentEntitlementTermId"),
            "sub_entitlement_term_ids": obj.get("subEntitlementTermIds"),
            "type": obj.get("type")
        })
        return _obj


