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

from pydantic import BaseModel, ConfigDict, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Optional, Union
from suger_sdk_python.models.snowflake_marketplace_plan_installment import SnowflakeMarketplacePlanInstallment
from typing import Optional, Set
from typing_extensions import Self

class SnowflakeMarketplacePlanInstallmentSchedule(BaseModel):
    """
    SnowflakeMarketplacePlanInstallmentSchedule
    """ # noqa: E501
    default_installment_amount: Optional[Union[StrictFloat, StrictInt]] = None
    installment_duration: Optional[Union[StrictFloat, StrictInt]] = None
    overridden_installments: Optional[List[SnowflakeMarketplacePlanInstallment]] = None
    __properties: ClassVar[List[str]] = ["default_installment_amount", "installment_duration", "overridden_installments"]

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
        """Create an instance of SnowflakeMarketplacePlanInstallmentSchedule from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in overridden_installments (list)
        _items = []
        if self.overridden_installments:
            for _item_overridden_installments in self.overridden_installments:
                if _item_overridden_installments:
                    _items.append(_item_overridden_installments.to_dict())
            _dict['overridden_installments'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SnowflakeMarketplacePlanInstallmentSchedule from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "default_installment_amount": obj.get("default_installment_amount"),
            "installment_duration": obj.get("installment_duration"),
            "overridden_installments": [SnowflakeMarketplacePlanInstallment.from_dict(_item) for _item in obj["overridden_installments"]] if obj.get("overridden_installments") is not None else None
        })
        return _obj


