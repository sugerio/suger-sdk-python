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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from suger_sdk_python.models.alibaba_marketplace_product_extras import AlibabaMarketplaceProductExtras
from suger_sdk_python.models.alibaba_marketplace_product_shop_info import AlibabaMarketplaceProductShopInfo
from suger_sdk_python.models.alibaba_marketplace_product_skus import AlibabaMarketplaceProductSkus
from typing import Optional, Set
from typing_extensions import Self

class AlibabaMarketplaceProduct(BaseModel):
    """
    AlibabaMarketplaceProduct
    """ # noqa: E501
    audit_fail_msg: Optional[StrictStr] = Field(default=None, alias="AuditFailMsg")
    audit_status: Optional[StrictStr] = Field(default=None, alias="AuditStatus")
    audit_time: Optional[StrictInt] = Field(default=None, alias="AuditTime")
    code: Optional[StrictStr] = Field(default=None, alias="Code")
    description: Optional[StrictStr] = Field(default=None, alias="Description")
    front_category_id: Optional[StrictInt] = Field(default=None, alias="FrontCategoryId")
    gmt_created: Optional[StrictInt] = Field(default=None, alias="GmtCreated")
    gmt_modified: Optional[StrictInt] = Field(default=None, alias="GmtModified")
    name: Optional[StrictStr] = Field(default=None, alias="Name")
    pic_url: Optional[StrictStr] = Field(default=None, alias="PicUrl")
    product_extras: Optional[AlibabaMarketplaceProductExtras] = Field(default=None, alias="ProductExtras")
    product_skus: Optional[AlibabaMarketplaceProductSkus] = Field(default=None, alias="ProductSkus")
    request_id: Optional[StrictStr] = Field(default=None, alias="RequestId")
    score: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="Score")
    shop_info: Optional[AlibabaMarketplaceProductShopInfo] = Field(default=None, alias="ShopInfo")
    short_description: Optional[StrictStr] = Field(default=None, alias="ShortDescription")
    status: Optional[StrictStr] = Field(default=None, alias="Status")
    supplier_pk: Optional[StrictInt] = Field(default=None, alias="SupplierPk")
    type: Optional[StrictStr] = Field(default=None, alias="Type")
    use_count: Optional[StrictInt] = Field(default=None, alias="UseCount")
    __properties: ClassVar[List[str]] = ["AuditFailMsg", "AuditStatus", "AuditTime", "Code", "Description", "FrontCategoryId", "GmtCreated", "GmtModified", "Name", "PicUrl", "ProductExtras", "ProductSkus", "RequestId", "Score", "ShopInfo", "ShortDescription", "Status", "SupplierPk", "Type", "UseCount"]

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
        """Create an instance of AlibabaMarketplaceProduct from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of product_extras
        if self.product_extras:
            _dict['ProductExtras'] = self.product_extras.to_dict()
        # override the default output from pydantic by calling `to_dict()` of product_skus
        if self.product_skus:
            _dict['ProductSkus'] = self.product_skus.to_dict()
        # override the default output from pydantic by calling `to_dict()` of shop_info
        if self.shop_info:
            _dict['ShopInfo'] = self.shop_info.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AlibabaMarketplaceProduct from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "AuditFailMsg": obj.get("AuditFailMsg"),
            "AuditStatus": obj.get("AuditStatus"),
            "AuditTime": obj.get("AuditTime"),
            "Code": obj.get("Code"),
            "Description": obj.get("Description"),
            "FrontCategoryId": obj.get("FrontCategoryId"),
            "GmtCreated": obj.get("GmtCreated"),
            "GmtModified": obj.get("GmtModified"),
            "Name": obj.get("Name"),
            "PicUrl": obj.get("PicUrl"),
            "ProductExtras": AlibabaMarketplaceProductExtras.from_dict(obj["ProductExtras"]) if obj.get("ProductExtras") is not None else None,
            "ProductSkus": AlibabaMarketplaceProductSkus.from_dict(obj["ProductSkus"]) if obj.get("ProductSkus") is not None else None,
            "RequestId": obj.get("RequestId"),
            "Score": obj.get("Score"),
            "ShopInfo": AlibabaMarketplaceProductShopInfo.from_dict(obj["ShopInfo"]) if obj.get("ShopInfo") is not None else None,
            "ShortDescription": obj.get("ShortDescription"),
            "Status": obj.get("Status"),
            "SupplierPk": obj.get("SupplierPk"),
            "Type": obj.get("Type"),
            "UseCount": obj.get("UseCount")
        })
        return _obj


