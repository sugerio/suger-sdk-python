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
from pydantic import BaseModel, Field, StrictInt, StrictStr
from openapi_client.models.alibaba_marketplace_product_shop_info_telephones import AlibabaMarketplaceProductShopInfoTelephones
from openapi_client.models.alibaba_marketplace_product_shop_info_wang_wangs import AlibabaMarketplaceProductShopInfoWangWangs

class AlibabaMarketplaceProductShopInfo(BaseModel):
    """
    AlibabaMarketplaceProductShopInfo
    """
    emails: Optional[StrictStr] = Field(None, alias="Emails")
    id: Optional[StrictInt] = Field(None, alias="Id")
    name: Optional[StrictStr] = Field(None, alias="Name")
    telephones: Optional[AlibabaMarketplaceProductShopInfoTelephones] = Field(None, alias="Telephones")
    wang_wangs: Optional[AlibabaMarketplaceProductShopInfoWangWangs] = Field(None, alias="WangWangs")
    __properties = ["Emails", "Id", "Name", "Telephones", "WangWangs"]

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
    def from_json(cls, json_str: str) -> AlibabaMarketplaceProductShopInfo:
        """Create an instance of AlibabaMarketplaceProductShopInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of telephones
        if self.telephones:
            _dict['Telephones'] = self.telephones.to_dict()
        # override the default output from pydantic by calling `to_dict()` of wang_wangs
        if self.wang_wangs:
            _dict['WangWangs'] = self.wang_wangs.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AlibabaMarketplaceProductShopInfo:
        """Create an instance of AlibabaMarketplaceProductShopInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AlibabaMarketplaceProductShopInfo.parse_obj(obj)

        _obj = AlibabaMarketplaceProductShopInfo.parse_obj({
            "emails": obj.get("Emails"),
            "id": obj.get("Id"),
            "name": obj.get("Name"),
            "telephones": AlibabaMarketplaceProductShopInfoTelephones.from_dict(obj.get("Telephones")) if obj.get("Telephones") is not None else None,
            "wang_wangs": AlibabaMarketplaceProductShopInfoWangWangs.from_dict(obj.get("WangWangs")) if obj.get("WangWangs") is not None else None
        })
        return _obj


