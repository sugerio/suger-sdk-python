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
from suger_sdk_python.models.gcp_marketplace_private_offer_price_model_commitment import GcpMarketplacePrivateOfferPriceModelCommitment
from suger_sdk_python.models.gcp_marketplace_private_offer_price_model_fixed import GcpMarketplacePrivateOfferPriceModelFixed
from suger_sdk_python.models.gcp_marketplace_private_offer_price_model_overage import GcpMarketplacePrivateOfferPriceModelOverage
from suger_sdk_python.models.gcp_marketplace_private_offer_price_model_payg import GcpMarketplacePrivateOfferPriceModelPayg
from suger_sdk_python.models.gcp_price_value import GcpPriceValue
from typing import Optional, Set
from typing_extensions import Self

class GcpMarketplacePrivateOfferPriceModel(BaseModel):
    """
    GcpMarketplacePrivateOfferPriceModel
    """ # noqa: E501
    base_offer: Optional[StrictStr] = Field(default=None, description="in format of \"projects/{projectNumber}/services/service-name.endpoints.gcp-project-id.cloud.goog/standardOffers/base-offer-id\"", alias="baseOffer")
    commitment: Optional[GcpMarketplacePrivateOfferPriceModelCommitment] = None
    fixed_price: Optional[GcpMarketplacePrivateOfferPriceModelFixed] = Field(default=None, alias="fixedPrice")
    one_time_credit: Optional[GcpPriceValue] = Field(default=None, description="The one time credit in amount of money", alias="oneTimeCredit")
    overage: Optional[GcpMarketplacePrivateOfferPriceModelOverage] = None
    payg: Optional[GcpMarketplacePrivateOfferPriceModelPayg] = Field(default=None, description="Pay as you go.")
    previous_credit_balance_policy: Optional[StrictStr] = Field(default=None, description="such as \"PREVIOUS_CREDIT_BALANCE_POLICY_UNSPECIFIED\"", alias="previousCreditBalancePolicy")
    __properties: ClassVar[List[str]] = ["baseOffer", "commitment", "fixedPrice", "oneTimeCredit", "overage", "payg", "previousCreditBalancePolicy"]

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
        """Create an instance of GcpMarketplacePrivateOfferPriceModel from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of commitment
        if self.commitment:
            _dict['commitment'] = self.commitment.to_dict()
        # override the default output from pydantic by calling `to_dict()` of fixed_price
        if self.fixed_price:
            _dict['fixedPrice'] = self.fixed_price.to_dict()
        # override the default output from pydantic by calling `to_dict()` of one_time_credit
        if self.one_time_credit:
            _dict['oneTimeCredit'] = self.one_time_credit.to_dict()
        # override the default output from pydantic by calling `to_dict()` of overage
        if self.overage:
            _dict['overage'] = self.overage.to_dict()
        # override the default output from pydantic by calling `to_dict()` of payg
        if self.payg:
            _dict['payg'] = self.payg.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GcpMarketplacePrivateOfferPriceModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "baseOffer": obj.get("baseOffer"),
            "commitment": GcpMarketplacePrivateOfferPriceModelCommitment.from_dict(obj["commitment"]) if obj.get("commitment") is not None else None,
            "fixedPrice": GcpMarketplacePrivateOfferPriceModelFixed.from_dict(obj["fixedPrice"]) if obj.get("fixedPrice") is not None else None,
            "oneTimeCredit": GcpPriceValue.from_dict(obj["oneTimeCredit"]) if obj.get("oneTimeCredit") is not None else None,
            "overage": GcpMarketplacePrivateOfferPriceModelOverage.from_dict(obj["overage"]) if obj.get("overage") is not None else None,
            "payg": GcpMarketplacePrivateOfferPriceModelPayg.from_dict(obj["payg"]) if obj.get("payg") is not None else None,
            "previousCreditBalancePolicy": obj.get("previousCreditBalancePolicy")
        })
        return _obj

