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
from pydantic import BaseModel, Field, conlist
from openapi_client.models.azure_commercial_marketplace_setup import (
    AzureCommercialMarketplaceSetup,
)
from openapi_client.models.azure_marketplace_customer_leads import (
    AzureMarketplaceCustomerLeads,
)
from openapi_client.models.azure_marketplace_listing import AzureMarketplaceListing
from openapi_client.models.azure_marketplace_listing_asset import (
    AzureMarketplaceListingAsset,
)
from openapi_client.models.azure_marketplace_plan_resource import (
    AzureMarketplacePlanResource,
)
from openapi_client.models.azure_marketplace_price_and_availability_custom_meter import (
    AzureMarketplacePriceAndAvailabilityCustomMeter,
)
from openapi_client.models.azure_marketplace_price_and_availability_offer import (
    AzureMarketplacePriceAndAvailabilityOffer,
)
from openapi_client.models.azure_marketplace_product import AzureMarketplaceProduct
from openapi_client.models.azure_marketplace_property import AzureMarketplaceProperty
from openapi_client.models.azure_marketplace_reseller import AzureMarketplaceReseller
from openapi_client.models.azure_marketplace_saas_technical_configuration import (
    AzureMarketplaceSaasTechnicalConfiguration,
)


class AzureMarketplaceProductResource(BaseModel):
    """
    AzureMarketplaceProductResource
    """

    customer_leads: Optional[AzureMarketplaceCustomerLeads] = Field(
        None, alias="customerLeads"
    )
    listing: Optional[AzureMarketplaceListing] = None
    listing_assets: Optional[conlist(AzureMarketplaceListingAsset)] = Field(
        None, alias="listingAssets"
    )
    plans: Optional[conlist(AzureMarketplacePlanResource)] = None
    price_and_availability_custom_meter: Optional[
        AzureMarketplacePriceAndAvailabilityCustomMeter
    ] = Field(None, alias="priceAndAvailabilityCustomMeter")
    price_and_availability_offer: Optional[
        AzureMarketplacePriceAndAvailabilityOffer
    ] = Field(None, alias="priceAndAvailabilityOffer")
    product: Optional[AzureMarketplaceProduct] = None
    var_property: Optional[AzureMarketplaceProperty] = Field(None, alias="property")
    reseller: Optional[AzureMarketplaceReseller] = None
    setup: Optional[AzureCommercialMarketplaceSetup] = None
    technical_configuration: Optional[
        AzureMarketplaceSaasTechnicalConfiguration
    ] = Field(None, alias="technicalConfiguration")
    __properties = [
        "customerLeads",
        "listing",
        "listingAssets",
        "plans",
        "priceAndAvailabilityCustomMeter",
        "priceAndAvailabilityOffer",
        "product",
        "property",
        "reseller",
        "setup",
        "technicalConfiguration",
    ]

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
    def from_json(cls, json_str: str) -> AzureMarketplaceProductResource:
        """Create an instance of AzureMarketplaceProductResource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of customer_leads
        if self.customer_leads:
            _dict["customerLeads"] = self.customer_leads.to_dict()
        # override the default output from pydantic by calling `to_dict()` of listing
        if self.listing:
            _dict["listing"] = self.listing.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in listing_assets (list)
        _items = []
        if self.listing_assets:
            for _item in self.listing_assets:
                if _item:
                    _items.append(_item.to_dict())
            _dict["listingAssets"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in plans (list)
        _items = []
        if self.plans:
            for _item in self.plans:
                if _item:
                    _items.append(_item.to_dict())
            _dict["plans"] = _items
        # override the default output from pydantic by calling `to_dict()` of price_and_availability_custom_meter
        if self.price_and_availability_custom_meter:
            _dict[
                "priceAndAvailabilityCustomMeter"
            ] = self.price_and_availability_custom_meter.to_dict()
        # override the default output from pydantic by calling `to_dict()` of price_and_availability_offer
        if self.price_and_availability_offer:
            _dict[
                "priceAndAvailabilityOffer"
            ] = self.price_and_availability_offer.to_dict()
        # override the default output from pydantic by calling `to_dict()` of product
        if self.product:
            _dict["product"] = self.product.to_dict()
        # override the default output from pydantic by calling `to_dict()` of var_property
        if self.var_property:
            _dict["property"] = self.var_property.to_dict()
        # override the default output from pydantic by calling `to_dict()` of reseller
        if self.reseller:
            _dict["reseller"] = self.reseller.to_dict()
        # override the default output from pydantic by calling `to_dict()` of setup
        if self.setup:
            _dict["setup"] = self.setup.to_dict()
        # override the default output from pydantic by calling `to_dict()` of technical_configuration
        if self.technical_configuration:
            _dict["technicalConfiguration"] = self.technical_configuration.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AzureMarketplaceProductResource:
        """Create an instance of AzureMarketplaceProductResource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AzureMarketplaceProductResource.parse_obj(obj)

        _obj = AzureMarketplaceProductResource.parse_obj(
            {
                "customer_leads": AzureMarketplaceCustomerLeads.from_dict(
                    obj.get("customerLeads")
                )
                if obj.get("customerLeads") is not None
                else None,
                "listing": AzureMarketplaceListing.from_dict(obj.get("listing"))
                if obj.get("listing") is not None
                else None,
                "listing_assets": [
                    AzureMarketplaceListingAsset.from_dict(_item)
                    for _item in obj.get("listingAssets")
                ]
                if obj.get("listingAssets") is not None
                else None,
                "plans": [
                    AzureMarketplacePlanResource.from_dict(_item)
                    for _item in obj.get("plans")
                ]
                if obj.get("plans") is not None
                else None,
                "price_and_availability_custom_meter": AzureMarketplacePriceAndAvailabilityCustomMeter.from_dict(
                    obj.get("priceAndAvailabilityCustomMeter")
                )
                if obj.get("priceAndAvailabilityCustomMeter") is not None
                else None,
                "price_and_availability_offer": AzureMarketplacePriceAndAvailabilityOffer.from_dict(
                    obj.get("priceAndAvailabilityOffer")
                )
                if obj.get("priceAndAvailabilityOffer") is not None
                else None,
                "product": AzureMarketplaceProduct.from_dict(obj.get("product"))
                if obj.get("product") is not None
                else None,
                "var_property": AzureMarketplaceProperty.from_dict(obj.get("property"))
                if obj.get("property") is not None
                else None,
                "reseller": AzureMarketplaceReseller.from_dict(obj.get("reseller"))
                if obj.get("reseller") is not None
                else None,
                "setup": AzureCommercialMarketplaceSetup.from_dict(obj.get("setup"))
                if obj.get("setup") is not None
                else None,
                "technical_configuration": AzureMarketplaceSaasTechnicalConfiguration.from_dict(
                    obj.get("technicalConfiguration")
                )
                if obj.get("technicalConfiguration") is not None
                else None,
            }
        )
        return _obj
