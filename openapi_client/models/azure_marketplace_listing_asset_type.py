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





class AzureMarketplaceListingAssetType(str, Enum):
    """
    AzureMarketplaceListingAssetType
    """

    """
    allowed enum values
    """
    AZURELOGOSMALL = 'azureLogoSmall'
    AZURELOGOMEDIUM = 'azureLogoMedium'
    AZURELOGOLARGE = 'azureLogoLarge'
    AZURELOGOWIDE = 'azureLogoWide'
    AZURELOGOSCREENSHOT = 'azureLogoScreenshot'
    AZURELOGOHERO = 'azureLogoHero'
    PDFDOCUMENT = 'pdfDocument'

    @classmethod
    def from_json(cls, json_str: str) -> AzureMarketplaceListingAssetType:
        """Create an instance of AzureMarketplaceListingAssetType from a JSON string"""
        return AzureMarketplaceListingAssetType(json.loads(json_str))


