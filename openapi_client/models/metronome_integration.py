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
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist
from openapi_client.models.metronome_billable_metric import MetronomeBillableMetric

class MetronomeIntegration(BaseModel):
    """
    MetronomeIntegration
    """
    api_token: Optional[StrictStr] = Field(None, alias="apiToken", description="The Bearer token for the metronome API. Required only when the metronome integration is created or updated with new API token.")
    billable_metric_full_list: Optional[conlist(MetronomeBillableMetric)] = Field(None, alias="billableMetricFullList", description="The full list of billable metrics fetched from metronome API for the available metronome customers.")
    billable_metric_whitelist: Optional[conlist(MetronomeBillableMetric)] = Field(None, alias="billableMetricWhitelist", description="The whitelist of billable metrics. Only the metrics in the whitelist will be metered & reported to cloud marketplace.")
    enable_auto_report_usage: Optional[StrictBool] = Field(None, alias="enableAutoReportUsage", description="Whether to enable the auto usage report for the metronome integration. If enabled, cron job runs every hour to fetch usage events from Metronome to Suger as UsageRecordGroups.")
    enable_billable_metric_whitelist: Optional[StrictBool] = Field(None, alias="enableBillableMetricWhitelist", description="Enable whitelist for billable metrics. If enabled, only the metrics in the whitelist will be metered & reported to cloud marketplace. Otherwise all the metrics in the billableMetricFullList will be metered & reported to cloud marketplace.")
    secret_key: Optional[StrictStr] = Field(None, alias="secretKey", description="The secret key used to store the ApiToken in AWS Secret manager. For internal usage only.")
    __properties = ["apiToken", "billableMetricFullList", "billableMetricWhitelist", "enableAutoReportUsage", "enableBillableMetricWhitelist", "secretKey"]

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
    def from_json(cls, json_str: str) -> MetronomeIntegration:
        """Create an instance of MetronomeIntegration from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in billable_metric_full_list (list)
        _items = []
        if self.billable_metric_full_list:
            for _item in self.billable_metric_full_list:
                if _item:
                    _items.append(_item.to_dict())
            _dict['billableMetricFullList'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in billable_metric_whitelist (list)
        _items = []
        if self.billable_metric_whitelist:
            for _item in self.billable_metric_whitelist:
                if _item:
                    _items.append(_item.to_dict())
            _dict['billableMetricWhitelist'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MetronomeIntegration:
        """Create an instance of MetronomeIntegration from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MetronomeIntegration.parse_obj(obj)

        _obj = MetronomeIntegration.parse_obj({
            "api_token": obj.get("apiToken"),
            "billable_metric_full_list": [MetronomeBillableMetric.from_dict(_item) for _item in obj.get("billableMetricFullList")] if obj.get("billableMetricFullList") is not None else None,
            "billable_metric_whitelist": [MetronomeBillableMetric.from_dict(_item) for _item in obj.get("billableMetricWhitelist")] if obj.get("billableMetricWhitelist") is not None else None,
            "enable_auto_report_usage": obj.get("enableAutoReportUsage"),
            "enable_billable_metric_whitelist": obj.get("enableBillableMetricWhitelist"),
            "secret_key": obj.get("secretKey")
        })
        return _obj


