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

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, StrictStr
from openapi_client.models.gcp_marketplace_external_google_link import GcpMarketplaceExternalGoogleLink
from openapi_client.models.gcp_marketplace_unstructured_document import GcpMarketplaceUnstructuredDocument

class GcpMarketplaceDocument(BaseModel):
    """
    GcpMarketplaceDocument
    """
    description: Optional[StrictStr] = None
    document_type: Optional[StrictStr] = Field(None, alias="documentType", description="such as \"PARTNER_EULA\"")
    external_google_link: Optional[GcpMarketplaceExternalGoogleLink] = Field(None, alias="externalGoogleLink")
    name: Optional[StrictStr] = Field(None, description="in format of \"projects/{projectNumber}/agreements/{agreementId}/documents/{documentId}\"")
    unstructured_document: Optional[GcpMarketplaceUnstructuredDocument] = Field(None, alias="unstructuredDocument")
    update_time: Optional[datetime] = Field(None, alias="updateTime")
    __properties = ["description", "documentType", "externalGoogleLink", "name", "unstructuredDocument", "updateTime"]

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
    def from_json(cls, json_str: str) -> GcpMarketplaceDocument:
        """Create an instance of GcpMarketplaceDocument from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of external_google_link
        if self.external_google_link:
            _dict['externalGoogleLink'] = self.external_google_link.to_dict()
        # override the default output from pydantic by calling `to_dict()` of unstructured_document
        if self.unstructured_document:
            _dict['unstructuredDocument'] = self.unstructured_document.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GcpMarketplaceDocument:
        """Create an instance of GcpMarketplaceDocument from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GcpMarketplaceDocument.parse_obj(obj)

        _obj = GcpMarketplaceDocument.parse_obj({
            "description": obj.get("description"),
            "document_type": obj.get("documentType"),
            "external_google_link": GcpMarketplaceExternalGoogleLink.from_dict(obj.get("externalGoogleLink")) if obj.get("externalGoogleLink") is not None else None,
            "name": obj.get("name"),
            "unstructured_document": GcpMarketplaceUnstructuredDocument.from_dict(obj.get("unstructuredDocument")) if obj.get("unstructuredDocument") is not None else None,
            "update_time": obj.get("updateTime")
        })
        return _obj


