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
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conlist
from openapi_client.models.alibaba_integration_credential import AlibabaIntegrationCredential

class AlibabaMarketplaceIntegration(BaseModel):
    """
    AlibabaMarketplaceIntegration
    """
    aliyun_uid: Optional[StrictStr] = Field(None, alias="aliyunUid", description="The uid of the seller's main Alibaba Account.")
    auto_cancel_suspended_entitlements_enabled: Optional[StrictBool] = Field(None, alias="autoCancelSuspendedEntitlementsEnabled", description="If true, the suspended entitlements will be automatically canceled after the specified days.")
    credential: Optional[AlibabaIntegrationCredential] = None
    days_until_auto_cancel_suspended_entitlements: Optional[StrictInt] = Field(None, alias="daysUntilAutoCancelSuspendedEntitlements", description="Specifies the number of days after which an entitlement in suspended status will be automatically canceled. Only applicable if AutoCancelSuspendedEntitlementsEnabled is true. If the value is 0 or negative, the auto cancel feature is disabled.")
    product_codes: Optional[conlist(StrictStr)] = Field(None, alias="productCodes", description="The codes of the products that the seller is selling on Alibaba Marketplace.")
    secret_key: Optional[StrictStr] = Field(None, alias="secretKey", description="The secret key used to store the AlibabaIntegrationCredential in AWS Secret manager. For internal usage only.")
    usage_metering_disabled: Optional[StrictBool] = Field(None, alias="usageMeteringDisabled", description="Disable Usage Metering to Alibaba Cloud Marketplace. If true, Suger stop to report usage records to Alibaba Cloud Marketplace.")
    __properties = ["aliyunUid", "autoCancelSuspendedEntitlementsEnabled", "credential", "daysUntilAutoCancelSuspendedEntitlements", "productCodes", "secretKey", "usageMeteringDisabled"]

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
    def from_json(cls, json_str: str) -> AlibabaMarketplaceIntegration:
        """Create an instance of AlibabaMarketplaceIntegration from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of credential
        if self.credential:
            _dict['credential'] = self.credential.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AlibabaMarketplaceIntegration:
        """Create an instance of AlibabaMarketplaceIntegration from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AlibabaMarketplaceIntegration.parse_obj(obj)

        _obj = AlibabaMarketplaceIntegration.parse_obj({
            "aliyun_uid": obj.get("aliyunUid"),
            "auto_cancel_suspended_entitlements_enabled": obj.get("autoCancelSuspendedEntitlementsEnabled"),
            "credential": AlibabaIntegrationCredential.from_dict(obj.get("credential")) if obj.get("credential") is not None else None,
            "days_until_auto_cancel_suspended_entitlements": obj.get("daysUntilAutoCancelSuspendedEntitlements"),
            "product_codes": obj.get("productCodes"),
            "secret_key": obj.get("secretKey"),
            "usage_metering_disabled": obj.get("usageMeteringDisabled")
        })
        return _obj


