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


class SupportTicketPriority(str, Enum):
    """
    SupportTicketPriority
    """

    """
    allowed enum values
    """
    LOW = 'LOW'
    NORMAL = 'NORMAL'
    HIGH = 'HIGH'
    URGENT = 'URGENT'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of SupportTicketPriority from a JSON string"""
        return cls(json.loads(json_str))


