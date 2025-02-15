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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class PaymentInstallment(BaseModel):
    """
    PaymentInstallment
    """ # noqa: E501
    amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The amount the buyer has paid for this installment. If there is a discount off the original price, the amount is the discounted price.")
    charge_on: Optional[datetime] = Field(default=None, description="When the buyer will be charged for this installment. If it is null, the buyer will be charged on the effective date of the entitlement.", alias="chargeOn")
    charge_on_str: Optional[StrictStr] = Field(default=None, description="The charge on date in string format. It is used for front-end display only.", alias="chargeOnStr")
    credit: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Used in GCP Marketplace private offer as one-time credit. Default as zero if there is no credit.")
    discount_percentage: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The discount percentage off the original price. For GCP Marketplace, it can be discount off the commitment amount or discount off the usage price. The value is between 0 to 100. For example, 20 means 20% off. Default as zero if there is no discount.", alias="discountPercentage")
    original_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The original amount before discount if there is a discount off the original price. nil if there is no discount.", alias="originalAmount")
    __properties: ClassVar[List[str]] = ["amount", "chargeOn", "chargeOnStr", "credit", "discountPercentage", "originalAmount"]

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
        """Create an instance of PaymentInstallment from a JSON string"""
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
        """Create an instance of PaymentInstallment from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "amount": obj.get("amount"),
            "chargeOn": obj.get("chargeOn"),
            "chargeOnStr": obj.get("chargeOnStr"),
            "credit": obj.get("credit"),
            "discountPercentage": obj.get("discountPercentage"),
            "originalAmount": obj.get("originalAmount")
        })
        return _obj


