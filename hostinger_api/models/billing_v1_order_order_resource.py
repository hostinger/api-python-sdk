# coding: utf-8

"""
    Hostinger API Python SDK

    API Version: 0.0.20

    NOTE: This file is auto-generated, DO NOT EDIT THIS FILE MANUALLY!
    If you want to contribute or request a new feature, please create an issue or pull request on https://github.com/hostinger/api
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from hostinger_api.models.billing_v1_order_order_billing_address_resource import BillingV1OrderOrderBillingAddressResource
from typing import Optional, Set
from typing_extensions import Self

class BillingV1OrderOrderResource(BaseModel):
    """
    BillingV1OrderOrderResource
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="Order ID")
    subscription_id: Optional[StrictStr] = Field(default=None, description="Subscription ID")
    status: Optional[StrictStr] = None
    currency: Optional[StrictStr] = Field(default=None, description="Currency code")
    subtotal: Optional[StrictInt] = Field(default=None, description="Subtotal price (exc. VAT) in cents")
    total: Optional[StrictInt] = Field(default=None, description="Total price (inc. VAT) in cents")
    billing_address: Optional[BillingV1OrderOrderBillingAddressResource] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    __properties: ClassVar[List[str]] = ["id", "subscription_id", "status", "currency", "subtotal", "total", "billing_address", "created_at", "updated_at"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['completed', 'pending', 'processing', 'failed', 'refunded', 'cancelled', 'awaiting_payment', 'payment_initiated', 'fraud_refund']):
            raise ValueError("must be one of enum values ('completed', 'pending', 'processing', 'failed', 'refunded', 'cancelled', 'awaiting_payment', 'payment_initiated', 'fraud_refund')")
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
        """Create an instance of BillingV1OrderOrderResource from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of billing_address
        if self.billing_address:
            _dict['billing_address'] = self.billing_address.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BillingV1OrderOrderResource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "subscription_id": obj.get("subscription_id"),
            "status": obj.get("status"),
            "currency": obj.get("currency"),
            "subtotal": obj.get("subtotal"),
            "total": obj.get("total"),
            "billing_address": BillingV1OrderOrderBillingAddressResource.from_dict(obj["billing_address"]) if obj.get("billing_address") is not None else None,
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at")
        })
        return _obj


