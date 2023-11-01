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


from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr, conlist, validator
from openapi_client.models.aws_marketplace_cppo_discount_type import AwsMarketplaceCppoDiscountType
from openapi_client.models.aws_marketplace_cppo_duration_type import AwsMarketplaceCppoDurationType
from openapi_client.models.aws_marketplace_cppo_opportunity_eula import AwsMarketplaceCppoOpportunityEula
from openapi_client.models.aws_marketplace_cppo_payment_terms import AwsMarketplaceCppoPaymentTerms
from openapi_client.models.aws_marketplace_cppo_price_terms import AwsMarketplaceCppoPriceTerms

class AwsMarketplaceCppoOpportunity(BaseModel):
    """
    AwsMarketplaceCppoOpportunity
    """
    buyer_ids: Optional[conlist(StrictStr)] = Field(None, alias="buyerIds", description="The AWS Account ID of buyer that are specified by the ISV/Seller in this CPPO Opportunity.")
    buyer_names: Optional[conlist(StrictStr)] = Field(None, alias="buyerNames")
    contract_duration_in_days: Optional[StrictInt] = Field(None, alias="contractDurationInDays")
    created_by: Optional[StrictStr] = Field(None, alias="createdBy", description="The AWS Account ID of the ISV/Seller who create this CPPO Opportunity.")
    created_date: Optional[StrictStr] = Field(None, alias="createdDate", description="in format of \"Wed Sep 13 17:50:07 UTC 2023\"")
    custom_price_terms: Optional[AwsMarketplaceCppoPriceTerms] = Field(None, alias="customPriceTerms")
    discount: Optional[StrictStr] = Field(None, description="in format of \"10.0\" (10%)")
    discount_percent: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="discountPercent")
    discount_type: Optional[AwsMarketplaceCppoDiscountType] = Field(None, alias="discountType")
    errors: Optional[conlist(Dict[str, Any])] = None
    expiration_date: Optional[StrictStr] = Field(None, alias="expirationDate", description="in format of \"Thu Nov 30 23:59:59 UTC 2023\"")
    listing_fee_renewal: Optional[StrictBool] = Field(None, alias="listingFeeRenewal")
    manufacturer_id: Optional[StrictStr] = Field(None, alias="manufacturerId", description="The AWS Account ID of the ISV/Seller")
    manufacturer_name: Optional[StrictStr] = Field(None, alias="manufacturerName", description="The name of the ISV/Seller")
    offers_count: Optional[StrictInt] = Field(None, alias="offersCount")
    opportunity_discription: Optional[StrictStr] = Field(None, alias="opportunityDiscription")
    opportunity_duration_type: Optional[AwsMarketplaceCppoDurationType] = Field(None, alias="opportunityDurationType")
    opportunity_eula: Optional[AwsMarketplaceCppoOpportunityEula] = Field(None, alias="opportunityEula")
    opportunity_id: Optional[StrictStr] = Field(None, alias="opportunityId")
    opportunity_name: Optional[StrictStr] = Field(None, alias="opportunityName")
    opportunity_rcmp: Optional[AwsMarketplaceCppoOpportunityEula] = Field(None, alias="opportunityRcmp")
    partner_id: Optional[StrictStr] = Field(None, alias="partnerId", description="The AWS Account ID of the Channel Partner")
    partner_name: Optional[StrictStr] = Field(None, alias="partnerName", description="The name of the Channel Partner")
    payment_terms: Optional[AwsMarketplaceCppoPaymentTerms] = Field(None, alias="paymentTerms")
    product_id: Optional[StrictStr] = Field(None, alias="productId", description="The AWS Product ID from the ISV/Seller in this CPPO Opportunity.")
    product_name: Optional[StrictStr] = Field(None, alias="productName", description="The AWS Product Name from the ISV/Seller in this CPPO Opportunity.")
    product_type: Optional[StrictStr] = Field(None, alias="productType", description="The type of the AWS Product from the ISV/Seller in this CPPO Opportunity.")
    sppo: Optional[StrictBool] = None
    status: Optional[StrictStr] = Field(None, description="The status of the CPPO Opportunity.")
    usage_allowed: Optional[StrictInt] = Field(None, alias="usageAllowed", description="How many times the CPPO Opportunity can be allowed to create CPPO Private Offer by the Channel Partner.")
    __properties = ["buyerIds", "buyerNames", "contractDurationInDays", "createdBy", "createdDate", "customPriceTerms", "discount", "discountPercent", "discountType", "errors", "expirationDate", "listingFeeRenewal", "manufacturerId", "manufacturerName", "offersCount", "opportunityDiscription", "opportunityDurationType", "opportunityEula", "opportunityId", "opportunityName", "opportunityRcmp", "partnerId", "partnerName", "paymentTerms", "productId", "productName", "productType", "sppo", "status", "usageAllowed"]

    @validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('active', 'restricted', 'complete'):
            raise ValueError("must be one of enum values ('active', 'restricted', 'complete')")
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
    def from_json(cls, json_str: str) -> AwsMarketplaceCppoOpportunity:
        """Create an instance of AwsMarketplaceCppoOpportunity from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of custom_price_terms
        if self.custom_price_terms:
            _dict['customPriceTerms'] = self.custom_price_terms.to_dict()
        # override the default output from pydantic by calling `to_dict()` of opportunity_eula
        if self.opportunity_eula:
            _dict['opportunityEula'] = self.opportunity_eula.to_dict()
        # override the default output from pydantic by calling `to_dict()` of opportunity_rcmp
        if self.opportunity_rcmp:
            _dict['opportunityRcmp'] = self.opportunity_rcmp.to_dict()
        # override the default output from pydantic by calling `to_dict()` of payment_terms
        if self.payment_terms:
            _dict['paymentTerms'] = self.payment_terms.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AwsMarketplaceCppoOpportunity:
        """Create an instance of AwsMarketplaceCppoOpportunity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AwsMarketplaceCppoOpportunity.parse_obj(obj)

        _obj = AwsMarketplaceCppoOpportunity.parse_obj({
            "buyer_ids": obj.get("buyerIds"),
            "buyer_names": obj.get("buyerNames"),
            "contract_duration_in_days": obj.get("contractDurationInDays"),
            "created_by": obj.get("createdBy"),
            "created_date": obj.get("createdDate"),
            "custom_price_terms": AwsMarketplaceCppoPriceTerms.from_dict(obj.get("customPriceTerms")) if obj.get("customPriceTerms") is not None else None,
            "discount": obj.get("discount"),
            "discount_percent": obj.get("discountPercent"),
            "discount_type": obj.get("discountType"),
            "errors": obj.get("errors"),
            "expiration_date": obj.get("expirationDate"),
            "listing_fee_renewal": obj.get("listingFeeRenewal"),
            "manufacturer_id": obj.get("manufacturerId"),
            "manufacturer_name": obj.get("manufacturerName"),
            "offers_count": obj.get("offersCount"),
            "opportunity_discription": obj.get("opportunityDiscription"),
            "opportunity_duration_type": obj.get("opportunityDurationType"),
            "opportunity_eula": AwsMarketplaceCppoOpportunityEula.from_dict(obj.get("opportunityEula")) if obj.get("opportunityEula") is not None else None,
            "opportunity_id": obj.get("opportunityId"),
            "opportunity_name": obj.get("opportunityName"),
            "opportunity_rcmp": AwsMarketplaceCppoOpportunityEula.from_dict(obj.get("opportunityRcmp")) if obj.get("opportunityRcmp") is not None else None,
            "partner_id": obj.get("partnerId"),
            "partner_name": obj.get("partnerName"),
            "payment_terms": AwsMarketplaceCppoPaymentTerms.from_dict(obj.get("paymentTerms")) if obj.get("paymentTerms") is not None else None,
            "product_id": obj.get("productId"),
            "product_name": obj.get("productName"),
            "product_type": obj.get("productType"),
            "sppo": obj.get("sppo"),
            "status": obj.get("status"),
            "usage_allowed": obj.get("usageAllowed")
        })
        return _obj


