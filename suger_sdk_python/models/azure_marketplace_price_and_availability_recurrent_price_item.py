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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Optional, Union
from suger_sdk_python.models.azure_marketplace_price import AzureMarketplacePrice
from suger_sdk_python.models.azure_marketplace_term import AzureMarketplaceTerm
from typing import Optional, Set
from typing_extensions import Self

class AzureMarketplacePriceAndAvailabilityRecurrentPriceItem(BaseModel):
    """
    AzureMarketplacePriceAndAvailabilityRecurrentPriceItem
    """ # noqa: E501
    billing_term: Optional[AzureMarketplaceTerm] = Field(default=None, alias="billingTerm")
    payment_option: Optional[AzureMarketplaceTerm] = Field(default=None, alias="paymentOption")
    price_per_payment_in_usd: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="pricePerPaymentInUsd")
    prices: Optional[List[AzureMarketplacePrice]] = None
    __properties: ClassVar[List[str]] = ["billingTerm", "paymentOption", "pricePerPaymentInUsd", "prices"]

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
        """Create an instance of AzureMarketplacePriceAndAvailabilityRecurrentPriceItem from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of billing_term
        if self.billing_term:
            _dict['billingTerm'] = self.billing_term.to_dict()
        # override the default output from pydantic by calling `to_dict()` of payment_option
        if self.payment_option:
            _dict['paymentOption'] = self.payment_option.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in prices (list)
        _items = []
        if self.prices:
            for _item_prices in self.prices:
                if _item_prices:
                    _items.append(_item_prices.to_dict())
            _dict['prices'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AzureMarketplacePriceAndAvailabilityRecurrentPriceItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "billingTerm": AzureMarketplaceTerm.from_dict(obj["billingTerm"]) if obj.get("billingTerm") is not None else None,
            "paymentOption": AzureMarketplaceTerm.from_dict(obj["paymentOption"]) if obj.get("paymentOption") is not None else None,
            "pricePerPaymentInUsd": obj.get("pricePerPaymentInUsd"),
            "prices": [AzureMarketplacePrice.from_dict(_item) for _item in obj["prices"]] if obj.get("prices") is not None else None
        })
        return _obj


