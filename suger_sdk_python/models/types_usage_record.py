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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from suger_sdk_python.models.types_usage_allocation import TypesUsageAllocation
from typing import Optional, Set
from typing_extensions import Self

class TypesUsageRecord(BaseModel):
    """
    TypesUsageRecord
    """ # noqa: E501
    customer_identifier: Optional[StrictStr] = Field(default=None, description="The CustomerIdentifier is obtained through the ResolveCustomer operation and represents an individual buyer in your application.  This member is required.", alias="customerIdentifier")
    dimension: Optional[StrictStr] = Field(default=None, description="During the process of registering a product on AWS Marketplace, dimensions are specified. These represent different units of value in your application.  This member is required.")
    quantity: Optional[StrictInt] = Field(default=None, description="The quantity of usage consumed by the customer for the given dimension and time. Defaults to 0 if not specified.")
    timestamp: Optional[StrictStr] = Field(default=None, description="Timestamp, in UTC, for which the usage is being reported. Your application can meter usage for up to one hour in the past. Make sure the timestamp value is not before the start of the software usage.  This member is required.")
    usage_allocations: Optional[List[TypesUsageAllocation]] = Field(default=None, description="The set of UsageAllocations to submit. The sum of all UsageAllocation quantities must equal the Quantity of the UsageRecord .", alias="usageAllocations")
    __properties: ClassVar[List[str]] = ["customerIdentifier", "dimension", "quantity", "timestamp", "usageAllocations"]

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
        """Create an instance of TypesUsageRecord from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in usage_allocations (list)
        _items = []
        if self.usage_allocations:
            for _item_usage_allocations in self.usage_allocations:
                if _item_usage_allocations:
                    _items.append(_item_usage_allocations.to_dict())
            _dict['usageAllocations'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TypesUsageRecord from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "customerIdentifier": obj.get("customerIdentifier"),
            "dimension": obj.get("dimension"),
            "quantity": obj.get("quantity"),
            "timestamp": obj.get("timestamp"),
            "usageAllocations": [TypesUsageAllocation.from_dict(_item) for _item in obj["usageAllocations"]] if obj.get("usageAllocations") is not None else None
        })
        return _obj


