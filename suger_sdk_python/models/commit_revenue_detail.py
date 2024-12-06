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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class CommitRevenueDetail(BaseModel):
    """
    CommitRevenueDetail
    """ # noqa: E501
    amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The total amount of the commit revenue.")
    description: Optional[StrictStr] = None
    expression: Optional[StrictStr] = None
    key: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    quantity: Optional[StrictInt] = Field(default=None, description="The quantity of the commit dimension. Default is 1.")
    rate: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The unit price of the commit dimension.")
    __properties: ClassVar[List[str]] = ["amount", "description", "expression", "key", "name", "quantity", "rate"]

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
        """Create an instance of CommitRevenueDetail from a JSON string"""
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
        """Create an instance of CommitRevenueDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "amount": obj.get("amount"),
            "description": obj.get("description"),
            "expression": obj.get("expression"),
            "key": obj.get("key"),
            "name": obj.get("name"),
            "quantity": obj.get("quantity"),
            "rate": obj.get("rate")
        })
        return _obj


