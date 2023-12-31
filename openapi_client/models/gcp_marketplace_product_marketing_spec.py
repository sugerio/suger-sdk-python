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
from pydantic import BaseModel, Field, StrictStr, conlist
from openapi_client.models.gcp_marketplace_product_documentation_spec import GcpMarketplaceProductDocumentationSpec
from openapi_client.models.gcp_marketplace_product_license_spec import GcpMarketplaceProductLicenseSpec
from openapi_client.models.gcp_marketplace_product_support_spec import GcpMarketplaceProductSupportSpec

class GcpMarketplaceProductMarketingSpec(BaseModel):
    """
    GcpMarketplaceProductMarketingSpec
    """
    description: Optional[StrictStr] = None
    display_names: Optional[conlist(StrictStr)] = Field(None, alias="displayNames")
    documentation_specs: Optional[conlist(GcpMarketplaceProductDocumentationSpec)] = Field(None, alias="documentationSpecs")
    eula_url: Optional[StrictStr] = Field(None, alias="eulaUrl")
    external_license_specs: Optional[conlist(GcpMarketplaceProductLicenseSpec)] = Field(None, alias="externalLicenseSpecs")
    external_marketing_url: Optional[StrictStr] = Field(None, alias="externalMarketingUrl")
    icon: Optional[StrictStr] = Field(None, description="in format of \"base64://...\"")
    search_categories: Optional[conlist(StrictStr)] = Field(None, alias="searchCategories")
    search_description: Optional[StrictStr] = Field(None, alias="searchDescription")
    search_keywords: Optional[conlist(StrictStr)] = Field(None, alias="searchKeywords")
    signup_uri: Optional[StrictStr] = Field(None, alias="signupUri")
    support_spec: Optional[GcpMarketplaceProductSupportSpec] = Field(None, alias="supportSpec")
    tag_line: Optional[StrictStr] = Field(None, alias="tagLine")
    title: Optional[StrictStr] = None
    __properties = ["description", "displayNames", "documentationSpecs", "eulaUrl", "externalLicenseSpecs", "externalMarketingUrl", "icon", "searchCategories", "searchDescription", "searchKeywords", "signupUri", "supportSpec", "tagLine", "title"]

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
    def from_json(cls, json_str: str) -> GcpMarketplaceProductMarketingSpec:
        """Create an instance of GcpMarketplaceProductMarketingSpec from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in documentation_specs (list)
        _items = []
        if self.documentation_specs:
            for _item in self.documentation_specs:
                if _item:
                    _items.append(_item.to_dict())
            _dict['documentationSpecs'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in external_license_specs (list)
        _items = []
        if self.external_license_specs:
            for _item in self.external_license_specs:
                if _item:
                    _items.append(_item.to_dict())
            _dict['externalLicenseSpecs'] = _items
        # override the default output from pydantic by calling `to_dict()` of support_spec
        if self.support_spec:
            _dict['supportSpec'] = self.support_spec.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GcpMarketplaceProductMarketingSpec:
        """Create an instance of GcpMarketplaceProductMarketingSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GcpMarketplaceProductMarketingSpec.parse_obj(obj)

        _obj = GcpMarketplaceProductMarketingSpec.parse_obj({
            "description": obj.get("description"),
            "display_names": obj.get("displayNames"),
            "documentation_specs": [GcpMarketplaceProductDocumentationSpec.from_dict(_item) for _item in obj.get("documentationSpecs")] if obj.get("documentationSpecs") is not None else None,
            "eula_url": obj.get("eulaUrl"),
            "external_license_specs": [GcpMarketplaceProductLicenseSpec.from_dict(_item) for _item in obj.get("externalLicenseSpecs")] if obj.get("externalLicenseSpecs") is not None else None,
            "external_marketing_url": obj.get("externalMarketingUrl"),
            "icon": obj.get("icon"),
            "search_categories": obj.get("searchCategories"),
            "search_description": obj.get("searchDescription"),
            "search_keywords": obj.get("searchKeywords"),
            "signup_uri": obj.get("signupUri"),
            "support_spec": GcpMarketplaceProductSupportSpec.from_dict(obj.get("supportSpec")) if obj.get("supportSpec") is not None else None,
            "tag_line": obj.get("tagLine"),
            "title": obj.get("title")
        })
        return _obj


