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
from pydantic import BaseModel, Field, StrictStr, conlist
from openapi_client.models.aws_saas_product_delivery_option import (
    AwsSaasProductDeliveryOption,
)


class AwsSaasProductVersion(BaseModel):
    """
    AwsSaasProductVersion
    """

    delivery_options: Optional[conlist(AwsSaasProductDeliveryOption)] = Field(
        None, alias="DeliveryOptions"
    )
    id: Optional[StrictStr] = Field(None, alias="Id")
    __properties = ["DeliveryOptions", "Id"]

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
    def from_json(cls, json_str: str) -> AwsSaasProductVersion:
        """Create an instance of AwsSaasProductVersion from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in delivery_options (list)
        _items = []
        if self.delivery_options:
            for _item in self.delivery_options:
                if _item:
                    _items.append(_item.to_dict())
            _dict["DeliveryOptions"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AwsSaasProductVersion:
        """Create an instance of AwsSaasProductVersion from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AwsSaasProductVersion.parse_obj(obj)

        _obj = AwsSaasProductVersion.parse_obj(
            {
                "delivery_options": [
                    AwsSaasProductDeliveryOption.from_dict(_item)
                    for _item in obj.get("DeliveryOptions")
                ]
                if obj.get("DeliveryOptions") is not None
                else None,
                "id": obj.get("Id"),
            }
        )
        return _obj