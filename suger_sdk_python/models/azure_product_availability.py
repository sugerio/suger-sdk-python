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
from suger_sdk_python.models.azure_audience import AzureAudience
from typing import Optional, Set
from typing_extensions import Self

class AzureProductAvailability(BaseModel):
    """
    AzureProductAvailability
    """ # noqa: E501
    email_audiences: Optional[List[AzureAudience]] = Field(default=None, alias="emailAudiences")
    enterprise_licensing: Optional[StrictStr] = Field(default=None, alias="enterpriseLicensing")
    id: Optional[StrictStr] = None
    resource_type: Optional[StrictStr] = Field(default=None, alias="resourceType")
    subscription_audiences: Optional[List[AzureAudience]] = Field(default=None, alias="subscriptionAudiences")
    visibility: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["emailAudiences", "enterpriseLicensing", "id", "resourceType", "subscriptionAudiences", "visibility"]

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
        """Create an instance of AzureProductAvailability from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in email_audiences (list)
        _items = []
        if self.email_audiences:
            for _item_email_audiences in self.email_audiences:
                if _item_email_audiences:
                    _items.append(_item_email_audiences.to_dict())
            _dict['emailAudiences'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in subscription_audiences (list)
        _items = []
        if self.subscription_audiences:
            for _item_subscription_audiences in self.subscription_audiences:
                if _item_subscription_audiences:
                    _items.append(_item_subscription_audiences.to_dict())
            _dict['subscriptionAudiences'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AzureProductAvailability from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "emailAudiences": [AzureAudience.from_dict(_item) for _item in obj["emailAudiences"]] if obj.get("emailAudiences") is not None else None,
            "enterpriseLicensing": obj.get("enterpriseLicensing"),
            "id": obj.get("id"),
            "resourceType": obj.get("resourceType"),
            "subscriptionAudiences": [AzureAudience.from_dict(_item) for _item in obj["subscriptionAudiences"]] if obj.get("subscriptionAudiences") is not None else None,
            "visibility": obj.get("visibility")
        })
        return _obj


