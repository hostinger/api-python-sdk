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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from hostinger_api.models.dnsv1_zone_name_record_resource import DNSV1ZoneNameRecordResource
from typing import Optional, Set
from typing_extensions import Self

class DNSV1ZoneRecordResource(BaseModel):
    """
    DNSV1ZoneRecordResource
    """ # noqa: E501
    name: Optional[StrictStr] = Field(default=None, description="Name of the record (use `@` for wildcard name)")
    records: Optional[List[DNSV1ZoneNameRecordResource]] = Field(default=None, description="Array of [`DNS.V1.Zone.NameRecordResource`](#model/dnsv1zonenamerecordresource)")
    ttl: Optional[StrictInt] = Field(default=None, description="TTL (Time-To-Live) of the record")
    type: Optional[StrictStr] = Field(default=None, description="Type of the record")
    __properties: ClassVar[List[str]] = ["name", "records", "ttl", "type"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['A', 'AAAA', 'CNAME', 'ALIAS', 'MX', 'TXT', 'NS', 'SOA', 'SRV', 'CAA']):
            raise ValueError("must be one of enum values ('A', 'AAAA', 'CNAME', 'ALIAS', 'MX', 'TXT', 'NS', 'SOA', 'SRV', 'CAA')")
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
        """Create an instance of DNSV1ZoneRecordResource from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in records (list)
        _items = []
        if self.records:
            for _item_records in self.records:
                if _item_records:
                    _items.append(_item_records.to_dict())
            _dict['records'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DNSV1ZoneRecordResource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "records": [DNSV1ZoneNameRecordResource.from_dict(_item) for _item in obj["records"]] if obj.get("records") is not None else None,
            "ttl": obj.get("ttl"),
            "type": obj.get("type")
        })
        return _obj


