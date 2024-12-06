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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from suger_sdk_python.models.auditing_event_priority import AuditingEventPriority
from suger_sdk_python.models.entity_type import EntityType
from suger_sdk_python.models.last_modified_by import LastModifiedBy
from suger_sdk_python.models.notification_channel import NotificationChannel
from suger_sdk_python.models.notification_event_action import NotificationEventAction
from suger_sdk_python.models.notification_event_status import NotificationEventStatus
from suger_sdk_python.models.partner import Partner
from suger_sdk_python.models.track_event import TrackEvent
from typing import Optional, Set
from typing_extensions import Self

class NotificationEvent(BaseModel):
    """
    NotificationEvent
    """ # noqa: E501
    action: Optional[NotificationEventAction] = None
    cc_contact_ids: Optional[List[StrictStr]] = Field(default=None, description="Cc contactIds that will receive this notification", alias="ccContactIds")
    channels: Optional[List[NotificationChannel]] = Field(default=None, description="The list of channels this event will be sent to, e.g., [\"SLACK\", \"EMAIL\"]")
    contact_emails: Optional[List[StrictStr]] = Field(default=None, description="Contact emails that will receive this notification", alias="contactEmails")
    contact_ids: Optional[List[StrictStr]] = Field(default=None, description="ContactIds that will receive this notification", alias="contactIds")
    created_by: Optional[LastModifiedBy] = Field(default=None, description="Who originally created or triggered this notification event. It can be user or API client.", alias="createdBy")
    custom_fields: Optional[Dict[str, Any]] = Field(default=None, description="Custom fields of the notification event.", alias="customFields")
    entity_id: Optional[StrictStr] = Field(default=None, alias="entityID")
    entity_name: Optional[StrictStr] = Field(default=None, description="The name of the entity.", alias="entityName")
    entity_status: Optional[StrictStr] = Field(default=None, alias="entityStatus")
    entity_type: Optional[EntityType] = Field(default=None, alias="entityType")
    event_id: Optional[StrictStr] = Field(default=None, description="notification event id.", alias="eventID")
    event_status: Optional[NotificationEventStatus] = Field(default=None, description="notification event status.", alias="eventStatus")
    info: Optional[Dict[str, Any]] = Field(default=None, description="Additional info of the notification event.")
    is_action_item: Optional[StrictBool] = Field(default=None, description="If this notification event is an action item.", alias="isActionItem")
    last_update_time: Optional[datetime] = Field(default=None, description="timestamp of the event when it is updated.", alias="lastUpdateTime")
    message: Optional[StrictStr] = Field(default=None, description="The message of the notification event such as email body, action item description.")
    organization_id: Optional[StrictStr] = Field(default=None, description="suger organization id.", alias="organizationID")
    partner: Optional[Partner] = Field(default=None, description="the partner of the entity. Optional.")
    priority: Optional[AuditingEventPriority] = Field(default=None, description="The priority of the notification event.")
    require_audit: Optional[StrictBool] = Field(default=None, description="If this notification event is an auditing event and need to store in DB.", alias="requireAudit")
    timestamp: Optional[datetime] = Field(default=None, description="timestamp of the event when it is scheduled or created.")
    title: Optional[StrictStr] = Field(default=None, description="The title of the notification event such as email subject, action item title.")
    track_events: Optional[List[TrackEvent]] = Field(default=None, description="The track events of the notification event.", alias="trackEvents")
    __properties: ClassVar[List[str]] = ["action", "ccContactIds", "channels", "contactEmails", "contactIds", "createdBy", "customFields", "entityID", "entityName", "entityStatus", "entityType", "eventID", "eventStatus", "info", "isActionItem", "lastUpdateTime", "message", "organizationID", "partner", "priority", "requireAudit", "timestamp", "title", "trackEvents"]

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
        """Create an instance of NotificationEvent from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of created_by
        if self.created_by:
            _dict['createdBy'] = self.created_by.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in track_events (list)
        _items = []
        if self.track_events:
            for _item_track_events in self.track_events:
                if _item_track_events:
                    _items.append(_item_track_events.to_dict())
            _dict['trackEvents'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NotificationEvent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "action": obj.get("action"),
            "ccContactIds": obj.get("ccContactIds"),
            "channels": obj.get("channels"),
            "contactEmails": obj.get("contactEmails"),
            "contactIds": obj.get("contactIds"),
            "createdBy": LastModifiedBy.from_dict(obj["createdBy"]) if obj.get("createdBy") is not None else None,
            "customFields": obj.get("customFields"),
            "entityID": obj.get("entityID"),
            "entityName": obj.get("entityName"),
            "entityStatus": obj.get("entityStatus"),
            "entityType": obj.get("entityType"),
            "eventID": obj.get("eventID"),
            "eventStatus": obj.get("eventStatus"),
            "info": obj.get("info"),
            "isActionItem": obj.get("isActionItem"),
            "lastUpdateTime": obj.get("lastUpdateTime"),
            "message": obj.get("message"),
            "organizationID": obj.get("organizationID"),
            "partner": obj.get("partner"),
            "priority": obj.get("priority"),
            "requireAudit": obj.get("requireAudit"),
            "timestamp": obj.get("timestamp"),
            "title": obj.get("title"),
            "trackEvents": [TrackEvent.from_dict(_item) for _item in obj["trackEvents"]] if obj.get("trackEvents") is not None else None
        })
        return _obj


