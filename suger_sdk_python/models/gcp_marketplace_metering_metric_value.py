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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from suger_sdk_python.models.gcp_marketplace_metering_money import GcpMarketplaceMeteringMoney
from typing import Optional, Set
from typing_extensions import Self

class GcpMarketplaceMeteringMetricValue(BaseModel):
    """
    GcpMarketplaceMeteringMetricValue
    """ # noqa: E501
    bool_value: Optional[StrictBool] = Field(default=None, description="BoolValue: A boolean value.", alias="boolValue")
    double_value: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="DoubleValue: A double precision floating point value.", alias="doubleValue")
    end_time: Optional[StrictStr] = Field(default=None, description="EndTime: The end of the time period over which this metric value's measurement applies. If not specified, google.api.servicecontrol.v1.Operation.end_time will be used.", alias="endTime")
    int64_value: Optional[StrictStr] = Field(default=None, description="Int64Value: A signed 64-bit integer value.", alias="int64Value")
    labels: Optional[Dict[str, StrictStr]] = Field(default=None, description="Labels: The labels describing the metric value. See comments on google.api.servicecontrol.v1.Operation.labels for the overriding relationship. Note that this map must not contain monitored resource labels.")
    money_value: Optional[GcpMarketplaceMeteringMoney] = Field(default=None, description="MoneyValue: A money value.", alias="moneyValue")
    start_time: Optional[StrictStr] = Field(default=None, description="StartTime: The start of the time period over which this metric value's measurement applies. The time period has different semantics for different metric types (cumulative, delta, and gauge). See the metric definition documentation in the service configuration for details. If not specified, google.api.servicecontrol.v1.Operation.start_time will be used.", alias="startTime")
    string_value: Optional[StrictStr] = Field(default=None, description="StringValue: A text string value.", alias="stringValue")
    __properties: ClassVar[List[str]] = ["boolValue", "doubleValue", "endTime", "int64Value", "labels", "moneyValue", "startTime", "stringValue"]

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
        """Create an instance of GcpMarketplaceMeteringMetricValue from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of money_value
        if self.money_value:
            _dict['moneyValue'] = self.money_value.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GcpMarketplaceMeteringMetricValue from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "boolValue": obj.get("boolValue"),
            "doubleValue": obj.get("doubleValue"),
            "endTime": obj.get("endTime"),
            "int64Value": obj.get("int64Value"),
            "labels": obj.get("labels"),
            "moneyValue": GcpMarketplaceMeteringMoney.from_dict(obj["moneyValue"]) if obj.get("moneyValue") is not None else None,
            "startTime": obj.get("startTime"),
            "stringValue": obj.get("stringValue")
        })
        return _obj

