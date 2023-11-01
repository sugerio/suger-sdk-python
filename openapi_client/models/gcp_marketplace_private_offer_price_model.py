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


from typing import Optional
from pydantic import BaseModel, Field, StrictStr
from openapi_client.models.gcp_marketplace_private_offer_price_model_commitment import (
    GcpMarketplacePrivateOfferPriceModelCommitment,
)
from openapi_client.models.gcp_marketplace_private_offer_price_model_fixed import (
    GcpMarketplacePrivateOfferPriceModelFixed,
)
from openapi_client.models.gcp_marketplace_private_offer_price_model_overage import (
    GcpMarketplacePrivateOfferPriceModelOverage,
)
from openapi_client.models.gcp_marketplace_private_offer_price_model_payg import (
    GcpMarketplacePrivateOfferPriceModelPayg,
)
from openapi_client.models.gcp_price_value import GcpPriceValue


class GcpMarketplacePrivateOfferPriceModel(BaseModel):
    """
    GcpMarketplacePrivateOfferPriceModel
    """

    base_offer: Optional[StrictStr] = Field(
        None,
        alias="baseOffer",
        description='in format of "projects/{projectNumber}/services/service-name.endpoints.gcp-project-id.cloud.goog/standardOffers/base-offer-id"',
    )
    commitment: Optional[GcpMarketplacePrivateOfferPriceModelCommitment] = None
    fixed_price: Optional[GcpMarketplacePrivateOfferPriceModelFixed] = Field(
        None, alias="fixedPrice"
    )
    one_time_credit: Optional[GcpPriceValue] = Field(None, alias="oneTimeCredit")
    overage: Optional[GcpMarketplacePrivateOfferPriceModelOverage] = None
    payg: Optional[GcpMarketplacePrivateOfferPriceModelPayg] = None
    previous_credit_balance_policy: Optional[StrictStr] = Field(
        None,
        alias="previousCreditBalancePolicy",
        description='such as "PREVIOUS_CREDIT_BALANCE_POLICY_UNSPECIFIED"',
    )
    __properties = [
        "baseOffer",
        "commitment",
        "fixedPrice",
        "oneTimeCredit",
        "overage",
        "payg",
        "previousCreditBalancePolicy",
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
    def from_json(cls, json_str: str) -> GcpMarketplacePrivateOfferPriceModel:
        """Create an instance of GcpMarketplacePrivateOfferPriceModel from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of commitment
        if self.commitment:
            _dict["commitment"] = self.commitment.to_dict()
        # override the default output from pydantic by calling `to_dict()` of fixed_price
        if self.fixed_price:
            _dict["fixedPrice"] = self.fixed_price.to_dict()
        # override the default output from pydantic by calling `to_dict()` of one_time_credit
        if self.one_time_credit:
            _dict["oneTimeCredit"] = self.one_time_credit.to_dict()
        # override the default output from pydantic by calling `to_dict()` of overage
        if self.overage:
            _dict["overage"] = self.overage.to_dict()
        # override the default output from pydantic by calling `to_dict()` of payg
        if self.payg:
            _dict["payg"] = self.payg.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GcpMarketplacePrivateOfferPriceModel:
        """Create an instance of GcpMarketplacePrivateOfferPriceModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GcpMarketplacePrivateOfferPriceModel.parse_obj(obj)

        _obj = GcpMarketplacePrivateOfferPriceModel.parse_obj(
            {
                "base_offer": obj.get("baseOffer"),
                "commitment": GcpMarketplacePrivateOfferPriceModelCommitment.from_dict(
                    obj.get("commitment")
                )
                if obj.get("commitment") is not None
                else None,
                "fixed_price": GcpMarketplacePrivateOfferPriceModelFixed.from_dict(
                    obj.get("fixedPrice")
                )
                if obj.get("fixedPrice") is not None
                else None,
                "one_time_credit": GcpPriceValue.from_dict(obj.get("oneTimeCredit"))
                if obj.get("oneTimeCredit") is not None
                else None,
                "overage": GcpMarketplacePrivateOfferPriceModelOverage.from_dict(
                    obj.get("overage")
                )
                if obj.get("overage") is not None
                else None,
                "payg": GcpMarketplacePrivateOfferPriceModelPayg.from_dict(
                    obj.get("payg")
                )
                if obj.get("payg") is not None
                else None,
                "previous_credit_balance_policy": obj.get(
                    "previousCreditBalancePolicy"
                ),
            }
        )
        return _obj