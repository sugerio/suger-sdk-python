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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from suger_sdk_python.models.azure_marketplace_validation import AzureMarketplaceValidation
from typing import Optional, Set
from typing_extensions import Self

class AzureMarketplaceSaasTechnicalConfiguration(BaseModel):
    """
    AzureMarketplaceSaasTechnicalConfiguration
    """ # noqa: E501
    var_schema: Optional[StrictStr] = Field(default=None, alias="$schema")
    azure_ad_app_id: Optional[StrictStr] = Field(default=None, description="Azure AD Application Id", alias="azureAdAppId")
    azure_ad_tenant_id: Optional[StrictStr] = Field(default=None, description="Azure AD Tenant Id", alias="azureAdTenantId")
    connection_webhook: Optional[StrictStr] = Field(default=None, alias="connectionWebhook")
    id: Optional[StrictStr] = None
    landing_page_url: Optional[StrictStr] = Field(default=None, alias="landingPageUrl")
    product: Optional[StrictStr] = Field(default=None, description="in format of \"product/product-durable-id\"")
    resource_name: Optional[StrictStr] = Field(default=None, alias="resourceName")
    validations: Optional[List[AzureMarketplaceValidation]] = None
    __properties: ClassVar[List[str]] = ["$schema", "azureAdAppId", "azureAdTenantId", "connectionWebhook", "id", "landingPageUrl", "product", "resourceName", "validations"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of AzureMarketplaceSaasTechnicalConfiguration from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in validations (list)
        _items = []
        if self.validations:
            for _item_validations in self.validations:
                if _item_validations:
                    _items.append(_item_validations.to_dict())
            _dict['validations'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AzureMarketplaceSaasTechnicalConfiguration from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "$schema": obj.get("$schema"),
            "azureAdAppId": obj.get("azureAdAppId"),
            "azureAdTenantId": obj.get("azureAdTenantId"),
            "connectionWebhook": obj.get("connectionWebhook"),
            "id": obj.get("id"),
            "landingPageUrl": obj.get("landingPageUrl"),
            "product": obj.get("product"),
            "resourceName": obj.get("resourceName"),
            "validations": [AzureMarketplaceValidation.from_dict(_item) for _item in obj["validations"]] if obj.get("validations") is not None else None
        })
        return _obj


