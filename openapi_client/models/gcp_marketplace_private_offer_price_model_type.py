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





class GcpMarketplacePrivateOfferPriceModelType(str, Enum):
    """
    GcpMarketplacePrivateOfferPriceModelType
    """

    """
    allowed enum values
    """
    EMPTY = ''
    PRICE_MODEL_TYPE_UNSPECIFIED = 'PRICE_MODEL_TYPE_UNSPECIFIED'
    CUD = 'CUD'
    PAYG = 'PAYG'
    PAYG_WITH_CUD = 'PAYG_WITH_CUD'
    FIXED_FEE = 'FIXED_FEE'
    FIXED_FEE_WITH_OVERAGE = 'FIXED_FEE_WITH_OVERAGE'

    @classmethod
    def from_json(cls, json_str: str) -> GcpMarketplacePrivateOfferPriceModelType:
        """Create an instance of GcpMarketplacePrivateOfferPriceModelType from a JSON string"""
        return GcpMarketplacePrivateOfferPriceModelType(json.loads(json_str))


