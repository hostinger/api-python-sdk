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
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from hostinger_api.models.dnsv1_zone_record_resource import DNSV1ZoneRecordResource
from typing import Optional, Set
from typing_extensions import Self

class DNSV1SnapshotSnapshotWithContentResource(BaseModel):
    """
    DNSV1SnapshotSnapshotWithContentResource
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="Snapshot ID")
    reason: Optional[StrictStr] = Field(default=None, description="Reason of the update")
    snapshot: Optional[List[DNSV1ZoneRecordResource]] = Field(default=None, description="Array of [`DNS.V1.Zone.RecordResource`](#model/dnsv1zonerecordresource)")
    created_at: Optional[datetime] = None
    __properties: ClassVar[List[str]] = ["id", "reason", "snapshot", "created_at"]

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
        """Create an instance of DNSV1SnapshotSnapshotWithContentResource from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in snapshot (list)
        _items = []
        if self.snapshot:
            for _item_snapshot in self.snapshot:
                if _item_snapshot:
                    _items.append(_item_snapshot.to_dict())
            _dict['snapshot'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DNSV1SnapshotSnapshotWithContentResource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "reason": obj.get("reason"),
            "snapshot": [DNSV1ZoneRecordResource.from_dict(_item) for _item in obj["snapshot"]] if obj.get("snapshot") is not None else None,
            "created_at": obj.get("created_at")
        })
        return _obj


