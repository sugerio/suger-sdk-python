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
from openapi_client.models.orb_billable_metric import OrbBillableMetric
from openapi_client.models.orb_billing_mode import OrbBillingMode
from openapi_client.models.orb_plan import OrbPlan

class OrbIntegration(BaseModel):
    """
    OrbIntegration
    """
    api_key: Optional[StrictStr] = Field(None, alias="apiKey", description="The Bearer key to access the orb API.")
    billable_metric_full_list: Optional[conlist(OrbBillableMetric)] = Field(None, alias="billableMetricFullList")
    billing_mode: Optional[OrbBillingMode] = Field(None, alias="billingMode")
    enable_auto_report_usage: Optional[StrictBool] = Field(None, alias="enableAutoReportUsage", description="Whether to enable the auto usage report for the orb integration. If enabled, cron job runs every hour to fetch usage events from Orb to Suger as UsageRecordGroups.")
    plan_full_list: Optional[conlist(OrbPlan)] = Field(None, alias="planFullList")
    secret_key: Optional[StrictStr] = Field(None, alias="secretKey", description="The secret key used to store the ApiKey in AWS Secret manager. For internal usage only.")
    __properties = ["apiKey", "billableMetricFullList", "billingMode", "enableAutoReportUsage", "planFullList", "secretKey"]

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
    def from_json(cls, json_str: str) -> OrbIntegration:
        """Create an instance of OrbIntegration from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in plan_full_list (list)
        _items = []
        if self.plan_full_list:
            for _item in self.plan_full_list:
                if _item:
                    _items.append(_item.to_dict())
            _dict['planFullList'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OrbIntegration:
        """Create an instance of OrbIntegration from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OrbIntegration.parse_obj(obj)

        _obj = OrbIntegration.parse_obj({
            "api_key": obj.get("apiKey"),
            "billable_metric_full_list": [OrbBillableMetric.from_dict(_item) for _item in obj.get("billableMetricFullList")] if obj.get("billableMetricFullList") is not None else None,
            "billing_mode": obj.get("billingMode"),
            "enable_auto_report_usage": obj.get("enableAutoReportUsage"),
            "plan_full_list": [OrbPlan.from_dict(_item) for _item in obj.get("planFullList")] if obj.get("planFullList") is not None else None,
            "secret_key": obj.get("secretKey")
        })
        return _obj


