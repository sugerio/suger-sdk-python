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
from typing import Optional, Set
from typing_extensions import Self

class AzureMarketplaceValidation(BaseModel):
    """
    AzureMarketplaceValidation
    """ # noqa: E501
    var_schema: Optional[StrictStr] = Field(default=None, alias="$schema")
    code: Optional[StrictStr] = None
    level: Optional[StrictStr] = None
    message: Optional[StrictStr] = None
    resource_id: Optional[StrictStr] = Field(default=None, alias="resourceId")
    __properties: ClassVar[List[str]] = ["$schema", "code", "level", "message", "resourceId"]

    @field_validator('code')
    def code_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['businessValidationError', 'collectionLimitExceeded', 'invalidId', 'invalidEntityStatus', 'invalidRequest', 'invalidResource', 'invalidState', 'notDeployed', 'notSupported', 'operationCanceled', 'productLocked', 'resourceNotFound', 'schemaValidationError']):
            raise ValueError("must be one of enum values ('businessValidationError', 'collectionLimitExceeded', 'invalidId', 'invalidEntityStatus', 'invalidRequest', 'invalidResource', 'invalidState', 'notDeployed', 'notSupported', 'operationCanceled', 'productLocked', 'resourceNotFound', 'schemaValidationError')")
        return value

    @field_validator('level')
    def level_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['informational', 'warning']):
            raise ValueError("must be one of enum values ('informational', 'warning')")
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
        """Create an instance of AzureMarketplaceValidation from a JSON string"""
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
        """Create an instance of AzureMarketplaceValidation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "$schema": obj.get("$schema"),
            "code": obj.get("code"),
            "level": obj.get("level"),
            "message": obj.get("message"),
            "resourceId": obj.get("resourceId")
        })
        return _obj

