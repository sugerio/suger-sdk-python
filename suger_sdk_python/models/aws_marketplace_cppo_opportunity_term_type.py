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
import json
from enum import Enum
from typing_extensions import Self


class AwsMarketplaceCppoOpportunityTermType(str, Enum):
    """
    AwsMarketplaceCppoOpportunityTermType
    """

    """
    allowed enum values
    """
    AwsMarketplaceCppoOpportunityTermType_BuyerTargetingTerm = 'BuyerTargetingTerm'
    AwsMarketplaceCppoOpportunityTermType_UpdateAvailability = 'UpdateAvailability'
    AwsMarketplaceCppoOpportunityTermType_BuyerValidityTerm = 'BuyerValidityTerm'
    AwsMarketplaceCppoOpportunityTermType_BuyerLegalTerm = 'BuyerLegalTerm'
    AwsMarketplaceCppoOpportunityTermType_ResaleLegalTerm = 'ResaleLegalTerm'
    AwsMarketplaceCppoOpportunityTermType_ResaleUsageBasedPricingTerm = 'ResaleUsageBasedPricingTerm'
    AwsMarketplaceCppoOpportunityTermType_ResaleConfigurableUpfrontPricingTerm = 'ResaleConfigurableUpfrontPricingTerm'
    AwsMarketplaceCppoOpportunityTermType_ResaleFixedUpfrontPricingTerm = 'ResaleFixedUpfrontPricingTerm'
    AwsMarketplaceCppoOpportunityTermType_ResalePaymentScheduleTerm = 'ResalePaymentScheduleTerm'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of AwsMarketplaceCppoOpportunityTermType from a JSON string"""
        return cls(json.loads(json_str))


