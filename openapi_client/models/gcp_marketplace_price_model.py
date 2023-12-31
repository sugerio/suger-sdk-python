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





class GcpMarketplacePriceModel(str, Enum):
    """
    GcpMarketplacePriceModel
    """

    """
    allowed enum values
    """
    FREE = 'FREE'
    SUBSCRIPTION = 'SUBSCRIPTION'
    USAGE = 'USAGE'
    SUBSCRIPTION_PLUS_USAGE = 'SUBSCRIPTION_PLUS_USAGE'

    @classmethod
    def from_json(cls, json_str: str) -> GcpMarketplacePriceModel:
        """Create an instance of GcpMarketplacePriceModel from a JSON string"""
        return GcpMarketplacePriceModel(json.loads(json_str))


