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
from suger_sdk_python.models.metering_usage_record import MeteringUsageRecord
from suger_sdk_python.models.metering_usage_record_group_meta_info import MeteringUsageRecordGroupMetaInfo
from typing import Optional, Set
from typing_extensions import Self

class CreateUsageRecordGroupParams(BaseModel):
    """
    CreateUsageRecordGroupParams
    """ # noqa: E501
    billable_records: Optional[List[MeteringUsageRecord]] = Field(default=None, description="for usage metering API v2, don't use it together with the records v1.", alias="billableRecords")
    entitlement_id: StrictStr = Field(alias="entitlementID")
    id: Optional[StrictStr] = Field(default=None, description="The uuid of the UsageRecordGroup (the size is up to 36 characters). Optional, if not provided, suger will generate one.")
    meta_info: Optional[MeteringUsageRecordGroupMetaInfo] = Field(default=None, description="read-only, don't set it up when reporting the usage record group.", alias="metaInfo")
    organization_id: StrictStr = Field(alias="organizationID")
    records: Dict[str, Union[StrictFloat, StrictInt]] = Field(description="for usage metering API v1, don't use it together with the billableRecords v2.")
    timestamp: Optional[datetime] = Field(default=None, description="The timestamp of when the usage records were generated. Optional, if not provided, the current report timestamp will be used. This is not the timestamp of when the usage records were reported to Suger.")
    __properties: ClassVar[List[str]] = ["billableRecords", "entitlementID", "id", "metaInfo", "organizationID", "records", "timestamp"]

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
        """Create an instance of CreateUsageRecordGroupParams from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in billable_records (list)
        _items = []
        if self.billable_records:
            for _item_billable_records in self.billable_records:
                if _item_billable_records:
                    _items.append(_item_billable_records.to_dict())
            _dict['billableRecords'] = _items
        # override the default output from pydantic by calling `to_dict()` of meta_info
        if self.meta_info:
            _dict['metaInfo'] = self.meta_info.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateUsageRecordGroupParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "billableRecords": [MeteringUsageRecord.from_dict(_item) for _item in obj["billableRecords"]] if obj.get("billableRecords") is not None else None,
            "entitlementID": obj.get("entitlementID"),
            "id": obj.get("id"),
            "metaInfo": MeteringUsageRecordGroupMetaInfo.from_dict(obj["metaInfo"]) if obj.get("metaInfo") is not None else None,
            "organizationID": obj.get("organizationID"),
            "records": obj.get("records"),
            "timestamp": obj.get("timestamp")
        })
        return _obj


