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
from suger_sdk_python.models.adyen_buyer import AdyenBuyer
from suger_sdk_python.models.aws_account_identifier import AwsAccountIdentifier
from suger_sdk_python.models.azure_ad_identifier import AzureADIdentifier
from suger_sdk_python.models.company_info import CompanyInfo
from suger_sdk_python.models.gcp_marketplace_user_account import GcpMarketplaceUserAccount
from suger_sdk_python.models.payment_config import PaymentConfig
from suger_sdk_python.models.stripe_customer import StripeCustomer
from typing import Optional, Set
from typing_extensions import Self

class BuyerInfo(BaseModel):
    """
    BuyerInfo
    """ # noqa: E501
    adyen_buyer: Optional[AdyenBuyer] = Field(default=None, description="Buyer on Adyen", alias="adyenBuyer")
    aws_buyer: Optional[AwsAccountIdentifier] = Field(default=None, description="Buyer from AWS Marketplace", alias="awsBuyer")
    azure_buyer: Optional[AzureADIdentifier] = Field(default=None, description="Buyer from Azure Marketplace", alias="azureBuyer")
    collectable_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The amount that the seller can collect. It excludes the marketplace commision fee.", alias="collectableAmount")
    company_info: Optional[CompanyInfo] = Field(default=None, alias="companyInfo")
    customer_id: Optional[StrictStr] = Field(default=None, description="customerID of buyer on seller's side", alias="customerId")
    disbursed_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The amount that has been disbursed to the seller account.", alias="disbursedAmount")
    email_address: Optional[StrictStr] = Field(default=None, description="The email address of the buyer. This was copied from the new client signup form.", alias="emailAddress")
    fields: Optional[Dict[str, Any]] = Field(default=None, description="Fields to store key-value pairs of buyer information.")
    gcp_buyer: Optional[GcpMarketplaceUserAccount] = Field(default=None, description="Buyer from GCP Marketplace", alias="gcpBuyer")
    gross_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The gross amount that the buyer has committed to pay, including usage metered amount.", alias="grossAmount")
    invoiced_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The amount that the buyer has got invoiced.", alias="invoicedAmount")
    lago_customer_id: Optional[StrictStr] = Field(default=None, description="The lgo customer ID for the buyer if it is connected to a lago customer.", alias="lagoCustomerId")
    last_modified_by: Optional[StrictStr] = Field(default=None, description="Last modifier user ID.", alias="lastModifiedBy")
    metronome_customer_id: Optional[StrictStr] = Field(default=None, description="The metronome customer ID for the buyer if it is connected to a metronome customer.", alias="metronomeCustomerId")
    orb_customer_id: Optional[StrictStr] = Field(default=None, description="The orb customer ID for the buyer if it is connected to a orb customer.", alias="orbCustomerId")
    payment_config: Optional[PaymentConfig] = Field(default=None, description="Payment Config for billing.", alias="paymentConfig")
    spa_url: Optional[StrictStr] = Field(default=None, description="Buyer SPA url, public page visited with jwt.", alias="spaUrl")
    stripe_buyer: Optional[StripeCustomer] = Field(default=None, description="Buyer as Customer on Stripe", alias="stripeBuyer")
    __properties: ClassVar[List[str]] = ["adyenBuyer", "awsBuyer", "azureBuyer", "collectableAmount", "companyInfo", "customerId", "disbursedAmount", "emailAddress", "fields", "gcpBuyer", "grossAmount", "invoicedAmount", "lagoCustomerId", "lastModifiedBy", "metronomeCustomerId", "orbCustomerId", "paymentConfig", "spaUrl", "stripeBuyer"]

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
        """Create an instance of BuyerInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of adyen_buyer
        if self.adyen_buyer:
            _dict['adyenBuyer'] = self.adyen_buyer.to_dict()
        # override the default output from pydantic by calling `to_dict()` of aws_buyer
        if self.aws_buyer:
            _dict['awsBuyer'] = self.aws_buyer.to_dict()
        # override the default output from pydantic by calling `to_dict()` of azure_buyer
        if self.azure_buyer:
            _dict['azureBuyer'] = self.azure_buyer.to_dict()
        # override the default output from pydantic by calling `to_dict()` of company_info
        if self.company_info:
            _dict['companyInfo'] = self.company_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of gcp_buyer
        if self.gcp_buyer:
            _dict['gcpBuyer'] = self.gcp_buyer.to_dict()
        # override the default output from pydantic by calling `to_dict()` of payment_config
        if self.payment_config:
            _dict['paymentConfig'] = self.payment_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of stripe_buyer
        if self.stripe_buyer:
            _dict['stripeBuyer'] = self.stripe_buyer.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BuyerInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "adyenBuyer": AdyenBuyer.from_dict(obj["adyenBuyer"]) if obj.get("adyenBuyer") is not None else None,
            "awsBuyer": AwsAccountIdentifier.from_dict(obj["awsBuyer"]) if obj.get("awsBuyer") is not None else None,
            "azureBuyer": AzureADIdentifier.from_dict(obj["azureBuyer"]) if obj.get("azureBuyer") is not None else None,
            "collectableAmount": obj.get("collectableAmount"),
            "companyInfo": CompanyInfo.from_dict(obj["companyInfo"]) if obj.get("companyInfo") is not None else None,
            "customerId": obj.get("customerId"),
            "disbursedAmount": obj.get("disbursedAmount"),
            "emailAddress": obj.get("emailAddress"),
            "fields": obj.get("fields"),
            "gcpBuyer": GcpMarketplaceUserAccount.from_dict(obj["gcpBuyer"]) if obj.get("gcpBuyer") is not None else None,
            "grossAmount": obj.get("grossAmount"),
            "invoicedAmount": obj.get("invoicedAmount"),
            "lagoCustomerId": obj.get("lagoCustomerId"),
            "lastModifiedBy": obj.get("lastModifiedBy"),
            "metronomeCustomerId": obj.get("metronomeCustomerId"),
            "orbCustomerId": obj.get("orbCustomerId"),
            "paymentConfig": PaymentConfig.from_dict(obj["paymentConfig"]) if obj.get("paymentConfig") is not None else None,
            "spaUrl": obj.get("spaUrl"),
            "stripeBuyer": StripeCustomer.from_dict(obj["stripeBuyer"]) if obj.get("stripeBuyer") is not None else None
        })
        return _obj


