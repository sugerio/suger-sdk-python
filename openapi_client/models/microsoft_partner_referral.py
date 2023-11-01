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


from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist
from openapi_client.models.microsoft_partner_referral_consent import (
    MicrosoftPartnerReferralConsent,
)
from openapi_client.models.microsoft_partner_referral_detail import (
    MicrosoftPartnerReferralDetail,
)
from openapi_client.models.microsoft_partner_referral_invite_context import (
    MicrosoftPartnerReferralInviteContext,
)
from openapi_client.models.microsoft_partner_referral_link import (
    MicrosoftPartnerReferralLink,
)
from openapi_client.models.microsoft_partner_referral_person import (
    MicrosoftPartnerReferralPerson,
)
from openapi_client.models.microsoft_partner_referral_profile import (
    MicrosoftPartnerReferralProfile,
)
from openapi_client.models.microsoft_partner_referral_qualification import (
    MicrosoftPartnerReferralQualification,
)
from openapi_client.models.microsoft_partner_referral_status import (
    MicrosoftPartnerReferralStatus,
)
from openapi_client.models.microsoft_partner_referral_sub_status import (
    MicrosoftPartnerReferralSubStatus,
)
from openapi_client.models.microsoft_partner_referral_target import (
    MicrosoftPartnerReferralTarget,
)
from openapi_client.models.microsoft_partner_referral_tracking_info import (
    MicrosoftPartnerReferralTrackingInfo,
)
from openapi_client.models.microsoft_partner_referral_type import (
    MicrosoftPartnerReferralType,
)


class MicrosoftPartnerReferral(BaseModel):
    """
    MicrosoftPartnerReferral
    """

    accepted_date_time: Optional[StrictStr] = Field(None, alias="acceptedDateTime")
    call_to_action: Optional[StrictStr] = Field(None, alias="callToAction")
    campaign_id: Optional[StrictStr] = Field(None, alias="campaignId")
    closed_date_time: Optional[StrictStr] = Field(None, alias="closedDateTime")
    consent: Optional[MicrosoftPartnerReferralConsent] = None
    created_date_time: Optional[StrictStr] = Field(None, alias="createdDateTime")
    created_via: Optional[StrictStr] = Field(None, alias="createdVia")
    customer_profile: Optional[MicrosoftPartnerReferralProfile] = Field(
        None, alias="customerProfile"
    )
    deal_sensitivity: Optional[StrictStr] = Field(None, alias="dealSensitivity")
    details: Optional[MicrosoftPartnerReferralDetail] = None
    direction: Optional[StrictStr] = None
    e_tag: Optional[StrictStr] = Field(None, alias="eTag")
    engagement_id: Optional[StrictStr] = Field(None, alias="engagementId")
    exception: Optional[Dict[str, Any]] = None
    expiration_date_time: Optional[StrictStr] = Field(None, alias="expirationDateTime")
    favorite: Optional[StrictBool] = None
    id: Optional[StrictStr] = None
    invite_context: Optional[MicrosoftPartnerReferralInviteContext] = Field(
        None, alias="inviteContext"
    )
    is_auto_registration_enabled: Optional[StrictBool] = Field(
        None, alias="isAutoRegistrationEnabled"
    )
    is_spam: Optional[StrictBool] = Field(None, alias="isSpam")
    last_modified_via: Optional[StrictStr] = Field(None, alias="lastModifiedVia")
    links: Optional[MicrosoftPartnerReferralLink] = None
    mpn_id: Optional[StrictStr] = Field(None, alias="mpnId")
    name: Optional[StrictStr] = None
    organization_id: Optional[StrictStr] = Field(None, alias="organizationId")
    organization_name: Optional[StrictStr] = Field(None, alias="organizationName")
    qualification: Optional[MicrosoftPartnerReferralQualification] = None
    quality: Optional[StrictStr] = None
    referral_program: Optional[Dict[str, Any]] = Field(None, alias="referralProgram")
    referral_source: Optional[Dict[str, Any]] = Field(None, alias="referralSource")
    registration_status: Optional[StrictStr] = Field(None, alias="registrationStatus")
    registrations: Optional[conlist(Dict[str, Any])] = None
    sales_stage: Optional[Dict[str, Any]] = Field(None, alias="salesStage")
    status: Optional[MicrosoftPartnerReferralStatus] = None
    substatus: Optional[MicrosoftPartnerReferralSubStatus] = None
    tags: Optional[conlist(Dict[str, Any])] = None
    target: Optional[conlist(MicrosoftPartnerReferralTarget)] = None
    team: Optional[conlist(MicrosoftPartnerReferralPerson)] = None
    tracking_info: Optional[MicrosoftPartnerReferralTrackingInfo] = Field(
        None, alias="trackingInfo"
    )
    type: Optional[MicrosoftPartnerReferralType] = None
    updated_date_time: Optional[StrictStr] = Field(None, alias="updatedDateTime")
    __properties = [
        "acceptedDateTime",
        "callToAction",
        "campaignId",
        "closedDateTime",
        "consent",
        "createdDateTime",
        "createdVia",
        "customerProfile",
        "dealSensitivity",
        "details",
        "direction",
        "eTag",
        "engagementId",
        "exception",
        "expirationDateTime",
        "favorite",
        "id",
        "inviteContext",
        "isAutoRegistrationEnabled",
        "isSpam",
        "lastModifiedVia",
        "links",
        "mpnId",
        "name",
        "organizationId",
        "organizationName",
        "qualification",
        "quality",
        "referralProgram",
        "referralSource",
        "registrationStatus",
        "registrations",
        "salesStage",
        "status",
        "substatus",
        "tags",
        "target",
        "team",
        "trackingInfo",
        "type",
        "updatedDateTime",
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
    def from_json(cls, json_str: str) -> MicrosoftPartnerReferral:
        """Create an instance of MicrosoftPartnerReferral from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of consent
        if self.consent:
            _dict["consent"] = self.consent.to_dict()
        # override the default output from pydantic by calling `to_dict()` of customer_profile
        if self.customer_profile:
            _dict["customerProfile"] = self.customer_profile.to_dict()
        # override the default output from pydantic by calling `to_dict()` of details
        if self.details:
            _dict["details"] = self.details.to_dict()
        # override the default output from pydantic by calling `to_dict()` of invite_context
        if self.invite_context:
            _dict["inviteContext"] = self.invite_context.to_dict()
        # override the default output from pydantic by calling `to_dict()` of links
        if self.links:
            _dict["links"] = self.links.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in target (list)
        _items = []
        if self.target:
            for _item in self.target:
                if _item:
                    _items.append(_item.to_dict())
            _dict["target"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in team (list)
        _items = []
        if self.team:
            for _item in self.team:
                if _item:
                    _items.append(_item.to_dict())
            _dict["team"] = _items
        # override the default output from pydantic by calling `to_dict()` of tracking_info
        if self.tracking_info:
            _dict["trackingInfo"] = self.tracking_info.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MicrosoftPartnerReferral:
        """Create an instance of MicrosoftPartnerReferral from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MicrosoftPartnerReferral.parse_obj(obj)

        _obj = MicrosoftPartnerReferral.parse_obj(
            {
                "accepted_date_time": obj.get("acceptedDateTime"),
                "call_to_action": obj.get("callToAction"),
                "campaign_id": obj.get("campaignId"),
                "closed_date_time": obj.get("closedDateTime"),
                "consent": MicrosoftPartnerReferralConsent.from_dict(obj.get("consent"))
                if obj.get("consent") is not None
                else None,
                "created_date_time": obj.get("createdDateTime"),
                "created_via": obj.get("createdVia"),
                "customer_profile": MicrosoftPartnerReferralProfile.from_dict(
                    obj.get("customerProfile")
                )
                if obj.get("customerProfile") is not None
                else None,
                "deal_sensitivity": obj.get("dealSensitivity"),
                "details": MicrosoftPartnerReferralDetail.from_dict(obj.get("details"))
                if obj.get("details") is not None
                else None,
                "direction": obj.get("direction"),
                "e_tag": obj.get("eTag"),
                "engagement_id": obj.get("engagementId"),
                "exception": obj.get("exception"),
                "expiration_date_time": obj.get("expirationDateTime"),
                "favorite": obj.get("favorite"),
                "id": obj.get("id"),
                "invite_context": MicrosoftPartnerReferralInviteContext.from_dict(
                    obj.get("inviteContext")
                )
                if obj.get("inviteContext") is not None
                else None,
                "is_auto_registration_enabled": obj.get("isAutoRegistrationEnabled"),
                "is_spam": obj.get("isSpam"),
                "last_modified_via": obj.get("lastModifiedVia"),
                "links": MicrosoftPartnerReferralLink.from_dict(obj.get("links"))
                if obj.get("links") is not None
                else None,
                "mpn_id": obj.get("mpnId"),
                "name": obj.get("name"),
                "organization_id": obj.get("organizationId"),
                "organization_name": obj.get("organizationName"),
                "qualification": obj.get("qualification"),
                "quality": obj.get("quality"),
                "referral_program": obj.get("referralProgram"),
                "referral_source": obj.get("referralSource"),
                "registration_status": obj.get("registrationStatus"),
                "registrations": obj.get("registrations"),
                "sales_stage": obj.get("salesStage"),
                "status": obj.get("status"),
                "substatus": obj.get("substatus"),
                "tags": obj.get("tags"),
                "target": [
                    MicrosoftPartnerReferralTarget.from_dict(_item)
                    for _item in obj.get("target")
                ]
                if obj.get("target") is not None
                else None,
                "team": [
                    MicrosoftPartnerReferralPerson.from_dict(_item)
                    for _item in obj.get("team")
                ]
                if obj.get("team") is not None
                else None,
                "tracking_info": MicrosoftPartnerReferralTrackingInfo.from_dict(
                    obj.get("trackingInfo")
                )
                if obj.get("trackingInfo") is not None
                else None,
                "type": obj.get("type"),
                "updated_date_time": obj.get("updatedDateTime"),
            }
        )
        return _obj
