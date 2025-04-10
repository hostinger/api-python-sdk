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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List
from typing import Optional, Set
from typing_extensions import Self

class VPSV1FirewallRulesStoreRequest(BaseModel):
    """
    VPSV1FirewallRulesStoreRequest
    """ # noqa: E501
    protocol: StrictStr
    port: StrictStr = Field(description="Port or port range, ex: 1024:2048")
    source: StrictStr
    source_detail: StrictStr = Field(description="IP range, CIDR, single IP or `any`")
    __properties: ClassVar[List[str]] = ["protocol", "port", "source", "source_detail"]

    @field_validator('protocol')
    def protocol_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['TCP', 'UDP', 'ICMP', 'GRE', 'any', 'ESP', 'AH', 'ICMPv6', 'SSH', 'HTTP', 'HTTPS', 'MySQL', 'PostgreSQL']):
            raise ValueError("must be one of enum values ('TCP', 'UDP', 'ICMP', 'GRE', 'any', 'ESP', 'AH', 'ICMPv6', 'SSH', 'HTTP', 'HTTPS', 'MySQL', 'PostgreSQL')")
        return value

    @field_validator('source')
    def source_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['any', 'custom']):
            raise ValueError("must be one of enum values ('any', 'custom')")
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
        """Create an instance of VPSV1FirewallRulesStoreRequest from a JSON string"""
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
        """Create an instance of VPSV1FirewallRulesStoreRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "protocol": obj.get("protocol"),
            "port": obj.get("port"),
            "source": obj.get("source"),
            "source_detail": obj.get("source_detail")
        })
        return _obj


