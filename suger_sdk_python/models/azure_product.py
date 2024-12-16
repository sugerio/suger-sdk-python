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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from suger_sdk_python.models.azure_marketplace_price_and_availability_private_offer_plan import AzureMarketplacePriceAndAvailabilityPrivateOfferPlan
from suger_sdk_python.models.azure_product_availability import AzureProductAvailability
from suger_sdk_python.models.azure_product_branch import AzureProductBranch
from suger_sdk_python.models.azure_product_listing import AzureProductListing
from suger_sdk_python.models.azure_product_package_configuration import AzureProductPackageConfiguration
from suger_sdk_python.models.azure_product_property import AzureProductProperty
from suger_sdk_python.models.azure_product_setup import AzureProductSetup
from suger_sdk_python.models.azure_product_submission import AzureProductSubmission
from suger_sdk_python.models.azure_product_variant import AzureProductVariant
from suger_sdk_python.models.azure_type_value import AzureTypeValue
from typing import Optional, Set
from typing_extensions import Self

class AzureProduct(BaseModel):
    """
    AzureProduct
    """ # noqa: E501
    availabilities: Optional[List[AzureProductAvailability]] = None
    branches: Optional[List[AzureProductBranch]] = None
    external_ids: Optional[List[AzureTypeValue]] = Field(default=None, alias="externalIDs")
    id: Optional[StrictStr] = None
    is_modular_publishing: Optional[StrictBool] = Field(default=None, alias="isModularPublishing")
    listings: Optional[List[AzureProductListing]] = None
    name: Optional[StrictStr] = None
    package_configurations: Optional[List[AzureProductPackageConfiguration]] = Field(default=None, alias="packageConfigurations")
    plans: Optional[List[AzureMarketplacePriceAndAvailabilityPrivateOfferPlan]] = Field(default=None, description="All plans under this product")
    properties: Optional[List[AzureProductProperty]] = None
    resource_type: Optional[StrictStr] = Field(default=None, alias="resourceType")
    setup: Optional[AzureProductSetup] = Field(default=None, description="Not original fields. They are populated by other API calls")
    submissions: Optional[List[AzureProductSubmission]] = None
    variants: Optional[List[AzureProductVariant]] = None
    __properties: ClassVar[List[str]] = ["availabilities", "branches", "externalIDs", "id", "isModularPublishing", "listings", "name", "packageConfigurations", "plans", "properties", "resourceType", "setup", "submissions", "variants"]

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
        """Create an instance of AzureProduct from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in availabilities (list)
        _items = []
        if self.availabilities:
            for _item_availabilities in self.availabilities:
                if _item_availabilities:
                    _items.append(_item_availabilities.to_dict())
            _dict['availabilities'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in branches (list)
        _items = []
        if self.branches:
            for _item_branches in self.branches:
                if _item_branches:
                    _items.append(_item_branches.to_dict())
            _dict['branches'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in external_ids (list)
        _items = []
        if self.external_ids:
            for _item_external_ids in self.external_ids:
                if _item_external_ids:
                    _items.append(_item_external_ids.to_dict())
            _dict['externalIDs'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in listings (list)
        _items = []
        if self.listings:
            for _item_listings in self.listings:
                if _item_listings:
                    _items.append(_item_listings.to_dict())
            _dict['listings'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in package_configurations (list)
        _items = []
        if self.package_configurations:
            for _item_package_configurations in self.package_configurations:
                if _item_package_configurations:
                    _items.append(_item_package_configurations.to_dict())
            _dict['packageConfigurations'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in plans (list)
        _items = []
        if self.plans:
            for _item_plans in self.plans:
                if _item_plans:
                    _items.append(_item_plans.to_dict())
            _dict['plans'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in properties (list)
        _items = []
        if self.properties:
            for _item_properties in self.properties:
                if _item_properties:
                    _items.append(_item_properties.to_dict())
            _dict['properties'] = _items
        # override the default output from pydantic by calling `to_dict()` of setup
        if self.setup:
            _dict['setup'] = self.setup.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in submissions (list)
        _items = []
        if self.submissions:
            for _item_submissions in self.submissions:
                if _item_submissions:
                    _items.append(_item_submissions.to_dict())
            _dict['submissions'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in variants (list)
        _items = []
        if self.variants:
            for _item_variants in self.variants:
                if _item_variants:
                    _items.append(_item_variants.to_dict())
            _dict['variants'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AzureProduct from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "availabilities": [AzureProductAvailability.from_dict(_item) for _item in obj["availabilities"]] if obj.get("availabilities") is not None else None,
            "branches": [AzureProductBranch.from_dict(_item) for _item in obj["branches"]] if obj.get("branches") is not None else None,
            "externalIDs": [AzureTypeValue.from_dict(_item) for _item in obj["externalIDs"]] if obj.get("externalIDs") is not None else None,
            "id": obj.get("id"),
            "isModularPublishing": obj.get("isModularPublishing"),
            "listings": [AzureProductListing.from_dict(_item) for _item in obj["listings"]] if obj.get("listings") is not None else None,
            "name": obj.get("name"),
            "packageConfigurations": [AzureProductPackageConfiguration.from_dict(_item) for _item in obj["packageConfigurations"]] if obj.get("packageConfigurations") is not None else None,
            "plans": [AzureMarketplacePriceAndAvailabilityPrivateOfferPlan.from_dict(_item) for _item in obj["plans"]] if obj.get("plans") is not None else None,
            "properties": [AzureProductProperty.from_dict(_item) for _item in obj["properties"]] if obj.get("properties") is not None else None,
            "resourceType": obj.get("resourceType"),
            "setup": AzureProductSetup.from_dict(obj["setup"]) if obj.get("setup") is not None else None,
            "submissions": [AzureProductSubmission.from_dict(_item) for _item in obj["submissions"]] if obj.get("submissions") is not None else None,
            "variants": [AzureProductVariant.from_dict(_item) for _item in obj["variants"]] if obj.get("variants") is not None else None
        })
        return _obj

