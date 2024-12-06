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
from typing import Optional, Set
from typing_extensions import Self

class AzureADIdentifier(BaseModel):
    """
    AzureADIdentifier
    """ # noqa: E501
    billing_account_id: Optional[StrictStr] = Field(default=None, description="Azure Billing Account ID", alias="billingAccountId")
    customer_id: Optional[StrictStr] = Field(default=None, alias="customerId")
    email_id: Optional[StrictStr] = Field(default=None, description="Email address", alias="emailId")
    first_name: Optional[StrictStr] = Field(default=None, alias="firstName")
    last_name: Optional[StrictStr] = Field(default=None, alias="lastName")
    license_type: Optional[StrictStr] = Field(default=None, description="Azure License Type", alias="licenseType")
    object_id: Optional[StrictStr] = Field(default=None, alias="objectId")
    puid: Optional[StrictStr] = Field(default=None, description="ID of the user, used as External ID of suger IdentityBuyer.")
    tenant_id: Optional[StrictStr] = Field(default=None, alias="tenantId")
    __properties: ClassVar[List[str]] = ["billingAccountId", "customerId", "emailId", "firstName", "lastName", "licenseType", "objectId", "puid", "tenantId"]

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
        """Create an instance of AzureADIdentifier from a JSON string"""
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
        """Create an instance of AzureADIdentifier from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "billingAccountId": obj.get("billingAccountId"),
            "customerId": obj.get("customerId"),
            "emailId": obj.get("emailId"),
            "firstName": obj.get("firstName"),
            "lastName": obj.get("lastName"),
            "licenseType": obj.get("licenseType"),
            "objectId": obj.get("objectId"),
            "puid": obj.get("puid"),
            "tenantId": obj.get("tenantId")
        })
        return _obj


