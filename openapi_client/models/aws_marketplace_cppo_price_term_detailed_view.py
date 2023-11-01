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
from openapi_client.models.aws_marketplace_cppo_price_term_entry import (
    AwsMarketplaceCppoPriceTermEntry,
)


class AwsMarketplaceCppoPriceTermDetailedView(BaseModel):
    """
    AwsMarketplaceCppoPriceTermDetailedView
    """

    additional_consumption_unit_column_names: Optional[conlist(StrictStr)] = Field(
        None,
        alias="additionalConsumptionUnitColumnNames",
        description="For Usage metering dimensions",
    )
    additional_consumption_unit_entries: Optional[
        conlist(AwsMarketplaceCppoPriceTermEntry)
    ] = Field(
        None,
        alias="additionalConsumptionUnitEntries",
        description="For Usage metering dimensions",
    )
    consumption_unit_column_names: Optional[conlist(StrictStr)] = Field(
        None, alias="consumptionUnitColumnNames", description="For Commit dimensions"
    )
    consumption_unit_entries: Optional[
        conlist(AwsMarketplaceCppoPriceTermEntry)
    ] = Field(None, alias="consumptionUnitEntries", description="For Commit dimensions")
    __properties = [
        "additionalConsumptionUnitColumnNames",
        "additionalConsumptionUnitEntries",
        "consumptionUnitColumnNames",
        "consumptionUnitEntries",
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
    def from_json(cls, json_str: str) -> AwsMarketplaceCppoPriceTermDetailedView:
        """Create an instance of AwsMarketplaceCppoPriceTermDetailedView from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in additional_consumption_unit_entries (list)
        _items = []
        if self.additional_consumption_unit_entries:
            for _item in self.additional_consumption_unit_entries:
                if _item:
                    _items.append(_item.to_dict())
            _dict["additionalConsumptionUnitEntries"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in consumption_unit_entries (list)
        _items = []
        if self.consumption_unit_entries:
            for _item in self.consumption_unit_entries:
                if _item:
                    _items.append(_item.to_dict())
            _dict["consumptionUnitEntries"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AwsMarketplaceCppoPriceTermDetailedView:
        """Create an instance of AwsMarketplaceCppoPriceTermDetailedView from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AwsMarketplaceCppoPriceTermDetailedView.parse_obj(obj)

        _obj = AwsMarketplaceCppoPriceTermDetailedView.parse_obj(
            {
                "additional_consumption_unit_column_names": obj.get(
                    "additionalConsumptionUnitColumnNames"
                ),
                "additional_consumption_unit_entries": [
                    AwsMarketplaceCppoPriceTermEntry.from_dict(_item)
                    for _item in obj.get("additionalConsumptionUnitEntries")
                ]
                if obj.get("additionalConsumptionUnitEntries") is not None
                else None,
                "consumption_unit_column_names": obj.get("consumptionUnitColumnNames"),
                "consumption_unit_entries": [
                    AwsMarketplaceCppoPriceTermEntry.from_dict(_item)
                    for _item in obj.get("consumptionUnitEntries")
                ]
                if obj.get("consumptionUnitEntries") is not None
                else None,
            }
        )
        return _obj
