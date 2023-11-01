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
from openapi_client.models.cosell_opp import CosellOpp
from openapi_client.models.cosell_opp_meta import CosellOppMeta


class CosellOppReferral(BaseModel):
    """
    CosellOppReferral
    """

    creation_time: Optional[StrictStr] = Field(None, alias="creationTime")
    destination: Optional[CosellOpp] = None
    destination_id: Optional[StrictStr] = Field(None, alias="destinationID")
    destination_partner: Optional[StrictStr] = Field(None, alias="destinationPartner")
    id: Optional[StrictStr] = None
    last_update_time: Optional[StrictStr] = Field(None, alias="lastUpdateTime")
    meta_info: Optional[CosellOppMeta] = None
    organization_id: Optional[StrictStr] = None
    source: Optional[CosellOpp] = None
    source_id: Optional[StrictStr] = Field(None, alias="sourceID")
    source_partner: Optional[StrictStr] = Field(None, alias="sourcePartner")
    __properties = [
        "creationTime",
        "destination",
        "destinationID",
        "destinationPartner",
        "id",
        "lastUpdateTime",
        "meta_info",
        "organization_id",
        "source",
        "sourceID",
        "sourcePartner",
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
    def from_json(cls, json_str: str) -> CosellOppReferral:
        """Create an instance of CosellOppReferral from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of destination
        if self.destination:
            _dict["destination"] = self.destination.to_dict()
        # override the default output from pydantic by calling `to_dict()` of meta_info
        if self.meta_info:
            _dict["meta_info"] = self.meta_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of source
        if self.source:
            _dict["source"] = self.source.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CosellOppReferral:
        """Create an instance of CosellOppReferral from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CosellOppReferral.parse_obj(obj)

        _obj = CosellOppReferral.parse_obj(
            {
                "creation_time": obj.get("creationTime"),
                "destination": CosellOpp.from_dict(obj.get("destination"))
                if obj.get("destination") is not None
                else None,
                "destination_id": obj.get("destinationID"),
                "destination_partner": obj.get("destinationPartner"),
                "id": obj.get("id"),
                "last_update_time": obj.get("lastUpdateTime"),
                "meta_info": CosellOppMeta.from_dict(obj.get("meta_info"))
                if obj.get("meta_info") is not None
                else None,
                "organization_id": obj.get("organization_id"),
                "source": CosellOpp.from_dict(obj.get("source"))
                if obj.get("source") is not None
                else None,
                "source_id": obj.get("sourceID"),
                "source_partner": obj.get("sourcePartner"),
            }
        )
        return _obj