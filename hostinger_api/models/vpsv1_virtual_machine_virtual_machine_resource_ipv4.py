# coding: utf-8

"""
    Hostinger API Python SDK

    API Version: 0.0.4

    NOTE: This file is auto-generated, DO NOT EDIT THIS FILE MANUALLY!
    If you want to contribute or request a new feature, please create an issue or pull request on https://github.com/hostinger/api
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from hostinger_api.models.vpsv1_ip_address_ip_address_resource import VPSV1IPAddressIPAddressResource
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

VPSV1VIRTUALMACHINEVIRTUALMACHINERESOURCEIPV4_ONE_OF_SCHEMAS = ["List[VPSV1IPAddressIPAddressResource]"]

class VPSV1VirtualMachineVirtualMachineResourceIpv4(BaseModel):
    """
    IPv4 address of virtual machine
    """
    # data type: List[VPSV1IPAddressIPAddressResource]
    oneof_schema_1_validator: Optional[List[VPSV1IPAddressIPAddressResource]] = Field(default=None, description="Array of [`VPS.V1.IPAddress.IPAddressResource`](#model/vpsv1ipaddressipaddressresource)")
    actual_instance: Optional[Union[List[VPSV1IPAddressIPAddressResource]]] = None
    one_of_schemas: Set[str] = { "List[VPSV1IPAddressIPAddressResource]" }

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )


    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        if v is None:
            return v

        instance = VPSV1VirtualMachineVirtualMachineResourceIpv4.model_construct()
        error_messages = []
        match = 0
        # validate data type: List[VPSV1IPAddressIPAddressResource]
        try:
            instance.oneof_schema_1_validator = v
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in VPSV1VirtualMachineVirtualMachineResourceIpv4 with oneOf schemas: List[VPSV1IPAddressIPAddressResource]. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in VPSV1VirtualMachineVirtualMachineResourceIpv4 with oneOf schemas: List[VPSV1IPAddressIPAddressResource]. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Union[str, Dict[str, Any]]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: Optional[str]) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        if json_str is None:
            return instance

        error_messages = []
        match = 0

        # deserialize data into List[VPSV1IPAddressIPAddressResource]
        try:
            # validation
            instance.oneof_schema_1_validator = json.loads(json_str)
            # assign value to actual_instance
            instance.actual_instance = instance.oneof_schema_1_validator
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into VPSV1VirtualMachineVirtualMachineResourceIpv4 with oneOf schemas: List[VPSV1IPAddressIPAddressResource]. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into VPSV1VirtualMachineVirtualMachineResourceIpv4 with oneOf schemas: List[VPSV1IPAddressIPAddressResource]. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], List[VPSV1IPAddressIPAddressResource]]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


