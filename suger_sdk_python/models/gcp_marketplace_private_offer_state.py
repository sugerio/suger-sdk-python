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


class GcpMarketplacePrivateOfferState(str, Enum):
    """
    GcpMarketplacePrivateOfferState
    """

    """
    allowed enum values
    """
    OFFER_ACTIVE = 'OFFER_ACTIVE'
    OFFER_ACTIVATING = 'OFFER_ACTIVATING'
    OFFER_SCHEDULED = 'OFFER_SCHEDULED'
    OFFER_ENTITLEMENT_ACCOUNT_PENDING = 'OFFER_ENTITLEMENT_ACCOUNT_PENDING'
    OFFER_PUBLISHED = 'OFFER_PUBLISHED'
    OFFER_LAPSED = 'OFFER_LAPSED'
    OFFER_EXPIRED = 'OFFER_EXPIRED'
    OFFER_CANCELLED = 'OFFER_CANCELLED'
    OFFER_UNAVAILABLE = 'OFFER_UNAVAILABLE'
    OFFER_DRAFT = 'OFFER_DRAFT'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of GcpMarketplacePrivateOfferState from a JSON string"""
        return cls(json.loads(json_str))


