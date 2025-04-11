# coding: utf-8

"""
    Hostinger API Python SDK

    API Version: 0.0.14

    NOTE: This file is auto-generated, DO NOT EDIT THIS FILE MANUALLY!
    If you want to contribute or request a new feature, please create an issue or pull request on https://github.com/hostinger/api
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from @hostinger/api.models.common_schema_pagination_meta_schema import CommonSchemaPaginationMetaSchema
from @hostinger/api.models.vpsv1_public_key_public_key_resource import VPSV1PublicKeyPublicKeyResource
from typing import Optional, Set
from typing_extensions import Self

class VPSGetPublicKeyListV1200Response(BaseModel):
    """
    VPSGetPublicKeyListV1200Response
    """ # noqa: E501
    data: Optional[List[VPSV1PublicKeyPublicKeyResource]] = Field(default=None, description="Array of [`VPS.V1.PublicKey.PublicKeyResource`](#model/vpsv1publickeypublickeyresource)")
    meta: Optional[CommonSchemaPaginationMetaSchema] = None
    __properties: ClassVar[List[str]] = ["data", "meta"]

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
        """Create an instance of VPSGetPublicKeyListV1200Response from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in data (list)
        _items = []
        if self.data:
            for _item_data in self.data:
                if _item_data:
                    _items.append(_item_data.to_dict())
            _dict['data'] = _items
        # override the default output from pydantic by calling `to_dict()` of meta
        if self.meta:
            _dict['meta'] = self.meta.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of VPSGetPublicKeyListV1200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "data": [VPSV1PublicKeyPublicKeyResource.from_dict(_item) for _item in obj["data"]] if obj.get("data") is not None else None,
            "meta": CommonSchemaPaginationMetaSchema.from_dict(obj["meta"]) if obj.get("meta") is not None else None
        })
        return _obj


