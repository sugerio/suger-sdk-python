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
    EntityType_UNKNOWN = ''
    EntityType_API_CLIENT = 'API_CLIENT'
    EntityType_AUDITING_EVENT = 'AUDITING_EVENT'
    EntityType_AUTO_SHARE_TASK = 'AUTO_SHARE_TASK'
    EntityType_BUYER = 'BUYER'
    EntityType_CONTACT = 'CONTACT'
    EntityType_ENTITLEMENT = 'ENTITLEMENT'
    EntityType_ENTITLEMENT_TERM = 'ENTITLEMENT_TERM'
    EntityType_HEADLESS_ENTITLEMENTS = 'HEADLESS_ENTITLEMENTS'
    EntityType_HUBSPOT_USER = 'HUBSPOT_USER'
    EntityType_INTEGRATION = 'INTEGRATION'
    EntityType_INVOICE = 'INVOICE'
    EntityType_NEW_CLIENT = 'NEW_CLIENT'
    EntityType_NOTIFICATION_MESSAGE = 'NOTIFICATION_MESSAGE'
    EntityType_OFFER = 'OFFER'
    EntityType_ORGANIZATION = 'ORGANIZATION'
    EntityType_PAYMENT_TRANSACTION = 'PAYMENT_TRANSACTION'
    EntityType_PRODUCT = 'PRODUCT'
    EntityType_REFERRAL = 'REFERRAL'
    EntityType_REVENUE_RECORD = 'REVENUE_RECORD'
    EntityType_SUPPORT_TICKET = 'SUPPORT_TICKET'
    EntityType_UNPURCHASED_OFFERS = 'UNPURCHASED_OFFERS'
    EntityType_USAGE_RECORD_GROUP = 'USAGE_RECORD_GROUP'
    EntityType_USAGE_RECORD_REPORT = 'USAGE_RECORD_REPORT'
    EntityType_USER = 'USER'
    EntityType_WORKFLOW = 'WORKFLOW'
    EntityType_WORKFLOW_EXECUTION = 'WORKFLOW_EXECUTION'
    EntityType_WORKFLOW_WEBHOOK = 'WORKFLOW_WEBHOOK'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of EntityType from a JSON string"""
        return cls(json.loads(json_str))


