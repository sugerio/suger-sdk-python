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


class SqlValueType(str, Enum):
    """
    SqlValueType
    """

    """
    allowed enum values
    """
    STRING = "STRING"
    INT = "INT"
    FLOAT = "FLOAT"
    BOOL = "BOOL"
    STRING_ARRAY = "STRING_ARRAY"
    INT_ARRAY = "INT_ARRAY"
    FLOAT_ARRAY = "FLOAT_ARRAY"
    BOOL_ARRAY = "BOOL_ARRAY"
    NULL = "NULL"

    @classmethod
    def from_json(cls, json_str: str) -> SqlValueType:
        """Create an instance of SqlValueType from a JSON string"""
        return SqlValueType(json.loads(json_str))