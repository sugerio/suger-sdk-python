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
from suger_sdk_python.models.billable_dimension_fee_detail import BillableDimensionFeeDetail
from suger_sdk_python.models.billing_discount import BillingDiscount
from suger_sdk_python.models.billing_minimum_commit_scope import BillingMinimumCommitScope
from suger_sdk_python.models.metering_usage_record_group_by_key import MeteringUsageRecordGroupByKey
from suger_sdk_python.models.price_model_category import PriceModelCategory
from typing import Optional, Set
from typing_extensions import Self

class BillableDimensionPriceModelDetail(BaseModel):
    """
    BillableDimensionPriceModelDetail
    """ # noqa: E501
    amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Amount is the amount that is calculated based on the FeeExpression")
    billable_metric_key: Optional[MeteringUsageRecordGroupByKey] = Field(default=None, description="BillableMetricKey is the key of the billable metric", alias="billableMetricKey")
    category: Optional[PriceModelCategory] = Field(default=None, description="Category of this billable dimension.")
    details: Optional[List[BillableDimensionFeeDetail]] = Field(default=None, description="Details is the details of the pricing model that is used to show what the amount is for.")
    discount: Optional[BillingDiscount] = Field(default=None, description="The discount of this billable dimension if applicable.")
    discount_expression: Optional[StrictStr] = Field(default=None, description="DiscountExpression is the expression used to calculate the discount that is used to show how the discount is calculated.", alias="discountExpression")
    is_trial: Optional[StrictBool] = Field(default=None, description="Flag to indicate if this period is a trial period.", alias="isTrial")
    minimum_commit: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="MinimumCommit is the minimum commit amount that is used to show the minimum commit amount. Will be ignored if the value is 0 or less.", alias="minimumCommit")
    minimum_commit_scope: Optional[BillingMinimumCommitScope] = Field(default=None, description="The minimum commit scope. The default value is \"DIMENSION\" if not set.", alias="minimumCommitScope")
    name: Optional[StrictStr] = Field(default=None, description="Name of this billable dimension.")
    quantity: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Final quantity of the billable dimension in the invoice period, which calculates the fee in price model. It may be the sum value of count/sum/unique_count or latest/max value according to different aggregation type.")
    __properties: ClassVar[List[str]] = ["amount", "billableMetricKey", "category", "details", "discount", "discountExpression", "isTrial", "minimumCommit", "minimumCommitScope", "name", "quantity"]

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
        """Create an instance of BillableDimensionPriceModelDetail from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of billable_metric_key
        if self.billable_metric_key:
            _dict['billableMetricKey'] = self.billable_metric_key.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in details (list)
        _items = []
        if self.details:
            for _item_details in self.details:
                if _item_details:
                    _items.append(_item_details.to_dict())
            _dict['details'] = _items
        # override the default output from pydantic by calling `to_dict()` of discount
        if self.discount:
            _dict['discount'] = self.discount.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BillableDimensionPriceModelDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "amount": obj.get("amount"),
            "billableMetricKey": MeteringUsageRecordGroupByKey.from_dict(obj["billableMetricKey"]) if obj.get("billableMetricKey") is not None else None,
            "category": obj.get("category"),
            "details": [BillableDimensionFeeDetail.from_dict(_item) for _item in obj["details"]] if obj.get("details") is not None else None,
            "discount": BillingDiscount.from_dict(obj["discount"]) if obj.get("discount") is not None else None,
            "discountExpression": obj.get("discountExpression"),
            "isTrial": obj.get("isTrial"),
            "minimumCommit": obj.get("minimumCommit"),
            "minimumCommitScope": obj.get("minimumCommitScope"),
            "name": obj.get("name"),
            "quantity": obj.get("quantity")
        })
        return _obj


