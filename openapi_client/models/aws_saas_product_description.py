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
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist

class AwsSaasProductDescription(BaseModel):
    """
    AwsSaasProductDescription
    """
    associated_products: Optional[StrictStr] = Field(None, alias="AssociatedProducts")
    categories: Optional[conlist(StrictStr)] = Field(None, alias="Categories")
    eu_w8_submitted: Optional[StrictBool] = Field(None, alias="EuW8Submitted")
    highlights: Optional[conlist(StrictStr)] = Field(None, alias="Highlights")
    long_description: Optional[StrictStr] = Field(None, alias="LongDescription")
    manufacturer: Optional[StrictStr] = Field(None, alias="Manufacturer")
    product_code: Optional[StrictStr] = Field(None, alias="ProductCode")
    product_title: Optional[StrictStr] = Field(None, alias="ProductTitle")
    registered: Optional[StrictBool] = Field(None, alias="Registered")
    search_keywords: Optional[conlist(StrictStr)] = Field(None, alias="SearchKeywords")
    short_description: Optional[StrictStr] = Field(None, alias="ShortDescription")
    sku: Optional[StrictStr] = Field(None, alias="Sku")
    us_w9_submitted: Optional[StrictBool] = Field(None, alias="UsW9Submitted")
    visibility: Optional[StrictStr] = Field(None, alias="Visibility")
    __properties = ["AssociatedProducts", "Categories", "EuW8Submitted", "Highlights", "LongDescription", "Manufacturer", "ProductCode", "ProductTitle", "Registered", "SearchKeywords", "ShortDescription", "Sku", "UsW9Submitted", "Visibility"]

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
    def from_json(cls, json_str: str) -> AwsSaasProductDescription:
        """Create an instance of AwsSaasProductDescription from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AwsSaasProductDescription:
        """Create an instance of AwsSaasProductDescription from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AwsSaasProductDescription.parse_obj(obj)

        _obj = AwsSaasProductDescription.parse_obj({
            "associated_products": obj.get("AssociatedProducts"),
            "categories": obj.get("Categories"),
            "eu_w8_submitted": obj.get("EuW8Submitted"),
            "highlights": obj.get("Highlights"),
            "long_description": obj.get("LongDescription"),
            "manufacturer": obj.get("Manufacturer"),
            "product_code": obj.get("ProductCode"),
            "product_title": obj.get("ProductTitle"),
            "registered": obj.get("Registered"),
            "search_keywords": obj.get("SearchKeywords"),
            "short_description": obj.get("ShortDescription"),
            "sku": obj.get("Sku"),
            "us_w9_submitted": obj.get("UsW9Submitted"),
            "visibility": obj.get("Visibility")
        })
        return _obj


