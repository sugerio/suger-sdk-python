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


from typing import Dict, Optional
from pydantic import BaseModel, StrictStr
from openapi_client.models.orb_billable_metric_status import OrbBillableMetricStatus

class OrbBillableMetric(BaseModel):
    """
    OrbBillableMetric
    """
    description: Optional[StrictStr] = None
    id: Optional[StrictStr] = None
    metadata: Optional[Dict[str, StrictStr]] = None
    name: Optional[StrictStr] = None
    status: Optional[OrbBillableMetricStatus] = None
    __properties = ["description", "id", "metadata", "name", "status"]

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
    def from_json(cls, json_str: str) -> OrbBillableMetric:
        """Create an instance of OrbBillableMetric from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OrbBillableMetric:
        """Create an instance of OrbBillableMetric from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OrbBillableMetric.parse_obj(obj)

        _obj = OrbBillableMetric.parse_obj({
            "description": obj.get("description"),
            "id": obj.get("id"),
            "metadata": obj.get("metadata"),
            "name": obj.get("name"),
            "status": obj.get("status")
        })
        return _obj


