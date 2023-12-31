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
from openapi_client.models.aws_saas_product_description import AwsSaasProductDescription
from openapi_client.models.aws_saas_product_dimension import AwsSaasProductDimension
from openapi_client.models.aws_saas_product_promotional_resources import AwsSaasProductPromotionalResources
from openapi_client.models.aws_saas_product_support_information import AwsSaasProductSupportInformation
from openapi_client.models.aws_saas_product_version import AwsSaasProductVersion

class AwsSaasProduct(BaseModel):
    """
    AwsSaasProduct
    """
    description: Optional[AwsSaasProductDescription] = Field(None, alias="Description")
    dimensions: Optional[conlist(AwsSaasProductDimension)] = Field(None, alias="Dimensions")
    promotional_resources: Optional[AwsSaasProductPromotionalResources] = Field(None, alias="PromotionalResources")
    support_information: Optional[AwsSaasProductSupportInformation] = Field(None, alias="SupportInformation")
    versions: Optional[conlist(AwsSaasProductVersion)] = Field(None, alias="Versions")
    data_feed_product_id: Optional[StrictStr] = Field(None, alias="dataFeedProductId", description="The product Id in AWS Marketplace Data Feed Service.")
    product_id: Optional[StrictStr] = Field(None, alias="productId", description="AWS Product ID")
    __properties = ["Description", "Dimensions", "PromotionalResources", "SupportInformation", "Versions", "dataFeedProductId", "productId"]

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
    def from_json(cls, json_str: str) -> AwsSaasProduct:
        """Create an instance of AwsSaasProduct from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of description
        if self.description:
            _dict['Description'] = self.description.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in dimensions (list)
        _items = []
        if self.dimensions:
            for _item in self.dimensions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['Dimensions'] = _items
        # override the default output from pydantic by calling `to_dict()` of promotional_resources
        if self.promotional_resources:
            _dict['PromotionalResources'] = self.promotional_resources.to_dict()
        # override the default output from pydantic by calling `to_dict()` of support_information
        if self.support_information:
            _dict['SupportInformation'] = self.support_information.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in versions (list)
        _items = []
        if self.versions:
            for _item in self.versions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['Versions'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AwsSaasProduct:
        """Create an instance of AwsSaasProduct from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AwsSaasProduct.parse_obj(obj)

        _obj = AwsSaasProduct.parse_obj({
            "description": AwsSaasProductDescription.from_dict(obj.get("Description")) if obj.get("Description") is not None else None,
            "dimensions": [AwsSaasProductDimension.from_dict(_item) for _item in obj.get("Dimensions")] if obj.get("Dimensions") is not None else None,
            "promotional_resources": AwsSaasProductPromotionalResources.from_dict(obj.get("PromotionalResources")) if obj.get("PromotionalResources") is not None else None,
            "support_information": AwsSaasProductSupportInformation.from_dict(obj.get("SupportInformation")) if obj.get("SupportInformation") is not None else None,
            "versions": [AwsSaasProductVersion.from_dict(_item) for _item in obj.get("Versions")] if obj.get("Versions") is not None else None,
            "data_feed_product_id": obj.get("dataFeedProductId"),
            "product_id": obj.get("productId")
        })
        return _obj


