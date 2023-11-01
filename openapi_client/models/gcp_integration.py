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
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist


class GcpIntegration(BaseModel):
    """
    GcpIntegration
    """

    enable_chrome_sync: Optional[StrictBool] = Field(
        None,
        alias="enableChromeSync",
        description="Enable GCP marketplace sync from GCP Chrome. If true, Suger will sync GCP Marketplace Product & Private Offer from GCP Chrome.",
    )
    enable_manual_approve_entitlement: Optional[StrictBool] = Field(
        None,
        alias="enableManualApproveEntitlement",
        description="Enable manually approve the GCP Marketplace Entitlement. If true, Suger will not automatically approve the GCP Marketplace Entitlement. Util the GCP Marketplace Entitlement is manually approved, it will not be activated.",
    )
    gcp_project_id: Optional[StrictStr] = Field(None, alias="gcpProjectId")
    gcp_project_number: Optional[StrictStr] = Field(None, alias="gcpProjectNumber")
    identity_provider_id: Optional[StrictStr] = Field(None, alias="identityProviderId")
    login_url: Optional[StrictStr] = Field(
        None,
        alias="loginUrl",
        description="The Login URL for GCP Marketplace buyers to login to your service with or without SSO JWT token. If not set, the login will be redirected to the Product's fulfillment URL.",
    )
    partner_id: Optional[StrictStr] = Field(
        None,
        alias="partnerId",
        description="The GCP Marketplace Partner ID, it is also called as Provider ID somewhere.",
    )
    pubsub_subscription: Optional[StrictStr] = Field(
        None,
        alias="pubsubSubscription",
        description="The resource name of the Pub/Sub subscription to receive notifications from Google cloud marketplace.",
    )
    pubsub_topic: Optional[StrictStr] = Field(
        None,
        alias="pubsubTopic",
        description="The resource name of the Pub/Sub topic to receive notifications from Google when a user signs up for your service, purchases a plan, or changes an existing plan.",
    )
    report_bucket: Optional[StrictStr] = Field(
        None,
        alias="reportBucket",
        description="The GCP storage bucket name to store the GCP Marketplace reports.",
    )
    report_full_sync_done: Optional[StrictBool] = Field(
        None,
        alias="reportFullSyncDone",
        description="Is GCP Marketplace Report full-sync done.",
    )
    report_start_date: Optional[datetime] = Field(
        None,
        alias="reportStartDate",
        description="The UTC date when GCP Marketplace reports start to generate.",
    )
    report_sync_disabled: Optional[StrictBool] = Field(
        None,
        alias="reportSyncDisabled",
        description="Disable GCP Marketplace Report sync. If true, Suger stop to sync GCP Marketplace reports.",
    )
    revenue_record_full_sync_done: Optional[StrictBool] = Field(
        None,
        alias="revenueRecordFullSyncDone",
        description="Is GCP Marketplace Revenue Record full-sync done.",
    )
    revenue_record_sync_disabled: Optional[StrictBool] = Field(
        None,
        alias="revenueRecordSyncDisabled",
        description="Disable GCP Marketplace Revenue Record sync. If true, Suger stop to sync GCP Marketplace Revenue Records.",
    )
    service_account_email: Optional[StrictStr] = Field(
        None, alias="serviceAccountEmail"
    )
    service_names: Optional[conlist(StrictStr)] = Field(
        None,
        alias="serviceNames",
        description="The array of service resource names of the listings in GCP Marketplace.",
    )
    signup_redirect_without_entitlement_enabled: Optional[StrictBool] = Field(
        None,
        alias="signupRedirectWithoutEntitlementEnabled",
        description="If enabled, Suger will redirect the new client to the signup page even the entitlement is not found. If disabled, Suger will redirect the new client to the error page if the entitlement is not found.",
    )
    usage_metering_disabled: Optional[StrictBool] = Field(
        None,
        alias="usageMeteringDisabled",
        description="Disable Usage Metering to GCP Marketplace. If true, Suger stop to report usage records to GCP Marketplace.",
    )
    workload_identity_pool_id: Optional[StrictStr] = Field(
        None, alias="workloadIdentityPoolId"
    )
    __properties = [
        "enableChromeSync",
        "enableManualApproveEntitlement",
        "gcpProjectId",
        "gcpProjectNumber",
        "identityProviderId",
        "loginUrl",
        "partnerId",
        "pubsubSubscription",
        "pubsubTopic",
        "reportBucket",
        "reportFullSyncDone",
        "reportStartDate",
        "reportSyncDisabled",
        "revenueRecordFullSyncDone",
        "revenueRecordSyncDisabled",
        "serviceAccountEmail",
        "serviceNames",
        "signupRedirectWithoutEntitlementEnabled",
        "usageMeteringDisabled",
        "workloadIdentityPoolId",
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
    def from_json(cls, json_str: str) -> GcpIntegration:
        """Create an instance of GcpIntegration from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GcpIntegration:
        """Create an instance of GcpIntegration from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GcpIntegration.parse_obj(obj)

        _obj = GcpIntegration.parse_obj(
            {
                "enable_chrome_sync": obj.get("enableChromeSync"),
                "enable_manual_approve_entitlement": obj.get(
                    "enableManualApproveEntitlement"
                ),
                "gcp_project_id": obj.get("gcpProjectId"),
                "gcp_project_number": obj.get("gcpProjectNumber"),
                "identity_provider_id": obj.get("identityProviderId"),
                "login_url": obj.get("loginUrl"),
                "partner_id": obj.get("partnerId"),
                "pubsub_subscription": obj.get("pubsubSubscription"),
                "pubsub_topic": obj.get("pubsubTopic"),
                "report_bucket": obj.get("reportBucket"),
                "report_full_sync_done": obj.get("reportFullSyncDone"),
                "report_start_date": obj.get("reportStartDate"),
                "report_sync_disabled": obj.get("reportSyncDisabled"),
                "revenue_record_full_sync_done": obj.get("revenueRecordFullSyncDone"),
                "revenue_record_sync_disabled": obj.get("revenueRecordSyncDisabled"),
                "service_account_email": obj.get("serviceAccountEmail"),
                "service_names": obj.get("serviceNames"),
                "signup_redirect_without_entitlement_enabled": obj.get(
                    "signupRedirectWithoutEntitlementEnabled"
                ),
                "usage_metering_disabled": obj.get("usageMeteringDisabled"),
                "workload_identity_pool_id": obj.get("workloadIdentityPoolId"),
            }
        )
        return _obj
