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
from suger_sdk_python.models.gcp_price_tier import GcpPriceTier
from typing import Optional, Set
from typing_extensions import Self

class GcpMarketplacePrivateOfferMetricDetail(BaseModel):
    """
    GcpMarketplacePrivateOfferMetricDetail
    """ # noqa: E501
    display_name: Optional[StrictStr] = Field(default=None, description="such as \"CPU\"", alias="displayName")
    parent_commerce_service: Optional[StrictStr] = Field(default=None, description="in format of \"projects/{projectNumber}/services/service-name.endpoints.gcp-project-id.cloud.goog\"", alias="parentCommerceService")
    sku_id: Optional[StrictStr] = Field(default=None, description="such as \"BC1B-6259-BF57\"", alias="skuId")
    tiers: Optional[List[GcpPriceTier]] = Field(default=None, description="Price tiers for this metric.")
    unit_description: Optional[StrictStr] = Field(default=None, description="such as \"minute\"", alias="unitDescription")
    __properties: ClassVar[List[str]] = ["displayName", "parentCommerceService", "skuId", "tiers", "unitDescription"]

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
        """Create an instance of GcpMarketplacePrivateOfferMetricDetail from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in tiers (list)
        _items = []
        if self.tiers:
            for _item_tiers in self.tiers:
                if _item_tiers:
                    _items.append(_item_tiers.to_dict())
            _dict['tiers'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GcpMarketplacePrivateOfferMetricDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "displayName": obj.get("displayName"),
            "parentCommerceService": obj.get("parentCommerceService"),
            "skuId": obj.get("skuId"),
            "tiers": [GcpPriceTier.from_dict(_item) for _item in obj["tiers"]] if obj.get("tiers") is not None else None,
            "unitDescription": obj.get("unitDescription")
        })
        return _obj


