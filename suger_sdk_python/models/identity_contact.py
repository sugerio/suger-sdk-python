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
from suger_sdk_python.models.identity_conctact_info import IdentityConctactInfo
from typing import Optional, Set
from typing_extensions import Self

class IdentityContact(BaseModel):
    """
    IdentityContact
    """ # noqa: E501
    creation_time: Optional[StrictStr] = Field(default=None, alias="creationTime")
    email_address: Optional[StrictStr] = Field(default=None, alias="emailAddress")
    id: Optional[StrictStr] = Field(default=None, description="This is generated by Suger. When you create a new contact, do not provide.")
    info: Optional[IdentityConctactInfo] = None
    last_update_time: Optional[StrictStr] = Field(default=None, alias="lastUpdateTime")
    name: Optional[StrictStr] = None
    organization_id: Optional[StrictStr] = Field(default=None, alias="organizationID")
    __properties: ClassVar[List[str]] = ["creationTime", "emailAddress", "id", "info", "lastUpdateTime", "name", "organizationID"]

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
        """Create an instance of IdentityContact from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of info
        if self.info:
            _dict['info'] = self.info.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IdentityContact from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "creationTime": obj.get("creationTime"),
            "emailAddress": obj.get("emailAddress"),
            "id": obj.get("id"),
            "info": IdentityConctactInfo.from_dict(obj["info"]) if obj.get("info") is not None else None,
            "lastUpdateTime": obj.get("lastUpdateTime"),
            "name": obj.get("name"),
            "organizationID": obj.get("organizationID")
        })
        return _obj

