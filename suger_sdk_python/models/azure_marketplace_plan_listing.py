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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from suger_sdk_python.models.azure_marketplace_resource_lifecycle_state import AzureMarketplaceResourceLifecycleState
from suger_sdk_python.models.azure_marketplace_validation import AzureMarketplaceValidation
from typing import Optional, Set
from typing_extensions import Self

class AzureMarketplacePlanListing(BaseModel):
    """
    AzureMarketplacePlanListing
    """ # noqa: E501
    var_schema: Optional[StrictStr] = Field(default=None, alias="$schema")
    description: Optional[StrictStr] = None
    id: Optional[StrictStr] = None
    kind: Optional[StrictStr] = None
    language_id: Optional[StrictStr] = Field(default=None, alias="languageId")
    lifecycle_state: Optional[AzureMarketplaceResourceLifecycleState] = Field(default=None, alias="lifecycleState")
    name: Optional[StrictStr] = None
    plan: Optional[StrictStr] = None
    product: Optional[StrictStr] = None
    resource_name: Optional[StrictStr] = Field(default=None, alias="resourceName")
    summary: Optional[StrictStr] = None
    validations: Optional[List[AzureMarketplaceValidation]] = None
    __properties: ClassVar[List[str]] = ["$schema", "description", "id", "kind", "languageId", "lifecycleState", "name", "plan", "product", "resourceName", "summary", "validations"]

    @field_validator('kind')
    def kind_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['azureVM-plan', 'azureSaaS-plan', 'azureCoreVM-plan', 'azureContainer-plan']):
            raise ValueError("must be one of enum values ('azureVM-plan', 'azureSaaS-plan', 'azureCoreVM-plan', 'azureContainer-plan')")
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
        """Create an instance of AzureMarketplacePlanListing from a JSON string"""
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
        """Create an instance of AzureMarketplacePlanListing from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "$schema": obj.get("$schema"),
            "description": obj.get("description"),
            "id": obj.get("id"),
            "kind": obj.get("kind"),
            "languageId": obj.get("languageId"),
            "lifecycleState": obj.get("lifecycleState"),
            "name": obj.get("name"),
            "plan": obj.get("plan"),
            "product": obj.get("product"),
            "resourceName": obj.get("resourceName"),
            "summary": obj.get("summary"),
            "validations": [AzureMarketplaceValidation.from_dict(_item) for _item in obj["validations"]] if obj.get("validations") is not None else None
        })
        return _obj


