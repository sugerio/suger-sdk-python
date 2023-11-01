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


from typing import List, Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr, conlist
from openapi_client.models.orb_price_discount_type import OrbPriceDiscountType


class OrbPriceDiscount(BaseModel):
    """
    OrbPriceDiscount
    """

    amount_discount: Optional[StrictStr] = Field(
        None, description="Only available if discount_type is amount."
    )
    applies_to_price_ids: Optional[conlist(StrictStr)] = None
    discount_type: Optional[OrbPriceDiscountType] = None
    percentage_discount: Optional[Union[StrictFloat, StrictInt]] = Field(
        None,
        description="Only available if discount_type is percentage.This is a number between 0 and 1.",
    )
    trial_amount_discount: Optional[StrictStr] = Field(
        None, description="Only available if discount_type is trial"
    )
    usage_discount: Optional[StrictStr] = Field(
        None,
        description="Only available if discount_type is usage. Number of usage units that this discount is for",
    )
    __properties = [
        "amount_discount",
        "applies_to_price_ids",
        "discount_type",
        "percentage_discount",
        "trial_amount_discount",
        "usage_discount",
    ]

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
    def from_json(cls, json_str: str) -> OrbPriceDiscount:
        """Create an instance of OrbPriceDiscount from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OrbPriceDiscount:
        """Create an instance of OrbPriceDiscount from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OrbPriceDiscount.parse_obj(obj)

        _obj = OrbPriceDiscount.parse_obj(
            {
                "amount_discount": obj.get("amount_discount"),
                "applies_to_price_ids": obj.get("applies_to_price_ids"),
                "discount_type": obj.get("discount_type"),
                "percentage_discount": obj.get("percentage_discount"),
                "trial_amount_discount": obj.get("trial_amount_discount"),
                "usage_discount": obj.get("usage_discount"),
            }
        )
        return _obj