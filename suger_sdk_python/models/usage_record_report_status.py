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


class UsageRecordReportStatus(str, Enum):
    """
    UsageRecordReportStatus
    """

    """
    allowed enum values
    """
    EMPTY = ''
    SUCCESS = 'SUCCESS'
    FAILED = 'FAILED'
    CREATED = 'CREATED'
    INVOICED = 'INVOICED'
    DELETED = 'DELETED'
    CANCELED = 'CANCELED'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of UsageRecordReportStatus from a JSON string"""
        return cls(json.loads(json_str))


