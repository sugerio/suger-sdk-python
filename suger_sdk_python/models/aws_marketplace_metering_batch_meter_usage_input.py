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
from suger_sdk_python.models.aws_marketplace_metering_usage_record import AwsMarketplaceMeteringUsageRecord
from typing import Optional, Set
from typing_extensions import Self

class AwsMarketplaceMeteringBatchMeterUsageInput(BaseModel):
    """
    AwsMarketplaceMeteringBatchMeterUsageInput
    """ # noqa: E501
    product_code: Optional[StrictStr] = Field(default=None, description="Product code is used to uniquely identify a product in AWS Marketplace. The product code should be the same as the one used during the publishing of a new product.", alias="ProductCode")
    usage_records: Optional[List[AwsMarketplaceMeteringUsageRecord]] = Field(default=None, description="The set of UsageRecords to submit. BatchMeterUsage accepts up to 25 UsageRecords at a time.", alias="UsageRecords")
    __properties: ClassVar[List[str]] = ["ProductCode", "UsageRecords"]

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
        """Create an instance of AwsMarketplaceMeteringBatchMeterUsageInput from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in usage_records (list)
        _items = []
        if self.usage_records:
            for _item_usage_records in self.usage_records:
                if _item_usage_records:
                    _items.append(_item_usage_records.to_dict())
            _dict['UsageRecords'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AwsMarketplaceMeteringBatchMeterUsageInput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ProductCode": obj.get("ProductCode"),
            "UsageRecords": [AwsMarketplaceMeteringUsageRecord.from_dict(_item) for _item in obj["UsageRecords"]] if obj.get("UsageRecords") is not None else None
        })
        return _obj


