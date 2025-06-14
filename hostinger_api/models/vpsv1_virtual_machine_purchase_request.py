# coding: utf-8

"""
    Hostinger API Python SDK

    API Version: 0.0.68

    NOTE: This file is auto-generated, DO NOT EDIT THIS FILE MANUALLY!
    If you want to contribute or request a new feature, please create an issue or pull request on https://github.com/hostinger/api
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from hostinger_api.models.vpsv1_virtual_machine_setup_request import VPSV1VirtualMachineSetupRequest
from typing import Optional, Set
from typing_extensions import Self

class VPSV1VirtualMachinePurchaseRequest(BaseModel):
    """
    VPSV1VirtualMachinePurchaseRequest
    """ # noqa: E501
    item_id: StrictStr = Field(description="Catalog price item ID")
    payment_method_id: Optional[StrictInt] = Field(default=None, description="Payment method ID, default will be used if not provided")
    setup: VPSV1VirtualMachineSetupRequest
    coupons: Optional[List[Any]] = Field(default=None, description="Discount coupon codes")
    __properties: ClassVar[List[str]] = ["item_id", "payment_method_id", "setup", "coupons"]

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
        """Create an instance of VPSV1VirtualMachinePurchaseRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of setup
        if self.setup:
            _dict['setup'] = self.setup.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of VPSV1VirtualMachinePurchaseRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "item_id": obj.get("item_id"),
            "payment_method_id": obj.get("payment_method_id"),
            "setup": VPSV1VirtualMachineSetupRequest.from_dict(obj["setup"]) if obj.get("setup") is not None else None,
            "coupons": obj.get("coupons")
        })
        return _obj


