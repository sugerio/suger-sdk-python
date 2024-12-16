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
from suger_sdk_python.models.azure_included_base_quantity import AzureIncludedBaseQuantity
from typing import Optional, Set
from typing_extensions import Self

class AzureProductVariantCustomMeter(BaseModel):
    """
    AzureProductVariantCustomMeter
    """ # noqa: E501
    display_name: Optional[StrictStr] = Field(default=None, alias="displayName")
    id: Optional[StrictStr] = None
    included_base_quantities: Optional[List[AzureIncludedBaseQuantity]] = Field(default=None, alias="includedBaseQuantities")
    is_enabled: Optional[StrictBool] = Field(default=None, alias="isEnabled")
    price_in_usd: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="priceInUsd")
    unique_id: Optional[StrictStr] = Field(default=None, alias="uniqueID")
    unit_of_measure: Optional[StrictStr] = Field(default=None, alias="unitOfMeasure")
    __properties: ClassVar[List[str]] = ["displayName", "id", "includedBaseQuantities", "isEnabled", "priceInUsd", "uniqueID", "unitOfMeasure"]

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
        """Create an instance of AzureProductVariantCustomMeter from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in included_base_quantities (list)
        _items = []
        if self.included_base_quantities:
            for _item_included_base_quantities in self.included_base_quantities:
                if _item_included_base_quantities:
                    _items.append(_item_included_base_quantities.to_dict())
            _dict['includedBaseQuantities'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AzureProductVariantCustomMeter from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "displayName": obj.get("displayName"),
            "id": obj.get("id"),
            "includedBaseQuantities": [AzureIncludedBaseQuantity.from_dict(_item) for _item in obj["includedBaseQuantities"]] if obj.get("includedBaseQuantities") is not None else None,
            "isEnabled": obj.get("isEnabled"),
            "priceInUsd": obj.get("priceInUsd"),
            "uniqueID": obj.get("uniqueID"),
            "unitOfMeasure": obj.get("unitOfMeasure")
        })
        return _obj

