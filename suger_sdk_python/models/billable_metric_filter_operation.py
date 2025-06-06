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


class BillableMetricFilterOperation(str, Enum):
    """
    BillableMetricFilterOperation
    """

    """
    allowed enum values
    """
    BillableMetricFilterOperation_IS = 'IS'
    BillableMetricFilterOperation_NOT_IS = 'NOT_IS'
    BillableMetricFilterOperation_CONTAINS = 'CONTAINS'
    BillableMetricFilterOperation_NOT_CONTAINS = 'NOT_CONTAINS'
    BillableMetricFilterOperation_GT = 'GT'
    BillableMetricFilterOperation_GTE = 'GTE'
    BillableMetricFilterOperation_LT = 'LT'
    BillableMetricFilterOperation_LTE = 'LTE'
    BillableMetricFilterOperation_EQ = 'EQ'
    BillableMetricFilterOperation_NEQ = 'NOT_EQ'
    BillableMetricFilterOperation_EXISTS = 'EXISTS'
    BillableMetricFilterOperation_NOT_EXISTS = 'NOT_EXISTS'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of BillableMetricFilterOperation from a JSON string"""
        return cls(json.loads(json_str))


