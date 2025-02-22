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
from suger_sdk_python.models.alibaba_marketplace_product_sku_modules import AlibabaMarketplaceProductSkuModules
from suger_sdk_python.models.alibaba_marketplace_product_sku_order_periods import AlibabaMarketplaceProductSkuOrderPeriods
from typing import Optional, Set
from typing_extensions import Self

class AlibabaMarketplaceProductSku(BaseModel):
    """
    AlibabaMarketplaceProductSku
    """ # noqa: E501
    charge_type: Optional[StrictStr] = Field(default=None, description="POSTPAY or PREPAY", alias="ChargeType")
    code: Optional[StrictStr] = Field(default=None, alias="Code")
    constraints: Optional[StrictStr] = Field(default=None, alias="Constraints")
    hidden: Optional[StrictBool] = Field(default=None, alias="Hidden")
    modules: Optional[AlibabaMarketplaceProductSkuModules] = Field(default=None, alias="Modules")
    name: Optional[StrictStr] = Field(default=None, alias="Name")
    order_periods: Optional[AlibabaMarketplaceProductSkuOrderPeriods] = Field(default=None, alias="OrderPeriods")
    __properties: ClassVar[List[str]] = ["ChargeType", "Code", "Constraints", "Hidden", "Modules", "Name", "OrderPeriods"]

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
        """Create an instance of AlibabaMarketplaceProductSku from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of modules
        if self.modules:
            _dict['Modules'] = self.modules.to_dict()
        # override the default output from pydantic by calling `to_dict()` of order_periods
        if self.order_periods:
            _dict['OrderPeriods'] = self.order_periods.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AlibabaMarketplaceProductSku from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ChargeType": obj.get("ChargeType"),
            "Code": obj.get("Code"),
            "Constraints": obj.get("Constraints"),
            "Hidden": obj.get("Hidden"),
            "Modules": AlibabaMarketplaceProductSkuModules.from_dict(obj["Modules"]) if obj.get("Modules") is not None else None,
            "Name": obj.get("Name"),
            "OrderPeriods": AlibabaMarketplaceProductSkuOrderPeriods.from_dict(obj["OrderPeriods"]) if obj.get("OrderPeriods") is not None else None
        })
        return _obj


