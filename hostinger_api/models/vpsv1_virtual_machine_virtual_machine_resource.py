# coding: utf-8

"""
    Hostinger API Python SDK

    API Version: 0.0.6

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
from hostinger_api.models.vpsv1_virtual_machine_virtual_machine_resource_ipv4 import VPSV1VirtualMachineVirtualMachineResourceIpv4
from hostinger_api.models.vpsv1_virtual_machine_virtual_machine_resource_ipv6 import VPSV1VirtualMachineVirtualMachineResourceIpv6
from hostinger_api.models.vpsv1_virtual_machine_virtual_machine_resource_template import VPSV1VirtualMachineVirtualMachineResourceTemplate
from typing import Optional, Set
from typing_extensions import Self

class VPSV1VirtualMachineVirtualMachineResource(BaseModel):
    """
    VPSV1VirtualMachineVirtualMachineResource
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="Virtual machine ID")
    firewall_group_id: Optional[StrictInt] = Field(default=None, description="Active firewall ID, `null` if disabled")
    subscription_id: Optional[StrictStr] = Field(default=None, description="Subscription ID")
    plan: Optional[StrictStr] = Field(default=None, description="VPS plan name")
    hostname: Optional[StrictStr] = None
    state: Optional[StrictStr] = None
    actions_lock: Optional[StrictStr] = None
    cpus: Optional[StrictInt] = Field(default=None, description="CPUs count assigned to virtual machine")
    memory: Optional[StrictInt] = Field(default=None, description="Memory available to virtual machine (in megabytes)")
    disk: Optional[StrictInt] = Field(default=None, description="Virtual machine disk size (in megabytes)")
    bandwidth: Optional[StrictInt] = Field(default=None, description="Monthly internet traffic available to virtual machine (in megabytes)")
    ns1: Optional[StrictStr] = Field(default=None, description="Primary DNS resolver")
    ns2: Optional[StrictStr] = Field(default=None, description="Secondary DNS resolver")
    ipv4: Optional[VPSV1VirtualMachineVirtualMachineResourceIpv4] = None
    ipv6: Optional[VPSV1VirtualMachineVirtualMachineResourceIpv6] = None
    template: Optional[VPSV1VirtualMachineVirtualMachineResourceTemplate] = None
    created_at: Optional[datetime] = None
    __properties: ClassVar[List[str]] = ["id", "firewall_group_id", "subscription_id", "plan", "hostname", "state", "actions_lock", "cpus", "memory", "disk", "bandwidth", "ns1", "ns2", "ipv4", "ipv6", "template", "created_at"]

    @field_validator('state')
    def state_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['running', 'stopped', 'creating', 'initial']):
            raise ValueError("must be one of enum values ('running', 'stopped', 'creating', 'initial')")
        return value

    @field_validator('actions_lock')
    def actions_lock_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['unlocked', 'locked']):
            raise ValueError("must be one of enum values ('unlocked', 'locked')")
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
        """Create an instance of VPSV1VirtualMachineVirtualMachineResource from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of ipv4
        if self.ipv4:
            _dict['ipv4'] = self.ipv4.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ipv6
        if self.ipv6:
            _dict['ipv6'] = self.ipv6.to_dict()
        # override the default output from pydantic by calling `to_dict()` of template
        if self.template:
            _dict['template'] = self.template.to_dict()
        # set to None if firewall_group_id (nullable) is None
        # and model_fields_set contains the field
        if self.firewall_group_id is None and "firewall_group_id" in self.model_fields_set:
            _dict['firewall_group_id'] = None

        # set to None if subscription_id (nullable) is None
        # and model_fields_set contains the field
        if self.subscription_id is None and "subscription_id" in self.model_fields_set:
            _dict['subscription_id'] = None

        # set to None if plan (nullable) is None
        # and model_fields_set contains the field
        if self.plan is None and "plan" in self.model_fields_set:
            _dict['plan'] = None

        # set to None if ns1 (nullable) is None
        # and model_fields_set contains the field
        if self.ns1 is None and "ns1" in self.model_fields_set:
            _dict['ns1'] = None

        # set to None if ns2 (nullable) is None
        # and model_fields_set contains the field
        if self.ns2 is None and "ns2" in self.model_fields_set:
            _dict['ns2'] = None

        # set to None if ipv4 (nullable) is None
        # and model_fields_set contains the field
        if self.ipv4 is None and "ipv4" in self.model_fields_set:
            _dict['ipv4'] = None

        # set to None if ipv6 (nullable) is None
        # and model_fields_set contains the field
        if self.ipv6 is None and "ipv6" in self.model_fields_set:
            _dict['ipv6'] = None

        # set to None if template (nullable) is None
        # and model_fields_set contains the field
        if self.template is None and "template" in self.model_fields_set:
            _dict['template'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of VPSV1VirtualMachineVirtualMachineResource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "firewall_group_id": obj.get("firewall_group_id"),
            "subscription_id": obj.get("subscription_id"),
            "plan": obj.get("plan"),
            "hostname": obj.get("hostname"),
            "state": obj.get("state"),
            "actions_lock": obj.get("actions_lock"),
            "cpus": obj.get("cpus"),
            "memory": obj.get("memory"),
            "disk": obj.get("disk"),
            "bandwidth": obj.get("bandwidth"),
            "ns1": obj.get("ns1"),
            "ns2": obj.get("ns2"),
            "ipv4": VPSV1VirtualMachineVirtualMachineResourceIpv4.from_dict(obj["ipv4"]) if obj.get("ipv4") is not None else None,
            "ipv6": VPSV1VirtualMachineVirtualMachineResourceIpv6.from_dict(obj["ipv6"]) if obj.get("ipv6") is not None else None,
            "template": VPSV1VirtualMachineVirtualMachineResourceTemplate.from_dict(obj["template"]) if obj.get("template") is not None else None,
            "created_at": obj.get("created_at")
        })
        return _obj


