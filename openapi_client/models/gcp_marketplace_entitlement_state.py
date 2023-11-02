# coding: utf-8

"""
    Suger API

    CRUD operations on a set of resources, including organizations, products, offers, entitlements, usage record groups for meterting, etc.

    The version of the OpenAPI document: 1.0
    Contact: support@suger.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class GcpMarketplaceEntitlementState(str, Enum):
    """
    GcpMarketplaceEntitlementState
    """

    """
    allowed enum values
    """
    ENTITLEMENT_STATE_UNSPECIFIED = 'ENTITLEMENT_STATE_UNSPECIFIED'
    ENTITLEMENT_ACTIVATION_REQUESTED = 'ENTITLEMENT_ACTIVATION_REQUESTED'
    ENTITLEMENT_ACTIVE = 'ENTITLEMENT_ACTIVE'
    ENTITLEMENT_PENDING_CANCELLATION = 'ENTITLEMENT_PENDING_CANCELLATION'
    ENTITLEMENT_CANCELLED = 'ENTITLEMENT_CANCELLED'
    ENTITLEMENT_PENDING_PLAN_CHANGE = 'ENTITLEMENT_PENDING_PLAN_CHANGE'
    ENTITLEMENT_PENDING_PLAN_CHANGE_APPROVAL = 'ENTITLEMENT_PENDING_PLAN_CHANGE_APPROVAL'
    ENTITLEMENT_SUSPENDED = 'ENTITLEMENT_SUSPENDED'

    @classmethod
    def from_json(cls, json_str: str) -> GcpMarketplaceEntitlementState:
        """Create an instance of GcpMarketplaceEntitlementState from a JSON string"""
        return GcpMarketplaceEntitlementState(json.loads(json_str))


