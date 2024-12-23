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
from suger_sdk_python.models.gcp_marketplace_product_feature_value import GcpMarketplaceProductFeatureValue
from suger_sdk_python.models.gcp_marketplace_product_price_info import GcpMarketplaceProductPriceInfo
from typing import Optional, Set
from typing_extensions import Self

class GcpMarketplaceProductPurchaseOptionSpec(BaseModel):
    """
    GcpMarketplaceProductPurchaseOptionSpec
    """ # noqa: E501
    feature_values: Optional[List[GcpMarketplaceProductFeatureValue]] = Field(default=None, alias="featureValues")
    name: Optional[StrictStr] = Field(default=None, description="The plan ID, such as \"starter\", without the duration suffix, such as \"P1Y\".")
    price_info: Optional[GcpMarketplaceProductPriceInfo] = Field(default=None, alias="priceInfo")
    purchase_mode: Optional[StrictStr] = Field(default=None, alias="purchaseMode")
    title: Optional[StrictStr] = Field(default=None, description="such as \"Starter\"")
    __properties: ClassVar[List[str]] = ["featureValues", "name", "priceInfo", "purchaseMode", "title"]

    @field_validator('purchase_mode')
    def purchase_mode_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['PURCHASE_MODE_PRIVATE', 'PURCHASE_MODE_PUBLIC']):
            raise ValueError("must be one of enum values ('PURCHASE_MODE_PRIVATE', 'PURCHASE_MODE_PUBLIC')")
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
        """Create an instance of GcpMarketplaceProductPurchaseOptionSpec from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in feature_values (list)
        _items = []
        if self.feature_values:
            for _item_feature_values in self.feature_values:
                if _item_feature_values:
                    _items.append(_item_feature_values.to_dict())
            _dict['featureValues'] = _items
        # override the default output from pydantic by calling `to_dict()` of price_info
        if self.price_info:
            _dict['priceInfo'] = self.price_info.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GcpMarketplaceProductPurchaseOptionSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "featureValues": [GcpMarketplaceProductFeatureValue.from_dict(_item) for _item in obj["featureValues"]] if obj.get("featureValues") is not None else None,
            "name": obj.get("name"),
            "priceInfo": GcpMarketplaceProductPriceInfo.from_dict(obj["priceInfo"]) if obj.get("priceInfo") is not None else None,
            "purchaseMode": obj.get("purchaseMode"),
            "title": obj.get("title")
        })
        return _obj


