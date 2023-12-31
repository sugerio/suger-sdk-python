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


from typing import List, Optional
from pydantic import BaseModel, conlist
from openapi_client.models.microsoft_partner_referral_iot import MicrosoftPartnerReferralIot
from openapi_client.models.microsoft_partner_referral_requirement_attribute import MicrosoftPartnerReferralRequirementAttribute

class MicrosoftPartnerReferralAdditionalRequirements(BaseModel):
    """
    MicrosoftPartnerReferralAdditionalRequirements
    """
    attributes: Optional[conlist(MicrosoftPartnerReferralRequirementAttribute)] = None
    iot: Optional[MicrosoftPartnerReferralIot] = None
    __properties = ["attributes", "iot"]

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
    def from_json(cls, json_str: str) -> MicrosoftPartnerReferralAdditionalRequirements:
        """Create an instance of MicrosoftPartnerReferralAdditionalRequirements from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in attributes (list)
        _items = []
        if self.attributes:
            for _item in self.attributes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['attributes'] = _items
        # override the default output from pydantic by calling `to_dict()` of iot
        if self.iot:
            _dict['iot'] = self.iot.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MicrosoftPartnerReferralAdditionalRequirements:
        """Create an instance of MicrosoftPartnerReferralAdditionalRequirements from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MicrosoftPartnerReferralAdditionalRequirements.parse_obj(obj)

        _obj = MicrosoftPartnerReferralAdditionalRequirements.parse_obj({
            "attributes": [MicrosoftPartnerReferralRequirementAttribute.from_dict(_item) for _item in obj.get("attributes")] if obj.get("attributes") is not None else None,
            "iot": MicrosoftPartnerReferralIot.from_dict(obj.get("iot")) if obj.get("iot") is not None else None
        })
        return _obj


