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


class OfferType(str, Enum):
    """
    OfferType
    """

    """
    allowed enum values
    """
    UNKNOWN = 'UNKNOWN'
    AMI = 'AMI'
    APPLICATION = 'APPLICATION'
    CONTAINER = 'CONTAINER'
    CONTRACT = 'CONTRACT'
    CPPO_OUT = 'CPPO_OUT'
    CPPO_IN = 'CPPO_IN'
    CPPO = 'CPPO'
    CUD = 'CUD'
    DATA = 'DATA'
    DEFAULT = 'DEFAULT'
    FIXED_FEE = 'FIXED_FEE'
    FIXED_FEE_WITH_OVERAGE = 'FIXED_FEE_WITH_OVERAGE'
    FLAT_RATE = 'FLAT_RATE'
    FREE_TRIAL = 'FREE_TRIAL'
    PAYG = 'PAYG'
    PAYG_WITH_CUD = 'PAYG_WITH_CUD'
    PER_USER = 'PER_USER'
    PRIVATE = 'PRIVATE'
    PROFESSIONAL_SERVICES = 'PROFESSIONAL_SERVICES'
    SUBSCRIPTION = 'SUBSCRIPTION'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of OfferType from a JSON string"""
        return cls(json.loads(json_str))


