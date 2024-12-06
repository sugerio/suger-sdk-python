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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from suger_sdk_python.models.azure_ad_identifier import AzureADIdentifier
from suger_sdk_python.models.azure_marketplace_subscription_status import AzureMarketplaceSubscriptionStatus
from suger_sdk_python.models.azure_term import AzureTerm
from typing import Optional, Set
from typing_extensions import Self

class AzureMarketplaceSubscription(BaseModel):
    """
    AzureMarketplaceSubscription
    """ # noqa: E501
    allowed_customer_operations: Optional[List[StrictStr]] = Field(default=None, alias="allowedCustomerOperations")
    auto_renew: Optional[StrictBool] = Field(default=None, alias="autoRenew")
    beneficiary: Optional[AzureADIdentifier] = None
    created: Optional[datetime] = None
    fulfillment_id: Optional[StrictStr] = Field(default=None, alias="fulfillmentId")
    id: Optional[StrictStr] = None
    is_free_trial: Optional[StrictBool] = Field(default=None, alias="isFreeTrial")
    is_test: Optional[StrictBool] = Field(default=None, alias="isTest")
    last_modified: Optional[StrictStr] = Field(default=None, alias="lastModified")
    name: Optional[StrictStr] = None
    offer_id: Optional[StrictStr] = Field(default=None, alias="offerId")
    plan_id: Optional[StrictStr] = Field(default=None, alias="planId")
    publisher_id: Optional[StrictStr] = Field(default=None, alias="publisherId")
    purchaser: Optional[AzureADIdentifier] = None
    quantity: Optional[StrictInt] = None
    saas_subscription_status: Optional[AzureMarketplaceSubscriptionStatus] = Field(default=None, alias="saasSubscriptionStatus")
    sandbox_type: Optional[StrictStr] = Field(default=None, alias="sandboxType")
    session_id: Optional[StrictStr] = Field(default=None, alias="sessionId")
    session_mode: Optional[StrictStr] = Field(default=None, alias="sessionMode")
    store_front: Optional[StrictStr] = Field(default=None, alias="storeFront")
    term: Optional[AzureTerm] = None
    __properties: ClassVar[List[str]] = ["allowedCustomerOperations", "autoRenew", "beneficiary", "created", "fulfillmentId", "id", "isFreeTrial", "isTest", "lastModified", "name", "offerId", "planId", "publisherId", "purchaser", "quantity", "saasSubscriptionStatus", "sandboxType", "sessionId", "sessionMode", "storeFront", "term"]

    @field_validator('allowed_customer_operations')
    def allowed_customer_operations_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['Read', 'Update', 'Delete']):
                raise ValueError("each list item must be one of ('Read', 'Update', 'Delete')")
        return value

    @field_validator('sandbox_type')
    def sandbox_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['None', 'Csp']):
            raise ValueError("must be one of enum values ('None', 'Csp')")
        return value

    @field_validator('session_mode')
    def session_mode_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['None', 'DryRun']):
            raise ValueError("must be one of enum values ('None', 'DryRun')")
        return value

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
        """Create an instance of AzureMarketplaceSubscription from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of beneficiary
        if self.beneficiary:
            _dict['beneficiary'] = self.beneficiary.to_dict()
        # override the default output from pydantic by calling `to_dict()` of purchaser
        if self.purchaser:
            _dict['purchaser'] = self.purchaser.to_dict()
        # override the default output from pydantic by calling `to_dict()` of term
        if self.term:
            _dict['term'] = self.term.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AzureMarketplaceSubscription from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "allowedCustomerOperations": obj.get("allowedCustomerOperations"),
            "autoRenew": obj.get("autoRenew"),
            "beneficiary": AzureADIdentifier.from_dict(obj["beneficiary"]) if obj.get("beneficiary") is not None else None,
            "created": obj.get("created"),
            "fulfillmentId": obj.get("fulfillmentId"),
            "id": obj.get("id"),
            "isFreeTrial": obj.get("isFreeTrial"),
            "isTest": obj.get("isTest"),
            "lastModified": obj.get("lastModified"),
            "name": obj.get("name"),
            "offerId": obj.get("offerId"),
            "planId": obj.get("planId"),
            "publisherId": obj.get("publisherId"),
            "purchaser": AzureADIdentifier.from_dict(obj["purchaser"]) if obj.get("purchaser") is not None else None,
            "quantity": obj.get("quantity"),
            "saasSubscriptionStatus": obj.get("saasSubscriptionStatus"),
            "sandboxType": obj.get("sandboxType"),
            "sessionId": obj.get("sessionId"),
            "sessionMode": obj.get("sessionMode"),
            "storeFront": obj.get("storeFront"),
            "term": AzureTerm.from_dict(obj["term"]) if obj.get("term") is not None else None
        })
        return _obj


