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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from suger_sdk_python.models.aws_marketplace_event_bridge_event_account import AwsMarketplaceEventBridgeEventAccount
from suger_sdk_python.models.aws_marketplace_event_bridge_event_offer import AwsMarketplaceEventBridgeEventOffer
from suger_sdk_python.models.aws_marketplace_event_bridge_event_product import AwsMarketplaceEventBridgeEventProduct
from typing import Optional, Set
from typing_extensions import Self

class AwsMarketplaceEventBridgeEventDetail(BaseModel):
    """
    AwsMarketplaceEventBridgeEventDetail
    """ # noqa: E501
    catalog: Optional[StrictStr] = None
    event_category: Optional[StrictStr] = Field(default=None, alias="eventCategory")
    event_id: Optional[StrictStr] = Field(default=None, alias="eventID")
    event_name: Optional[StrictStr] = Field(default=None, alias="eventName")
    event_source: Optional[StrictStr] = Field(default=None, alias="eventSource")
    event_type: Optional[StrictStr] = Field(default=None, alias="eventType")
    event_version: Optional[StrictStr] = Field(default=None, alias="eventVersion")
    management_event: Optional[StrictBool] = Field(default=None, alias="managementEvent")
    manufacturer: Optional[AwsMarketplaceEventBridgeEventAccount] = Field(default=None, description="The seller/ISV's AWS Account Id.")
    offer: Optional[AwsMarketplaceEventBridgeEventOffer] = None
    product: Optional[AwsMarketplaceEventBridgeEventProduct] = None
    request_id: Optional[StrictStr] = Field(default=None, alias="requestID")
    request_parameters: Optional[Dict[str, Any]] = Field(default=None, alias="requestParameters")
    response_elements: Optional[Dict[str, Any]] = Field(default=None, alias="responseElements")
    seller_of_record: Optional[AwsMarketplaceEventBridgeEventAccount] = Field(default=None, description="For private offer created by a channel partner, this is the channel partner's AWS Account Id. For private offer created by a seller/ISV, this is the seller/ISV's AWS Account Id.", alias="sellerOfRecord")
    targeted_buyer_account_ids: Optional[List[StrictStr]] = Field(default=None, alias="targetedBuyerAccountIds")
    __properties: ClassVar[List[str]] = ["catalog", "eventCategory", "eventID", "eventName", "eventSource", "eventType", "eventVersion", "managementEvent", "manufacturer", "offer", "product", "requestID", "requestParameters", "responseElements", "sellerOfRecord", "targetedBuyerAccountIds"]

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
        """Create an instance of AwsMarketplaceEventBridgeEventDetail from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of manufacturer
        if self.manufacturer:
            _dict['manufacturer'] = self.manufacturer.to_dict()
        # override the default output from pydantic by calling `to_dict()` of offer
        if self.offer:
            _dict['offer'] = self.offer.to_dict()
        # override the default output from pydantic by calling `to_dict()` of product
        if self.product:
            _dict['product'] = self.product.to_dict()
        # override the default output from pydantic by calling `to_dict()` of seller_of_record
        if self.seller_of_record:
            _dict['sellerOfRecord'] = self.seller_of_record.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AwsMarketplaceEventBridgeEventDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "catalog": obj.get("catalog"),
            "eventCategory": obj.get("eventCategory"),
            "eventID": obj.get("eventID"),
            "eventName": obj.get("eventName"),
            "eventSource": obj.get("eventSource"),
            "eventType": obj.get("eventType"),
            "eventVersion": obj.get("eventVersion"),
            "managementEvent": obj.get("managementEvent"),
            "manufacturer": AwsMarketplaceEventBridgeEventAccount.from_dict(obj["manufacturer"]) if obj.get("manufacturer") is not None else None,
            "offer": AwsMarketplaceEventBridgeEventOffer.from_dict(obj["offer"]) if obj.get("offer") is not None else None,
            "product": AwsMarketplaceEventBridgeEventProduct.from_dict(obj["product"]) if obj.get("product") is not None else None,
            "requestID": obj.get("requestID"),
            "requestParameters": obj.get("requestParameters"),
            "responseElements": obj.get("responseElements"),
            "sellerOfRecord": AwsMarketplaceEventBridgeEventAccount.from_dict(obj["sellerOfRecord"]) if obj.get("sellerOfRecord") is not None else None,
            "targetedBuyerAccountIds": obj.get("targetedBuyerAccountIds")
        })
        return _obj


