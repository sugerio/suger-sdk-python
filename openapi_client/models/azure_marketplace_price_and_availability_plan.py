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
from pydantic import BaseModel, Field, StrictStr, conlist, validator
from openapi_client.models.azure_marketplace_price_and_availability_audience import AzureMarketplacePriceAndAvailabilityAudience
from openapi_client.models.azure_marketplace_price_and_availability_price import AzureMarketplacePriceAndAvailabilityPrice
from openapi_client.models.azure_marketplace_price_and_availability_software_reservation import AzureMarketplacePriceAndAvailabilitySoftwareReservation
from openapi_client.models.azure_marketplace_term import AzureMarketplaceTerm
from openapi_client.models.azure_marketplace_validation import AzureMarketplaceValidation

class AzureMarketplacePriceAndAvailabilityPlan(BaseModel):
    """
    AzureMarketplacePriceAndAvailabilityPlan
    """
    var_schema: Optional[StrictStr] = Field(None, alias="$schema")
    audience: Optional[StrictStr] = None
    billing_tag: Optional[StrictStr] = Field(None, alias="billingTag")
    customer_markets: Optional[StrictStr] = Field(None, alias="customerMarkets")
    id: Optional[StrictStr] = None
    markets: Optional[conlist(StrictStr)] = None
    plan: Optional[StrictStr] = None
    pricing: Optional[AzureMarketplacePriceAndAvailabilityPrice] = None
    private_audiences: Optional[conlist(AzureMarketplacePriceAndAvailabilityAudience)] = Field(None, alias="privateAudiences")
    product: Optional[StrictStr] = None
    resource_name: Optional[StrictStr] = Field(None, alias="resourceName")
    software_reservation: Optional[conlist(AzureMarketplacePriceAndAvailabilitySoftwareReservation)] = Field(None, alias="softwareReservation")
    trial: Optional[AzureMarketplaceTerm] = None
    validations: Optional[conlist(AzureMarketplaceValidation)] = None
    visibility: Optional[StrictStr] = None
    __properties = ["$schema", "audience", "billingTag", "customerMarkets", "id", "markets", "plan", "pricing", "privateAudiences", "product", "resourceName", "softwareReservation", "trial", "validations", "visibility"]

    @validator('audience')
    def audience_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('public', 'private'):
            raise ValueError("must be one of enum values ('public', 'private')")
        return value

    @validator('customer_markets')
    def customer_markets_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('customMarkets', 'allMarkets', 'allTaxRemittedMarkets'):
            raise ValueError("must be one of enum values ('customMarkets', 'allMarkets', 'allTaxRemittedMarkets')")
        return value

    @validator('visibility')
    def visibility_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('visible', 'hidden'):
            raise ValueError("must be one of enum values ('visible', 'hidden')")
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
    def from_json(cls, json_str: str) -> AzureMarketplacePriceAndAvailabilityPlan:
        """Create an instance of AzureMarketplacePriceAndAvailabilityPlan from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of pricing
        if self.pricing:
            _dict['pricing'] = self.pricing.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in private_audiences (list)
        _items = []
        if self.private_audiences:
            for _item in self.private_audiences:
                if _item:
                    _items.append(_item.to_dict())
            _dict['privateAudiences'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in software_reservation (list)
        _items = []
        if self.software_reservation:
            for _item in self.software_reservation:
                if _item:
                    _items.append(_item.to_dict())
            _dict['softwareReservation'] = _items
        # override the default output from pydantic by calling `to_dict()` of trial
        if self.trial:
            _dict['trial'] = self.trial.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in validations (list)
        _items = []
        if self.validations:
            for _item in self.validations:
                if _item:
                    _items.append(_item.to_dict())
            _dict['validations'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AzureMarketplacePriceAndAvailabilityPlan:
        """Create an instance of AzureMarketplacePriceAndAvailabilityPlan from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AzureMarketplacePriceAndAvailabilityPlan.parse_obj(obj)

        _obj = AzureMarketplacePriceAndAvailabilityPlan.parse_obj({
            "var_schema": obj.get("$schema"),
            "audience": obj.get("audience"),
            "billing_tag": obj.get("billingTag"),
            "customer_markets": obj.get("customerMarkets"),
            "id": obj.get("id"),
            "markets": obj.get("markets"),
            "plan": obj.get("plan"),
            "pricing": AzureMarketplacePriceAndAvailabilityPrice.from_dict(obj.get("pricing")) if obj.get("pricing") is not None else None,
            "private_audiences": [AzureMarketplacePriceAndAvailabilityAudience.from_dict(_item) for _item in obj.get("privateAudiences")] if obj.get("privateAudiences") is not None else None,
            "product": obj.get("product"),
            "resource_name": obj.get("resourceName"),
            "software_reservation": [AzureMarketplacePriceAndAvailabilitySoftwareReservation.from_dict(_item) for _item in obj.get("softwareReservation")] if obj.get("softwareReservation") is not None else None,
            "trial": AzureMarketplaceTerm.from_dict(obj.get("trial")) if obj.get("trial") is not None else None,
            "validations": [AzureMarketplaceValidation.from_dict(_item) for _item in obj.get("validations")] if obj.get("validations") is not None else None,
            "visibility": obj.get("visibility")
        })
        return _obj


