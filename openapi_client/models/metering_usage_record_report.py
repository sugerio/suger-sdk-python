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

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, StrictStr, validator
from openapi_client.models.metering_usage_record_report_info import MeteringUsageRecordReportInfo

class MeteringUsageRecordReport(BaseModel):
    """
    MeteringUsageRecordReport
    """
    buyer_id: Optional[StrictStr] = Field(None, alias="buyerID")
    creation_time: Optional[datetime] = Field(None, alias="creationTime")
    entitlement_id: Optional[StrictStr] = Field(None, alias="entitlementID")
    entitlement_term_id: Optional[StrictStr] = Field(None, alias="entitlementTermID")
    id: Optional[StrictStr] = None
    info: Optional[MeteringUsageRecordReportInfo] = None
    organization_id: Optional[StrictStr] = Field(None, alias="organizationID")
    partner: Optional[StrictStr] = None
    product_id: Optional[StrictStr] = Field(None, alias="productID")
    __properties = ["buyerID", "creationTime", "entitlementID", "entitlementTermID", "id", "info", "organizationID", "partner", "productID"]

    @validator('partner')
    def partner_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('AWS', 'AZURE', 'GCP'):
            raise ValueError("must be one of enum values ('AWS', 'AZURE', 'GCP')")
        return value

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
    def from_json(cls, json_str: str) -> MeteringUsageRecordReport:
        """Create an instance of MeteringUsageRecordReport from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of info
        if self.info:
            _dict['info'] = self.info.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MeteringUsageRecordReport:
        """Create an instance of MeteringUsageRecordReport from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MeteringUsageRecordReport.parse_obj(obj)

        _obj = MeteringUsageRecordReport.parse_obj({
            "buyer_id": obj.get("buyerID"),
            "creation_time": obj.get("creationTime"),
            "entitlement_id": obj.get("entitlementID"),
            "entitlement_term_id": obj.get("entitlementTermID"),
            "id": obj.get("id"),
            "info": MeteringUsageRecordReportInfo.from_dict(obj.get("info")) if obj.get("info") is not None else None,
            "organization_id": obj.get("organizationID"),
            "partner": obj.get("partner"),
            "product_id": obj.get("productID")
        })
        return _obj


