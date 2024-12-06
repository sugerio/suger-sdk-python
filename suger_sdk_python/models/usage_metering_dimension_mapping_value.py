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
from suger_sdk_python.models.usage_metering_dimension_mapping_mode import UsageMeteringDimensionMappingMode
from typing import Optional, Set
from typing_extensions import Self

class UsageMeteringDimensionMappingValue(BaseModel):
    """
    UsageMeteringDimensionMappingValue
    """ # noqa: E501
    convertion_multiplier: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The convertion multiplier when mapping from the source dimension key to the destination dimensionKey by quantity mode. Not required if the mapping mode is AMOUNT.", alias="convertionMultiplier")
    dimension_key: Optional[StrictStr] = Field(default=None, description="The destination dimension key of the usage metering mapping.", alias="dimensionKey")
    mapping_mode: Optional[UsageMeteringDimensionMappingMode] = Field(default=None, description="The conversion mode of UsageMeteringDimensionMapping. The default is QUANTITY if not available.", alias="mappingMode")
    __properties: ClassVar[List[str]] = ["convertionMultiplier", "dimensionKey", "mappingMode"]

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
        """Create an instance of UsageMeteringDimensionMappingValue from a JSON string"""
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
        """Create an instance of UsageMeteringDimensionMappingValue from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "convertionMultiplier": obj.get("convertionMultiplier"),
            "dimensionKey": obj.get("dimensionKey"),
            "mappingMode": obj.get("mappingMode")
        })
        return _obj


