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



from pydantic import BaseModel, Field, StrictStr
from openapi_client.models.integration_info import IntegrationInfo
from openapi_client.models.partner import Partner
from openapi_client.models.partner_service import PartnerService

class UpdateIntegrationParams(BaseModel):
    """
    UpdateIntegrationParams
    """
    info: IntegrationInfo = Field(...)
    organization_id: StrictStr = Field(..., alias="organizationID")
    partner: Partner = Field(...)
    service: PartnerService = Field(...)
    __properties = ["info", "organizationID", "partner", "service"]

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
    def from_json(cls, json_str: str) -> UpdateIntegrationParams:
        """Create an instance of UpdateIntegrationParams from a JSON string"""
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
    def from_dict(cls, obj: dict) -> UpdateIntegrationParams:
        """Create an instance of UpdateIntegrationParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UpdateIntegrationParams.parse_obj(obj)

        _obj = UpdateIntegrationParams.parse_obj({
            "info": IntegrationInfo.from_dict(obj.get("info")) if obj.get("info") is not None else None,
            "organization_id": obj.get("organizationID"),
            "partner": obj.get("partner"),
            "service": obj.get("service")
        })
        return _obj


