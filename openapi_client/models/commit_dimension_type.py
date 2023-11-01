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


class CommitDimensionType(str, Enum):
    """
    CommitDimensionType
    """

    """
    allowed enum values
    """
    FLAT_RATE = "FLAT_RATE"
    PER_USER = "PER_USER"

    @classmethod
    def from_json(cls, json_str: str) -> CommitDimensionType:
        """Create an instance of CommitDimensionType from a JSON string"""
        return CommitDimensionType(json.loads(json_str))