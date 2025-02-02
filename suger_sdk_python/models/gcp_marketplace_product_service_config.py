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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from suger_sdk_python.models.gcp_marketplace_product_metering_metric import GcpMarketplaceProductMeteringMetric
from suger_sdk_python.models.gcp_marketplace_product_service_config_billing import GcpMarketplaceProductServiceConfigBilling
from typing import Optional, Set
from typing_extensions import Self

class GcpMarketplaceProductServiceConfig(BaseModel):
    """
    GcpMarketplaceProductServiceConfig
    """ # noqa: E501
    billing: Optional[GcpMarketplaceProductServiceConfigBilling] = None
    metrics: Optional[List[GcpMarketplaceProductMeteringMetric]] = None
    name: Optional[StrictStr] = Field(default=None, description="in format of \"product-name.endpoints.gcp-project-id.cloud.goog\"")
    producer_project_id: Optional[StrictStr] = Field(default=None, description="The GCP project ID of the producer.", alias="producerProjectId")
    title: Optional[StrictStr] = Field(default=None, description="The title of the product listing.")
    __properties: ClassVar[List[str]] = ["billing", "metrics", "name", "producerProjectId", "title"]

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
        """Create an instance of GcpMarketplaceProductServiceConfig from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of billing
        if self.billing:
            _dict['billing'] = self.billing.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in metrics (list)
        _items = []
        if self.metrics:
            for _item_metrics in self.metrics:
                if _item_metrics:
                    _items.append(_item_metrics.to_dict())
            _dict['metrics'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GcpMarketplaceProductServiceConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "billing": GcpMarketplaceProductServiceConfigBilling.from_dict(obj["billing"]) if obj.get("billing") is not None else None,
            "metrics": [GcpMarketplaceProductMeteringMetric.from_dict(_item) for _item in obj["metrics"]] if obj.get("metrics") is not None else None,
            "name": obj.get("name"),
            "producerProjectId": obj.get("producerProjectId"),
            "title": obj.get("title")
        })
        return _obj


