# coding: utf-8

"""
    Hostinger API Python SDK

    API Version: 0.0.1-beta

    NOTE: This file is auto-generated, DO NOT EDIT THIS FILE MANUALLY!
    If you want to contribute or request a new feature, please create an issue or pull request on https://github.com/hostinger/api
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from hostinger_api.models.vpsv1_template_template_resource import VPSV1TemplateTemplateResource
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

VPSV1VIRTUALMACHINEVIRTUALMACHINERESOURCETEMPLATE_ONE_OF_SCHEMAS = ["VPSV1TemplateTemplateResource"]

class VPSV1VirtualMachineVirtualMachineResourceTemplate(BaseModel):
    """
    OS template installed in virtual machine
    """
    # data type: VPSV1TemplateTemplateResource
    oneof_schema_1_validator: Optional[VPSV1TemplateTemplateResource] = None
    actual_instance: Optional[Union[VPSV1TemplateTemplateResource]] = None
    one_of_schemas: Set[str] = { "VPSV1TemplateTemplateResource" }

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

        instance = VPSV1VirtualMachineVirtualMachineResourceTemplate.model_construct()
        error_messages = []
        match = 0
        # validate data type: VPSV1TemplateTemplateResource
        if not isinstance(v, VPSV1TemplateTemplateResource):
            error_messages.append(f"Error! Input type `{type(v)}` is not `VPSV1TemplateTemplateResource`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in VPSV1VirtualMachineVirtualMachineResourceTemplate with oneOf schemas: VPSV1TemplateTemplateResource. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in VPSV1VirtualMachineVirtualMachineResourceTemplate with oneOf schemas: VPSV1TemplateTemplateResource. Details: " + ", ".join(error_messages))
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

        # deserialize data into VPSV1TemplateTemplateResource
        try:
            instance.actual_instance = VPSV1TemplateTemplateResource.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into VPSV1VirtualMachineVirtualMachineResourceTemplate with oneOf schemas: VPSV1TemplateTemplateResource. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into VPSV1VirtualMachineVirtualMachineResourceTemplate with oneOf schemas: VPSV1TemplateTemplateResource. Details: " + ", ".join(error_messages))
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

    def to_dict(self) -> Optional[Union[Dict[str, Any], VPSV1TemplateTemplateResource]]:
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


