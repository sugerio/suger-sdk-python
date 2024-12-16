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
from suger_sdk_python.models.support_ticket_comment_detail import SupportTicketCommentDetail
from suger_sdk_python.models.support_ticket_user import SupportTicketUser
from typing import Optional, Set
from typing_extensions import Self

class SupportTicketComment(BaseModel):
    """
    SupportTicketComment
    """ # noqa: E501
    comment: Optional[List[SupportTicketCommentDetail]] = None
    comment_text: Optional[StrictStr] = Field(default=None, description="When creating a new comment, only CommentText is required.")
    creator: Optional[SupportTicketUser] = Field(default=None, description="who created the comment")
    var_date: Optional[StrictStr] = Field(default=None, alias="date")
    id: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["comment", "comment_text", "creator", "date", "id"]

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
        """Create an instance of SupportTicketComment from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in comment (list)
        _items = []
        if self.comment:
            for _item_comment in self.comment:
                if _item_comment:
                    _items.append(_item_comment.to_dict())
            _dict['comment'] = _items
        # override the default output from pydantic by calling `to_dict()` of creator
        if self.creator:
            _dict['creator'] = self.creator.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SupportTicketComment from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "comment": [SupportTicketCommentDetail.from_dict(_item) for _item in obj["comment"]] if obj.get("comment") is not None else None,
            "comment_text": obj.get("comment_text"),
            "creator": SupportTicketUser.from_dict(obj["creator"]) if obj.get("creator") is not None else None,
            "date": obj.get("date"),
            "id": obj.get("id")
        })
        return _obj

