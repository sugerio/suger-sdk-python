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


class NotificationChannel(str, Enum):
    """
    NotificationChannel
    """

    """
    allowed enum values
    """
    EMAIL = 'EMAIL'
    SLACK = 'SLACK'
    SMS = 'SMS'
    SNS = 'SNS'
    SALESFORCE = 'SALESFORCE'
    WEBHOOK = 'WEBHOOK'
    SUGER_SUPPORT = 'SUGER_SUPPORT'
    MICROSOFT_TEAMS = 'MICROSOFT_TEAMS'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of NotificationChannel from a JSON string"""
        return cls(json.loads(json_str))


