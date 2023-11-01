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
from openapi_client.models.salesforce_crm_credential import SalesforceCrmCredential
from openapi_client.models.salesforce_sync_filter import SalesforceSyncFilter

class SalesforceCrmIntegration(BaseModel):
    """
    SalesforceCrmIntegration
    """
    credential: Optional[SalesforceCrmCredential] = None
    filters: Optional[conlist(SalesforceSyncFilter)] = None
    instance_url: Optional[StrictStr] = Field(None, alias="instanceUrl")
    is_sandbox: Optional[StrictBool] = Field(None, alias="isSandbox")
    paused: Optional[StrictBool] = None
    secret_key: Optional[StrictStr] = Field(None, alias="secretKey")
    subdomain: Optional[StrictStr] = Field(None, description="User defined when setting up the integration")
    suger_app_installed: Optional[StrictBool] = Field(None, alias="sugerAppInstalled")
    __properties = ["credential", "filters", "instanceUrl", "isSandbox", "paused", "secretKey", "subdomain", "sugerAppInstalled"]

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
    def from_json(cls, json_str: str) -> SalesforceCrmIntegration:
        """Create an instance of SalesforceCrmIntegration from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of credential
        if self.credential:
            _dict['credential'] = self.credential.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in filters (list)
        _items = []
        if self.filters:
            for _item in self.filters:
                if _item:
                    _items.append(_item.to_dict())
            _dict['filters'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SalesforceCrmIntegration:
        """Create an instance of SalesforceCrmIntegration from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SalesforceCrmIntegration.parse_obj(obj)

        _obj = SalesforceCrmIntegration.parse_obj({
            "credential": SalesforceCrmCredential.from_dict(obj.get("credential")) if obj.get("credential") is not None else None,
            "filters": [SalesforceSyncFilter.from_dict(_item) for _item in obj.get("filters")] if obj.get("filters") is not None else None,
            "instance_url": obj.get("instanceUrl"),
            "is_sandbox": obj.get("isSandbox"),
            "paused": obj.get("paused"),
            "secret_key": obj.get("secretKey"),
            "subdomain": obj.get("subdomain"),
            "suger_app_installed": obj.get("sugerAppInstalled")
        })
        return _obj


