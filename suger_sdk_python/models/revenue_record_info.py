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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from suger_sdk_python.models.github_com_sugerio_marketplace_service_rds_db_lib_billing_aws_billing_event import GithubComSugerioMarketplaceServiceRdsDbLibBillingAwsBillingEvent
from suger_sdk_python.models.github_com_sugerio_marketplace_service_rds_db_lib_billing_azure_cma_revenue import GithubComSugerioMarketplaceServiceRdsDbLibBillingAzureCmaRevenue
from suger_sdk_python.models.github_com_sugerio_marketplace_service_rds_db_lib_billing_gcp_charge_usage import GithubComSugerioMarketplaceServiceRdsDbLibBillingGcpChargeUsage
from typing import Optional, Set
from typing_extensions import Self

class RevenueRecordInfo(BaseModel):
    """
    RevenueRecordInfo
    """ # noqa: E501
    aws_revenue_records: Optional[List[GithubComSugerioMarketplaceServiceRdsDbLibBillingAwsBillingEvent]] = Field(default=None, description="For raw revenue records in AWS Marketplace", alias="awsRevenueRecords")
    azure_revenue_records: Optional[List[GithubComSugerioMarketplaceServiceRdsDbLibBillingAzureCmaRevenue]] = Field(default=None, description="For raw revenue records in Azure Marketplace", alias="azureRevenueRecords")
    credit_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The credit amount used in the revenue record.", alias="creditAmount")
    disbursement_notification_sent: Optional[StrictBool] = Field(default=None, description="Whether the disbursement notification has been sent to the seller/ISV.", alias="disbursementNotificationSent")
    gcp_revenue_records: Optional[List[GithubComSugerioMarketplaceServiceRdsDbLibBillingGcpChargeUsage]] = Field(default=None, description="For raw revenue records in GCP Marketplace", alias="gcpRevenueRecords")
    id_source: Optional[StrictStr] = Field(default=None, description="Source of the revenue record ID.", alias="idSource")
    resource: Optional[StrictStr] = Field(default=None, description="Resource name for the revenue record. Applicable only to GCP Marketplace.")
    __properties: ClassVar[List[str]] = ["awsRevenueRecords", "azureRevenueRecords", "creditAmount", "disbursementNotificationSent", "gcpRevenueRecords", "idSource", "resource"]

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
        """Create an instance of RevenueRecordInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in aws_revenue_records (list)
        _items = []
        if self.aws_revenue_records:
            for _item_aws_revenue_records in self.aws_revenue_records:
                if _item_aws_revenue_records:
                    _items.append(_item_aws_revenue_records.to_dict())
            _dict['awsRevenueRecords'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in azure_revenue_records (list)
        _items = []
        if self.azure_revenue_records:
            for _item_azure_revenue_records in self.azure_revenue_records:
                if _item_azure_revenue_records:
                    _items.append(_item_azure_revenue_records.to_dict())
            _dict['azureRevenueRecords'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in gcp_revenue_records (list)
        _items = []
        if self.gcp_revenue_records:
            for _item_gcp_revenue_records in self.gcp_revenue_records:
                if _item_gcp_revenue_records:
                    _items.append(_item_gcp_revenue_records.to_dict())
            _dict['gcpRevenueRecords'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RevenueRecordInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "awsRevenueRecords": [GithubComSugerioMarketplaceServiceRdsDbLibBillingAwsBillingEvent.from_dict(_item) for _item in obj["awsRevenueRecords"]] if obj.get("awsRevenueRecords") is not None else None,
            "azureRevenueRecords": [GithubComSugerioMarketplaceServiceRdsDbLibBillingAzureCmaRevenue.from_dict(_item) for _item in obj["azureRevenueRecords"]] if obj.get("azureRevenueRecords") is not None else None,
            "creditAmount": obj.get("creditAmount"),
            "disbursementNotificationSent": obj.get("disbursementNotificationSent"),
            "gcpRevenueRecords": [GithubComSugerioMarketplaceServiceRdsDbLibBillingGcpChargeUsage.from_dict(_item) for _item in obj["gcpRevenueRecords"]] if obj.get("gcpRevenueRecords") is not None else None,
            "idSource": obj.get("idSource"),
            "resource": obj.get("resource")
        })
        return _obj


