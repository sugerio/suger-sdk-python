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
from openapi_client.models.microsoft_partner_referral_address import MicrosoftPartnerReferralAddress
from openapi_client.models.microsoft_partner_referral_person import MicrosoftPartnerReferralPerson
from openapi_client.models.microsoft_partner_referral_profile_id import MicrosoftPartnerReferralProfileId

class MicrosoftPartnerReferralProfile(BaseModel):
    """
    MicrosoftPartnerReferralProfile
    """
    activities: Optional[Dict[str, Any]] = None
    address: Optional[MicrosoftPartnerReferralAddress] = None
    ids: Optional[conlist(MicrosoftPartnerReferralProfileId)] = None
    is_macc_eligible: Optional[StrictBool] = Field(None, alias="isMaccEligible")
    is_matching_complete: Optional[StrictBool] = Field(None, alias="isMatchingComplete")
    name: Optional[StrictStr] = None
    size: Optional[StrictStr] = None
    team: Optional[conlist(MicrosoftPartnerReferralPerson)] = None
    __properties = ["activities", "address", "ids", "isMaccEligible", "isMatchingComplete", "name", "size", "team"]

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
    def from_json(cls, json_str: str) -> MicrosoftPartnerReferralProfile:
        """Create an instance of MicrosoftPartnerReferralProfile from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of address
        if self.address:
            _dict['address'] = self.address.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in ids (list)
        _items = []
        if self.ids:
            for _item in self.ids:
                if _item:
                    _items.append(_item.to_dict())
            _dict['ids'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in team (list)
        _items = []
        if self.team:
            for _item in self.team:
                if _item:
                    _items.append(_item.to_dict())
            _dict['team'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MicrosoftPartnerReferralProfile:
        """Create an instance of MicrosoftPartnerReferralProfile from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MicrosoftPartnerReferralProfile.parse_obj(obj)

        _obj = MicrosoftPartnerReferralProfile.parse_obj({
            "activities": obj.get("activities"),
            "address": MicrosoftPartnerReferralAddress.from_dict(obj.get("address")) if obj.get("address") is not None else None,
            "ids": [MicrosoftPartnerReferralProfileId.from_dict(_item) for _item in obj.get("ids")] if obj.get("ids") is not None else None,
            "is_macc_eligible": obj.get("isMaccEligible"),
            "is_matching_complete": obj.get("isMatchingComplete"),
            "name": obj.get("name"),
            "size": obj.get("size"),
            "team": [MicrosoftPartnerReferralPerson.from_dict(_item) for _item in obj.get("team")] if obj.get("team") is not None else None
        })
        return _obj


