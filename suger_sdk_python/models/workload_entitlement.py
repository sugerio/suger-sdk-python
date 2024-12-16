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
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from suger_sdk_python.models.entitlement_info import EntitlementInfo
from suger_sdk_python.models.entitlement_status import EntitlementStatus
from suger_sdk_python.models.partner import Partner
from suger_sdk_python.models.partner_service import PartnerService
from suger_sdk_python.models.workload_meta_info import WorkloadMetaInfo
from typing import Optional, Set
from typing_extensions import Self

class WorkloadEntitlement(BaseModel):
    """
    WorkloadEntitlement
    """ # noqa: E501
    buyer_id: Optional[StrictStr] = Field(default=None, alias="buyerID")
    creation_time: Optional[datetime] = Field(default=None, alias="creationTime")
    end_time: Optional[datetime] = Field(default=None, description="nullable", alias="endTime")
    entitlement_term_id: Optional[StrictStr] = Field(default=None, alias="entitlementTermID")
    external_buyer_id: Optional[StrictStr] = Field(default=None, alias="externalBuyerID")
    external_id: Optional[StrictStr] = Field(default=None, alias="externalID")
    external_product_id: Optional[StrictStr] = Field(default=None, alias="externalProductID")
    id: Optional[StrictStr] = None
    info: Optional[EntitlementInfo] = None
    last_update_time: Optional[datetime] = Field(default=None, alias="lastUpdateTime")
    meta_info: Optional[WorkloadMetaInfo] = Field(default=None, alias="metaInfo")
    name: Optional[StrictStr] = None
    offer_id: Optional[StrictStr] = Field(default=None, alias="offerID")
    organization_id: Optional[StrictStr] = Field(default=None, alias="organizationID")
    partner: Optional[Partner] = None
    product_id: Optional[StrictStr] = Field(default=None, alias="productID")
    service: Optional[PartnerService] = None
    start_time: Optional[datetime] = Field(default=None, alias="startTime")
    status: Optional[EntitlementStatus] = None
    type: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["buyerID", "creationTime", "endTime", "entitlementTermID", "externalBuyerID", "externalID", "externalProductID", "id", "info", "lastUpdateTime", "metaInfo", "name", "offerID", "organizationID", "partner", "productID", "service", "startTime", "status", "type"]

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
        """Create an instance of WorkloadEntitlement from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of info
        if self.info:
            _dict['info'] = self.info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of meta_info
        if self.meta_info:
            _dict['metaInfo'] = self.meta_info.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WorkloadEntitlement from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "buyerID": obj.get("buyerID"),
            "creationTime": obj.get("creationTime"),
            "endTime": obj.get("endTime"),
            "entitlementTermID": obj.get("entitlementTermID"),
            "externalBuyerID": obj.get("externalBuyerID"),
            "externalID": obj.get("externalID"),
            "externalProductID": obj.get("externalProductID"),
            "id": obj.get("id"),
            "info": EntitlementInfo.from_dict(obj["info"]) if obj.get("info") is not None else None,
            "lastUpdateTime": obj.get("lastUpdateTime"),
            "metaInfo": WorkloadMetaInfo.from_dict(obj["metaInfo"]) if obj.get("metaInfo") is not None else None,
            "name": obj.get("name"),
            "offerID": obj.get("offerID"),
            "organizationID": obj.get("organizationID"),
            "partner": obj.get("partner"),
            "productID": obj.get("productID"),
            "service": obj.get("service"),
            "startTime": obj.get("startTime"),
            "status": obj.get("status"),
            "type": obj.get("type")
        })
        return _obj

