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

class AlibabaIntegrationCredential(BaseModel):
    """
    AlibabaIntegrationCredential
    """
    access_key_id: Optional[StrictStr] = Field(None, alias="accessKeyId")
    access_key_secret: Optional[StrictStr] = Field(None, alias="accessKeySecret")
    region_id: Optional[StrictStr] = Field(None, alias="regionId")
    spi_key: Optional[StrictStr] = Field(None, alias="spiKey")
    __properties = ["accessKeyId", "accessKeySecret", "regionId", "spiKey"]

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
    def from_json(cls, json_str: str) -> AlibabaIntegrationCredential:
        """Create an instance of AlibabaIntegrationCredential from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AlibabaIntegrationCredential:
        """Create an instance of AlibabaIntegrationCredential from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AlibabaIntegrationCredential.parse_obj(obj)

        _obj = AlibabaIntegrationCredential.parse_obj({
            "access_key_id": obj.get("accessKeyId"),
            "access_key_secret": obj.get("accessKeySecret"),
            "region_id": obj.get("regionId"),
            "spi_key": obj.get("spiKey")
        })
        return _obj


