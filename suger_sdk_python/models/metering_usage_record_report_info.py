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
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from suger_sdk_python.models.aggregated_metering_usage_record import AggregatedMeteringUsageRecord
from suger_sdk_python.models.aws_marketplace_metering_batch_meter_usage_input import AwsMarketplaceMeteringBatchMeterUsageInput
from suger_sdk_python.models.azure_marketplace_metering_batch_usage_event import AzureMarketplaceMeteringBatchUsageEvent
from suger_sdk_python.models.client_push_metering_data_request import ClientPushMeteringDataRequest
from suger_sdk_python.models.client_push_metering_data_response_body import ClientPushMeteringDataResponseBody
from suger_sdk_python.models.gcp_marketplace_metering_operation import GcpMarketplaceMeteringOperation
from suger_sdk_python.models.github_com_sugerio_marketplace_service_third_party_azure_sdk_marketplacemeteringv1_batch_usage_event_ok_response import GithubComSugerioMarketplaceServiceThirdPartyAzureSdkMarketplacemeteringv1BatchUsageEventOkResponse
from suger_sdk_python.models.marketplacemetering_batch_meter_usage_output import MarketplacemeteringBatchMeterUsageOutput
from suger_sdk_python.models.servicecontrol_report_response import ServicecontrolReportResponse
from suger_sdk_python.models.usage_record_report_status import UsageRecordReportStatus
from typing import Optional, Set
from typing_extensions import Self

class MeteringUsageRecordReportInfo(BaseModel):
    """
    MeteringUsageRecordReportInfo
    """ # noqa: E501
    aggregated_billable_records: Optional[List[AggregatedMeteringUsageRecord]] = Field(default=None, description="The aggregated billable records from the usage metering API v2.", alias="aggregatedBillableRecords")
    alibaba_metering_request: Optional[ClientPushMeteringDataRequest] = Field(default=None, description="The raw request to call Alibaba metering service.", alias="alibabaMeteringRequest")
    alibaba_metering_response: Optional[ClientPushMeteringDataResponseBody] = Field(default=None, description="The raw response from Alibaba metering service.", alias="alibabaMeteringResponse")
    aws_metering_request: Optional[AwsMarketplaceMeteringBatchMeterUsageInput] = Field(default=None, description="The raw request to call AWS metering service.", alias="awsMeteringRequest")
    aws_metering_response: Optional[MarketplacemeteringBatchMeterUsageOutput] = Field(default=None, description="The raw response from AWS metering service.", alias="awsMeteringResponse")
    azure_metering_request: Optional[AzureMarketplaceMeteringBatchUsageEvent] = Field(default=None, description="The raw request to call Azure metering service.", alias="azureMeteringRequest")
    azure_metering_response: Optional[GithubComSugerioMarketplaceServiceThirdPartyAzureSdkMarketplacemeteringv1BatchUsageEventOkResponse] = Field(default=None, description="The raw response from Azure metering service.", alias="azureMeteringResponse")
    commit_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The amount of the commit if applicable.", alias="commitAmount")
    credit_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The amount of the credit if applicable.", alias="creditAmount")
    credit_records: Optional[Dict[str, Union[StrictFloat, StrictInt]]] = Field(default=None, description="The credit usage records in the map of <DimensionKey, Count> for usage metering API v1.", alias="creditRecords")
    decimal_parts: Optional[Dict[str, Union[StrictFloat, StrictInt]]] = Field(default=None, description="The decimal parts of the usage dimension quantity in the map of <DimensionKey, DecimalPart>, before this usage record report.", alias="decimalParts")
    dimension_categories: Optional[Dict[str, StrictStr]] = Field(default=None, description="The categories of the usage records in the map of <DimensionKey, Category>. The dimension category is required when reporting usage records to Alibaba Marketplace. It comes from the metering dimension category.", alias="dimensionCategories")
    dimension_unit_list_price: Optional[Dict[str, Union[StrictFloat, StrictInt]]] = Field(default=None, description="The public list price of each dimension in the map of <DimensionKey, UnitPrice>.", alias="dimensionUnitListPrice")
    dimension_unit_price: Optional[Dict[str, Union[StrictFloat, StrictInt]]] = Field(default=None, description="The unit price of each dimension in the map of <DimensionKey, UnitPrice>. It can be the negotiated price in the private offer or the public list price.", alias="dimensionUnitPrice")
    end_time: Optional[datetime] = Field(default=None, description="time in UTC when the UsageRecordReport ends", alias="endTime")
    gcp_metering_request: Optional[GcpMarketplaceMeteringOperation] = Field(default=None, description="The raw request to call GCP metering service.", alias="gcpMeteringRequest")
    gcp_metering_response: Optional[ServicecontrolReportResponse] = Field(default=None, description="The raw response from GCP metering service.", alias="gcpMeteringResponse")
    included_records: Optional[Dict[str, Union[StrictFloat, StrictInt]]] = Field(default=None, description="The included usage records in the map of <DimensionKey, Count> for usage metering API v1.", alias="includedRecords")
    message: Optional[StrictStr] = None
    new_decimal_parts: Optional[Dict[str, Union[StrictFloat, StrictInt]]] = Field(default=None, description="The decimal parts of the usage dimension quantity in the map of <DimensionKey, DecimalPart>, after this usage record report.", alias="newDecimalParts")
    partner: Optional[StrictStr] = Field(default=None, description="The partner where this usage record report is sent to. Such as AWS, AZURE or GCP.")
    records_to_report_before_adjustment_at_list_price: Optional[Dict[str, Union[StrictFloat, StrictInt]]] = Field(default=None, description="The usage records to report before the adjustment by the commit with additional usage at list price, in the map of <DimensionKey, Count>.", alias="recordsToReportBeforeAdjustmentAtListPrice")
    reported_records: Optional[Dict[str, Union[StrictFloat, StrictInt]]] = Field(default=None, description="The reported usage records in the map of <DimensionKey, Count> for usage metering API v1.", alias="reportedRecords")
    start_time: Optional[datetime] = Field(default=None, description="time in UTC when the UsageRecordReport starts", alias="startTime")
    status: Optional[UsageRecordReportStatus] = None
    usage_record_group_ids: Optional[List[StrictStr]] = Field(default=None, description="The IDs of UsageRecordGroups aggregated in this UsageRecordReport.", alias="usageRecordGroupIds")
    used_commit_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The amount of the used commit before this usage record report if applicable.", alias="usedCommitAmount")
    used_commit_amount_increment: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The amount of the used commit increment in this usage record report if applicable.", alias="usedCommitAmountIncrement")
    used_credit_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The amount of the used credit before this usage record report if applicable.", alias="usedCreditAmount")
    used_credit_amount_increment: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The amount of the used credit increment in this usage record report if applicable.", alias="usedCreditAmountIncrement")
    __properties: ClassVar[List[str]] = ["aggregatedBillableRecords", "alibabaMeteringRequest", "alibabaMeteringResponse", "awsMeteringRequest", "awsMeteringResponse", "azureMeteringRequest", "azureMeteringResponse", "commitAmount", "creditAmount", "creditRecords", "decimalParts", "dimensionCategories", "dimensionUnitListPrice", "dimensionUnitPrice", "endTime", "gcpMeteringRequest", "gcpMeteringResponse", "includedRecords", "message", "newDecimalParts", "partner", "recordsToReportBeforeAdjustmentAtListPrice", "reportedRecords", "startTime", "status", "usageRecordGroupIds", "usedCommitAmount", "usedCommitAmountIncrement", "usedCreditAmount", "usedCreditAmountIncrement"]

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
        """Create an instance of MeteringUsageRecordReportInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in aggregated_billable_records (list)
        _items = []
        if self.aggregated_billable_records:
            for _item_aggregated_billable_records in self.aggregated_billable_records:
                if _item_aggregated_billable_records:
                    _items.append(_item_aggregated_billable_records.to_dict())
            _dict['aggregatedBillableRecords'] = _items
        # override the default output from pydantic by calling `to_dict()` of alibaba_metering_request
        if self.alibaba_metering_request:
            _dict['alibabaMeteringRequest'] = self.alibaba_metering_request.to_dict()
        # override the default output from pydantic by calling `to_dict()` of alibaba_metering_response
        if self.alibaba_metering_response:
            _dict['alibabaMeteringResponse'] = self.alibaba_metering_response.to_dict()
        # override the default output from pydantic by calling `to_dict()` of aws_metering_request
        if self.aws_metering_request:
            _dict['awsMeteringRequest'] = self.aws_metering_request.to_dict()
        # override the default output from pydantic by calling `to_dict()` of aws_metering_response
        if self.aws_metering_response:
            _dict['awsMeteringResponse'] = self.aws_metering_response.to_dict()
        # override the default output from pydantic by calling `to_dict()` of azure_metering_request
        if self.azure_metering_request:
            _dict['azureMeteringRequest'] = self.azure_metering_request.to_dict()
        # override the default output from pydantic by calling `to_dict()` of azure_metering_response
        if self.azure_metering_response:
            _dict['azureMeteringResponse'] = self.azure_metering_response.to_dict()
        # override the default output from pydantic by calling `to_dict()` of gcp_metering_request
        if self.gcp_metering_request:
            _dict['gcpMeteringRequest'] = self.gcp_metering_request.to_dict()
        # override the default output from pydantic by calling `to_dict()` of gcp_metering_response
        if self.gcp_metering_response:
            _dict['gcpMeteringResponse'] = self.gcp_metering_response.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MeteringUsageRecordReportInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "aggregatedBillableRecords": [AggregatedMeteringUsageRecord.from_dict(_item) for _item in obj["aggregatedBillableRecords"]] if obj.get("aggregatedBillableRecords") is not None else None,
            "alibabaMeteringRequest": ClientPushMeteringDataRequest.from_dict(obj["alibabaMeteringRequest"]) if obj.get("alibabaMeteringRequest") is not None else None,
            "alibabaMeteringResponse": ClientPushMeteringDataResponseBody.from_dict(obj["alibabaMeteringResponse"]) if obj.get("alibabaMeteringResponse") is not None else None,
            "awsMeteringRequest": AwsMarketplaceMeteringBatchMeterUsageInput.from_dict(obj["awsMeteringRequest"]) if obj.get("awsMeteringRequest") is not None else None,
            "awsMeteringResponse": MarketplacemeteringBatchMeterUsageOutput.from_dict(obj["awsMeteringResponse"]) if obj.get("awsMeteringResponse") is not None else None,
            "azureMeteringRequest": AzureMarketplaceMeteringBatchUsageEvent.from_dict(obj["azureMeteringRequest"]) if obj.get("azureMeteringRequest") is not None else None,
            "azureMeteringResponse": GithubComSugerioMarketplaceServiceThirdPartyAzureSdkMarketplacemeteringv1BatchUsageEventOkResponse.from_dict(obj["azureMeteringResponse"]) if obj.get("azureMeteringResponse") is not None else None,
            "commitAmount": obj.get("commitAmount"),
            "creditAmount": obj.get("creditAmount"),
            "creditRecords": obj.get("creditRecords"),
            "decimalParts": obj.get("decimalParts"),
            "dimensionCategories": obj.get("dimensionCategories"),
            "dimensionUnitListPrice": obj.get("dimensionUnitListPrice"),
            "dimensionUnitPrice": obj.get("dimensionUnitPrice"),
            "endTime": obj.get("endTime"),
            "gcpMeteringRequest": GcpMarketplaceMeteringOperation.from_dict(obj["gcpMeteringRequest"]) if obj.get("gcpMeteringRequest") is not None else None,
            "gcpMeteringResponse": ServicecontrolReportResponse.from_dict(obj["gcpMeteringResponse"]) if obj.get("gcpMeteringResponse") is not None else None,
            "includedRecords": obj.get("includedRecords"),
            "message": obj.get("message"),
            "newDecimalParts": obj.get("newDecimalParts"),
            "partner": obj.get("partner"),
            "recordsToReportBeforeAdjustmentAtListPrice": obj.get("recordsToReportBeforeAdjustmentAtListPrice"),
            "reportedRecords": obj.get("reportedRecords"),
            "startTime": obj.get("startTime"),
            "status": obj.get("status"),
            "usageRecordGroupIds": obj.get("usageRecordGroupIds"),
            "usedCommitAmount": obj.get("usedCommitAmount"),
            "usedCommitAmountIncrement": obj.get("usedCommitAmountIncrement"),
            "usedCreditAmount": obj.get("usedCreditAmount"),
            "usedCreditAmountIncrement": obj.get("usedCreditAmountIncrement")
        })
        return _obj


