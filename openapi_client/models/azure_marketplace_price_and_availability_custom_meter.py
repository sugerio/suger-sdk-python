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


from typing import Dict, List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist
from openapi_client.models.azure_marketplace_price_and_availability_custom_meter_item import AzureMarketplacePriceAndAvailabilityCustomMeterItem
from openapi_client.models.azure_marketplace_validation import AzureMarketplaceValidation

class AzureMarketplacePriceAndAvailabilityCustomMeter(BaseModel):
    """
    AzureMarketplacePriceAndAvailabilityCustomMeter
    """
    var_schema: Optional[StrictStr] = Field(None, alias="$schema")
    custom_meters: Optional[Dict[str, AzureMarketplacePriceAndAvailabilityCustomMeterItem]] = Field(None, alias="customMeters")
    id: Optional[StrictStr] = None
    product: Optional[StrictStr] = None
    resource_name: Optional[StrictStr] = Field(None, alias="resourceName")
    validations: Optional[conlist(AzureMarketplaceValidation)] = None
    __properties = ["$schema", "customMeters", "id", "product", "resourceName", "validations"]

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
    def from_json(cls, json_str: str) -> AzureMarketplacePriceAndAvailabilityCustomMeter:
        """Create an instance of AzureMarketplacePriceAndAvailabilityCustomMeter from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each value in custom_meters (dict)
        _field_dict = {}
        if self.custom_meters:
            for _key in self.custom_meters:
                if self.custom_meters[_key]:
                    _field_dict[_key] = self.custom_meters[_key].to_dict()
            _dict['customMeters'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each item in validations (list)
        _items = []
        if self.validations:
            for _item in self.validations:
                if _item:
                    _items.append(_item.to_dict())
            _dict['validations'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AzureMarketplacePriceAndAvailabilityCustomMeter:
        """Create an instance of AzureMarketplacePriceAndAvailabilityCustomMeter from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AzureMarketplacePriceAndAvailabilityCustomMeter.parse_obj(obj)

        _obj = AzureMarketplacePriceAndAvailabilityCustomMeter.parse_obj({
            "var_schema": obj.get("$schema"),
            "custom_meters": dict(
                (_k, AzureMarketplacePriceAndAvailabilityCustomMeterItem.from_dict(_v))
                for _k, _v in obj.get("customMeters").items()
            )
            if obj.get("customMeters") is not None
            else None,
            "id": obj.get("id"),
            "product": obj.get("product"),
            "resource_name": obj.get("resourceName"),
            "validations": [AzureMarketplaceValidation.from_dict(_item) for _item in obj.get("validations")] if obj.get("validations") is not None else None
        })
        return _obj


