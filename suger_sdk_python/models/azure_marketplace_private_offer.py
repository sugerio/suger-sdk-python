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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from suger_sdk_python.models.azure_marketplace_offer_pricing_type import AzureMarketplaceOfferPricingType
from suger_sdk_python.models.azure_marketplace_private_offer_acceptance_link import AzureMarketplacePrivateOfferAcceptanceLink
from suger_sdk_python.models.azure_marketplace_private_offer_beneficiary import AzureMarketplacePrivateOfferBeneficiary
from suger_sdk_python.models.azure_marketplace_private_offer_partner import AzureMarketplacePrivateOfferPartner
from suger_sdk_python.models.azure_marketplace_private_offer_pricing import AzureMarketplacePrivateOfferPricing
from suger_sdk_python.models.azure_marketplace_private_offer_promotion_reference import AzureMarketplacePrivateOfferPromotionReference
from suger_sdk_python.models.azure_marketplace_private_offer_state import AzureMarketplacePrivateOfferState
from suger_sdk_python.models.azure_marketplace_private_offer_sub_state import AzureMarketplacePrivateOfferSubState
from suger_sdk_python.models.azure_marketplace_private_offer_terms_doc import AzureMarketplacePrivateOfferTermsDoc
from suger_sdk_python.models.azure_marketplace_private_offer_type import AzureMarketplacePrivateOfferType
from suger_sdk_python.models.azure_marketplace_validation import AzureMarketplaceValidation
from typing import Optional, Set
from typing_extensions import Self

class AzureMarketplacePrivateOffer(BaseModel):
    """
    AzureMarketplacePrivateOffer
    """ # noqa: E501
    var_schema: Optional[StrictStr] = Field(default=None, alias="$schema")
    accept_by: Optional[datetime] = Field(default=None, description="in format YYYY-MM-DD", alias="acceptBy")
    acceptance_links: Optional[List[AzureMarketplacePrivateOfferAcceptanceLink]] = Field(default=None, alias="acceptanceLinks")
    beneficiaries: Optional[List[AzureMarketplacePrivateOfferBeneficiary]] = None
    customer_contract_renewal: Optional[StrictBool] = Field(default=None, description="If true, it is a renewal offer for an existing customer.", alias="customerContractRenewal")
    e_tag: Optional[StrictStr] = Field(default=None, alias="eTag")
    end: Optional[datetime] = Field(default=None, description="in format YYYY-MM-DD")
    id: Optional[StrictStr] = Field(default=None, description="in format of \"private-offer/private-offer-durable-id\"")
    last_modified: Optional[datetime] = Field(default=None, description="in format YYYY-MM-DD", alias="lastModified")
    name: Optional[StrictStr] = None
    notification_contacts: Optional[List[StrictStr]] = Field(default=None, description="array of email addresses of the users to be notified of any changes in the private offer status.", alias="notificationContacts")
    offer_pricing_type: Optional[AzureMarketplaceOfferPricingType] = Field(default=None, alias="offerPricingType")
    partners: Optional[List[AzureMarketplacePrivateOfferPartner]] = None
    prepared_by: Optional[StrictStr] = Field(default=None, alias="preparedBy")
    pricing: Optional[List[AzureMarketplacePrivateOfferPricing]] = Field(default=None, description="Up to 10 pricing entries are allowed.")
    private_offer_type: Optional[AzureMarketplacePrivateOfferType] = Field(default=None, alias="privateOfferType")
    resource_name: Optional[StrictStr] = Field(default=None, alias="resourceName")
    start: Optional[datetime] = Field(default=None, description="in format YYYY-MM-DD, if VariableStartDate = true, this field should be empty.")
    state: Optional[AzureMarketplacePrivateOfferState] = None
    sub_state: Optional[AzureMarketplacePrivateOfferSubState] = Field(default=None, alias="subState")
    terms_and_conditions_doc_sas_url: Optional[StrictStr] = Field(default=None, description="Only applicable to private offers with privateOfferType = customerPromotion || cspPromotion", alias="termsAndConditionsDocSasUrl")
    terms_and_conditions_docs: Optional[List[AzureMarketplacePrivateOfferTermsDoc]] = Field(default=None, description="Only applicable to private offers with privateOfferType = multipartyPromotionOriginator || multipartyPromotionChannelPartner", alias="termsAndConditionsDocs")
    upgraded_from: Optional[AzureMarketplacePrivateOfferPromotionReference] = Field(default=None, alias="upgradedFrom")
    validations: Optional[List[AzureMarketplaceValidation]] = None
    variable_start_date: Optional[StrictBool] = Field(default=None, alias="variableStartDate")
    __properties: ClassVar[List[str]] = ["$schema", "acceptBy", "acceptanceLinks", "beneficiaries", "customerContractRenewal", "eTag", "end", "id", "lastModified", "name", "notificationContacts", "offerPricingType", "partners", "preparedBy", "pricing", "privateOfferType", "resourceName", "start", "state", "subState", "termsAndConditionsDocSasUrl", "termsAndConditionsDocs", "upgradedFrom", "validations", "variableStartDate"]

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
        """Create an instance of AzureMarketplacePrivateOffer from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in acceptance_links (list)
        _items = []
        if self.acceptance_links:
            for _item_acceptance_links in self.acceptance_links:
                if _item_acceptance_links:
                    _items.append(_item_acceptance_links.to_dict())
            _dict['acceptanceLinks'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in beneficiaries (list)
        _items = []
        if self.beneficiaries:
            for _item_beneficiaries in self.beneficiaries:
                if _item_beneficiaries:
                    _items.append(_item_beneficiaries.to_dict())
            _dict['beneficiaries'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in partners (list)
        _items = []
        if self.partners:
            for _item_partners in self.partners:
                if _item_partners:
                    _items.append(_item_partners.to_dict())
            _dict['partners'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in pricing (list)
        _items = []
        if self.pricing:
            for _item_pricing in self.pricing:
                if _item_pricing:
                    _items.append(_item_pricing.to_dict())
            _dict['pricing'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in terms_and_conditions_docs (list)
        _items = []
        if self.terms_and_conditions_docs:
            for _item_terms_and_conditions_docs in self.terms_and_conditions_docs:
                if _item_terms_and_conditions_docs:
                    _items.append(_item_terms_and_conditions_docs.to_dict())
            _dict['termsAndConditionsDocs'] = _items
        # override the default output from pydantic by calling `to_dict()` of upgraded_from
        if self.upgraded_from:
            _dict['upgradedFrom'] = self.upgraded_from.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in validations (list)
        _items = []
        if self.validations:
            for _item_validations in self.validations:
                if _item_validations:
                    _items.append(_item_validations.to_dict())
            _dict['validations'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AzureMarketplacePrivateOffer from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "$schema": obj.get("$schema"),
            "acceptBy": obj.get("acceptBy"),
            "acceptanceLinks": [AzureMarketplacePrivateOfferAcceptanceLink.from_dict(_item) for _item in obj["acceptanceLinks"]] if obj.get("acceptanceLinks") is not None else None,
            "beneficiaries": [AzureMarketplacePrivateOfferBeneficiary.from_dict(_item) for _item in obj["beneficiaries"]] if obj.get("beneficiaries") is not None else None,
            "customerContractRenewal": obj.get("customerContractRenewal"),
            "eTag": obj.get("eTag"),
            "end": obj.get("end"),
            "id": obj.get("id"),
            "lastModified": obj.get("lastModified"),
            "name": obj.get("name"),
            "notificationContacts": obj.get("notificationContacts"),
            "offerPricingType": obj.get("offerPricingType"),
            "partners": [AzureMarketplacePrivateOfferPartner.from_dict(_item) for _item in obj["partners"]] if obj.get("partners") is not None else None,
            "preparedBy": obj.get("preparedBy"),
            "pricing": [AzureMarketplacePrivateOfferPricing.from_dict(_item) for _item in obj["pricing"]] if obj.get("pricing") is not None else None,
            "privateOfferType": obj.get("privateOfferType"),
            "resourceName": obj.get("resourceName"),
            "start": obj.get("start"),
            "state": obj.get("state"),
            "subState": obj.get("subState"),
            "termsAndConditionsDocSasUrl": obj.get("termsAndConditionsDocSasUrl"),
            "termsAndConditionsDocs": [AzureMarketplacePrivateOfferTermsDoc.from_dict(_item) for _item in obj["termsAndConditionsDocs"]] if obj.get("termsAndConditionsDocs") is not None else None,
            "upgradedFrom": AzureMarketplacePrivateOfferPromotionReference.from_dict(obj["upgradedFrom"]) if obj.get("upgradedFrom") is not None else None,
            "validations": [AzureMarketplaceValidation.from_dict(_item) for _item in obj["validations"]] if obj.get("validations") is not None else None,
            "variableStartDate": obj.get("variableStartDate")
        })
        return _obj


