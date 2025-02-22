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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from suger_sdk_python.models.stripe_refund_destination_details_card import StripeRefundDestinationDetailsCard
from suger_sdk_python.models.stripe_refund_destination_details_us_bank_transfer import StripeRefundDestinationDetailsUSBankTransfer
from typing import Optional, Set
from typing_extensions import Self

class StripeRefundDestinationDetails(BaseModel):
    """
    StripeRefundDestinationDetails
    """ # noqa: E501
    card: Optional[StripeRefundDestinationDetailsCard] = None
    type: Optional[StrictStr] = Field(default=None, description="The type of transaction-specific details of the payment method used in the refund (e.g., `card`). An additional hash is included on `destination_details` with a name matching this value. It contains information specific to the refund transaction.")
    us_bank_transfer: Optional[StripeRefundDestinationDetailsUSBankTransfer] = None
    __properties: ClassVar[List[str]] = ["card", "type", "us_bank_transfer"]

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
        """Create an instance of StripeRefundDestinationDetails from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of card
        if self.card:
            _dict['card'] = self.card.to_dict()
        # override the default output from pydantic by calling `to_dict()` of us_bank_transfer
        if self.us_bank_transfer:
            _dict['us_bank_transfer'] = self.us_bank_transfer.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of StripeRefundDestinationDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "card": StripeRefundDestinationDetailsCard.from_dict(obj["card"]) if obj.get("card") is not None else None,
            "type": obj.get("type"),
            "us_bank_transfer": StripeRefundDestinationDetailsUSBankTransfer.from_dict(obj["us_bank_transfer"]) if obj.get("us_bank_transfer") is not None else None
        })
        return _obj


