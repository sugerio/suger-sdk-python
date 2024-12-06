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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class TypesEntitlementValue(BaseModel):
    """
    TypesEntitlementValue
    """ # noqa: E501
    boolean_value: Optional[StrictBool] = Field(default=None, description="The BooleanValue field will be populated with a boolean value when the entitlement is a boolean type. Otherwise, the field will not be set.", alias="booleanValue")
    double_value: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The DoubleValue field will be populated with a double value when the entitlement is a double type. Otherwise, the field will not be set.", alias="doubleValue")
    integer_value: Optional[StrictInt] = Field(default=None, description="The IntegerValue field will be populated with an integer value when the entitlement is an integer type. Otherwise, the field will not be set.", alias="integerValue")
    string_value: Optional[StrictStr] = Field(default=None, description="The StringValue field will be populated with a string value when the entitlement is a string type. Otherwise, the field will not be set.", alias="stringValue")
    __properties: ClassVar[List[str]] = ["booleanValue", "doubleValue", "integerValue", "stringValue"]

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
        """Create an instance of TypesEntitlementValue from a JSON string"""
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
        """Create an instance of TypesEntitlementValue from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "booleanValue": obj.get("booleanValue"),
            "doubleValue": obj.get("doubleValue"),
            "integerValue": obj.get("integerValue"),
            "stringValue": obj.get("stringValue")
        })
        return _obj


