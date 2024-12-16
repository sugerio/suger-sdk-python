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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from suger_sdk_python.models.notification_event_action import NotificationEventAction
from typing import Optional, Set
from typing_extensions import Self

class NotificationMessageInfo(BaseModel):
    """
    NotificationMessageInfo
    """ # noqa: E501
    action: Optional[NotificationEventAction] = Field(default=None, description="The action of this notification message.")
    cc_recipients: Optional[List[StrictStr]] = Field(default=None, alias="ccRecipients")
    custom_fields: Optional[Dict[str, Any]] = Field(default=None, description="All other fields", alias="customFields")
    html_content: Optional[StrictStr] = Field(default=None, description="The HTML content of the email.", alias="htmlContent")
    rcc_recipients: Optional[List[StrictStr]] = Field(default=None, alias="rccRecipients")
    standard_fields: Optional[Dict[str, Any]] = Field(default=None, description="The standard fields to render the email content.", alias="standardFields")
    subject: Optional[StrictStr] = None
    text_content: Optional[StrictStr] = Field(default=None, description="The text content of the email in case the recipient's email client does not support HTML.", alias="textContent")
    __properties: ClassVar[List[str]] = ["action", "ccRecipients", "customFields", "htmlContent", "rccRecipients", "standardFields", "subject", "textContent"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of NotificationMessageInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NotificationMessageInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "action": obj.get("action"),
            "ccRecipients": obj.get("ccRecipients"),
            "customFields": obj.get("customFields"),
            "htmlContent": obj.get("htmlContent"),
            "rccRecipients": obj.get("rccRecipients"),
            "standardFields": obj.get("standardFields"),
            "subject": obj.get("subject"),
            "textContent": obj.get("textContent")
        })
        return _obj

