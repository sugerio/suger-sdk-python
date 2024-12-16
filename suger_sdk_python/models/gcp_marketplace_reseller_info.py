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
from typing import Optional, Set
from typing_extensions import Self

class GcpMarketplaceResellerInfo(BaseModel):
    """
    GcpMarketplaceResellerInfo
    """ # noqa: E501
    billing_account_id: Optional[StrictStr] = Field(default=None, alias="billingAccountId")
    billing_account_nickname: Optional[StrictStr] = Field(default=None, alias="billingAccountNickname")
    billing_account_org_display_name: Optional[StrictStr] = Field(default=None, alias="billingAccountOrgDisplayName")
    billing_account_type: Optional[StrictStr] = Field(default=None, alias="billingAccountType")
    notes_to_reseller: Optional[StrictStr] = Field(default=None, alias="notesToReseller")
    partner_account_name: Optional[StrictStr] = Field(default=None, description="In the format of \"\"organizations/{GcpOrganizationID}/partnerAccounts/{partnerAccountID}\"", alias="partnerAccountName")
    resell_offer_template_id: Optional[StrictStr] = Field(default=None, alias="resellOfferTemplateId")
    reseller_contact_email: Optional[StrictStr] = Field(default=None, alias="resellerContactEmail")
    reseller_contact_name: Optional[StrictStr] = Field(default=None, alias="resellerContactName")
    reseller_private_offer_plan_id: Optional[StrictStr] = Field(default=None, alias="resellerPrivateOfferPlanId")
    reseller_private_offer_plan_scope: Optional[StrictStr] = Field(default=None, alias="resellerPrivateOfferPlanScope")
    sub_billing_account: Optional[StrictStr] = Field(default=None, description="In the format of \"billingAccounts/...\"", alias="subBillingAccount")
    __properties: ClassVar[List[str]] = ["billingAccountId", "billingAccountNickname", "billingAccountOrgDisplayName", "billingAccountType", "notesToReseller", "partnerAccountName", "resellOfferTemplateId", "resellerContactEmail", "resellerContactName", "resellerPrivateOfferPlanId", "resellerPrivateOfferPlanScope", "subBillingAccount"]

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
        """Create an instance of GcpMarketplaceResellerInfo from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GcpMarketplaceResellerInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "billingAccountId": obj.get("billingAccountId"),
            "billingAccountNickname": obj.get("billingAccountNickname"),
            "billingAccountOrgDisplayName": obj.get("billingAccountOrgDisplayName"),
            "billingAccountType": obj.get("billingAccountType"),
            "notesToReseller": obj.get("notesToReseller"),
            "partnerAccountName": obj.get("partnerAccountName"),
            "resellOfferTemplateId": obj.get("resellOfferTemplateId"),
            "resellerContactEmail": obj.get("resellerContactEmail"),
            "resellerContactName": obj.get("resellerContactName"),
            "resellerPrivateOfferPlanId": obj.get("resellerPrivateOfferPlanId"),
            "resellerPrivateOfferPlanScope": obj.get("resellerPrivateOfferPlanScope"),
            "subBillingAccount": obj.get("subBillingAccount")
        })
        return _obj


