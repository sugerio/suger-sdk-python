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
from suger_sdk_python.models.database_sql_null_time import DatabaseSqlNullTime
from typing import Optional, Set
from typing_extensions import Self

class GithubComSugerioMarketplaceServiceRdsDbLibBillingAwsBillingEvent(BaseModel):
    """
    GithubComSugerioMarketplaceServiceRdsDbLibBillingAwsBillingEvent
    """ # noqa: E501
    action: Optional[StrictStr] = None
    agreement_id: Optional[StrictStr] = Field(default=None, alias="agreementID")
    amount: Optional[Union[StrictFloat, StrictInt]] = None
    balance_impacting: Optional[StrictInt] = Field(default=None, alias="balanceImpacting")
    bank_trace_id: Optional[StrictStr] = Field(default=None, alias="bankTraceID")
    billing_address_id: Optional[StrictStr] = Field(default=None, alias="billingAddressID")
    broker_id: Optional[StrictStr] = Field(default=None, alias="brokerID")
    buyer_id: Optional[StrictStr] = Field(default=None, alias="buyerID")
    currency: Optional[StrictStr] = None
    data_feed_product_id: Optional[StrictStr] = Field(default=None, alias="dataFeedProductID")
    disbursement_billing_event_id: Optional[StrictStr] = Field(default=None, alias="disbursementBillingEventID")
    end_user_account_id: Optional[StrictStr] = Field(default=None, alias="endUserAccountID")
    entitlement_id: Optional[StrictStr] = Field(default=None, alias="entitlementID")
    from_account_id: Optional[StrictStr] = Field(default=None, alias="fromAccountID")
    id: Optional[StrictStr] = None
    insert_date: Optional[DatabaseSqlNullTime] = Field(default=None, alias="insertDate")
    invoice_date: Optional[DatabaseSqlNullTime] = Field(default=None, alias="invoiceDate")
    invoice_id: Optional[StrictStr] = Field(default=None, alias="invoiceID")
    offer_id: Optional[StrictStr] = Field(default=None, alias="offerID")
    organization_id: Optional[StrictStr] = Field(default=None, alias="organizationID")
    parent_billing_event_id: Optional[StrictStr] = Field(default=None, alias="parentBillingEventID")
    payment_due_date: Optional[DatabaseSqlNullTime] = Field(default=None, alias="paymentDueDate")
    product_id: Optional[StrictStr] = Field(default=None, alias="productID")
    to_account_id: Optional[StrictStr] = Field(default=None, alias="toAccountID")
    transaction_reference_id: Optional[StrictStr] = Field(default=None, alias="transactionReferenceID")
    transaction_type: Optional[StrictStr] = Field(default=None, alias="transactionType")
    usage_period_end_date: Optional[DatabaseSqlNullTime] = Field(default=None, alias="usagePeriodEndDate")
    usage_period_start_date: Optional[DatabaseSqlNullTime] = Field(default=None, alias="usagePeriodStartDate")
    __properties: ClassVar[List[str]] = ["action", "agreementID", "amount", "balanceImpacting", "bankTraceID", "billingAddressID", "brokerID", "buyerID", "currency", "dataFeedProductID", "disbursementBillingEventID", "endUserAccountID", "entitlementID", "fromAccountID", "id", "insertDate", "invoiceDate", "invoiceID", "offerID", "organizationID", "parentBillingEventID", "paymentDueDate", "productID", "toAccountID", "transactionReferenceID", "transactionType", "usagePeriodEndDate", "usagePeriodStartDate"]

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
        """Create an instance of GithubComSugerioMarketplaceServiceRdsDbLibBillingAwsBillingEvent from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of insert_date
        if self.insert_date:
            _dict['insertDate'] = self.insert_date.to_dict()
        # override the default output from pydantic by calling `to_dict()` of invoice_date
        if self.invoice_date:
            _dict['invoiceDate'] = self.invoice_date.to_dict()
        # override the default output from pydantic by calling `to_dict()` of payment_due_date
        if self.payment_due_date:
            _dict['paymentDueDate'] = self.payment_due_date.to_dict()
        # override the default output from pydantic by calling `to_dict()` of usage_period_end_date
        if self.usage_period_end_date:
            _dict['usagePeriodEndDate'] = self.usage_period_end_date.to_dict()
        # override the default output from pydantic by calling `to_dict()` of usage_period_start_date
        if self.usage_period_start_date:
            _dict['usagePeriodStartDate'] = self.usage_period_start_date.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GithubComSugerioMarketplaceServiceRdsDbLibBillingAwsBillingEvent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "action": obj.get("action"),
            "agreementID": obj.get("agreementID"),
            "amount": obj.get("amount"),
            "balanceImpacting": obj.get("balanceImpacting"),
            "bankTraceID": obj.get("bankTraceID"),
            "billingAddressID": obj.get("billingAddressID"),
            "brokerID": obj.get("brokerID"),
            "buyerID": obj.get("buyerID"),
            "currency": obj.get("currency"),
            "dataFeedProductID": obj.get("dataFeedProductID"),
            "disbursementBillingEventID": obj.get("disbursementBillingEventID"),
            "endUserAccountID": obj.get("endUserAccountID"),
            "entitlementID": obj.get("entitlementID"),
            "fromAccountID": obj.get("fromAccountID"),
            "id": obj.get("id"),
            "insertDate": DatabaseSqlNullTime.from_dict(obj["insertDate"]) if obj.get("insertDate") is not None else None,
            "invoiceDate": DatabaseSqlNullTime.from_dict(obj["invoiceDate"]) if obj.get("invoiceDate") is not None else None,
            "invoiceID": obj.get("invoiceID"),
            "offerID": obj.get("offerID"),
            "organizationID": obj.get("organizationID"),
            "parentBillingEventID": obj.get("parentBillingEventID"),
            "paymentDueDate": DatabaseSqlNullTime.from_dict(obj["paymentDueDate"]) if obj.get("paymentDueDate") is not None else None,
            "productID": obj.get("productID"),
            "toAccountID": obj.get("toAccountID"),
            "transactionReferenceID": obj.get("transactionReferenceID"),
            "transactionType": obj.get("transactionType"),
            "usagePeriodEndDate": DatabaseSqlNullTime.from_dict(obj["usagePeriodEndDate"]) if obj.get("usagePeriodEndDate") is not None else None,
            "usagePeriodStartDate": DatabaseSqlNullTime.from_dict(obj["usagePeriodStartDate"]) if obj.get("usagePeriodStartDate") is not None else None
        })
        return _obj


