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
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist, validator
from openapi_client.models.azure_marketplace_listing_asset_type import AzureMarketplaceListingAssetType
from openapi_client.models.azure_marketplace_resource_lifecycle_state import AzureMarketplaceResourceLifecycleState
from openapi_client.models.azure_marketplace_validation import AzureMarketplaceValidation

class AzureMarketplaceListingAsset(BaseModel):
    """
    AzureMarketplaceListingAsset
    """
    var_schema: Optional[StrictStr] = Field(None, alias="$schema")
    description: Optional[StrictStr] = None
    display_order: Optional[StrictInt] = Field(None, alias="displayOrder", description="minimum: 0")
    file_name: Optional[StrictStr] = Field(None, alias="fileName")
    friendly_name: Optional[StrictStr] = Field(None, alias="friendlyName")
    id: Optional[StrictStr] = None
    kind: Optional[StrictStr] = None
    language_id: Optional[StrictStr] = Field(None, alias="languageId", description="Max string length is 10.")
    lifecycle_state: Optional[AzureMarketplaceResourceLifecycleState] = Field(None, alias="lifecycleState")
    listing: Optional[StrictStr] = None
    product: Optional[StrictStr] = Field(None, description="Product resource name, in format of \"product/product-durable-id\"")
    resource_name: Optional[StrictStr] = Field(None, alias="resourceName")
    type: Optional[AzureMarketplaceListingAssetType] = None
    url: Optional[StrictStr] = Field(None, description="pattern: \"^https?://\"")
    validations: Optional[conlist(AzureMarketplaceValidation)] = None
    __properties = ["$schema", "description", "displayOrder", "fileName", "friendlyName", "id", "kind", "languageId", "lifecycleState", "listing", "product", "resourceName", "type", "url", "validations"]

    @validator('kind')
    def kind_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('azure'):
            raise ValueError("must be one of enum values ('azure')")
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
    def from_json(cls, json_str: str) -> AzureMarketplaceListingAsset:
        """Create an instance of AzureMarketplaceListingAsset from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in validations (list)
        _items = []
        if self.validations:
            for _item in self.validations:
                if _item:
                    _items.append(_item.to_dict())
            _dict['validations'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AzureMarketplaceListingAsset:
        """Create an instance of AzureMarketplaceListingAsset from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AzureMarketplaceListingAsset.parse_obj(obj)

        _obj = AzureMarketplaceListingAsset.parse_obj({
            "var_schema": obj.get("$schema"),
            "description": obj.get("description"),
            "display_order": obj.get("displayOrder"),
            "file_name": obj.get("fileName"),
            "friendly_name": obj.get("friendlyName"),
            "id": obj.get("id"),
            "kind": obj.get("kind"),
            "language_id": obj.get("languageId"),
            "lifecycle_state": obj.get("lifecycleState"),
            "listing": obj.get("listing"),
            "product": obj.get("product"),
            "resource_name": obj.get("resourceName"),
            "type": obj.get("type"),
            "url": obj.get("url"),
            "validations": [AzureMarketplaceValidation.from_dict(_item) for _item in obj.get("validations")] if obj.get("validations") is not None else None
        })
        return _obj


