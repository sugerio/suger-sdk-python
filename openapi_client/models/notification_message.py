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

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, StrictStr
from openapi_client.models.notification_message_info import NotificationMessageInfo
from openapi_client.models.notification_type import NotificationType


class NotificationMessage(BaseModel):
    """
    NotificationMessage
    """

    creation_time: Optional[datetime] = Field(None, alias="creationTime")
    id: Optional[StrictStr] = None
    info: Optional[NotificationMessageInfo] = None
    organization_id: Optional[StrictStr] = Field(None, alias="organizationID")
    recipient: Optional[StrictStr] = None
    type: Optional[NotificationType] = None
    __properties = ["creationTime", "id", "info", "organizationID", "recipient", "type"]

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
    def from_json(cls, json_str: str) -> NotificationMessage:
        """Create an instance of NotificationMessage from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of info
        if self.info:
            _dict["info"] = self.info.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> NotificationMessage:
        """Create an instance of NotificationMessage from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return NotificationMessage.parse_obj(obj)

        _obj = NotificationMessage.parse_obj(
            {
                "creation_time": obj.get("creationTime"),
                "id": obj.get("id"),
                "info": NotificationMessageInfo.from_dict(obj.get("info"))
                if obj.get("info") is not None
                else None,
                "organization_id": obj.get("organizationID"),
                "recipient": obj.get("recipient"),
                "type": obj.get("type"),
            }
        )
        return _obj