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


class GcpMarketplaceUserAccountApprovalState(str, Enum):
    """
    GcpMarketplaceUserAccountApprovalState
    """

    """
    allowed enum values
    """
    STATE_UNSPECIFIED = "STATE_UNSPECIFIED"
    PENDING = "PENDING"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"

    @classmethod
    def from_json(cls, json_str: str) -> GcpMarketplaceUserAccountApprovalState:
        """Create an instance of GcpMarketplaceUserAccountApprovalState from a JSON string"""
        return GcpMarketplaceUserAccountApprovalState(json.loads(json_str))