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


from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictBool
from openapi_client.models.gcp_marketplace_entitlement import GcpMarketplaceEntitlement
from openapi_client.models.gcp_marketplace_existing_private_offer import GcpMarketplaceExistingPrivateOffer
from openapi_client.models.gcp_marketplace_private_offer_price_model_type import GcpMarketplacePrivateOfferPriceModelType

class GcpMarketplaceExistingOfferData(BaseModel):
    """
    GcpMarketplaceExistingOfferData
    """
    entitlement: Optional[GcpMarketplaceEntitlement] = None
    existing_price_model_type: Optional[GcpMarketplacePrivateOfferPriceModelType] = Field(None, alias="existingPriceModelType")
    has_entitlement_changed: Optional[StrictBool] = Field(None, alias="hasEntitlementChanged")
    private_offer: Optional[GcpMarketplaceExistingPrivateOffer] = Field(None, alias="privateOffer")
    standard_offer: Optional[Dict[str, Any]] = Field(None, alias="standardOffer")
    __properties = ["entitlement", "existingPriceModelType", "hasEntitlementChanged", "privateOffer", "standardOffer"]

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
    def from_json(cls, json_str: str) -> GcpMarketplaceExistingOfferData:
        """Create an instance of GcpMarketplaceExistingOfferData from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of entitlement
        if self.entitlement:
            _dict['entitlement'] = self.entitlement.to_dict()
        # override the default output from pydantic by calling `to_dict()` of private_offer
        if self.private_offer:
            _dict['privateOffer'] = self.private_offer.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GcpMarketplaceExistingOfferData:
        """Create an instance of GcpMarketplaceExistingOfferData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GcpMarketplaceExistingOfferData.parse_obj(obj)

        _obj = GcpMarketplaceExistingOfferData.parse_obj({
            "entitlement": GcpMarketplaceEntitlement.from_dict(obj.get("entitlement")) if obj.get("entitlement") is not None else None,
            "existing_price_model_type": obj.get("existingPriceModelType"),
            "has_entitlement_changed": obj.get("hasEntitlementChanged"),
            "private_offer": GcpMarketplaceExistingPrivateOffer.from_dict(obj.get("privateOffer")) if obj.get("privateOffer") is not None else None,
            "standard_offer": obj.get("standardOffer")
        })
        return _obj


