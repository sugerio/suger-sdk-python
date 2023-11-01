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
from pydantic import BaseModel, Field, StrictStr, conlist
from openapi_client.models.servicecontrol_report_error import ServicecontrolReportError


class ServicecontrolReportResponse(BaseModel):
    """
    ServicecontrolReportResponse
    """

    report_errors: Optional[conlist(ServicecontrolReportError)] = Field(
        None,
        alias="reportErrors",
        description="ReportErrors: Partial failures, one for each `Operation` in the request that failed processing. There are three possible combinations of the RPC status: 1. The combination of a successful RPC status and an empty `report_errors` list indicates a complete success where all `Operations` in the request are processed successfully. 2. The combination of a successful RPC status and a non-empty `report_errors` list indicates a partial success where some `Operations` in the request succeeded. Each `Operation` that failed processing has a corresponding item in this list. 3. A failed RPC status indicates a general non-deterministic failure. When this happens, it's impossible to know which of the 'Operations' in the request succeeded or failed.",
    )
    service_config_id: Optional[StrictStr] = Field(
        None,
        alias="serviceConfigId",
        description="ServiceConfigId: The actual config id used to process the request.",
    )
    service_rollout_id: Optional[StrictStr] = Field(
        None,
        alias="serviceRolloutId",
        description="ServiceRolloutId: The current service rollout id used to process the request.",
    )
    __properties = ["reportErrors", "serviceConfigId", "serviceRolloutId"]

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
    def from_json(cls, json_str: str) -> ServicecontrolReportResponse:
        """Create an instance of ServicecontrolReportResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in report_errors (list)
        _items = []
        if self.report_errors:
            for _item in self.report_errors:
                if _item:
                    _items.append(_item.to_dict())
            _dict["reportErrors"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ServicecontrolReportResponse:
        """Create an instance of ServicecontrolReportResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ServicecontrolReportResponse.parse_obj(obj)

        _obj = ServicecontrolReportResponse.parse_obj(
            {
                "report_errors": [
                    ServicecontrolReportError.from_dict(_item)
                    for _item in obj.get("reportErrors")
                ]
                if obj.get("reportErrors") is not None
                else None,
                "service_config_id": obj.get("serviceConfigId"),
                "service_rollout_id": obj.get("serviceRolloutId"),
            }
        )
        return _obj