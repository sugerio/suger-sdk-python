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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from suger_sdk_python.models.azure_marketplace_price_and_availability_private_offer_custom_meters import AzureMarketplacePriceAndAvailabilityPrivateOfferCustomMeters
from suger_sdk_python.models.azure_marketplace_price_and_availability_recurrent_price import AzureMarketplacePriceAndAvailabilityRecurrentPrice
from typing import Optional, Set
from typing_extensions import Self

class AzureMarketplacePriceAndAvailabilityPrivateOfferPrice(BaseModel):
    """
    AzureMarketplacePriceAndAvailabilityPrivateOfferPrice
    """ # noqa: E501
    custom_meters: Optional[AzureMarketplacePriceAndAvailabilityPrivateOfferCustomMeters] = Field(default=None, alias="customMeters")
    recurrent_price: Optional[AzureMarketplacePriceAndAvailabilityRecurrentPrice] = Field(default=None, alias="recurrentPrice")
    __properties: ClassVar[List[str]] = ["customMeters", "recurrentPrice"]

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
        """Create an instance of AzureMarketplacePriceAndAvailabilityPrivateOfferPrice from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of custom_meters
        if self.custom_meters:
            _dict['customMeters'] = self.custom_meters.to_dict()
        # override the default output from pydantic by calling `to_dict()` of recurrent_price
        if self.recurrent_price:
            _dict['recurrentPrice'] = self.recurrent_price.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AzureMarketplacePriceAndAvailabilityPrivateOfferPrice from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "customMeters": AzureMarketplacePriceAndAvailabilityPrivateOfferCustomMeters.from_dict(obj["customMeters"]) if obj.get("customMeters") is not None else None,
            "recurrentPrice": AzureMarketplacePriceAndAvailabilityRecurrentPrice.from_dict(obj["recurrentPrice"]) if obj.get("recurrentPrice") is not None else None
        })
        return _obj


