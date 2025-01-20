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
from suger_sdk_python.models.billable_dimension_price_model_detail import BillableDimensionPriceModelDetail
from suger_sdk_python.models.billable_dimension_usage_daily_revenue import BillableDimensionUsageDailyRevenue
from suger_sdk_python.models.billing_addon_record import BillingAddonRecord
from suger_sdk_python.models.billing_payment_installment_detail import BillingPaymentInstallmentDetail
from suger_sdk_python.models.commit_revenue_detail import CommitRevenueDetail
from suger_sdk_python.models.invoice_add_fixed_fee import InvoiceAddFixedFee
from suger_sdk_python.models.invoice_adjust_discount_by_dimension import InvoiceAdjustDiscountByDimension
from suger_sdk_python.models.invoice_adjust_minimum_spend_by_dimension import InvoiceAdjustMinimumSpendByDimension
from suger_sdk_python.models.invoice_adjust_overall_discount import InvoiceAdjustOverallDiscount
from suger_sdk_python.models.invoice_adjust_overall_minimum_spend import InvoiceAdjustOverallMinimumSpend
from typing import Optional, Set
from typing_extensions import Self

class BillingInvoiceInfo(BaseModel):
    """
    BillingInvoiceInfo
    """ # noqa: E501
    add_fixed_fees: Optional[List[InvoiceAddFixedFee]] = Field(default=None, description="Adjust charge fields The fixed fees to be added to the invoice.", alias="addFixedFees")
    addon_detail: Optional[BillingAddonRecord] = Field(default=None, alias="addonDetail")
    adjust_discount_by_dimensions: Optional[List[InvoiceAdjustDiscountByDimension]] = Field(default=None, description="add or adjust discount for a specific dimension", alias="adjustDiscountByDimensions")
    adjust_minimum_spend_by_dimensions: Optional[List[InvoiceAdjustMinimumSpendByDimension]] = Field(default=None, description="add or adjust minimum spend for a specific dimension", alias="adjustMinimumSpendByDimensions")
    adjust_overall_discount: Optional[InvoiceAdjustOverallDiscount] = Field(default=None, description="add or adjust overall discount calculate each dimension's discount first, then apply the overall discount", alias="adjustOverallDiscount")
    adjust_overall_minimum_spend: Optional[InvoiceAdjustOverallMinimumSpend] = Field(default=None, description="add or adjust overall minimum spend calculate each dimension's minimum spend first, then apply the overall minimum spend", alias="adjustOverallMinimumSpend")
    billable_dimension_details: Optional[List[BillableDimensionPriceModelDetail]] = Field(default=None, alias="billableDimensionDetails")
    commits_revenue_details: Optional[List[CommitRevenueDetail]] = Field(default=None, description="Recurring flat fee for the invoice. There should be only one type fee for each invoice, commits, or usage.", alias="commitsRevenueDetails")
    creation_date: Optional[datetime] = Field(default=None, description="The creation date of the invoice when the status of the invoice may be draft or issued. It may be different from the issue date.", alias="creationDate")
    currency: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    due_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Due amount = SubtotalAmount + TaxAmount - AdjustOverallDiscount", alias="dueAmount")
    due_date: Optional[datetime] = Field(default=None, description="DueDate = IssueDate + NetTerm", alias="dueDate")
    grace_period_in_days: Optional[StrictInt] = Field(default=None, description="Grace Period in number of days", alias="gracePeriodInDays")
    issue_date: Optional[datetime] = Field(default=None, description="IssueDate, issue invoice automatically when CreationDate + GracePeriod, or issue invoice manually IssueDate >= CreationDate && IssueDate <= CreationDate + GracePeriod", alias="issueDate")
    memo: Optional[StrictStr] = None
    net_terms_in_days: Optional[StrictInt] = Field(default=None, description="Net Terms period in number of days", alias="netTermsInDays")
    payment_installments_detail: Optional[BillingPaymentInstallmentDetail] = Field(default=None, alias="paymentInstallmentsDetail")
    receipt_url: Optional[StrictStr] = Field(default=None, description="Invoice receipt url, it only exists when there are transactions.", alias="receiptUrl")
    spa_url: Optional[StrictStr] = Field(default=None, description="SPA url with JWT.", alias="spaUrl")
    subtotal_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Subtotal amount calculated from the user usage.", alias="subtotalAmount")
    tax_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="taxAmount")
    trial_period_in_days: Optional[StrictInt] = Field(default=None, description="Trial period in number of days", alias="trialPeriodInDays")
    usage_daily_revenues: Optional[List[BillableDimensionUsageDailyRevenue]] = Field(default=None, description="Billable dimension fees for the invoice.", alias="usageDailyRevenues")
    __properties: ClassVar[List[str]] = ["addFixedFees", "addonDetail", "adjustDiscountByDimensions", "adjustMinimumSpendByDimensions", "adjustOverallDiscount", "adjustOverallMinimumSpend", "billableDimensionDetails", "commitsRevenueDetails", "creationDate", "currency", "description", "dueAmount", "dueDate", "gracePeriodInDays", "issueDate", "memo", "netTermsInDays", "paymentInstallmentsDetail", "receiptUrl", "spaUrl", "subtotalAmount", "taxAmount", "trialPeriodInDays", "usageDailyRevenues"]

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
        """Create an instance of BillingInvoiceInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in add_fixed_fees (list)
        _items = []
        if self.add_fixed_fees:
            for _item_add_fixed_fees in self.add_fixed_fees:
                if _item_add_fixed_fees:
                    _items.append(_item_add_fixed_fees.to_dict())
            _dict['addFixedFees'] = _items
        # override the default output from pydantic by calling `to_dict()` of addon_detail
        if self.addon_detail:
            _dict['addonDetail'] = self.addon_detail.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in adjust_discount_by_dimensions (list)
        _items = []
        if self.adjust_discount_by_dimensions:
            for _item_adjust_discount_by_dimensions in self.adjust_discount_by_dimensions:
                if _item_adjust_discount_by_dimensions:
                    _items.append(_item_adjust_discount_by_dimensions.to_dict())
            _dict['adjustDiscountByDimensions'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in adjust_minimum_spend_by_dimensions (list)
        _items = []
        if self.adjust_minimum_spend_by_dimensions:
            for _item_adjust_minimum_spend_by_dimensions in self.adjust_minimum_spend_by_dimensions:
                if _item_adjust_minimum_spend_by_dimensions:
                    _items.append(_item_adjust_minimum_spend_by_dimensions.to_dict())
            _dict['adjustMinimumSpendByDimensions'] = _items
        # override the default output from pydantic by calling `to_dict()` of adjust_overall_discount
        if self.adjust_overall_discount:
            _dict['adjustOverallDiscount'] = self.adjust_overall_discount.to_dict()
        # override the default output from pydantic by calling `to_dict()` of adjust_overall_minimum_spend
        if self.adjust_overall_minimum_spend:
            _dict['adjustOverallMinimumSpend'] = self.adjust_overall_minimum_spend.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in billable_dimension_details (list)
        _items = []
        if self.billable_dimension_details:
            for _item_billable_dimension_details in self.billable_dimension_details:
                if _item_billable_dimension_details:
                    _items.append(_item_billable_dimension_details.to_dict())
            _dict['billableDimensionDetails'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in commits_revenue_details (list)
        _items = []
        if self.commits_revenue_details:
            for _item_commits_revenue_details in self.commits_revenue_details:
                if _item_commits_revenue_details:
                    _items.append(_item_commits_revenue_details.to_dict())
            _dict['commitsRevenueDetails'] = _items
        # override the default output from pydantic by calling `to_dict()` of payment_installments_detail
        if self.payment_installments_detail:
            _dict['paymentInstallmentsDetail'] = self.payment_installments_detail.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in usage_daily_revenues (list)
        _items = []
        if self.usage_daily_revenues:
            for _item_usage_daily_revenues in self.usage_daily_revenues:
                if _item_usage_daily_revenues:
                    _items.append(_item_usage_daily_revenues.to_dict())
            _dict['usageDailyRevenues'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BillingInvoiceInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "addFixedFees": [InvoiceAddFixedFee.from_dict(_item) for _item in obj["addFixedFees"]] if obj.get("addFixedFees") is not None else None,
            "addonDetail": BillingAddonRecord.from_dict(obj["addonDetail"]) if obj.get("addonDetail") is not None else None,
            "adjustDiscountByDimensions": [InvoiceAdjustDiscountByDimension.from_dict(_item) for _item in obj["adjustDiscountByDimensions"]] if obj.get("adjustDiscountByDimensions") is not None else None,
            "adjustMinimumSpendByDimensions": [InvoiceAdjustMinimumSpendByDimension.from_dict(_item) for _item in obj["adjustMinimumSpendByDimensions"]] if obj.get("adjustMinimumSpendByDimensions") is not None else None,
            "adjustOverallDiscount": InvoiceAdjustOverallDiscount.from_dict(obj["adjustOverallDiscount"]) if obj.get("adjustOverallDiscount") is not None else None,
            "adjustOverallMinimumSpend": InvoiceAdjustOverallMinimumSpend.from_dict(obj["adjustOverallMinimumSpend"]) if obj.get("adjustOverallMinimumSpend") is not None else None,
            "billableDimensionDetails": [BillableDimensionPriceModelDetail.from_dict(_item) for _item in obj["billableDimensionDetails"]] if obj.get("billableDimensionDetails") is not None else None,
            "commitsRevenueDetails": [CommitRevenueDetail.from_dict(_item) for _item in obj["commitsRevenueDetails"]] if obj.get("commitsRevenueDetails") is not None else None,
            "creationDate": obj.get("creationDate"),
            "currency": obj.get("currency"),
            "description": obj.get("description"),
            "dueAmount": obj.get("dueAmount"),
            "dueDate": obj.get("dueDate"),
            "gracePeriodInDays": obj.get("gracePeriodInDays"),
            "issueDate": obj.get("issueDate"),
            "memo": obj.get("memo"),
            "netTermsInDays": obj.get("netTermsInDays"),
            "paymentInstallmentsDetail": BillingPaymentInstallmentDetail.from_dict(obj["paymentInstallmentsDetail"]) if obj.get("paymentInstallmentsDetail") is not None else None,
            "receiptUrl": obj.get("receiptUrl"),
            "spaUrl": obj.get("spaUrl"),
            "subtotalAmount": obj.get("subtotalAmount"),
            "taxAmount": obj.get("taxAmount"),
            "trialPeriodInDays": obj.get("trialPeriodInDays"),
            "usageDailyRevenues": [BillableDimensionUsageDailyRevenue.from_dict(_item) for _item in obj["usageDailyRevenues"]] if obj.get("usageDailyRevenues") is not None else None
        })
        return _obj


