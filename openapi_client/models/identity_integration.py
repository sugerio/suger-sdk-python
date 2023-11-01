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
from openapi_client.models.integration_info import IntegrationInfo


class IdentityIntegration(BaseModel):
    """
    IdentityIntegration
    """

    created_by: Optional[StrictStr] = Field(None, alias="createdBy")
    creation_time: Optional[datetime] = Field(None, alias="creationTime")
    info: Optional[IntegrationInfo] = None
    last_update_time: Optional[datetime] = Field(None, alias="lastUpdateTime")
    last_updated_by: Optional[StrictStr] = Field(None, alias="lastUpdatedBy")
    organization_id: Optional[StrictStr] = Field(None, alias="organizationID")
    partner: Optional[StrictStr] = None
    service: Optional[StrictStr] = None
    status: Optional[StrictStr] = None
    __properties = [
        "createdBy",
        "creationTime",
        "info",
        "lastUpdateTime",
        "lastUpdatedBy",
        "organizationID",
        "partner",
        "service",
        "status",
    ]

    @validator("partner")
    def partner_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ("AWS", "AZURE", "GCP", "ALIBABA"):
            raise ValueError(
                "must be one of enum values ('AWS', 'AZURE', 'GCP', 'ALIBABA')"
            )
        return value

    @validator("service")
    def service_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ("MARKETPLACE", "BILLING"):
            raise ValueError("must be one of enum values ('MARKETPLACE', 'BILLING')")
        return value

    @validator("status")
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ("CREATED", "VERIFIED", "NOT_VERIFIED"):
            raise ValueError(
                "must be one of enum values ('CREATED', 'VERIFIED', 'NOT_VERIFIED')"
            )
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
    def from_json(cls, json_str: str) -> IdentityIntegration:
        """Create an instance of IdentityIntegration from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of info
        if self.info:
            _dict["info"] = self.info.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> IdentityIntegration:
        """Create an instance of IdentityIntegration from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return IdentityIntegration.parse_obj(obj)

        _obj = IdentityIntegration.parse_obj(
            {
                "created_by": obj.get("createdBy"),
                "creation_time": obj.get("creationTime"),
                "info": IntegrationInfo.from_dict(obj.get("info"))
                if obj.get("info") is not None
                else None,
                "last_update_time": obj.get("lastUpdateTime"),
                "last_updated_by": obj.get("lastUpdatedBy"),
                "organization_id": obj.get("organizationID"),
                "partner": obj.get("partner"),
                "service": obj.get("service"),
                "status": obj.get("status"),
            }
        )
        return _obj
