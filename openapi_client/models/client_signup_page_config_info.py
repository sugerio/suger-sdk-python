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
from pydantic import BaseModel, Field, StrictStr, conlist

class ClientSignupPageConfigInfo(BaseModel):
    """
    ClientSignupPageConfigInfo
    """
    cc_emails: Optional[conlist(StrictStr)] = Field(None, alias="ccEmails", description="The cc email contacts of the new client signup notification.")
    company_logo_url: Optional[StrictStr] = Field(None, alias="companyLogoUrl", description="The company logo url of the seller/ISV.")
    company_name: Optional[StrictStr] = Field(None, alias="companyName", description="The company name of the seller/ISV to show in the client signup page.")
    landing_image_url: Optional[StrictStr] = Field(None, alias="landingImageUrl", description="The signup landing image aws url of the organization")
    notification_email_subject: Optional[StrictStr] = Field(None, alias="notificationEmailSubject", description="The email subject of the new client signup notification.")
    public_notes: Optional[StrictStr] = Field(None, alias="publicNotes", description="The public notes to append in new client signup notification email.")
    signup_id: Optional[StrictStr] = Field(None, alias="signupId", description="The signup ID for the new client signup page url. It is populated by Suger service when creating the new client signup page.")
    video_link: Optional[StrictStr] = Field(None, alias="videoLink", description="The video link of the product. Optional.")
    __properties = ["ccEmails", "companyLogoUrl", "companyName", "landingImageUrl", "notificationEmailSubject", "publicNotes", "signupId", "videoLink"]

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
    def from_json(cls, json_str: str) -> ClientSignupPageConfigInfo:
        """Create an instance of ClientSignupPageConfigInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ClientSignupPageConfigInfo:
        """Create an instance of ClientSignupPageConfigInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ClientSignupPageConfigInfo.parse_obj(obj)

        _obj = ClientSignupPageConfigInfo.parse_obj({
            "cc_emails": obj.get("ccEmails"),
            "company_logo_url": obj.get("companyLogoUrl"),
            "company_name": obj.get("companyName"),
            "landing_image_url": obj.get("landingImageUrl"),
            "notification_email_subject": obj.get("notificationEmailSubject"),
            "public_notes": obj.get("publicNotes"),
            "signup_id": obj.get("signupId"),
            "video_link": obj.get("videoLink")
        })
        return _obj


