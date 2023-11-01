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
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist, validator
from openapi_client.models.azure_marketplace_validation import (
    AzureMarketplaceValidation,
)


class AzureCommercialMarketplaceSetup(BaseModel):
    """
    AzureCommercialMarketplaceSetup
    """

    var_schema: Optional[StrictStr] = Field(None, alias="$schema")
    access_url: Optional[StrictStr] = Field(
        None, alias="accessUrl", description='in patern of "^(http|https)://"'
    )
    call_to_action: Optional[StrictStr] = Field(None, alias="callToAction")
    id: Optional[StrictStr] = Field(
        None, description='In format of "commercial-marketplace-setup/setup-durable-id"'
    )
    product: Optional[StrictStr] = Field(
        None,
        description='Product resource name, in format of "product/product-durable-id"',
    )
    require_license_for_install: Optional[StrictBool] = Field(
        None, alias="requireLicenseForInstall"
    )
    resource_name: Optional[StrictStr] = Field(None, alias="resourceName")
    sell_through_microsoft: Optional[StrictBool] = Field(
        None, alias="sellThroughMicrosoft"
    )
    use_microsoft_license_management_service: Optional[StrictBool] = Field(
        None,
        alias="useMicrosoftLicenseManagementService",
        description="If true, only per_user pricing model is allowed.",
    )
    validations: Optional[conlist(AzureMarketplaceValidation)] = None
    __properties = [
        "$schema",
        "accessUrl",
        "callToAction",
        "id",
        "product",
        "requireLicenseForInstall",
        "resourceName",
        "sellThroughMicrosoft",
        "useMicrosoftLicenseManagementService",
        "validations",
    ]

    @validator("call_to_action")
    def call_to_action_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ("free", "freeTrial", "contactMe"):
            raise ValueError(
                "must be one of enum values ('free', 'freeTrial', 'contactMe')"
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
    def from_json(cls, json_str: str) -> AzureCommercialMarketplaceSetup:
        """Create an instance of AzureCommercialMarketplaceSetup from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in validations (list)
        _items = []
        if self.validations:
            for _item in self.validations:
                if _item:
                    _items.append(_item.to_dict())
            _dict["validations"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AzureCommercialMarketplaceSetup:
        """Create an instance of AzureCommercialMarketplaceSetup from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AzureCommercialMarketplaceSetup.parse_obj(obj)

        _obj = AzureCommercialMarketplaceSetup.parse_obj(
            {
                "var_schema": obj.get("$schema"),
                "access_url": obj.get("accessUrl"),
                "call_to_action": obj.get("callToAction"),
                "id": obj.get("id"),
                "product": obj.get("product"),
                "require_license_for_install": obj.get("requireLicenseForInstall"),
                "resource_name": obj.get("resourceName"),
                "sell_through_microsoft": obj.get("sellThroughMicrosoft"),
                "use_microsoft_license_management_service": obj.get(
                    "useMicrosoftLicenseManagementService"
                ),
                "validations": [
                    AzureMarketplaceValidation.from_dict(_item)
                    for _item in obj.get("validations")
                ]
                if obj.get("validations") is not None
                else None,
            }
        )
        return _obj