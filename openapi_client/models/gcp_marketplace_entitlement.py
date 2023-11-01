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
from typing import List, Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist
from openapi_client.models.gcp_marketplace_consumer import GcpMarketplaceConsumer
from openapi_client.models.gcp_marketplace_entitlement_state import (
    GcpMarketplaceEntitlementState,
)


class GcpMarketplaceEntitlement(BaseModel):
    """
    GcpMarketplaceEntitlement
    """

    account: Optional[StrictStr] = Field(
        None,
        description='The resource name of the account that this entitlement is based on, if any, in format ""providers/{provider_id}/accounts/{account_id}"',
    )
    consumers: Optional[conlist(GcpMarketplaceConsumer)] = Field(
        None, description="The resources using this entitlement, if applicable."
    )
    create_time: Optional[datetime] = Field(None, alias="createTime")
    id: Optional[StrictStr] = Field(
        None,
        description="Entitlement Id generated by GCP Marketplace. For Marketplace pub/sub event.",
    )
    input_properties: Optional[conlist(StrictInt)] = Field(
        None,
        alias="inputProperties",
        description="The custom properties that were collected from the user to create this entitlement.",
    )
    message_to_user: Optional[StrictStr] = Field(
        None,
        alias="messageToUser",
        description="Provider-supplied message that is displayed to the end user. Currently this is used to communicate progress and ETA for provisioning. This field can be updated only when a user is waiting for an action from the provider, i.e. entitlement state is EntitlementState.ENTITLEMENT_ACTIVATION_REQUESTED or EntitlementState.ENTITLEMENT_PENDING_PLAN_CHANGE_APPROVAL. This field is cleared automatically when the entitlement state changes.",
    )
    name: Optional[StrictStr] = Field(
        None,
        description="The resource name of the entitlement. Entitlement names have the form of `providers/{provider_id}/entitlements/{entitlement_id}`.",
    )
    new_offer_duration: Optional[StrictStr] = Field(
        None,
        alias="newOfferDuration",
        description='in ISO 8601 duration format, such as "P2Y3M". For Marketplace pub/sub event.',
    )
    new_offer_end_time: Optional[StrictStr] = Field(
        None,
        alias="newOfferEndTime",
        description="Output only. The end time of the new offer. Field is empty if the pending plan change is not moving to an offer. If the offer was created with a term instead of a specified end date, this field is empty.",
    )
    new_offer_start_time: Optional[StrictStr] = Field(
        None,
        alias="newOfferStartTime",
        description="Output only. The start time of the new offer. Field is empty if the pending plan change is not moving to an offer.",
    )
    new_pending_offer: Optional[StrictStr] = Field(
        None,
        alias="newPendingOffer",
        description="The name of the offer the entitlement is switching to upon a pending plan change. Only exists if the pending plan change is moving to an offer. Format: 'projects/{project}/services/{service}/privateOffers/{offer-id}' OR 'projects/{project}/services/{service}/standardOffers/{offer-id}', depending on whether the offer is private or public.",
    )
    new_pending_offer_duration: Optional[StrictStr] = Field(
        None,
        alias="newPendingOfferDuration",
        description="The offer duration of the new offer in ISO 8601 duration format. Field is empty if the pending plan change is not moving to an offer since the entitlement is not pending, only the plan change is pending.",
    )
    new_pending_plan: Optional[StrictStr] = Field(
        None,
        alias="newPendingPlan",
        description="The identifier of the pending new plan. Required if the product has plans and the entitlement has a pending plan change.",
    )
    new_plan: Optional[StrictStr] = Field(
        None,
        alias="newPlan",
        description="When the buyer changes plan, For Marketplace pub/sub event.",
    )
    offer: Optional[StrictStr] = Field(
        None,
        description="The name of the offer that was procured. Field is empty if order was not made using an offer. Format: 'projects/{project}/services/{service}/privateOffers/{offer-id}' OR 'projects/{project}/services/{service}/standardOffers/{offer-id}', depending on whether the offer is private or public.",
    )
    offer_duration: Optional[StrictStr] = Field(
        None,
        alias="offerDuration",
        description='The offer duration of the current offer in ISO 8601 duration format. Field is empty if entitlement was not made using an offer, such as "P1Y", "P2M"',
    )
    offer_effective_time: Optional[datetime] = Field(
        None, alias="offerEffectiveTime", description="When the offer is effective."
    )
    offer_end_time: Optional[datetime] = Field(
        None,
        alias="offerEndTime",
        description="Output only. End time for the Offer association corresponding to this entitlement. The field is only populated if the entitlement is currently associated with an Offer.",
    )
    plan: Optional[StrictStr] = Field(
        None,
        description="The identifier of the plan that was procured. Required if the product has plans.",
    )
    product: Optional[StrictStr] = Field(
        None,
        description='The identifier of the entity that was purchased. This may actually represent a product, quote, or offer. For Private offer, "projects/project-id/services/product-id.endpoints.partner-id.cloud.goog/privateOffers/private-offer-id"',
    )
    product_external_name: Optional[StrictStr] = Field(
        None,
        alias="productExternalName",
        description="The identifier of the product that was procured.",
    )
    provider: Optional[StrictStr] = Field(
        None,
        description="The ID of the service provider under Cloud Commerce platform that this entitlement was created against.",
    )
    quote_external_name: Optional[StrictStr] = Field(
        None,
        alias="quoteExternalName",
        description="The identifier of the quote that was used to procure, such as the private offer Id. Empty if the order is not purchased using a quote.",
    )
    state: Optional[GcpMarketplaceEntitlementState] = None
    subscription_end_time: Optional[datetime] = Field(
        None,
        alias="subscriptionEndTime",
        description="The End time for the subscription corresponding to this entitlement.",
    )
    update_time: Optional[datetime] = Field(
        None,
        alias="updateTime",
        description="The last update timestamp. It is the endTime for the cancelled entitlement.",
    )
    usage_reporting_id: Optional[StrictStr] = Field(
        None,
        alias="usageReportingId",
        description="The consumerId to use when reporting usage through the Service Control API. See the consumerId field at Reporting Metrics (https://cloud.google.com/service-control/reporting-metrics) for more details. This field is present only if the product has usage-based billing configured.",
    )
    __properties = [
        "account",
        "consumers",
        "createTime",
        "id",
        "inputProperties",
        "messageToUser",
        "name",
        "newOfferDuration",
        "newOfferEndTime",
        "newOfferStartTime",
        "newPendingOffer",
        "newPendingOfferDuration",
        "newPendingPlan",
        "newPlan",
        "offer",
        "offerDuration",
        "offerEffectiveTime",
        "offerEndTime",
        "plan",
        "product",
        "productExternalName",
        "provider",
        "quoteExternalName",
        "state",
        "subscriptionEndTime",
        "updateTime",
        "usageReportingId",
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
    def from_json(cls, json_str: str) -> GcpMarketplaceEntitlement:
        """Create an instance of GcpMarketplaceEntitlement from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in consumers (list)
        _items = []
        if self.consumers:
            for _item in self.consumers:
                if _item:
                    _items.append(_item.to_dict())
            _dict["consumers"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GcpMarketplaceEntitlement:
        """Create an instance of GcpMarketplaceEntitlement from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GcpMarketplaceEntitlement.parse_obj(obj)

        _obj = GcpMarketplaceEntitlement.parse_obj(
            {
                "account": obj.get("account"),
                "consumers": [
                    GcpMarketplaceConsumer.from_dict(_item)
                    for _item in obj.get("consumers")
                ]
                if obj.get("consumers") is not None
                else None,
                "create_time": obj.get("createTime"),
                "id": obj.get("id"),
                "input_properties": obj.get("inputProperties"),
                "message_to_user": obj.get("messageToUser"),
                "name": obj.get("name"),
                "new_offer_duration": obj.get("newOfferDuration"),
                "new_offer_end_time": obj.get("newOfferEndTime"),
                "new_offer_start_time": obj.get("newOfferStartTime"),
                "new_pending_offer": obj.get("newPendingOffer"),
                "new_pending_offer_duration": obj.get("newPendingOfferDuration"),
                "new_pending_plan": obj.get("newPendingPlan"),
                "new_plan": obj.get("newPlan"),
                "offer": obj.get("offer"),
                "offer_duration": obj.get("offerDuration"),
                "offer_effective_time": obj.get("offerEffectiveTime"),
                "offer_end_time": obj.get("offerEndTime"),
                "plan": obj.get("plan"),
                "product": obj.get("product"),
                "product_external_name": obj.get("productExternalName"),
                "provider": obj.get("provider"),
                "quote_external_name": obj.get("quoteExternalName"),
                "state": obj.get("state"),
                "subscription_end_time": obj.get("subscriptionEndTime"),
                "update_time": obj.get("updateTime"),
                "usage_reporting_id": obj.get("usageReportingId"),
            }
        )
        return _obj
