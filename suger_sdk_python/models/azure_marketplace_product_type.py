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


class AzureMarketplaceProductType(str, Enum):
    """
    AzureMarketplaceProductType
    """

    """
    allowed enum values
    """
    AZUREAPPLICATION = 'azureApplication'
    AZURECONTAINER = 'azureContainer'
    AZUREVIRTUALMACHINE = 'azureVirtualMachine'
    CONSULTINGSERVICE = 'consultingService'
    CONTAINERAPP = 'containerApp'
    COREVIRTUALMACHINE = 'coreVirtualMachine'
    COSELLONLY = 'cosellOnly'
    DYNAMICS365BUSINESSCENTRAL = 'dynamics365BusinessCentral'
    DYNAMICS365FORCUSTOMERENGAGEMENT = 'dynamics365ForCustomerEngagement'
    DYNAMICS365FOROPERATIONS = 'dynamics365ForOperations'
    IOTEDGEMODULE = 'iotEdgeModule'
    MANAGEDSERVICE = 'managedService'
    POWERBIAPP = 'powerBiApp'
    POWERBIVISUAL = 'powerBiVisual'
    SOFTWAREASASERVICE = 'softwareAsAService'
    XBOX360NONBACKCOMPAT = 'xbox360NonBackcompat'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of AzureMarketplaceProductType from a JSON string"""
        return cls(json.loads(json_str))


