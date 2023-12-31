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


from typing import Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr
from openapi_client.models.orb_billable_metric import OrbBillableMetric
from openapi_client.models.orb_cadence import OrbCadence
from openapi_client.models.orb_item import OrbItem
from openapi_client.models.orb_price_discount import OrbPriceDiscount
from openapi_client.models.orb_price_maximum import OrbPriceMaximum
from openapi_client.models.orb_price_minimum import OrbPriceMinimum
from openapi_client.models.orb_price_model_config_bps import OrbPriceModelConfigBPS
from openapi_client.models.orb_price_model_config_bulk import OrbPriceModelConfigBULK
from openapi_client.models.orb_price_model_config_bulkbps import OrbPriceModelConfigBULKBPS
from openapi_client.models.orb_price_model_config_matrix import OrbPriceModelConfigMATRIX
from openapi_client.models.orb_price_model_config_package import OrbPriceModelConfigPACKAGE
from openapi_client.models.orb_price_model_config_tiered import OrbPriceModelConfigTIERED
from openapi_client.models.orb_price_model_config_tieredbps import OrbPriceModelConfigTIEREDBPS
from openapi_client.models.orb_price_model_config_unit import OrbPriceModelConfigUNIT
from openapi_client.models.orb_price_model_type import OrbPriceModelType

class OrbPrice(BaseModel):
    """
    OrbPrice
    """
    billable_metric: Optional[OrbBillableMetric] = None
    bps_config: Optional[OrbPriceModelConfigBPS] = None
    bulk_bps_config: Optional[OrbPriceModelConfigBULKBPS] = None
    bulk_config: Optional[OrbPriceModelConfigBULK] = None
    cadence: Optional[OrbCadence] = None
    created_at: Optional[StrictStr] = None
    currency: Optional[StrictStr] = None
    discount: Optional[OrbPriceDiscount] = None
    fixed_price_quantity: Optional[StrictInt] = Field(None, description="If the Price represents a fixed cost, this represents the quantity of units applied. Mutually exclusive with billable_metric.")
    id: Optional[StrictStr] = None
    item: Optional[OrbItem] = None
    matrix_config: Optional[OrbPriceModelConfigMATRIX] = None
    maximum: Optional[OrbPriceMaximum] = None
    minimum: Optional[OrbPriceMinimum] = None
    model_type: Optional[OrbPriceModelType] = None
    name: Optional[StrictStr] = None
    package_config: Optional[OrbPriceModelConfigPACKAGE] = None
    plan_phase_order: Optional[StrictInt] = Field(None, description="The phase order which includes this price, only applicable to a plan with phases.")
    tiered_bps_config: Optional[OrbPriceModelConfigTIEREDBPS] = None
    tiered_config: Optional[OrbPriceModelConfigTIERED] = None
    unit_config: Optional[OrbPriceModelConfigUNIT] = None
    __properties = ["billable_metric", "bps_config", "bulk_bps_config", "bulk_config", "cadence", "created_at", "currency", "discount", "fixed_price_quantity", "id", "item", "matrix_config", "maximum", "minimum", "model_type", "name", "package_config", "plan_phase_order", "tiered_bps_config", "tiered_config", "unit_config"]

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
    def from_json(cls, json_str: str) -> OrbPrice:
        """Create an instance of OrbPrice from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of billable_metric
        if self.billable_metric:
            _dict['billable_metric'] = self.billable_metric.to_dict()
        # override the default output from pydantic by calling `to_dict()` of bps_config
        if self.bps_config:
            _dict['bps_config'] = self.bps_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of bulk_bps_config
        if self.bulk_bps_config:
            _dict['bulk_bps_config'] = self.bulk_bps_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of bulk_config
        if self.bulk_config:
            _dict['bulk_config'] = self.bulk_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of discount
        if self.discount:
            _dict['discount'] = self.discount.to_dict()
        # override the default output from pydantic by calling `to_dict()` of item
        if self.item:
            _dict['item'] = self.item.to_dict()
        # override the default output from pydantic by calling `to_dict()` of matrix_config
        if self.matrix_config:
            _dict['matrix_config'] = self.matrix_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of maximum
        if self.maximum:
            _dict['maximum'] = self.maximum.to_dict()
        # override the default output from pydantic by calling `to_dict()` of minimum
        if self.minimum:
            _dict['minimum'] = self.minimum.to_dict()
        # override the default output from pydantic by calling `to_dict()` of package_config
        if self.package_config:
            _dict['package_config'] = self.package_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tiered_bps_config
        if self.tiered_bps_config:
            _dict['tiered_bps_config'] = self.tiered_bps_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tiered_config
        if self.tiered_config:
            _dict['tiered_config'] = self.tiered_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of unit_config
        if self.unit_config:
            _dict['unit_config'] = self.unit_config.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OrbPrice:
        """Create an instance of OrbPrice from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OrbPrice.parse_obj(obj)

        _obj = OrbPrice.parse_obj({
            "billable_metric": OrbBillableMetric.from_dict(obj.get("billable_metric")) if obj.get("billable_metric") is not None else None,
            "bps_config": OrbPriceModelConfigBPS.from_dict(obj.get("bps_config")) if obj.get("bps_config") is not None else None,
            "bulk_bps_config": OrbPriceModelConfigBULKBPS.from_dict(obj.get("bulk_bps_config")) if obj.get("bulk_bps_config") is not None else None,
            "bulk_config": OrbPriceModelConfigBULK.from_dict(obj.get("bulk_config")) if obj.get("bulk_config") is not None else None,
            "cadence": obj.get("cadence"),
            "created_at": obj.get("created_at"),
            "currency": obj.get("currency"),
            "discount": OrbPriceDiscount.from_dict(obj.get("discount")) if obj.get("discount") is not None else None,
            "fixed_price_quantity": obj.get("fixed_price_quantity"),
            "id": obj.get("id"),
            "item": OrbItem.from_dict(obj.get("item")) if obj.get("item") is not None else None,
            "matrix_config": OrbPriceModelConfigMATRIX.from_dict(obj.get("matrix_config")) if obj.get("matrix_config") is not None else None,
            "maximum": OrbPriceMaximum.from_dict(obj.get("maximum")) if obj.get("maximum") is not None else None,
            "minimum": OrbPriceMinimum.from_dict(obj.get("minimum")) if obj.get("minimum") is not None else None,
            "model_type": obj.get("model_type"),
            "name": obj.get("name"),
            "package_config": OrbPriceModelConfigPACKAGE.from_dict(obj.get("package_config")) if obj.get("package_config") is not None else None,
            "plan_phase_order": obj.get("plan_phase_order"),
            "tiered_bps_config": OrbPriceModelConfigTIEREDBPS.from_dict(obj.get("tiered_bps_config")) if obj.get("tiered_bps_config") is not None else None,
            "tiered_config": OrbPriceModelConfigTIERED.from_dict(obj.get("tiered_config")) if obj.get("tiered_config") is not None else None,
            "unit_config": OrbPriceModelConfigUNIT.from_dict(obj.get("unit_config")) if obj.get("unit_config") is not None else None
        })
        return _obj


