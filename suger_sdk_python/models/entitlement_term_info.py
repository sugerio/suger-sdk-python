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
from suger_sdk_python.models.entitlement_term_type import EntitlementTermType
from typing import Optional, Set
from typing_extensions import Self

class EntitlementTermInfo(BaseModel):
    """
    EntitlementTermInfo
    """ # noqa: E501
    dimension_quantity_decimal_parts: Optional[Dict[str, Union[StrictFloat, StrictInt]]] = Field(default=None, description="The decimal part of the dimension quantity, in format of <dimensionKey, decimalPart> It is used to save the decimal part of the dimension quantity for AWS Marketplace only. Because AWS Marketplace only accepts integer for dimension quantity. If the dimension quantity is a decimal number, we need to save the decimal part for future use.", alias="dimensionQuantityDecimalParts")
    is_commit_divided: Optional[StrictBool] = Field(default=None, description="Whether the commit is divided into multiple sub entitlement terms. If true, it has subEntitlementTermIds.", alias="isCommitDivided")
    parent_entitlement_term_id: Optional[StrictStr] = Field(default=None, description="The partner's entitlement term ID. It stands for the partner's entitlement term. Applicable to the sub entitlement term only.", alias="parentEntitlementTermId")
    sub_entitlement_term_ids: Optional[List[StrictStr]] = Field(default=None, description="All sub entitlement terms id of this entitlement term if it is commit divided.", alias="subEntitlementTermIds")
    type: Optional[EntitlementTermType] = None
    __properties: ClassVar[List[str]] = ["dimensionQuantityDecimalParts", "isCommitDivided", "parentEntitlementTermId", "subEntitlementTermIds", "type"]

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
        """Create an instance of EntitlementTermInfo from a JSON string"""
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
        """Create an instance of EntitlementTermInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "dimensionQuantityDecimalParts": obj.get("dimensionQuantityDecimalParts"),
            "isCommitDivided": obj.get("isCommitDivided"),
            "parentEntitlementTermId": obj.get("parentEntitlementTermId"),
            "subEntitlementTermIds": obj.get("subEntitlementTermIds"),
            "type": obj.get("type")
        })
        return _obj


