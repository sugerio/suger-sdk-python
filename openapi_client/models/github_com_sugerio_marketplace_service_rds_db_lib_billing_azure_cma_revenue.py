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


from typing import Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr
from openapi_client.models.sql_null_time import SqlNullTime


class GithubComSugerioMarketplaceServiceRdsDbLibBillingAzureCmaRevenue(BaseModel):
    """
    GithubComSugerioMarketplaceServiceRdsDbLibBillingAzureCmaRevenue
    """

    azure_asset_id: Optional[StrictStr] = Field(None, alias="azureAssetID")
    azure_billing_account_id: Optional[StrictStr] = Field(
        None, alias="azureBillingAccountID"
    )
    azure_customer_id: Optional[StrictStr] = Field(None, alias="azureCustomerID")
    azure_offer_id: Optional[StrictStr] = Field(None, alias="azureOfferID")
    azure_plan_id: Optional[StrictStr] = Field(None, alias="azurePlanID")
    billing_model: Optional[StrictStr] = Field(None, alias="billingModel")
    buyer_id: Optional[StrictStr] = Field(None, alias="buyerID")
    earning_usd: Optional[Union[StrictFloat, StrictInt]] = Field(
        None, alias="earningUsd"
    )
    entitlement_id: Optional[StrictStr] = Field(None, alias="entitlementID")
    estimated_payout_month: Optional[SqlNullTime] = Field(
        None, alias="estimatedPayoutMonth"
    )
    offer_id: Optional[StrictStr] = Field(None, alias="offerID")
    organization_id: Optional[StrictStr] = Field(None, alias="organizationID")
    payment_sent_date: Optional[SqlNullTime] = Field(None, alias="paymentSentDate")
    payout_status: Optional[StrictStr] = Field(None, alias="payoutStatus")
    product_id: Optional[StrictStr] = Field(None, alias="productID")
    purchase_record_id: Optional[StrictStr] = Field(None, alias="purchaseRecordID")
    revenue_usd: Optional[Union[StrictFloat, StrictInt]] = Field(
        None, alias="revenueUsd"
    )
    term_end_date: Optional[StrictStr] = Field(None, alias="termEndDate")
    term_start_date: Optional[StrictStr] = Field(None, alias="termStartDate")
    __properties = [
        "azureAssetID",
        "azureBillingAccountID",
        "azureCustomerID",
        "azureOfferID",
        "azurePlanID",
        "billingModel",
        "buyerID",
        "earningUsd",
        "entitlementID",
        "estimatedPayoutMonth",
        "offerID",
        "organizationID",
        "paymentSentDate",
        "payoutStatus",
        "productID",
        "purchaseRecordID",
        "revenueUsd",
        "termEndDate",
        "termStartDate",
    ]

    class Config:
        """Pydantic configuration"""

        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(
        cls, json_str: str
    ) -> GithubComSugerioMarketplaceServiceRdsDbLibBillingAzureCmaRevenue:
        """Create an instance of GithubComSugerioMarketplaceServiceRdsDbLibBillingAzureCmaRevenue from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of estimated_payout_month
        if self.estimated_payout_month:
            _dict["estimatedPayoutMonth"] = self.estimated_payout_month.to_dict()
        # override the default output from pydantic by calling `to_dict()` of payment_sent_date
        if self.payment_sent_date:
            _dict["paymentSentDate"] = self.payment_sent_date.to_dict()
        return _dict

    @classmethod
    def from_dict(
        cls, obj: dict
    ) -> GithubComSugerioMarketplaceServiceRdsDbLibBillingAzureCmaRevenue:
        """Create an instance of GithubComSugerioMarketplaceServiceRdsDbLibBillingAzureCmaRevenue from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GithubComSugerioMarketplaceServiceRdsDbLibBillingAzureCmaRevenue.parse_obj(
                obj
            )

        _obj = (
            GithubComSugerioMarketplaceServiceRdsDbLibBillingAzureCmaRevenue.parse_obj(
                {
                    "azure_asset_id": obj.get("azureAssetID"),
                    "azure_billing_account_id": obj.get("azureBillingAccountID"),
                    "azure_customer_id": obj.get("azureCustomerID"),
                    "azure_offer_id": obj.get("azureOfferID"),
                    "azure_plan_id": obj.get("azurePlanID"),
                    "billing_model": obj.get("billingModel"),
                    "buyer_id": obj.get("buyerID"),
                    "earning_usd": obj.get("earningUsd"),
                    "entitlement_id": obj.get("entitlementID"),
                    "estimated_payout_month": SqlNullTime.from_dict(
                        obj.get("estimatedPayoutMonth")
                    )
                    if obj.get("estimatedPayoutMonth") is not None
                    else None,
                    "offer_id": obj.get("offerID"),
                    "organization_id": obj.get("organizationID"),
                    "payment_sent_date": SqlNullTime.from_dict(
                        obj.get("paymentSentDate")
                    )
                    if obj.get("paymentSentDate") is not None
                    else None,
                    "payout_status": obj.get("payoutStatus"),
                    "product_id": obj.get("productID"),
                    "purchase_record_id": obj.get("purchaseRecordID"),
                    "revenue_usd": obj.get("revenueUsd"),
                    "term_end_date": obj.get("termEndDate"),
                    "term_start_date": obj.get("termStartDate"),
                }
            )
        )
        return _obj
