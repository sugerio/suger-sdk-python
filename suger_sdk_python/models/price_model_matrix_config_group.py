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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Optional, Union
from suger_sdk_python.models.price_model_matrix_property import PriceModelMatrixProperty
from typing import Optional, Set
from typing_extensions import Self

class PriceModelMatrixConfigGroup(BaseModel):
    """
    PriceModelMatrixConfigGroup
    """ # noqa: E501
    properties: Optional[List[PriceModelMatrixProperty]] = None
    unit_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="unitAmount")
    __properties: ClassVar[List[str]] = ["properties", "unitAmount"]

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
        """Create an instance of PriceModelMatrixConfigGroup from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in properties (list)
        _items = []
        if self.properties:
            for _item_properties in self.properties:
                if _item_properties:
                    _items.append(_item_properties.to_dict())
            _dict['properties'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PriceModelMatrixConfigGroup from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "properties": [PriceModelMatrixProperty.from_dict(_item) for _item in obj["properties"]] if obj.get("properties") is not None else None,
            "unitAmount": obj.get("unitAmount")
        })
        return _obj


