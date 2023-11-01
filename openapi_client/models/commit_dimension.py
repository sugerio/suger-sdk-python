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


from typing import List, Optional, Union
from pydantic import (
    BaseModel,
    Field,
    StrictBool,
    StrictFloat,
    StrictInt,
    StrictStr,
    conint,
    conlist,
)
from openapi_client.models.commit_dimension_time_unit import CommitDimensionTimeUnit
from openapi_client.models.commit_dimension_type import CommitDimensionType


class CommitDimension(BaseModel):
    """
    The commit dimension. There may be one or more commit dimensions defined in single product, offer or entitlement.  # noqa: E501
    """

    category: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    is_user_created: Optional[StrictBool] = Field(
        None,
        alias="isUserCreated",
        description="Whether this commit dimension is newly created by user, when creating AWS Marketplace Contract private offer.",
    )
    key: Optional[StrictStr] = Field(None, description="API name of the dimension")
    length: Optional[StrictInt] = Field(
        None,
        description="The term length for the commit amount, such as 6 months, or 1 year. The length is used together with timeUnit. If the length is zero, use the TermEndTime.",
    )
    maximum_users: Optional[conint(strict=True, le=1000000, ge=1)] = Field(
        None,
        alias="maximumUsers",
        description="The maximum number of users for PER_USER commit",
    )
    minimum_users: Optional[conint(strict=True, le=1000000, ge=1)] = Field(
        None,
        alias="minimumUsers",
        description="The minimum number of users for PER_USER commit",
    )
    name: Optional[StrictStr] = Field(None, description="Display name of the dimension")
    quantity: Optional[StrictInt] = Field(
        None, description="The quantity of this commit."
    )
    rate: Optional[Union[StrictFloat, StrictInt]] = Field(
        None, description="The commit amount. For GCP, it is monthly commitment."
    )
    term: Optional[StrictStr] = Field(
        None,
        description="The term of the commit amount. It is used for front-end display only.",
    )
    term_end_time: Optional[StrictStr] = Field(
        None, alias="termEndTime", description="The end time of the commit term."
    )
    time_unit: Optional[CommitDimensionTimeUnit] = Field(None, alias="timeUnit")
    type: Optional[CommitDimensionType] = None
    types: Optional[conlist(StrictStr)] = Field(
        None,
        description="These indicate whether the dimension covers metering, entitlement, or support for external metering",
    )
    __properties = [
        "category",
        "description",
        "isUserCreated",
        "key",
        "length",
        "maximumUsers",
        "minimumUsers",
        "name",
        "quantity",
        "rate",
        "term",
        "termEndTime",
        "timeUnit",
        "type",
        "types",
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
    def from_json(cls, json_str: str) -> CommitDimension:
        """Create an instance of CommitDimension from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CommitDimension:
        """Create an instance of CommitDimension from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CommitDimension.parse_obj(obj)

        _obj = CommitDimension.parse_obj(
            {
                "category": obj.get("category"),
                "description": obj.get("description"),
                "is_user_created": obj.get("isUserCreated"),
                "key": obj.get("key"),
                "length": obj.get("length"),
                "maximum_users": obj.get("maximumUsers"),
                "minimum_users": obj.get("minimumUsers"),
                "name": obj.get("name"),
                "quantity": obj.get("quantity"),
                "rate": obj.get("rate"),
                "term": obj.get("term"),
                "term_end_time": obj.get("termEndTime"),
                "time_unit": obj.get("timeUnit"),
                "type": obj.get("type"),
                "types": obj.get("types"),
            }
        )
        return _obj
