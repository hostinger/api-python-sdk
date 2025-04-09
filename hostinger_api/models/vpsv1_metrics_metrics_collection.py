# coding: utf-8

"""
    Hostinger API Python SDK

    API Version: 0.0.2

    NOTE: This file is auto-generated, DO NOT EDIT THIS FILE MANUALLY!
    If you want to contribute or request a new feature, please create an issue or pull request on https://github.com/hostinger/api
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from hostinger_api.models.vpsv1_metrics_metrics_collection_cpu_usage import VPSV1MetricsMetricsCollectionCpuUsage
from hostinger_api.models.vpsv1_metrics_metrics_collection_disk_space import VPSV1MetricsMetricsCollectionDiskSpace
from hostinger_api.models.vpsv1_metrics_metrics_collection_incoming_traffic import VPSV1MetricsMetricsCollectionIncomingTraffic
from hostinger_api.models.vpsv1_metrics_metrics_collection_outgoing_traffic import VPSV1MetricsMetricsCollectionOutgoingTraffic
from hostinger_api.models.vpsv1_metrics_metrics_collection_ram_usage import VPSV1MetricsMetricsCollectionRamUsage
from hostinger_api.models.vpsv1_metrics_metrics_collection_uptime import VPSV1MetricsMetricsCollectionUptime
from typing import Optional, Set
from typing_extensions import Self

class VPSV1MetricsMetricsCollection(BaseModel):
    """
    VPSV1MetricsMetricsCollection
    """ # noqa: E501
    cpu_usage: Optional[VPSV1MetricsMetricsCollectionCpuUsage] = None
    ram_usage: Optional[VPSV1MetricsMetricsCollectionRamUsage] = None
    disk_space: Optional[VPSV1MetricsMetricsCollectionDiskSpace] = None
    outgoing_traffic: Optional[VPSV1MetricsMetricsCollectionOutgoingTraffic] = None
    incoming_traffic: Optional[VPSV1MetricsMetricsCollectionIncomingTraffic] = None
    uptime: Optional[VPSV1MetricsMetricsCollectionUptime] = None
    __properties: ClassVar[List[str]] = ["cpu_usage", "ram_usage", "disk_space", "outgoing_traffic", "incoming_traffic", "uptime"]

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
        """Create an instance of VPSV1MetricsMetricsCollection from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of cpu_usage
        if self.cpu_usage:
            _dict['cpu_usage'] = self.cpu_usage.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ram_usage
        if self.ram_usage:
            _dict['ram_usage'] = self.ram_usage.to_dict()
        # override the default output from pydantic by calling `to_dict()` of disk_space
        if self.disk_space:
            _dict['disk_space'] = self.disk_space.to_dict()
        # override the default output from pydantic by calling `to_dict()` of outgoing_traffic
        if self.outgoing_traffic:
            _dict['outgoing_traffic'] = self.outgoing_traffic.to_dict()
        # override the default output from pydantic by calling `to_dict()` of incoming_traffic
        if self.incoming_traffic:
            _dict['incoming_traffic'] = self.incoming_traffic.to_dict()
        # override the default output from pydantic by calling `to_dict()` of uptime
        if self.uptime:
            _dict['uptime'] = self.uptime.to_dict()
        # set to None if cpu_usage (nullable) is None
        # and model_fields_set contains the field
        if self.cpu_usage is None and "cpu_usage" in self.model_fields_set:
            _dict['cpu_usage'] = None

        # set to None if ram_usage (nullable) is None
        # and model_fields_set contains the field
        if self.ram_usage is None and "ram_usage" in self.model_fields_set:
            _dict['ram_usage'] = None

        # set to None if disk_space (nullable) is None
        # and model_fields_set contains the field
        if self.disk_space is None and "disk_space" in self.model_fields_set:
            _dict['disk_space'] = None

        # set to None if outgoing_traffic (nullable) is None
        # and model_fields_set contains the field
        if self.outgoing_traffic is None and "outgoing_traffic" in self.model_fields_set:
            _dict['outgoing_traffic'] = None

        # set to None if incoming_traffic (nullable) is None
        # and model_fields_set contains the field
        if self.incoming_traffic is None and "incoming_traffic" in self.model_fields_set:
            _dict['incoming_traffic'] = None

        # set to None if uptime (nullable) is None
        # and model_fields_set contains the field
        if self.uptime is None and "uptime" in self.model_fields_set:
            _dict['uptime'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of VPSV1MetricsMetricsCollection from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "cpu_usage": VPSV1MetricsMetricsCollectionCpuUsage.from_dict(obj["cpu_usage"]) if obj.get("cpu_usage") is not None else None,
            "ram_usage": VPSV1MetricsMetricsCollectionRamUsage.from_dict(obj["ram_usage"]) if obj.get("ram_usage") is not None else None,
            "disk_space": VPSV1MetricsMetricsCollectionDiskSpace.from_dict(obj["disk_space"]) if obj.get("disk_space") is not None else None,
            "outgoing_traffic": VPSV1MetricsMetricsCollectionOutgoingTraffic.from_dict(obj["outgoing_traffic"]) if obj.get("outgoing_traffic") is not None else None,
            "incoming_traffic": VPSV1MetricsMetricsCollectionIncomingTraffic.from_dict(obj["incoming_traffic"]) if obj.get("incoming_traffic") is not None else None,
            "uptime": VPSV1MetricsMetricsCollectionUptime.from_dict(obj["uptime"]) if obj.get("uptime") is not None else None
        })
        return _obj


