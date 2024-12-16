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
from suger_sdk_python.models.gcp_marketplace_product_external_account_spec import GcpMarketplaceProductExternalAccountSpec
from suger_sdk_python.models.gcp_marketplace_product_marketing_spec import GcpMarketplaceProductMarketingSpec
from suger_sdk_python.models.gcp_marketplace_product_purchase_spec import GcpMarketplaceProductPurchaseSpec
from suger_sdk_python.models.gcp_marketplace_product_terms_spec import GcpMarketplaceProductTermsSpec
from typing import Optional, Set
from typing_extensions import Self

class GcpMarketplaceProductListingSpec(BaseModel):
    """
    GcpMarketplaceProductListingSpec
    """ # noqa: E501
    external_account_spec: Optional[GcpMarketplaceProductExternalAccountSpec] = Field(default=None, alias="externalAccountSpec")
    listing_type: Optional[StrictStr] = Field(default=None, alias="listingType")
    marketing_spec: Optional[GcpMarketplaceProductMarketingSpec] = Field(default=None, alias="marketingSpec")
    purchase_spec: Optional[GcpMarketplaceProductPurchaseSpec] = Field(default=None, alias="purchaseSpec")
    terms_spec: Optional[GcpMarketplaceProductTermsSpec] = Field(default=None, alias="termsSpec")
    __properties: ClassVar[List[str]] = ["externalAccountSpec", "listingType", "marketingSpec", "purchaseSpec", "termsSpec"]

    @field_validator('listing_type')
    def listing_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['BillingIntegratedManagedService']):
            raise ValueError("must be one of enum values ('BillingIntegratedManagedService')")
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
        """Create an instance of GcpMarketplaceProductListingSpec from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of external_account_spec
        if self.external_account_spec:
            _dict['externalAccountSpec'] = self.external_account_spec.to_dict()
        # override the default output from pydantic by calling `to_dict()` of marketing_spec
        if self.marketing_spec:
            _dict['marketingSpec'] = self.marketing_spec.to_dict()
        # override the default output from pydantic by calling `to_dict()` of purchase_spec
        if self.purchase_spec:
            _dict['purchaseSpec'] = self.purchase_spec.to_dict()
        # override the default output from pydantic by calling `to_dict()` of terms_spec
        if self.terms_spec:
            _dict['termsSpec'] = self.terms_spec.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GcpMarketplaceProductListingSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "externalAccountSpec": GcpMarketplaceProductExternalAccountSpec.from_dict(obj["externalAccountSpec"]) if obj.get("externalAccountSpec") is not None else None,
            "listingType": obj.get("listingType"),
            "marketingSpec": GcpMarketplaceProductMarketingSpec.from_dict(obj["marketingSpec"]) if obj.get("marketingSpec") is not None else None,
            "purchaseSpec": GcpMarketplaceProductPurchaseSpec.from_dict(obj["purchaseSpec"]) if obj.get("purchaseSpec") is not None else None,
            "termsSpec": GcpMarketplaceProductTermsSpec.from_dict(obj["termsSpec"]) if obj.get("termsSpec") is not None else None
        })
        return _obj

