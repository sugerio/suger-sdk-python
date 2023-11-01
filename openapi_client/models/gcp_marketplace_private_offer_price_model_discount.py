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


from typing import Optional
from pydantic import BaseModel, Field
from openapi_client.models.gcp_discount_percentage import GcpDiscountPercentage
from openapi_client.models.gcp_price_value import GcpPriceValue


class GcpMarketplacePrivateOfferPriceModelDiscount(BaseModel):
    """
    GcpMarketplacePrivateOfferPriceModelDiscount
    """

    discount_percentage: Optional[GcpDiscountPercentage] = Field(
        None, alias="discountPercentage"
    )
    discounted_price: Optional[GcpPriceValue] = Field(None, alias="discountedPrice")
    __properties = ["discountPercentage", "discountedPrice"]

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
    def from_json(cls, json_str: str) -> GcpMarketplacePrivateOfferPriceModelDiscount:
        """Create an instance of GcpMarketplacePrivateOfferPriceModelDiscount from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of discount_percentage
        if self.discount_percentage:
            _dict["discountPercentage"] = self.discount_percentage.to_dict()
        # override the default output from pydantic by calling `to_dict()` of discounted_price
        if self.discounted_price:
            _dict["discountedPrice"] = self.discounted_price.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GcpMarketplacePrivateOfferPriceModelDiscount:
        """Create an instance of GcpMarketplacePrivateOfferPriceModelDiscount from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GcpMarketplacePrivateOfferPriceModelDiscount.parse_obj(obj)

        _obj = GcpMarketplacePrivateOfferPriceModelDiscount.parse_obj(
            {
                "discount_percentage": GcpDiscountPercentage.from_dict(
                    obj.get("discountPercentage")
                )
                if obj.get("discountPercentage") is not None
                else None,
                "discounted_price": GcpPriceValue.from_dict(obj.get("discountedPrice"))
                if obj.get("discountedPrice") is not None
                else None,
            }
        )
        return _obj