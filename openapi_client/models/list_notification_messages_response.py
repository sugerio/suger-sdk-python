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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictInt, conlist
from openapi_client.models.notification_message import NotificationMessage

class ListNotificationMessagesResponse(BaseModel):
    """
    ListNotificationMessagesResponse
    """
    next_offset: Optional[StrictInt] = Field(None, alias="nextOffset", description="The next offset to use in the next request to get the next page of notification messages. If this field is null, there are no more notification messages to get.")
    notification_messages: Optional[conlist(NotificationMessage)] = Field(None, alias="notificationMessages")
    total_count: Optional[StrictInt] = Field(None, alias="totalCount", description="The total number of notification messages. Only available when the request is made with the first offset = 0.")
    __properties = ["nextOffset", "notificationMessages", "totalCount"]

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
    def from_json(cls, json_str: str) -> ListNotificationMessagesResponse:
        """Create an instance of ListNotificationMessagesResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in notification_messages (list)
        _items = []
        if self.notification_messages:
            for _item in self.notification_messages:
                if _item:
                    _items.append(_item.to_dict())
            _dict['notificationMessages'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ListNotificationMessagesResponse:
        """Create an instance of ListNotificationMessagesResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ListNotificationMessagesResponse.parse_obj(obj)

        _obj = ListNotificationMessagesResponse.parse_obj({
            "next_offset": obj.get("nextOffset"),
            "notification_messages": [NotificationMessage.from_dict(_item) for _item in obj.get("notificationMessages")] if obj.get("notificationMessages") is not None else None,
            "total_count": obj.get("totalCount")
        })
        return _obj


