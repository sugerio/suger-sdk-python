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
from openapi_client.models.gcp_marketplace_product_metering_metric import (
    GcpMarketplaceProductMeteringMetric,
)
from openapi_client.models.gcp_marketplace_product_service_config_billing import (
    GcpMarketplaceProductServiceConfigBilling,
)


class GcpMarketplaceProductServiceConfig(BaseModel):
    """
    GcpMarketplaceProductServiceConfig
    """

    billing: Optional[GcpMarketplaceProductServiceConfigBilling] = None
    metrics: Optional[conlist(GcpMarketplaceProductMeteringMetric)] = None
    name: Optional[StrictStr] = Field(
        None,
        description='in format of "product-name.endpoints.gcp-project-id.cloud.goog"',
    )
    producer_project_id: Optional[StrictStr] = Field(
        None,
        alias="producerProjectId",
        description="The GCP project ID of the producer.",
    )
    title: Optional[StrictStr] = Field(
        None, description="The title of the product listing."
    )
    __properties = ["billing", "metrics", "name", "producerProjectId", "title"]

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
    def from_json(cls, json_str: str) -> GcpMarketplaceProductServiceConfig:
        """Create an instance of GcpMarketplaceProductServiceConfig from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of billing
        if self.billing:
            _dict["billing"] = self.billing.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in metrics (list)
        _items = []
        if self.metrics:
            for _item in self.metrics:
                if _item:
                    _items.append(_item.to_dict())
            _dict["metrics"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GcpMarketplaceProductServiceConfig:
        """Create an instance of GcpMarketplaceProductServiceConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GcpMarketplaceProductServiceConfig.parse_obj(obj)

        _obj = GcpMarketplaceProductServiceConfig.parse_obj(
            {
                "billing": GcpMarketplaceProductServiceConfigBilling.from_dict(
                    obj.get("billing")
                )
                if obj.get("billing") is not None
                else None,
                "metrics": [
                    GcpMarketplaceProductMeteringMetric.from_dict(_item)
                    for _item in obj.get("metrics")
                ]
                if obj.get("metrics") is not None
                else None,
                "name": obj.get("name"),
                "producer_project_id": obj.get("producerProjectId"),
                "title": obj.get("title"),
            }
        )
        return _obj