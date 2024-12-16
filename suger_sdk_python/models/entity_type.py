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


class EntityType(str, Enum):
    """
    EntityType
    """

    """
    allowed enum values
    """
    EMPTY = ''
    API_CLIENT = 'API_CLIENT'
    AUDITING_EVENT = 'AUDITING_EVENT'
    AUTO_SHARE_TASK = 'AUTO_SHARE_TASK'
    BUYER = 'BUYER'
    CONTACT = 'CONTACT'
    ENTITLEMENT = 'ENTITLEMENT'
    ENTITLEMENT_TERM = 'ENTITLEMENT_TERM'
    HEADLESS_ENTITLEMENTS = 'HEADLESS_ENTITLEMENTS'
    HUBSPOT_USER = 'HUBSPOT_USER'
    INTEGRATION = 'INTEGRATION'
    INVOICE = 'INVOICE'
    NEW_CLIENT = 'NEW_CLIENT'
    NOTIFICATION_MESSAGE = 'NOTIFICATION_MESSAGE'
    OFFER = 'OFFER'
    ORGANIZATION = 'ORGANIZATION'
    PAYMENT_TRANSACTION = 'PAYMENT_TRANSACTION'
    PRODUCT = 'PRODUCT'
    REFERRAL = 'REFERRAL'
    REVENUE_RECORD = 'REVENUE_RECORD'
    SUPPORT_TICKET = 'SUPPORT_TICKET'
    UNPURCHASED_OFFERS = 'UNPURCHASED_OFFERS'
    USAGE_RECORD_GROUP = 'USAGE_RECORD_GROUP'
    USAGE_RECORD_REPORT = 'USAGE_RECORD_REPORT'
    USER = 'USER'
    WORKFLOW = 'WORKFLOW'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of EntityType from a JSON string"""
        return cls(json.loads(json_str))

