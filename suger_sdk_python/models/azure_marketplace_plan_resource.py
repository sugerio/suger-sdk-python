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
from suger_sdk_python.models.azure_marketplace_plan import AzureMarketplacePlan
from suger_sdk_python.models.azure_marketplace_plan_listing import AzureMarketplacePlanListing
from suger_sdk_python.models.azure_marketplace_price_and_availability_plan import AzureMarketplacePriceAndAvailabilityPlan
from typing import Optional, Set
from typing_extensions import Self

class AzureMarketplacePlanResource(BaseModel):
    """
    AzureMarketplacePlanResource
    """ # noqa: E501
    plan: Optional[AzureMarketplacePlan] = None
    plan_listing: Optional[AzureMarketplacePlanListing] = Field(default=None, alias="planListing")
    price_and_availability_plan: Optional[AzureMarketplacePriceAndAvailabilityPlan] = Field(default=None, alias="priceAndAvailabilityPlan")
    __properties: ClassVar[List[str]] = ["plan", "planListing", "priceAndAvailabilityPlan"]

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
        """Create an instance of AzureMarketplacePlanResource from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of plan
        if self.plan:
            _dict['plan'] = self.plan.to_dict()
        # override the default output from pydantic by calling `to_dict()` of plan_listing
        if self.plan_listing:
            _dict['planListing'] = self.plan_listing.to_dict()
        # override the default output from pydantic by calling `to_dict()` of price_and_availability_plan
        if self.price_and_availability_plan:
            _dict['priceAndAvailabilityPlan'] = self.price_and_availability_plan.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AzureMarketplacePlanResource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "plan": AzureMarketplacePlan.from_dict(obj["plan"]) if obj.get("plan") is not None else None,
            "planListing": AzureMarketplacePlanListing.from_dict(obj["planListing"]) if obj.get("planListing") is not None else None,
            "priceAndAvailabilityPlan": AzureMarketplacePriceAndAvailabilityPlan.from_dict(obj["priceAndAvailabilityPlan"]) if obj.get("priceAndAvailabilityPlan") is not None else None
        })
        return _obj

