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


from typing import Optional
from pydantic import BaseModel, Field, StrictStr, validator
from openapi_client.models.revenue_report_type import RevenueReportType

class GetRevenueReportParams(BaseModel):
    """
    GetRevenueReportParams
    """
    buyer_id: Optional[StrictStr] = Field(None, alias="buyerID", description="Optional, if available, return the report for the Buyer.")
    entitlement_id: Optional[StrictStr] = Field(None, alias="entitlementID", description="Optional, if available, return the report for the Entitlement.")
    organization_id: StrictStr = Field(..., alias="organizationID", description="Required. If the productID & entitlementID are emtpy, return the report for the entire Organization.")
    partner: StrictStr = Field(...)
    product_id: Optional[StrictStr] = Field(None, alias="productID", description="Optional, if available, return the report for the Product.")
    report_type: RevenueReportType = Field(..., alias="reportType")
    service: StrictStr = Field(...)
    __properties = ["buyerID", "entitlementID", "organizationID", "partner", "productID", "reportType", "service"]

    @validator('partner')
    def partner_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('AWS', 'AZURE', 'GCP'):
            raise ValueError("must be one of enum values ('AWS', 'AZURE', 'GCP')")
        return value

    @validator('service')
    def service_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('MARKETPLACE'):
            raise ValueError("must be one of enum values ('MARKETPLACE')")
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
    def from_json(cls, json_str: str) -> GetRevenueReportParams:
        """Create an instance of GetRevenueReportParams from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GetRevenueReportParams:
        """Create an instance of GetRevenueReportParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GetRevenueReportParams.parse_obj(obj)

        _obj = GetRevenueReportParams.parse_obj({
            "buyer_id": obj.get("buyerID"),
            "entitlement_id": obj.get("entitlementID"),
            "organization_id": obj.get("organizationID"),
            "partner": obj.get("partner"),
            "product_id": obj.get("productID"),
            "report_type": obj.get("reportType"),
            "service": obj.get("service")
        })
        return _obj


