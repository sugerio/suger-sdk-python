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

class GithubComSugerioMarketplaceServicePkgLegacyRdsDbLibBillingAzureCmaRevenue(BaseModel):
    """
    GithubComSugerioMarketplaceServicePkgLegacyRdsDbLibBillingAzureCmaRevenue
    """ # noqa: E501
    azure_asset_id: Optional[StrictStr] = Field(default=None, alias="azureAssetID")
    azure_billing_account_id: Optional[StrictStr] = Field(default=None, alias="azureBillingAccountID")
    azure_customer_id: Optional[StrictStr] = Field(default=None, alias="azureCustomerID")
    azure_offer_id: Optional[StrictStr] = Field(default=None, alias="azureOfferID")
    azure_plan_id: Optional[StrictStr] = Field(default=None, alias="azurePlanID")
    billing_model: Optional[StrictStr] = Field(default=None, alias="billingModel")
    buyer_id: Optional[StrictStr] = Field(default=None, alias="buyerID")
    earning_usd: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="earningUsd")
    entitlement_id: Optional[StrictStr] = Field(default=None, alias="entitlementID")
    estimated_payout_month: Optional[DatabaseSqlNullTime] = Field(default=None, alias="estimatedPayoutMonth")
    offer_id: Optional[StrictStr] = Field(default=None, alias="offerID")
    organization_id: Optional[StrictStr] = Field(default=None, alias="organizationID")
    payment_sent_date: Optional[DatabaseSqlNullTime] = Field(default=None, alias="paymentSentDate")
    payout_status: Optional[StrictStr] = Field(default=None, alias="payoutStatus")
    product_id: Optional[StrictStr] = Field(default=None, alias="productID")
    purchase_record_id: Optional[StrictStr] = Field(default=None, alias="purchaseRecordID")
    revenue_usd: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="revenueUsd")
    term_end_date: Optional[StrictStr] = Field(default=None, alias="termEndDate")
    term_start_date: Optional[StrictStr] = Field(default=None, alias="termStartDate")
    __properties: ClassVar[List[str]] = ["azureAssetID", "azureBillingAccountID", "azureCustomerID", "azureOfferID", "azurePlanID", "billingModel", "buyerID", "earningUsd", "entitlementID", "estimatedPayoutMonth", "offerID", "organizationID", "paymentSentDate", "payoutStatus", "productID", "purchaseRecordID", "revenueUsd", "termEndDate", "termStartDate"]

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
        """Create an instance of GithubComSugerioMarketplaceServicePkgLegacyRdsDbLibBillingAzureCmaRevenue from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of estimated_payout_month
        if self.estimated_payout_month:
            _dict['estimatedPayoutMonth'] = self.estimated_payout_month.to_dict()
        # override the default output from pydantic by calling `to_dict()` of payment_sent_date
        if self.payment_sent_date:
            _dict['paymentSentDate'] = self.payment_sent_date.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GithubComSugerioMarketplaceServicePkgLegacyRdsDbLibBillingAzureCmaRevenue from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "azureAssetID": obj.get("azureAssetID"),
            "azureBillingAccountID": obj.get("azureBillingAccountID"),
            "azureCustomerID": obj.get("azureCustomerID"),
            "azureOfferID": obj.get("azureOfferID"),
            "azurePlanID": obj.get("azurePlanID"),
            "billingModel": obj.get("billingModel"),
            "buyerID": obj.get("buyerID"),
            "earningUsd": obj.get("earningUsd"),
            "entitlementID": obj.get("entitlementID"),
            "estimatedPayoutMonth": DatabaseSqlNullTime.from_dict(obj["estimatedPayoutMonth"]) if obj.get("estimatedPayoutMonth") is not None else None,
            "offerID": obj.get("offerID"),
            "organizationID": obj.get("organizationID"),
            "paymentSentDate": DatabaseSqlNullTime.from_dict(obj["paymentSentDate"]) if obj.get("paymentSentDate") is not None else None,
            "payoutStatus": obj.get("payoutStatus"),
            "productID": obj.get("productID"),
            "purchaseRecordID": obj.get("purchaseRecordID"),
            "revenueUsd": obj.get("revenueUsd"),
            "termEndDate": obj.get("termEndDate"),
            "termStartDate": obj.get("termStartDate")
        })
        return _obj


