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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from suger_sdk_python.models.alibaba_marketplace_product import AlibabaMarketplaceProduct
from suger_sdk_python.models.aws_product import AwsProduct
from suger_sdk_python.models.aws_sns_subscription import AwsSnsSubscription
from suger_sdk_python.models.azure_marketplace_product_resource import AzureMarketplaceProductResource
from suger_sdk_python.models.azure_product import AzureProduct
from suger_sdk_python.models.commit_dimension import CommitDimension
from suger_sdk_python.models.eula_type import EulaType
from suger_sdk_python.models.gcp_marketplace_product import GcpMarketplaceProduct
from suger_sdk_python.models.metering_dimension import MeteringDimension
from suger_sdk_python.models.pkg_structs_snowflake_marketplace_product import PkgStructsSnowflakeMarketplaceProduct
from suger_sdk_python.models.stripe_product import StripeProduct
from typing import Optional, Set
from typing_extensions import Self

class ProductInfo(BaseModel):
    """
    ProductInfo
    """ # noqa: E501
    alibaba_product: Optional[AlibabaMarketplaceProduct] = Field(default=None, alias="alibabaProduct")
    attributes: Optional[Dict[str, StrictStr]] = None
    aws_ami_product: Optional[AwsProduct] = Field(default=None, alias="awsAmiProduct")
    aws_container_product: Optional[AwsProduct] = Field(default=None, alias="awsContainerProduct")
    aws_professional_services_product: Optional[AwsProduct] = Field(default=None, alias="awsProfessionalServicesProduct")
    aws_saas_product: Optional[AwsProduct] = Field(default=None, alias="awsSaasProduct")
    aws_sns_subscriptions: Optional[List[AwsSnsSubscription]] = Field(default=None, alias="awsSnsSubscriptions")
    azure_product: Optional[AzureProduct] = Field(default=None, alias="azureProduct")
    azure_product_resource: Optional[AzureMarketplaceProductResource] = Field(default=None, alias="azureProductResource")
    commits: Optional[List[CommitDimension]] = None
    currency: Optional[StrictStr] = None
    dimensions: Optional[List[MeteringDimension]] = None
    eula_type: Optional[EulaType] = Field(default=None, description="The public offer's EULA type.", alias="eulaType")
    eula_url: Optional[StrictStr] = Field(default=None, description="The public offer's EULA URL.", alias="eulaUrl")
    gcp_product: Optional[GcpMarketplaceProduct] = Field(default=None, alias="gcpProduct")
    refund_cancellation_policy: Optional[StrictStr] = Field(default=None, alias="refundCancellationPolicy")
    seller_notes: Optional[StrictStr] = Field(default=None, alias="sellerNotes")
    snowflake_product: Optional[PkgStructsSnowflakeMarketplaceProduct] = Field(default=None, alias="snowflakeProduct")
    stripe_product: Optional[StripeProduct] = Field(default=None, alias="stripeProduct")
    __properties: ClassVar[List[str]] = ["alibabaProduct", "attributes", "awsAmiProduct", "awsContainerProduct", "awsProfessionalServicesProduct", "awsSaasProduct", "awsSnsSubscriptions", "azureProduct", "azureProductResource", "commits", "currency", "dimensions", "eulaType", "eulaUrl", "gcpProduct", "refundCancellationPolicy", "sellerNotes", "snowflakeProduct", "stripeProduct"]

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
        """Create an instance of ProductInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of alibaba_product
        if self.alibaba_product:
            _dict['alibabaProduct'] = self.alibaba_product.to_dict()
        # override the default output from pydantic by calling `to_dict()` of aws_ami_product
        if self.aws_ami_product:
            _dict['awsAmiProduct'] = self.aws_ami_product.to_dict()
        # override the default output from pydantic by calling `to_dict()` of aws_container_product
        if self.aws_container_product:
            _dict['awsContainerProduct'] = self.aws_container_product.to_dict()
        # override the default output from pydantic by calling `to_dict()` of aws_professional_services_product
        if self.aws_professional_services_product:
            _dict['awsProfessionalServicesProduct'] = self.aws_professional_services_product.to_dict()
        # override the default output from pydantic by calling `to_dict()` of aws_saas_product
        if self.aws_saas_product:
            _dict['awsSaasProduct'] = self.aws_saas_product.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in aws_sns_subscriptions (list)
        _items = []
        if self.aws_sns_subscriptions:
            for _item_aws_sns_subscriptions in self.aws_sns_subscriptions:
                if _item_aws_sns_subscriptions:
                    _items.append(_item_aws_sns_subscriptions.to_dict())
            _dict['awsSnsSubscriptions'] = _items
        # override the default output from pydantic by calling `to_dict()` of azure_product
        if self.azure_product:
            _dict['azureProduct'] = self.azure_product.to_dict()
        # override the default output from pydantic by calling `to_dict()` of azure_product_resource
        if self.azure_product_resource:
            _dict['azureProductResource'] = self.azure_product_resource.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in commits (list)
        _items = []
        if self.commits:
            for _item_commits in self.commits:
                if _item_commits:
                    _items.append(_item_commits.to_dict())
            _dict['commits'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in dimensions (list)
        _items = []
        if self.dimensions:
            for _item_dimensions in self.dimensions:
                if _item_dimensions:
                    _items.append(_item_dimensions.to_dict())
            _dict['dimensions'] = _items
        # override the default output from pydantic by calling `to_dict()` of gcp_product
        if self.gcp_product:
            _dict['gcpProduct'] = self.gcp_product.to_dict()
        # override the default output from pydantic by calling `to_dict()` of snowflake_product
        if self.snowflake_product:
            _dict['snowflakeProduct'] = self.snowflake_product.to_dict()
        # override the default output from pydantic by calling `to_dict()` of stripe_product
        if self.stripe_product:
            _dict['stripeProduct'] = self.stripe_product.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ProductInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "alibabaProduct": AlibabaMarketplaceProduct.from_dict(obj["alibabaProduct"]) if obj.get("alibabaProduct") is not None else None,
            "attributes": obj.get("attributes"),
            "awsAmiProduct": AwsProduct.from_dict(obj["awsAmiProduct"]) if obj.get("awsAmiProduct") is not None else None,
            "awsContainerProduct": AwsProduct.from_dict(obj["awsContainerProduct"]) if obj.get("awsContainerProduct") is not None else None,
            "awsProfessionalServicesProduct": AwsProduct.from_dict(obj["awsProfessionalServicesProduct"]) if obj.get("awsProfessionalServicesProduct") is not None else None,
            "awsSaasProduct": AwsProduct.from_dict(obj["awsSaasProduct"]) if obj.get("awsSaasProduct") is not None else None,
            "awsSnsSubscriptions": [AwsSnsSubscription.from_dict(_item) for _item in obj["awsSnsSubscriptions"]] if obj.get("awsSnsSubscriptions") is not None else None,
            "azureProduct": AzureProduct.from_dict(obj["azureProduct"]) if obj.get("azureProduct") is not None else None,
            "azureProductResource": AzureMarketplaceProductResource.from_dict(obj["azureProductResource"]) if obj.get("azureProductResource") is not None else None,
            "commits": [CommitDimension.from_dict(_item) for _item in obj["commits"]] if obj.get("commits") is not None else None,
            "currency": obj.get("currency"),
            "dimensions": [MeteringDimension.from_dict(_item) for _item in obj["dimensions"]] if obj.get("dimensions") is not None else None,
            "eulaType": obj.get("eulaType"),
            "eulaUrl": obj.get("eulaUrl"),
            "gcpProduct": GcpMarketplaceProduct.from_dict(obj["gcpProduct"]) if obj.get("gcpProduct") is not None else None,
            "refundCancellationPolicy": obj.get("refundCancellationPolicy"),
            "sellerNotes": obj.get("sellerNotes"),
            "snowflakeProduct": PkgStructsSnowflakeMarketplaceProduct.from_dict(obj["snowflakeProduct"]) if obj.get("snowflakeProduct") is not None else None,
            "stripeProduct": StripeProduct.from_dict(obj["stripeProduct"]) if obj.get("stripeProduct") is not None else None
        })
        return _obj


