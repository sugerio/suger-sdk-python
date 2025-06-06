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
from typing import Optional, Set
from typing_extensions import Self

class GcpUserInfo(BaseModel):
    """
    GcpUserInfo
    """ # noqa: E501
    orders: Optional[List[StrictStr]] = Field(default=None, description="a list of unique order IDs for each entitlement ID that indicates the different offers on the same product. This field is available only if multiple orders of the same product is enabled")
    roles: Optional[List[StrictStr]] = Field(default=None, description="An array of strings representing the user's roles. Right now, it can be either: ** account_admin, which indicates that the user is a Billing Account Administrator of the billing account that purchased the product, or ** project_editor, which indicates that the user is a Project Editor, but not a Billing Administrator, of the project under that billing account.")
    user_identity: Optional[StrictStr] = Field(default=None, description="The user's obfuscated GAIA ID, which can be used to initiate Open ID Connect.")
    __properties: ClassVar[List[str]] = ["orders", "roles", "user_identity"]

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
        """Create an instance of GcpUserInfo from a JSON string"""
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
        """Create an instance of GcpUserInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "orders": obj.get("orders"),
            "roles": obj.get("roles"),
            "user_identity": obj.get("user_identity")
        })
        return _obj


