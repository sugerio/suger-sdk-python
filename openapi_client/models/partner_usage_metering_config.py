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


from typing import Dict, Optional
from pydantic import BaseModel, Field, StrictBool
from openapi_client.models.partner import Partner
from openapi_client.models.usage_metering_dimension_mapping_value import UsageMeteringDimensionMappingValue

class PartnerUsageMeteringConfig(BaseModel):
    """
    PartnerUsageMeteringConfig
    """
    dimension_mapping: Optional[Dict[str, UsageMeteringDimensionMappingValue]] = Field(None, alias="dimensionMapping", description="The mapping of the source dimension key to the destination dimension key of the usage metering.")
    enable_commit_with_additional_usage_at_list_price: Optional[StrictBool] = Field(None, alias="enableCommitWithAdditionalUsageAtListPrice", description="Enable the commit (discount) with additional usage metering at list price. Only applicable if EnableCommitWithAdditionalUsageMetering is true. The default is false, which means the commit with additional usage metering at the discounted price in the private offer. If set to true, the additional usage is metered at the list price (the price in public product listing) instead of the discounted price.")
    enable_commit_with_additional_usage_metering: Optional[StrictBool] = Field(None, alias="enableCommitWithAdditionalUsageMetering", description="Enable the commit with additional usage metering. The default is false, which means all usage records are reported to partner no matter how much is the commit. If set to true, the usage records will be reported to partner only if the current commit has been exhausted.")
    enable_dimension_mapping: Optional[StrictBool] = Field(None, alias="enableDimensionMapping", description="Enable the dimension mapping for the usage metering. The default is false, which means no dimension conversion and just use the origin dimension.")
    partner: Optional[Partner] = None
    __properties = ["dimensionMapping", "enableCommitWithAdditionalUsageAtListPrice", "enableCommitWithAdditionalUsageMetering", "enableDimensionMapping", "partner"]

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
    def from_json(cls, json_str: str) -> PartnerUsageMeteringConfig:
        """Create an instance of PartnerUsageMeteringConfig from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each value in dimension_mapping (dict)
        _field_dict = {}
        if self.dimension_mapping:
            for _key in self.dimension_mapping:
                if self.dimension_mapping[_key]:
                    _field_dict[_key] = self.dimension_mapping[_key].to_dict()
            _dict['dimensionMapping'] = _field_dict
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PartnerUsageMeteringConfig:
        """Create an instance of PartnerUsageMeteringConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PartnerUsageMeteringConfig.parse_obj(obj)

        _obj = PartnerUsageMeteringConfig.parse_obj({
            "dimension_mapping": dict(
                (_k, UsageMeteringDimensionMappingValue.from_dict(_v))
                for _k, _v in obj.get("dimensionMapping").items()
            )
            if obj.get("dimensionMapping") is not None
            else None,
            "enable_commit_with_additional_usage_at_list_price": obj.get("enableCommitWithAdditionalUsageAtListPrice"),
            "enable_commit_with_additional_usage_metering": obj.get("enableCommitWithAdditionalUsageMetering"),
            "enable_dimension_mapping": obj.get("enableDimensionMapping"),
            "partner": obj.get("partner")
        })
        return _obj


