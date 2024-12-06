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
from suger_sdk_python.models.stripe_balance_transaction_fee_detail import StripeBalanceTransactionFeeDetail
from typing import Optional, Set
from typing_extensions import Self

class StripeBalanceTransaction(BaseModel):
    """
    StripeBalanceTransaction
    """ # noqa: E501
    amount: Optional[StrictInt] = Field(default=None, description="Gross amount of this transaction (in cents (or local equivalent)). A positive value represents funds charged to another party, and a negative value represents funds sent to another party.")
    available_on: Optional[StrictInt] = Field(default=None, description="The date that the transaction's net funds become available in the Stripe balance.")
    charge_id: Optional[StrictStr] = Field(default=None, description="ID of the charge which the balance transaction comes from.", alias="chargeId")
    created: Optional[StrictInt] = Field(default=None, description="Time at which the object was created. Measured in seconds since the Unix epoch.")
    description: Optional[StrictStr] = Field(default=None, description="An arbitrary string attached to the object. Often useful for displaying to users.")
    exchange_rate: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="If applicable, this transaction uses an exchange rate. If money converts from currency A to currency B, then the `amount` in currency A, multipled by the `exchange_rate`, equals the `amount` in currency B. For example, if you charge a customer 10.00 EUR, the PaymentIntent's `amount` is `1000` and `currency` is `eur`. If this converts to 12.34 USD in your Stripe account, the BalanceTransaction's `amount` is `1234`, its `currency` is `usd`, and the `exchange_rate` is `1.234`.")
    fee: Optional[StrictInt] = Field(default=None, description="Fees (in cents (or local equivalent)) paid for this transaction. Represented as a positive integer when assessed.")
    fee_details: Optional[List[StripeBalanceTransactionFeeDetail]] = Field(default=None, description="Detailed breakdown of fees (in cents (or local equivalent)) paid for this transaction.")
    id: Optional[StrictStr] = Field(default=None, description="Unique identifier for the object.")
    net: Optional[StrictInt] = Field(default=None, description="Net impact to a Stripe balance (in cents (or local equivalent)). A positive value represents incrementing a Stripe balance, and a negative value decrementing a Stripe balance. You can calculate the net impact of a transaction on a balance by `amount` - `fee`")
    status: Optional[StrictStr] = Field(default=None, description="The transaction's net funds status in the Stripe balance, which are either `available` or `pending`.")
    type: Optional[StrictStr] = Field(default=None, description="Transaction type: `adjustment`, `advance`, `advance_funding`, `anticipation_repayment`, `application_fee`, `application_fee_refund`, `charge`, `climate_order_purchase`, `climate_order_refund`, `connect_collection_transfer`, `contribution`, `issuing_authorization_hold`, `issuing_authorization_release`, `issuing_dispute`, `issuing_transaction`, `obligation_outbound`, `obligation_reversal_inbound`, `payment`, `payment_failure_refund`, `payment_network_reserve_hold`, `payment_network_reserve_release`, `payment_refund`, `payment_reversal`, `payment_unreconciled`, `payout`, `payout_cancel`, `payout_failure`, `refund`, `refund_failure`, `reserve_transaction`, `reserved_funds`, `stripe_fee`, `stripe_fx_fee`, `tax_fee`, `topup`, `topup_reversal`, `transfer`, `transfer_cancel`, `transfer_failure`, or `transfer_refund`. Learn more about [balance transaction types and what they represent](https://stripe.com/docs/reports/balance-transaction-types). To classify transactions for accounting purposes, consider `reporting_category` instead.")
    __properties: ClassVar[List[str]] = ["amount", "available_on", "chargeId", "created", "description", "exchange_rate", "fee", "fee_details", "id", "net", "status", "type"]

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
        """Create an instance of StripeBalanceTransaction from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in fee_details (list)
        _items = []
        if self.fee_details:
            for _item_fee_details in self.fee_details:
                if _item_fee_details:
                    _items.append(_item_fee_details.to_dict())
            _dict['fee_details'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of StripeBalanceTransaction from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "amount": obj.get("amount"),
            "available_on": obj.get("available_on"),
            "chargeId": obj.get("chargeId"),
            "created": obj.get("created"),
            "description": obj.get("description"),
            "exchange_rate": obj.get("exchange_rate"),
            "fee": obj.get("fee"),
            "fee_details": [StripeBalanceTransactionFeeDetail.from_dict(_item) for _item in obj["fee_details"]] if obj.get("fee_details") is not None else None,
            "id": obj.get("id"),
            "net": obj.get("net"),
            "status": obj.get("status"),
            "type": obj.get("type")
        })
        return _obj


