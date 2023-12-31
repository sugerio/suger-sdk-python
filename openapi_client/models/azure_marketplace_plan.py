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
from openapi_client.models.azure_marketplace_deprecation_schedule import AzureMarketplaceDeprecationSchedule
from openapi_client.models.azure_marketplace_government_certification import AzureMarketplaceGovernmentCertification
from openapi_client.models.azure_marketplace_identity import AzureMarketplaceIdentity
from openapi_client.models.azure_marketplace_resource_lifecycle_state import AzureMarketplaceResourceLifecycleState
from openapi_client.models.azure_marketplace_validation import AzureMarketplaceValidation

class AzureMarketplacePlan(BaseModel):
    """
    AzureMarketplacePlan
    """
    var_schema: Optional[StrictStr] = Field(None, alias="$schema")
    alias: Optional[StrictStr] = None
    azure_government_certifications: Optional[conlist(AzureMarketplaceGovernmentCertification)] = Field(None, alias="azureGovernmentCertifications")
    azure_regions: Optional[conlist(StrictStr)] = Field(None, alias="azureRegions", description="enums:[azureGlobal,azureGovernment,azureGermany,azureChina]")
    deprecation_schedule: Optional[AzureMarketplaceDeprecationSchedule] = Field(None, alias="deprecationSchedule")
    display_rank: Optional[StrictInt] = Field(None, alias="displayRank", description="default 2147483647")
    id: Optional[StrictStr] = Field(None, description="in format of \"plan/product-durable-id/plan-durable-id\"")
    identity: Optional[AzureMarketplaceIdentity] = None
    lifecycle_state: Optional[AzureMarketplaceResourceLifecycleState] = Field(None, alias="lifecycleState")
    product: Optional[StrictStr] = Field(None, description="in format of \"product/product-durable-id\"")
    resource_name: Optional[StrictStr] = Field(None, alias="resourceName")
    subtype: Optional[StrictStr] = Field(None, description="Specifies the plan type (AzureApplication-type products only) see: https://go.microsoft.com/fwlink/?linkid=2106322")
    validations: Optional[conlist(AzureMarketplaceValidation)] = None
    __properties = ["$schema", "alias", "azureGovernmentCertifications", "azureRegions", "deprecationSchedule", "displayRank", "id", "identity", "lifecycleState", "product", "resourceName", "subtype", "validations"]

    @validator('subtype')
    def subtype_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('managedApplication', 'solutionTemplate'):
            raise ValueError("must be one of enum values ('managedApplication', 'solutionTemplate')")
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
    def from_json(cls, json_str: str) -> AzureMarketplacePlan:
        """Create an instance of AzureMarketplacePlan from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in azure_government_certifications (list)
        _items = []
        if self.azure_government_certifications:
            for _item in self.azure_government_certifications:
                if _item:
                    _items.append(_item.to_dict())
            _dict['azureGovernmentCertifications'] = _items
        # override the default output from pydantic by calling `to_dict()` of deprecation_schedule
        if self.deprecation_schedule:
            _dict['deprecationSchedule'] = self.deprecation_schedule.to_dict()
        # override the default output from pydantic by calling `to_dict()` of identity
        if self.identity:
            _dict['identity'] = self.identity.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in validations (list)
        _items = []
        if self.validations:
            for _item in self.validations:
                if _item:
                    _items.append(_item.to_dict())
            _dict['validations'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AzureMarketplacePlan:
        """Create an instance of AzureMarketplacePlan from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AzureMarketplacePlan.parse_obj(obj)

        _obj = AzureMarketplacePlan.parse_obj({
            "var_schema": obj.get("$schema"),
            "alias": obj.get("alias"),
            "azure_government_certifications": [AzureMarketplaceGovernmentCertification.from_dict(_item) for _item in obj.get("azureGovernmentCertifications")] if obj.get("azureGovernmentCertifications") is not None else None,
            "azure_regions": obj.get("azureRegions"),
            "deprecation_schedule": AzureMarketplaceDeprecationSchedule.from_dict(obj.get("deprecationSchedule")) if obj.get("deprecationSchedule") is not None else None,
            "display_rank": obj.get("displayRank"),
            "id": obj.get("id"),
            "identity": AzureMarketplaceIdentity.from_dict(obj.get("identity")) if obj.get("identity") is not None else None,
            "lifecycle_state": obj.get("lifecycleState"),
            "product": obj.get("product"),
            "resource_name": obj.get("resourceName"),
            "subtype": obj.get("subtype"),
            "validations": [AzureMarketplaceValidation.from_dict(_item) for _item in obj.get("validations")] if obj.get("validations") is not None else None
        })
        return _obj


