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
from openapi_client.models.gcp_price_tier import GcpPriceTier
from openapi_client.models.value_type import ValueType

class GcpMarketplaceProductMeteringMetric(BaseModel):
    """
    GcpMarketplaceProductMeteringMetric
    """
    description: Optional[StrictStr] = Field(None, description="Description: A detailed description of the metric, which can be used in documentation.")
    display_name: Optional[StrictStr] = Field(None, alias="displayName")
    display_unit: Optional[StrictStr] = Field(None, alias="displayUnit", description="such as \"min\"")
    display_unit_description: Optional[StrictStr] = Field(None, alias="displayUnitDescription", description="such as \"minute\"")
    id: Optional[StrictStr] = Field(None, description="The usage metering metric/dimension key, all in lower case with underscore. It is in format of \"{plan_id}_{usage_dimension_key}\". For example, \"basic_plan_storage\".")
    metric_kind: Optional[StrictStr] = Field(None, alias="metricKind", description="such as \"DELTA\"")
    name: Optional[StrictStr] = Field(None, description="Name: The resource name of the metric descriptor, in format of \"{productServiceName}/{plan_id}_{usage_dimension_key}\"")
    price_tiers: Optional[conlist(GcpPriceTier)] = Field(None, alias="priceTiers", description="Price info of this usage metering metric. Only applicable for the default offer (plan) and private offer.")
    reporting_unit: Optional[StrictStr] = Field(None, alias="reportingUnit", description="such as \"min\"")
    sku_id: Optional[StrictStr] = Field(None, alias="skuId", description="The SKU ID of this usage metering metric. Applicable only in Private Offer.")
    unit: Optional[StrictStr] = Field(None, description="such as \"min\"")
    value_type: Optional[ValueType] = Field(None, alias="valueType")
    __properties = ["description", "displayName", "displayUnit", "displayUnitDescription", "id", "metricKind", "name", "priceTiers", "reportingUnit", "skuId", "unit", "valueType"]

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
    def from_json(cls, json_str: str) -> GcpMarketplaceProductMeteringMetric:
        """Create an instance of GcpMarketplaceProductMeteringMetric from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in price_tiers (list)
        _items = []
        if self.price_tiers:
            for _item in self.price_tiers:
                if _item:
                    _items.append(_item.to_dict())
            _dict['priceTiers'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GcpMarketplaceProductMeteringMetric:
        """Create an instance of GcpMarketplaceProductMeteringMetric from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GcpMarketplaceProductMeteringMetric.parse_obj(obj)

        _obj = GcpMarketplaceProductMeteringMetric.parse_obj({
            "description": obj.get("description"),
            "display_name": obj.get("displayName"),
            "display_unit": obj.get("displayUnit"),
            "display_unit_description": obj.get("displayUnitDescription"),
            "id": obj.get("id"),
            "metric_kind": obj.get("metricKind"),
            "name": obj.get("name"),
            "price_tiers": [GcpPriceTier.from_dict(_item) for _item in obj.get("priceTiers")] if obj.get("priceTiers") is not None else None,
            "reporting_unit": obj.get("reportingUnit"),
            "sku_id": obj.get("skuId"),
            "unit": obj.get("unit"),
            "value_type": obj.get("valueType")
        })
        return _obj


