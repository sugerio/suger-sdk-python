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
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr
from openapi_client.models.aws_sns_subscription_status import AwsSnsSubscriptionStatus

class AwsSnsSubscription(BaseModel):
    """
    AwsSnsSubscription
    """
    endpoint: Optional[StrictStr] = Field(None, alias="Endpoint")
    protocol: Optional[StrictStr] = Field(None, alias="Protocol")
    status: Optional[AwsSnsSubscriptionStatus] = Field(None, alias="Status")
    subscription_arn: Optional[StrictStr] = Field(None, alias="SubscriptionArn")
    topic_arn: Optional[StrictStr] = Field(None, alias="TopicArn")
    __properties = ["Endpoint", "Protocol", "Status", "SubscriptionArn", "TopicArn"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> AwsSnsSubscription:
        """Create an instance of AwsSnsSubscription from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AwsSnsSubscription:
        """Create an instance of AwsSnsSubscription from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AwsSnsSubscription.parse_obj(obj)

        _obj = AwsSnsSubscription.parse_obj({
            "endpoint": obj.get("Endpoint"),
            "protocol": obj.get("Protocol"),
            "status": obj.get("Status"),
            "subscription_arn": obj.get("SubscriptionArn"),
            "topic_arn": obj.get("TopicArn")
        })
        return _obj


