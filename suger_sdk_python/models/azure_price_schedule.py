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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from suger_sdk_python.models.azure_price import AzurePrice
from suger_sdk_python.models.azure_price_cadence import AzurePriceCadence
from suger_sdk_python.models.azure_pricing_unit import AzurePricingUnit
from typing import Optional, Set
from typing_extensions import Self

class AzurePriceSchedule(BaseModel):
    """
    AzurePriceSchedule
    """ # noqa: E501
    price_cadence: Optional[AzurePriceCadence] = Field(default=None, alias="priceCadence")
    pricing_model: Optional[StrictStr] = Field(default=None, alias="pricingModel")
    pricing_units: Optional[List[AzurePricingUnit]] = Field(default=None, alias="pricingUnits")
    retail_price: Optional[AzurePrice] = Field(default=None, alias="retailPrice")
    __properties: ClassVar[List[str]] = ["priceCadence", "pricingModel", "pricingUnits", "retailPrice"]

    @field_validator('pricing_model')
    def pricing_model_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Flat', 'Recurring', 'Usage']):
            raise ValueError("must be one of enum values ('Flat', 'Recurring', 'Usage')")
        return value

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
        """Create an instance of AzurePriceSchedule from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of price_cadence
        if self.price_cadence:
            _dict['priceCadence'] = self.price_cadence.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in pricing_units (list)
        _items = []
        if self.pricing_units:
            for _item_pricing_units in self.pricing_units:
                if _item_pricing_units:
                    _items.append(_item_pricing_units.to_dict())
            _dict['pricingUnits'] = _items
        # override the default output from pydantic by calling `to_dict()` of retail_price
        if self.retail_price:
            _dict['retailPrice'] = self.retail_price.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AzurePriceSchedule from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "priceCadence": AzurePriceCadence.from_dict(obj["priceCadence"]) if obj.get("priceCadence") is not None else None,
            "pricingModel": obj.get("pricingModel"),
            "pricingUnits": [AzurePricingUnit.from_dict(_item) for _item in obj["pricingUnits"]] if obj.get("pricingUnits") is not None else None,
            "retailPrice": AzurePrice.from_dict(obj["retailPrice"]) if obj.get("retailPrice") is not None else None
        })
        return _obj

