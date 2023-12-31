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





class ValueType(str, Enum):
    """
    ValueType
    """

    """
    allowed enum values
    """
    VALUE_TYPE_UNSPECIFIED = 'VALUE_TYPE_UNSPECIFIED'
    BOOL = 'BOOL'
    INT64 = 'INT64'
    DOUBLE = 'DOUBLE'
    STRING = 'STRING'
    DISTRIBUTION = 'DISTRIBUTION'
    MONEY = 'MONEY'

    @classmethod
    def from_json(cls, json_str: str) -> ValueType:
        """Create an instance of ValueType from a JSON string"""
        return ValueType(json.loads(json_str))


