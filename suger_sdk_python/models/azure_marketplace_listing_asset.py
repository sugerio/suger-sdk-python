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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from suger_sdk_python.models.azure_marketplace_listing_asset_type import AzureMarketplaceListingAssetType
from suger_sdk_python.models.azure_marketplace_resource_lifecycle_state import AzureMarketplaceResourceLifecycleState
from suger_sdk_python.models.azure_marketplace_validation import AzureMarketplaceValidation
from typing import Optional, Set
from typing_extensions import Self

class AzureMarketplaceListingAsset(BaseModel):
    """
    AzureMarketplaceListingAsset
    """ # noqa: E501
    var_schema: Optional[StrictStr] = Field(default=None, alias="$schema")
    description: Optional[StrictStr] = None
    display_order: Optional[StrictInt] = Field(default=None, description="minimum: 0", alias="displayOrder")
    file_name: Optional[StrictStr] = Field(default=None, alias="fileName")
    friendly_name: Optional[StrictStr] = Field(default=None, alias="friendlyName")
    id: Optional[StrictStr] = None
    kind: Optional[StrictStr] = None
    language_id: Optional[StrictStr] = Field(default=None, description="Max string length is 10.", alias="languageId")
    lifecycle_state: Optional[AzureMarketplaceResourceLifecycleState] = Field(default=None, description="Default value is \"generallyAvailable\".", alias="lifecycleState")
    listing: Optional[StrictStr] = None
    product: Optional[StrictStr] = Field(default=None, description="Product resource name, in format of \"product/product-durable-id\"")
    resource_name: Optional[StrictStr] = Field(default=None, alias="resourceName")
    type: Optional[AzureMarketplaceListingAssetType] = None
    url: Optional[StrictStr] = Field(default=None, description="pattern: \"^https?://\"")
    validations: Optional[List[AzureMarketplaceValidation]] = None
    __properties: ClassVar[List[str]] = ["$schema", "description", "displayOrder", "fileName", "friendlyName", "id", "kind", "languageId", "lifecycleState", "listing", "product", "resourceName", "type", "url", "validations"]

    @field_validator('kind')
    def kind_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['azure']):
            raise ValueError("must be one of enum values ('azure')")
        return value

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
        """Create an instance of AzureMarketplaceListingAsset from a JSON string"""
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
        """Create an instance of AzureMarketplaceListingAsset from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "$schema": obj.get("$schema"),
            "description": obj.get("description"),
            "displayOrder": obj.get("displayOrder"),
            "fileName": obj.get("fileName"),
            "friendlyName": obj.get("friendlyName"),
            "id": obj.get("id"),
            "kind": obj.get("kind"),
            "languageId": obj.get("languageId"),
            "lifecycleState": obj.get("lifecycleState"),
            "listing": obj.get("listing"),
            "product": obj.get("product"),
            "resourceName": obj.get("resourceName"),
            "type": obj.get("type"),
            "url": obj.get("url"),
            "validations": [AzureMarketplaceValidation.from_dict(_item) for _item in obj["validations"]] if obj.get("validations") is not None else None
        })
        return _obj


