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


class Partner(str, Enum):
    """
    Partner
    """

    """
    allowed enum values
    """
    EMPTY = ''
    ADYEN = 'ADYEN'
    ALIBABA = 'ALIBABA'
    AWS = 'AWS'
    AWS_CHINA = 'AWS_CHINA'
    AZURE = 'AZURE'
    GCP = 'GCP'
    GOOGLE = 'GOOGLE'
    HUBSPOT = 'HUBSPOT'
    INTUIT = 'INTUIT'
    LAGO = 'LAGO'
    MARKETO = 'MARKETO'
    METRONOME = 'METRONOME'
    MICROSOFT = 'MICROSOFT'
    ORACLE = 'ORACLE'
    ORB = 'ORB'
    REDHAT = 'REDHAT'
    SALESFORCE = 'SALESFORCE'
    SLACK = 'SLACK'
    SNOWFLAKE = 'SNOWFLAKE'
    STRIPE = 'STRIPE'
    ZOHO = 'ZOHO'
    DATABRICKS = 'DATABRICKS'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of Partner from a JSON string"""
        return cls(json.loads(json_str))


