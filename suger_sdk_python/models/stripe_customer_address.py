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

class StripeCustomerAddress(BaseModel):
    """
    StripeCustomerAddress
    """ # noqa: E501
    city: Optional[StrictStr] = Field(default=None, description="City, district, suburb, town, or village.")
    country: Optional[StrictStr] = Field(default=None, description="Two-letter country code (ISO 3166-1 alpha-2)")
    line1: Optional[StrictStr] = Field(default=None, description="Address line 1 (e.g., street, PO Box, or company name).")
    line2: Optional[StrictStr] = Field(default=None, description="Address line 2 (e.g., apartment, suite, unit, or building).")
    postal_code: Optional[StrictStr] = Field(default=None, description="ZIP or postal code.")
    state: Optional[StrictStr] = Field(default=None, description="State, county, province, or region.")
    __properties: ClassVar[List[str]] = ["city", "country", "line1", "line2", "postal_code", "state"]

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
        """Create an instance of StripeCustomerAddress from a JSON string"""
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
        """Create an instance of StripeCustomerAddress from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "city": obj.get("city"),
            "country": obj.get("country"),
            "line1": obj.get("line1"),
            "line2": obj.get("line2"),
            "postal_code": obj.get("postal_code"),
            "state": obj.get("state")
        })
        return _obj


