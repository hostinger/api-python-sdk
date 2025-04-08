# coding: utf-8

"""
    Hostinger API Python SDK

    API Version: 0.0.1-beta

    NOTE: This file is auto-generated, DO NOT EDIT THIS FILE MANUALLY!
    If you want to contribute or request a new feature, please create an issue or pull request on https://github.com/hostinger/api
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from hostinger_api.models.vpsv1_virtual_machine_setup_request_public_key import VPSV1VirtualMachineSetupRequestPublicKey
from typing import Optional, Set
from typing_extensions import Self

class VPSV1VirtualMachineSetupRequest(BaseModel):
    """
    VPSV1VirtualMachineSetupRequest
    """ # noqa: E501
    template_id: StrictInt = Field(description="Template ID")
    data_center_id: StrictInt = Field(description="Data center ID")
    post_install_script_id: Optional[StrictInt] = Field(default=None, description="Post-install script ID")
    password: Annotated[str, Field(min_length=8, strict=True)]
    hostname: Optional[StrictStr] = Field(default=None, description="Override default hostname of the virtual machine")
    install_monarx: Optional[StrictBool] = Field(default=False, description="Install Monarx malware scanner (if supported)")
    enable_backups: Optional[StrictBool] = Field(default=True, description="Enable weekly backup schedule")
    ns1: Optional[StrictStr] = None
    ns2: Optional[StrictStr] = None
    public_key: Optional[VPSV1VirtualMachineSetupRequestPublicKey] = None
    __properties: ClassVar[List[str]] = ["template_id", "data_center_id", "post_install_script_id", "password", "hostname", "install_monarx", "enable_backups", "ns1", "ns2", "public_key"]

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
        """Create an instance of VPSV1VirtualMachineSetupRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of public_key
        if self.public_key:
            _dict['public_key'] = self.public_key.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of VPSV1VirtualMachineSetupRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "template_id": obj.get("template_id"),
            "data_center_id": obj.get("data_center_id"),
            "post_install_script_id": obj.get("post_install_script_id"),
            "password": obj.get("password"),
            "hostname": obj.get("hostname"),
            "install_monarx": obj.get("install_monarx") if obj.get("install_monarx") is not None else False,
            "enable_backups": obj.get("enable_backups") if obj.get("enable_backups") is not None else True,
            "ns1": obj.get("ns1"),
            "ns2": obj.get("ns2"),
            "public_key": VPSV1VirtualMachineSetupRequestPublicKey.from_dict(obj["public_key"]) if obj.get("public_key") is not None else None
        })
        return _obj


