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


class OfferStatus(str, Enum):
    """
    OfferStatus
    """

    """
    allowed enum values
    """
    EMPTY = ''
    INVALID = 'INVALID'
    ACCEPTED = 'ACCEPTED'
    ACTIVE = 'ACTIVE'
    CANCEL_FAILED = 'CANCEL_FAILED'
    CANCEL_SUCCESS = 'CANCEL_SUCCESS'
    CANCELLED = 'CANCELLED'
    CREATE_FAILED = 'CREATE_FAILED'
    CREATE_SUCCESS = 'CREATE_SUCCESS'
    DELETED = 'DELETED'
    DEPRECATED = 'DEPRECATED'
    DRAFT = 'DRAFT'
    EXPIRED = 'EXPIRED'
    PENDING_ACCEPTANCE = 'PENDING_ACCEPTANCE'
    PENDING_CANCEL = 'PENDING_CANCEL'
    PENDING_CREATE = 'PENDING_CREATE'
    PENDING_UPDATE = 'PENDING_UPDATE'
    PREVIEW = 'PREVIEW'
    READY_TO_USE = 'READY_TO_USE'
    REJECTED = 'REJECTED'
    RESTRICTED = 'RESTRICTED'
    TEST = 'TEST'
    UPDATE_FAILED = 'UPDATE_FAILED'
    UPDATE_SUCCESS = 'UPDATE_SUCCESS'
    USED = 'USED'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of OfferStatus from a JSON string"""
        return cls(json.loads(json_str))


