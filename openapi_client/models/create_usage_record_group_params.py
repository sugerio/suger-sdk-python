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
from typing import Dict, Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr
from openapi_client.models.metering_usage_record_group_meta_info import MeteringUsageRecordGroupMetaInfo

class CreateUsageRecordGroupParams(BaseModel):
    """
    CreateUsageRecordGroupParams
    """
    entitlement_id: StrictStr = Field(..., alias="entitlementID")
    id: Optional[StrictStr] = Field(None, description="The uuid of the UsageRecordGroup (the size is up to 36 characters). Optional, if not provided, suger will generate one.")
    meta_info: Optional[MeteringUsageRecordGroupMetaInfo] = Field(None, alias="metaInfo")
    organization_id: StrictStr = Field(..., alias="organizationID")
    records: Dict[str, Union[StrictFloat, StrictInt]] = Field(...)
    timestamp: Optional[datetime] = Field(None, description="The timestamp of when the usage records were generated. Optional, if not provided, the current report timestamp will be used. This is not the timestamp of when the usage records were reported to Suger.")
    __properties = ["entitlementID", "id", "metaInfo", "organizationID", "records", "timestamp"]

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
    def from_json(cls, json_str: str) -> CreateUsageRecordGroupParams:
        """Create an instance of CreateUsageRecordGroupParams from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of meta_info
        if self.meta_info:
            _dict['metaInfo'] = self.meta_info.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CreateUsageRecordGroupParams:
        """Create an instance of CreateUsageRecordGroupParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CreateUsageRecordGroupParams.parse_obj(obj)

        _obj = CreateUsageRecordGroupParams.parse_obj({
            "entitlement_id": obj.get("entitlementID"),
            "id": obj.get("id"),
            "meta_info": MeteringUsageRecordGroupMetaInfo.from_dict(obj.get("metaInfo")) if obj.get("metaInfo") is not None else None,
            "organization_id": obj.get("organizationID"),
            "records": obj.get("records"),
            "timestamp": obj.get("timestamp")
        })
        return _obj


