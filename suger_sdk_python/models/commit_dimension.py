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
from typing_extensions import Annotated
from suger_sdk_python.models.commit_dimension_type import CommitDimensionType
from suger_sdk_python.models.time_unit import TimeUnit
from typing import Optional, Set
from typing_extensions import Self

class CommitDimension(BaseModel):
    """
    The commit dimension. There may be one or more commit dimensions defined in single product, offer or entitlement.
    """ # noqa: E501
    category: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    is_user_created: Optional[StrictBool] = Field(default=None, description="Whether this commit dimension is newly created by user, when creating AWS Marketplace Contract private offer.", alias="isUserCreated")
    key: Optional[StrictStr] = Field(default=None, description="API name of the dimension")
    length: Optional[StrictInt] = Field(default=None, description="The term length for the commit amount, such as 6 months, or 1 year. The length is used together with timeUnit. If the length is zero, use the TermEndTime.")
    maximum_users: Optional[Annotated[int, Field(le=1000000, strict=True, ge=1)]] = Field(default=None, description="The maximum number of users for PER_USER commit", alias="maximumUsers")
    minimum_users: Optional[Annotated[int, Field(le=1000000, strict=True, ge=1)]] = Field(default=None, description="The minimum number of users for PER_USER commit", alias="minimumUsers")
    name: Optional[StrictStr] = Field(default=None, description="Display name of the dimension")
    quantity: Optional[StrictInt] = Field(default=None, description="The quantity of this commit.")
    rate: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The commit amount. For GCP, it is monthly commitment.")
    term: Optional[StrictStr] = Field(default=None, description="The term of the commit amount. It is used for front-end display only.")
    term_end_time: Optional[StrictStr] = Field(default=None, description="The end time of the commit term.", alias="termEndTime")
    time_unit: Optional[TimeUnit] = Field(default=None, description="The term unit for the commit amount.", alias="timeUnit")
    type: Optional[CommitDimensionType] = Field(default=None, description="The type of the commit dimension. Applicable only to Azure Marketplace.")
    types: Optional[List[StrictStr]] = Field(default=None, description="These indicate whether the dimension covers metering, entitlement, or support for external metering")
    __properties: ClassVar[List[str]] = ["category", "description", "isUserCreated", "key", "length", "maximumUsers", "minimumUsers", "name", "quantity", "rate", "term", "termEndTime", "timeUnit", "type", "types"]

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
        """Create an instance of CommitDimension from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CommitDimension from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "category": obj.get("category"),
            "description": obj.get("description"),
            "isUserCreated": obj.get("isUserCreated"),
            "key": obj.get("key"),
            "length": obj.get("length"),
            "maximumUsers": obj.get("maximumUsers"),
            "minimumUsers": obj.get("minimumUsers"),
            "name": obj.get("name"),
            "quantity": obj.get("quantity"),
            "rate": obj.get("rate"),
            "term": obj.get("term"),
            "termEndTime": obj.get("termEndTime"),
            "timeUnit": obj.get("timeUnit"),
            "type": obj.get("type"),
            "types": obj.get("types")
        })
        return _obj

