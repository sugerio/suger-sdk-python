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
from pydantic import BaseModel, Field, conlist
from openapi_client.models.gcp_marketplace_product_feature import GcpMarketplaceProductFeature
from openapi_client.models.gcp_marketplace_product_metering_metric import GcpMarketplaceProductMeteringMetric
from openapi_client.models.gcp_marketplace_product_purchase_option_spec import GcpMarketplaceProductPurchaseOptionSpec

class GcpMarketplaceProductPurchaseSpec(BaseModel):
    """
    GcpMarketplaceProductPurchaseSpec
    """
    features: Optional[conlist(GcpMarketplaceProductFeature)] = None
    metrics: Optional[conlist(GcpMarketplaceProductMeteringMetric)] = Field(None, description="GCP Marketplace Product Usage Metering Dimension/Metric")
    purchase_option_specs: Optional[conlist(GcpMarketplaceProductPurchaseOptionSpec)] = Field(None, alias="purchaseOptionSpecs", description="GCP Marketplace Product Pricing Plans")
    __properties = ["features", "metrics", "purchaseOptionSpecs"]

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
    def from_json(cls, json_str: str) -> GcpMarketplaceProductPurchaseSpec:
        """Create an instance of GcpMarketplaceProductPurchaseSpec from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in features (list)
        _items = []
        if self.features:
            for _item in self.features:
                if _item:
                    _items.append(_item.to_dict())
            _dict['features'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in metrics (list)
        _items = []
        if self.metrics:
            for _item in self.metrics:
                if _item:
                    _items.append(_item.to_dict())
            _dict['metrics'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in purchase_option_specs (list)
        _items = []
        if self.purchase_option_specs:
            for _item in self.purchase_option_specs:
                if _item:
                    _items.append(_item.to_dict())
            _dict['purchaseOptionSpecs'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GcpMarketplaceProductPurchaseSpec:
        """Create an instance of GcpMarketplaceProductPurchaseSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GcpMarketplaceProductPurchaseSpec.parse_obj(obj)

        _obj = GcpMarketplaceProductPurchaseSpec.parse_obj({
            "features": [GcpMarketplaceProductFeature.from_dict(_item) for _item in obj.get("features")] if obj.get("features") is not None else None,
            "metrics": [GcpMarketplaceProductMeteringMetric.from_dict(_item) for _item in obj.get("metrics")] if obj.get("metrics") is not None else None,
            "purchase_option_specs": [GcpMarketplaceProductPurchaseOptionSpec.from_dict(_item) for _item in obj.get("purchaseOptionSpecs")] if obj.get("purchaseOptionSpecs") is not None else None
        })
        return _obj


