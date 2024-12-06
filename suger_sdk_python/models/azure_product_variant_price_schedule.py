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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from suger_sdk_python.models.azure_localized_time_range import AzureLocalizedTimeRange
from suger_sdk_python.models.azure_price_schedule import AzurePriceSchedule
from typing import Optional, Set
from typing_extensions import Self

class AzureProductVariantPriceSchedule(BaseModel):
    """
    AzureProductVariantPriceSchedule
    """ # noqa: E501
    date_time_range: Optional[AzureLocalizedTimeRange] = Field(default=None, alias="dateTimeRange")
    friendly_name: Optional[StrictStr] = Field(default=None, alias="friendlyName")
    is_base_schedule: Optional[StrictBool] = Field(default=None, description="There is only one base schedule.", alias="isBaseSchedule")
    market_codes: Optional[List[StrictStr]] = Field(default=None, description="ISO country code", alias="marketCodes")
    schedules: Optional[List[AzurePriceSchedule]] = None
    __properties: ClassVar[List[str]] = ["dateTimeRange", "friendlyName", "isBaseSchedule", "marketCodes", "schedules"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of AzureProductVariantPriceSchedule from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of date_time_range
        if self.date_time_range:
            _dict['dateTimeRange'] = self.date_time_range.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in schedules (list)
        _items = []
        if self.schedules:
            for _item_schedules in self.schedules:
                if _item_schedules:
                    _items.append(_item_schedules.to_dict())
            _dict['schedules'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AzureProductVariantPriceSchedule from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "dateTimeRange": AzureLocalizedTimeRange.from_dict(obj["dateTimeRange"]) if obj.get("dateTimeRange") is not None else None,
            "friendlyName": obj.get("friendlyName"),
            "isBaseSchedule": obj.get("isBaseSchedule"),
            "marketCodes": obj.get("marketCodes"),
            "schedules": [AzurePriceSchedule.from_dict(_item) for _item in obj["schedules"]] if obj.get("schedules") is not None else None
        })
        return _obj


