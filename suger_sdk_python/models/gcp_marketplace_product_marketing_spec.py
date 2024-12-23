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
from suger_sdk_python.models.gcp_marketplace_product_documentation_spec import GcpMarketplaceProductDocumentationSpec
from suger_sdk_python.models.gcp_marketplace_product_license_spec import GcpMarketplaceProductLicenseSpec
from suger_sdk_python.models.gcp_marketplace_product_support_spec import GcpMarketplaceProductSupportSpec
from typing import Optional, Set
from typing_extensions import Self

class GcpMarketplaceProductMarketingSpec(BaseModel):
    """
    GcpMarketplaceProductMarketingSpec
    """ # noqa: E501
    description: Optional[StrictStr] = None
    display_names: Optional[List[StrictStr]] = Field(default=None, alias="displayNames")
    documentation_specs: Optional[List[GcpMarketplaceProductDocumentationSpec]] = Field(default=None, alias="documentationSpecs")
    eula_url: Optional[StrictStr] = Field(default=None, alias="eulaUrl")
    external_license_specs: Optional[List[GcpMarketplaceProductLicenseSpec]] = Field(default=None, alias="externalLicenseSpecs")
    external_marketing_url: Optional[StrictStr] = Field(default=None, alias="externalMarketingUrl")
    icon: Optional[StrictStr] = Field(default=None, description="in format of \"base64://...\"")
    search_categories: Optional[List[StrictStr]] = Field(default=None, alias="searchCategories")
    search_description: Optional[StrictStr] = Field(default=None, alias="searchDescription")
    search_keywords: Optional[List[StrictStr]] = Field(default=None, alias="searchKeywords")
    signup_uri: Optional[StrictStr] = Field(default=None, alias="signupUri")
    support_spec: Optional[GcpMarketplaceProductSupportSpec] = Field(default=None, alias="supportSpec")
    tag_line: Optional[StrictStr] = Field(default=None, alias="tagLine")
    title: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["description", "displayNames", "documentationSpecs", "eulaUrl", "externalLicenseSpecs", "externalMarketingUrl", "icon", "searchCategories", "searchDescription", "searchKeywords", "signupUri", "supportSpec", "tagLine", "title"]

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
        """Create an instance of GcpMarketplaceProductMarketingSpec from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in documentation_specs (list)
        _items = []
        if self.documentation_specs:
            for _item_documentation_specs in self.documentation_specs:
                if _item_documentation_specs:
                    _items.append(_item_documentation_specs.to_dict())
            _dict['documentationSpecs'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in external_license_specs (list)
        _items = []
        if self.external_license_specs:
            for _item_external_license_specs in self.external_license_specs:
                if _item_external_license_specs:
                    _items.append(_item_external_license_specs.to_dict())
            _dict['externalLicenseSpecs'] = _items
        # override the default output from pydantic by calling `to_dict()` of support_spec
        if self.support_spec:
            _dict['supportSpec'] = self.support_spec.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GcpMarketplaceProductMarketingSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "description": obj.get("description"),
            "displayNames": obj.get("displayNames"),
            "documentationSpecs": [GcpMarketplaceProductDocumentationSpec.from_dict(_item) for _item in obj["documentationSpecs"]] if obj.get("documentationSpecs") is not None else None,
            "eulaUrl": obj.get("eulaUrl"),
            "externalLicenseSpecs": [GcpMarketplaceProductLicenseSpec.from_dict(_item) for _item in obj["externalLicenseSpecs"]] if obj.get("externalLicenseSpecs") is not None else None,
            "externalMarketingUrl": obj.get("externalMarketingUrl"),
            "icon": obj.get("icon"),
            "searchCategories": obj.get("searchCategories"),
            "searchDescription": obj.get("searchDescription"),
            "searchKeywords": obj.get("searchKeywords"),
            "signupUri": obj.get("signupUri"),
            "supportSpec": GcpMarketplaceProductSupportSpec.from_dict(obj["supportSpec"]) if obj.get("supportSpec") is not None else None,
            "tagLine": obj.get("tagLine"),
            "title": obj.get("title")
        })
        return _obj


