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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class AzureMarketplaceMeteringUsageEvent(BaseModel):
    """
    AzureMarketplaceMeteringUsageEvent
    """ # noqa: E501
    dimension: Optional[StrictStr] = Field(default=None, description="Dimension identifier")
    effective_start_time: Optional[StrictStr] = Field(default=None, description="Time in UTC when the usage event occurred", alias="effectiveStartTime")
    plan_id: Optional[StrictStr] = Field(default=None, description="Plan associated with the purchased offer", alias="planId")
    quantity: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Number of units consumed")
    resource_id: Optional[StrictStr] = Field(default=None, description="subscriptionId property value for SaaS offer subscriptions; resourceUsageId property on the managed application resource for managed application offers. For managed applications, only use one of resourceId or resourceUri.", alias="resourceId")
    resource_uri: Optional[StrictStr] = Field(default=None, description="Resource URI for the managed app. Used with managed applications. Only use resourceUri or resourceId, but never both.", alias="resourceUri")
    __properties: ClassVar[List[str]] = ["dimension", "effectiveStartTime", "planId", "quantity", "resourceId", "resourceUri"]

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
        """Create an instance of AzureMarketplaceMeteringUsageEvent from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AzureMarketplaceMeteringUsageEvent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "dimension": obj.get("dimension"),
            "effectiveStartTime": obj.get("effectiveStartTime"),
            "planId": obj.get("planId"),
            "quantity": obj.get("quantity"),
            "resourceId": obj.get("resourceId"),
            "resourceUri": obj.get("resourceUri")
        })
        return _obj


