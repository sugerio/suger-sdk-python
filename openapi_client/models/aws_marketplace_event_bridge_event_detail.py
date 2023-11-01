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


from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist
from openapi_client.models.aws_marketplace_event_bridge_event_account import (
    AwsMarketplaceEventBridgeEventAccount,
)
from openapi_client.models.aws_marketplace_event_bridge_event_offer import (
    AwsMarketplaceEventBridgeEventOffer,
)
from openapi_client.models.aws_marketplace_event_bridge_event_product import (
    AwsMarketplaceEventBridgeEventProduct,
)


class AwsMarketplaceEventBridgeEventDetail(BaseModel):
    """
    AwsMarketplaceEventBridgeEventDetail
    """

    catalog: Optional[StrictStr] = None
    event_category: Optional[StrictStr] = Field(None, alias="eventCategory")
    event_id: Optional[StrictStr] = Field(None, alias="eventID")
    event_name: Optional[StrictStr] = Field(None, alias="eventName")
    event_source: Optional[StrictStr] = Field(None, alias="eventSource")
    event_type: Optional[StrictStr] = Field(None, alias="eventType")
    event_version: Optional[StrictStr] = Field(None, alias="eventVersion")
    management_event: Optional[StrictBool] = Field(None, alias="managementEvent")
    manufacturer: Optional[AwsMarketplaceEventBridgeEventAccount] = None
    offer: Optional[AwsMarketplaceEventBridgeEventOffer] = None
    product: Optional[AwsMarketplaceEventBridgeEventProduct] = None
    request_id: Optional[StrictStr] = Field(None, alias="requestID")
    request_parameters: Optional[Dict[str, Any]] = Field(
        None, alias="requestParameters"
    )
    response_elements: Optional[Dict[str, Any]] = Field(None, alias="responseElements")
    seller_of_record: Optional[AwsMarketplaceEventBridgeEventAccount] = Field(
        None, alias="sellerOfRecord"
    )
    targeted_buyer_account_ids: Optional[conlist(StrictStr)] = Field(
        None, alias="targetedBuyerAccountIds"
    )
    __properties = [
        "catalog",
        "eventCategory",
        "eventID",
        "eventName",
        "eventSource",
        "eventType",
        "eventVersion",
        "managementEvent",
        "manufacturer",
        "offer",
        "product",
        "requestID",
        "requestParameters",
        "responseElements",
        "sellerOfRecord",
        "targetedBuyerAccountIds",
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
    def from_json(cls, json_str: str) -> AwsMarketplaceEventBridgeEventDetail:
        """Create an instance of AwsMarketplaceEventBridgeEventDetail from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of manufacturer
        if self.manufacturer:
            _dict["manufacturer"] = self.manufacturer.to_dict()
        # override the default output from pydantic by calling `to_dict()` of offer
        if self.offer:
            _dict["offer"] = self.offer.to_dict()
        # override the default output from pydantic by calling `to_dict()` of product
        if self.product:
            _dict["product"] = self.product.to_dict()
        # override the default output from pydantic by calling `to_dict()` of seller_of_record
        if self.seller_of_record:
            _dict["sellerOfRecord"] = self.seller_of_record.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AwsMarketplaceEventBridgeEventDetail:
        """Create an instance of AwsMarketplaceEventBridgeEventDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AwsMarketplaceEventBridgeEventDetail.parse_obj(obj)

        _obj = AwsMarketplaceEventBridgeEventDetail.parse_obj(
            {
                "catalog": obj.get("catalog"),
                "event_category": obj.get("eventCategory"),
                "event_id": obj.get("eventID"),
                "event_name": obj.get("eventName"),
                "event_source": obj.get("eventSource"),
                "event_type": obj.get("eventType"),
                "event_version": obj.get("eventVersion"),
                "management_event": obj.get("managementEvent"),
                "manufacturer": AwsMarketplaceEventBridgeEventAccount.from_dict(
                    obj.get("manufacturer")
                )
                if obj.get("manufacturer") is not None
                else None,
                "offer": AwsMarketplaceEventBridgeEventOffer.from_dict(obj.get("offer"))
                if obj.get("offer") is not None
                else None,
                "product": AwsMarketplaceEventBridgeEventProduct.from_dict(
                    obj.get("product")
                )
                if obj.get("product") is not None
                else None,
                "request_id": obj.get("requestID"),
                "request_parameters": obj.get("requestParameters"),
                "response_elements": obj.get("responseElements"),
                "seller_of_record": AwsMarketplaceEventBridgeEventAccount.from_dict(
                    obj.get("sellerOfRecord")
                )
                if obj.get("sellerOfRecord") is not None
                else None,
                "targeted_buyer_account_ids": obj.get("targetedBuyerAccountIds"),
            }
        )
        return _obj
