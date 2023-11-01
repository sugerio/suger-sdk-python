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
from pydantic import BaseModel, StrictStr
from openapi_client.models.microsoft_partner_referral_target_type import MicrosoftPartnerReferralTargetType

class MicrosoftPartnerReferralTarget(BaseModel):
    """
    MicrosoftPartnerReferralTarget
    """
    id: Optional[StrictStr] = None
    type: Optional[MicrosoftPartnerReferralTargetType] = None
    __properties = ["id", "type"]

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
    def from_json(cls, json_str: str) -> MicrosoftPartnerReferralTarget:
        """Create an instance of MicrosoftPartnerReferralTarget from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MicrosoftPartnerReferralTarget:
        """Create an instance of MicrosoftPartnerReferralTarget from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MicrosoftPartnerReferralTarget.parse_obj(obj)

        _obj = MicrosoftPartnerReferralTarget.parse_obj({
            "id": obj.get("id"),
            "type": obj.get("type")
        })
        return _obj


