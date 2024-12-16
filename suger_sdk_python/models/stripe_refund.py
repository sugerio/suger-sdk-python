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
from suger_sdk_python.models.stripe_refund_destination_details import StripeRefundDestinationDetails
from suger_sdk_python.models.stripe_refund_status import StripeRefundStatus
from typing import Optional, Set
from typing_extensions import Self

class StripeRefund(BaseModel):
    """
    StripeRefund
    """ # noqa: E501
    charge_id: Optional[StrictStr] = Field(default=None, description="ID of the charge that's refunded.", alias="chargeId")
    estination_details: Optional[StripeRefundDestinationDetails] = Field(default=None, description="Transaction-specific details for the refund.", alias="estinationDetails")
    failure_balance_transaction_id: Optional[StrictStr] = Field(default=None, description="After the refund fails, this balance transaction describes the adjustment made on your account balance that reverses the initial balance transaction.", alias="failureBalanceTransactionId")
    failure_reason: Optional[StrictStr] = Field(default=None, description="Provides the reason for the refund failure. Possible values are: `lost_or_stolen_card`, `expired_or_canceled_card`, `charge_for_pending_refund_disputed`, `insufficient_funds`, `declined`, `merchant_request`, or `unknown`.", alias="failureReason")
    id: Optional[StrictStr] = None
    payment_intent_id: Optional[StrictStr] = Field(default=None, description="ID of the PaymentIntent that's refunded.", alias="paymentIntentId")
    status: Optional[StripeRefundStatus] = Field(default=None, description="Status of the refund. This can be `pending`, `requires_action`, `succeeded`, `failed`, or `canceled`. Learn more about [failed refunds](https://stripe.com/docs/refunds#failed-refunds).")
    __properties: ClassVar[List[str]] = ["chargeId", "estinationDetails", "failureBalanceTransactionId", "failureReason", "id", "paymentIntentId", "status"]

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
        """Create an instance of StripeRefund from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of estination_details
        if self.estination_details:
            _dict['estinationDetails'] = self.estination_details.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of StripeRefund from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "chargeId": obj.get("chargeId"),
            "estinationDetails": StripeRefundDestinationDetails.from_dict(obj["estinationDetails"]) if obj.get("estinationDetails") is not None else None,
            "failureBalanceTransactionId": obj.get("failureBalanceTransactionId"),
            "failureReason": obj.get("failureReason"),
            "id": obj.get("id"),
            "paymentIntentId": obj.get("paymentIntentId"),
            "status": obj.get("status")
        })
        return _obj

