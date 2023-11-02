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
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr
from openapi_client.models.client_describe_instance_response_body_modules import ClientDescribeInstanceResponseBodyModules
from openapi_client.models.client_describe_instance_response_body_relational_data import ClientDescribeInstanceResponseBodyRelationalData

class ClientDescribeInstanceResponseBody(BaseModel):
    """
    ClientDescribeInstanceResponseBody
    """
    app_json: Optional[StrictStr] = Field(None, alias="AppJson")
    auto_renewal: Optional[StrictStr] = Field(None, alias="AutoRenewal")
    began_on: Optional[StrictInt] = Field(None, alias="BeganOn")
    component_json: Optional[StrictStr] = Field(None, alias="ComponentJson")
    constraints: Optional[StrictStr] = Field(None, alias="Constraints")
    created_on: Optional[StrictInt] = Field(None, alias="CreatedOn")
    end_on: Optional[StrictInt] = Field(None, alias="EndOn")
    extend_json: Optional[StrictStr] = Field(None, alias="ExtendJson")
    host_json: Optional[StrictStr] = Field(None, alias="HostJson")
    instance_id: Optional[StrictInt] = Field(None, alias="InstanceId")
    is_trial: Optional[StrictBool] = Field(None, alias="IsTrial")
    modules: Optional[ClientDescribeInstanceResponseBodyModules] = Field(None, alias="Modules")
    order_id: Optional[StrictInt] = Field(None, alias="OrderId")
    product_code: Optional[StrictStr] = Field(None, alias="ProductCode")
    product_name: Optional[StrictStr] = Field(None, alias="ProductName")
    product_sku_code: Optional[StrictStr] = Field(None, alias="ProductSkuCode")
    product_type: Optional[StrictStr] = Field(None, alias="ProductType")
    relational_data: Optional[ClientDescribeInstanceResponseBodyRelationalData] = Field(None, alias="RelationalData")
    status: Optional[StrictStr] = Field(None, alias="Status")
    supplier_name: Optional[StrictStr] = Field(None, alias="SupplierName")
    __properties = ["AppJson", "AutoRenewal", "BeganOn", "ComponentJson", "Constraints", "CreatedOn", "EndOn", "ExtendJson", "HostJson", "InstanceId", "IsTrial", "Modules", "OrderId", "ProductCode", "ProductName", "ProductSkuCode", "ProductType", "RelationalData", "Status", "SupplierName"]

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
    def from_json(cls, json_str: str) -> ClientDescribeInstanceResponseBody:
        """Create an instance of ClientDescribeInstanceResponseBody from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of modules
        if self.modules:
            _dict['Modules'] = self.modules.to_dict()
        # override the default output from pydantic by calling `to_dict()` of relational_data
        if self.relational_data:
            _dict['RelationalData'] = self.relational_data.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ClientDescribeInstanceResponseBody:
        """Create an instance of ClientDescribeInstanceResponseBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ClientDescribeInstanceResponseBody.parse_obj(obj)

        _obj = ClientDescribeInstanceResponseBody.parse_obj({
            "app_json": obj.get("AppJson"),
            "auto_renewal": obj.get("AutoRenewal"),
            "began_on": obj.get("BeganOn"),
            "component_json": obj.get("ComponentJson"),
            "constraints": obj.get("Constraints"),
            "created_on": obj.get("CreatedOn"),
            "end_on": obj.get("EndOn"),
            "extend_json": obj.get("ExtendJson"),
            "host_json": obj.get("HostJson"),
            "instance_id": obj.get("InstanceId"),
            "is_trial": obj.get("IsTrial"),
            "modules": ClientDescribeInstanceResponseBodyModules.from_dict(obj.get("Modules")) if obj.get("Modules") is not None else None,
            "order_id": obj.get("OrderId"),
            "product_code": obj.get("ProductCode"),
            "product_name": obj.get("ProductName"),
            "product_sku_code": obj.get("ProductSkuCode"),
            "product_type": obj.get("ProductType"),
            "relational_data": ClientDescribeInstanceResponseBodyRelationalData.from_dict(obj.get("RelationalData")) if obj.get("RelationalData") is not None else None,
            "status": obj.get("Status"),
            "supplier_name": obj.get("SupplierName")
        })
        return _obj


