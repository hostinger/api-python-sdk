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

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from hostinger_api.models.billing_v1_order_store_request_items_inner import BillingV1OrderStoreRequestItemsInner
from typing import Optional, Set
from typing_extensions import Self

class BillingV1OrderStoreRequest(BaseModel):
    """
    BillingV1OrderStoreRequest
    """ # noqa: E501
    payment_method_id: StrictInt = Field(description="Payment method ID")
    items: List[BillingV1OrderStoreRequestItemsInner]
    coupons: Optional[List[Any]] = None
    __properties: ClassVar[List[str]] = ["payment_method_id", "items", "coupons"]

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
        """Create an instance of BillingV1OrderStoreRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in items (list)
        _items = []
        if self.items:
            for _item_items in self.items:
                if _item_items:
                    _items.append(_item_items.to_dict())
            _dict['items'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BillingV1OrderStoreRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "payment_method_id": obj.get("payment_method_id"),
            "items": [BillingV1OrderStoreRequestItemsInner.from_dict(_item) for _item in obj["items"]] if obj.get("items") is not None else None,
            "coupons": obj.get("coupons")
        })
        return _obj


