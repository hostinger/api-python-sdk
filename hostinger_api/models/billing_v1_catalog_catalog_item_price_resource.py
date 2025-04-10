# coding: utf-8

"""
    Hostinger API Python SDK

    API Version: 0.0.4

    NOTE: This file is auto-generated, DO NOT EDIT THIS FILE MANUALLY!
    If you want to contribute or request a new feature, please create an issue or pull request on https://github.com/hostinger/api
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class BillingV1CatalogCatalogItemPriceResource(BaseModel):
    """
    BillingV1CatalogCatalogItemPriceResource
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="Price item ID")
    name: Optional[StrictStr] = Field(default=None, description="Price item name")
    currency: Optional[StrictStr] = Field(default=None, description="Currency code")
    price: Optional[StrictInt] = Field(default=None, description="Price in cents")
    first_period_price: Optional[StrictInt] = Field(default=None, description="First period price in cents")
    period: Optional[StrictInt] = Field(default=None, description="Period")
    period_unit: Optional[StrictStr] = Field(default=None, description="Period unit")
    __properties: ClassVar[List[str]] = ["id", "name", "currency", "price", "first_period_price", "period", "period_unit"]

    @field_validator('period_unit')
    def period_unit_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['day', 'week', 'month', 'year', 'none']):
            raise ValueError("must be one of enum values ('day', 'week', 'month', 'year', 'none')")
        return value

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
        """Create an instance of BillingV1CatalogCatalogItemPriceResource from a JSON string"""
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
        """Create an instance of BillingV1CatalogCatalogItemPriceResource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "currency": obj.get("currency"),
            "price": obj.get("price"),
            "first_period_price": obj.get("first_period_price"),
            "period": obj.get("period"),
            "period_unit": obj.get("period_unit")
        })
        return _obj


