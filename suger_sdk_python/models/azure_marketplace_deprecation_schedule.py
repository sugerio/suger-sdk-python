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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from suger_sdk_python.models.azure_marketplace_deprecation_schedule_alternative import AzureMarketplaceDeprecationScheduleAlternative
from typing import Optional, Set
from typing_extensions import Self

class AzureMarketplaceDeprecationSchedule(BaseModel):
    """
    AzureMarketplaceDeprecationSchedule
    """ # noqa: E501
    var_schema: Optional[StrictStr] = Field(default=None, alias="$schema")
    alternative: Optional[AzureMarketplaceDeprecationScheduleAlternative] = None
    var_date: Optional[StrictStr] = Field(default=None, description="format: date-time", alias="date")
    date_offset: Optional[StrictStr] = Field(default=None, description="format: duration", alias="dateOffset")
    reason: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["$schema", "alternative", "date", "dateOffset", "reason"]

    @field_validator('reason')
    def reason_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['criticalSecurityIssue', 'endOfSupport', 'other']):
            raise ValueError("must be one of enum values ('criticalSecurityIssue', 'endOfSupport', 'other')")
        return value

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
        """Create an instance of AzureMarketplaceDeprecationSchedule from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of alternative
        if self.alternative:
            _dict['alternative'] = self.alternative.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AzureMarketplaceDeprecationSchedule from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "$schema": obj.get("$schema"),
            "alternative": AzureMarketplaceDeprecationScheduleAlternative.from_dict(obj["alternative"]) if obj.get("alternative") is not None else None,
            "date": obj.get("date"),
            "dateOffset": obj.get("dateOffset"),
            "reason": obj.get("reason")
        })
        return _obj


