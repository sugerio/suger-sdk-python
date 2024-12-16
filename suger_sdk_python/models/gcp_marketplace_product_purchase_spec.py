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
from suger_sdk_python.models.gcp_marketplace_product_feature import GcpMarketplaceProductFeature
from suger_sdk_python.models.gcp_marketplace_product_metering_metric import GcpMarketplaceProductMeteringMetric
from suger_sdk_python.models.gcp_marketplace_product_purchase_option_spec import GcpMarketplaceProductPurchaseOptionSpec
from typing import Optional, Set
from typing_extensions import Self

class GcpMarketplaceProductPurchaseSpec(BaseModel):
    """
    GcpMarketplaceProductPurchaseSpec
    """ # noqa: E501
    features: Optional[List[GcpMarketplaceProductFeature]] = None
    metrics: Optional[List[GcpMarketplaceProductMeteringMetric]] = Field(default=None, description="GCP Marketplace Product Usage Metering Dimension/Metric")
    purchase_option_specs: Optional[List[GcpMarketplaceProductPurchaseOptionSpec]] = Field(default=None, description="GCP Marketplace Product Pricing Plans", alias="purchaseOptionSpecs")
    __properties: ClassVar[List[str]] = ["features", "metrics", "purchaseOptionSpecs"]

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
        """Create an instance of GcpMarketplaceProductPurchaseSpec from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in features (list)
        _items = []
        if self.features:
            for _item_features in self.features:
                if _item_features:
                    _items.append(_item_features.to_dict())
            _dict['features'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in metrics (list)
        _items = []
        if self.metrics:
            for _item_metrics in self.metrics:
                if _item_metrics:
                    _items.append(_item_metrics.to_dict())
            _dict['metrics'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in purchase_option_specs (list)
        _items = []
        if self.purchase_option_specs:
            for _item_purchase_option_specs in self.purchase_option_specs:
                if _item_purchase_option_specs:
                    _items.append(_item_purchase_option_specs.to_dict())
            _dict['purchaseOptionSpecs'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GcpMarketplaceProductPurchaseSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "features": [GcpMarketplaceProductFeature.from_dict(_item) for _item in obj["features"]] if obj.get("features") is not None else None,
            "metrics": [GcpMarketplaceProductMeteringMetric.from_dict(_item) for _item in obj["metrics"]] if obj.get("metrics") is not None else None,
            "purchaseOptionSpecs": [GcpMarketplaceProductPurchaseOptionSpec.from_dict(_item) for _item in obj["purchaseOptionSpecs"]] if obj.get("purchaseOptionSpecs") is not None else None
        })
        return _obj

