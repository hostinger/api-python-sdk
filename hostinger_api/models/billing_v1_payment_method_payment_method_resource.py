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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class BillingV1PaymentMethodPaymentMethodResource(BaseModel):
    """
    BillingV1PaymentMethodPaymentMethodResource
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="Payment method ID")
    name: Optional[StrictStr] = None
    identifier: Optional[StrictStr] = None
    payment_method: Optional[StrictStr] = None
    is_default: Optional[StrictBool] = None
    is_expired: Optional[StrictBool] = None
    is_suspended: Optional[StrictBool] = None
    created_at: Optional[datetime] = None
    expires_at: Optional[datetime] = None
    __properties: ClassVar[List[str]] = ["id", "name", "identifier", "payment_method", "is_default", "is_expired", "is_suspended", "created_at", "expires_at"]

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
        """Create an instance of BillingV1PaymentMethodPaymentMethodResource from a JSON string"""
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
        """Create an instance of BillingV1PaymentMethodPaymentMethodResource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "identifier": obj.get("identifier"),
            "payment_method": obj.get("payment_method"),
            "is_default": obj.get("is_default"),
            "is_expired": obj.get("is_expired"),
            "is_suspended": obj.get("is_suspended"),
            "created_at": obj.get("created_at"),
            "expires_at": obj.get("expires_at")
        })
        return _obj


