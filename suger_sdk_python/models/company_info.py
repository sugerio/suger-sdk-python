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

class CompanyInfo(BaseModel):
    """
    CompanyInfo
    """ # noqa: E501
    address_line1: Optional[StrictStr] = Field(default=None, alias="addressLine1")
    address_line2: Optional[StrictStr] = Field(default=None, alias="addressLine2")
    city: Optional[StrictStr] = None
    country: Optional[StrictStr] = None
    email_domain: Optional[StrictStr] = Field(default=None, alias="emailDomain")
    name: Optional[StrictStr] = None
    postal_code: Optional[StrictStr] = Field(default=None, alias="postalCode")
    state: Optional[StrictStr] = None
    valid_from: Optional[StrictStr] = Field(default=None, description="When the company info becomes valid. in format \"2006-01-02T15:04:05Z\"", alias="validFrom")
    __properties: ClassVar[List[str]] = ["addressLine1", "addressLine2", "city", "country", "emailDomain", "name", "postalCode", "state", "validFrom"]

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
        """Create an instance of CompanyInfo from a JSON string"""
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
        """Create an instance of CompanyInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "addressLine1": obj.get("addressLine1"),
            "addressLine2": obj.get("addressLine2"),
            "city": obj.get("city"),
            "country": obj.get("country"),
            "emailDomain": obj.get("emailDomain"),
            "name": obj.get("name"),
            "postalCode": obj.get("postalCode"),
            "state": obj.get("state"),
            "validFrom": obj.get("validFrom")
        })
        return _obj


