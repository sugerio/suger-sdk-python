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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from suger_sdk_python.models.stripe_payment_method_bacs_debit import StripePaymentMethodBACSDebit
from suger_sdk_python.models.stripe_payment_method_card import StripePaymentMethodCard
from suger_sdk_python.models.stripe_payment_method_sepa_debit import StripePaymentMethodSEPADebit
from suger_sdk_python.models.stripe_payment_method_us_bank_account import StripePaymentMethodUSBankAccount
from typing import Optional, Set
from typing_extensions import Self

class StripePaymentMethod(BaseModel):
    """
    StripePaymentMethod
    """ # noqa: E501
    bacs_debit: Optional[StripePaymentMethodBACSDebit] = None
    card: Optional[StripePaymentMethodCard] = None
    created: Optional[StrictInt] = Field(default=None, description="Time at which the object was created. Measured in seconds since the Unix epoch.")
    id: Optional[StrictStr] = Field(default=None, description="Unique identifier for the payment method on stripe.")
    livemode: Optional[StrictBool] = Field(default=None, description="Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.")
    object: Optional[StrictStr] = Field(default=None, description="String representing the object’s type. Always has the value `payment_method`.")
    sepa_debit: Optional[StripePaymentMethodSEPADebit] = None
    us_bank_account: Optional[StripePaymentMethodUSBankAccount] = None
    __properties: ClassVar[List[str]] = ["bacs_debit", "card", "created", "id", "livemode", "object", "sepa_debit", "us_bank_account"]

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
        """Create an instance of StripePaymentMethod from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of bacs_debit
        if self.bacs_debit:
            _dict['bacs_debit'] = self.bacs_debit.to_dict()
        # override the default output from pydantic by calling `to_dict()` of card
        if self.card:
            _dict['card'] = self.card.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sepa_debit
        if self.sepa_debit:
            _dict['sepa_debit'] = self.sepa_debit.to_dict()
        # override the default output from pydantic by calling `to_dict()` of us_bank_account
        if self.us_bank_account:
            _dict['us_bank_account'] = self.us_bank_account.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of StripePaymentMethod from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "bacs_debit": StripePaymentMethodBACSDebit.from_dict(obj["bacs_debit"]) if obj.get("bacs_debit") is not None else None,
            "card": StripePaymentMethodCard.from_dict(obj["card"]) if obj.get("card") is not None else None,
            "created": obj.get("created"),
            "id": obj.get("id"),
            "livemode": obj.get("livemode"),
            "object": obj.get("object"),
            "sepa_debit": StripePaymentMethodSEPADebit.from_dict(obj["sepa_debit"]) if obj.get("sepa_debit") is not None else None,
            "us_bank_account": StripePaymentMethodUSBankAccount.from_dict(obj["us_bank_account"]) if obj.get("us_bank_account") is not None else None
        })
        return _obj


