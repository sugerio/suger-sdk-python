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
from suger_sdk_python.models.aws_marketplace_catalog_legal_term_document_type import AwsMarketplaceCatalogLegalTermDocumentType
from typing import Optional, Set
from typing_extensions import Self

class AwsMarketplaceCatalogLegalTermDocument(BaseModel):
    """
    AwsMarketplaceCatalogLegalTermDocument
    """ # noqa: E501
    type: Optional[AwsMarketplaceCatalogLegalTermDocumentType] = Field(default=None, alias="Type")
    url: Optional[StrictStr] = Field(default=None, description="A URL to the legal document for buyers to read. Required when Type is one of the following [CustomEula, CustomDsa].", alias="Url")
    version: Optional[StrictStr] = Field(default=None, description="Version of standard contracts provided by AWS Marketplace. Required when Type is one of the following [StandardEula, StandardDsa]. The version of StandardEula is \"2022-07-14\". The version of StandardDsa is \"2019-12-12\".", alias="Version")
    __properties: ClassVar[List[str]] = ["Type", "Url", "Version"]

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
        """Create an instance of AwsMarketplaceCatalogLegalTermDocument from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AwsMarketplaceCatalogLegalTermDocument from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "Type": obj.get("Type"),
            "Url": obj.get("Url"),
            "Version": obj.get("Version")
        })
        return _obj


