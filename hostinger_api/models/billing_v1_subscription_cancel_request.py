# coding: utf-8

"""
    Hostinger API Python SDK

    API Version: 0.0.16

    NOTE: This file is auto-generated, DO NOT EDIT THIS FILE MANUALLY!
    If you want to contribute or request a new feature, please create an issue or pull request on https://github.com/hostinger/api
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class BillingV1SubscriptionCancelRequest(BaseModel):
    """
    BillingV1SubscriptionCancelRequest
    """ # noqa: E501
    reason_code: Optional[StrictStr] = Field(default=None, description="Cancellation reason code")
    cancel_option: Optional[StrictStr] = Field(default=None, description="Cancellation option")
    __properties: ClassVar[List[str]] = ["reason_code", "cancel_option"]

    @field_validator('reason_code')
    def reason_code_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['other']):
            raise ValueError("must be one of enum values ('other')")
        return value

    @field_validator('cancel_option')
    def cancel_option_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['immediately']):
            raise ValueError("must be one of enum values ('immediately')")
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
        """Create an instance of BillingV1SubscriptionCancelRequest from a JSON string"""
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
        # set to None if reason_code (nullable) is None
        # and model_fields_set contains the field
        if self.reason_code is None and "reason_code" in self.model_fields_set:
            _dict['reason_code'] = None

        # set to None if cancel_option (nullable) is None
        # and model_fields_set contains the field
        if self.cancel_option is None and "cancel_option" in self.model_fields_set:
            _dict['cancel_option'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BillingV1SubscriptionCancelRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "reason_code": obj.get("reason_code"),
            "cancel_option": obj.get("cancel_option")
        })
        return _obj


