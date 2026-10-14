# HostingV1HeadlessStoreAgentReportRequestTiming

Run start and end times and per-stage timings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**started_at** | **datetime** |  | 
**ended_at** | **datetime** |  | 
**minutes_total** | **float** |  | 
**stages** | **List[object]** |  | 

## Example

```python
from hostinger_api.models.hosting_v1_headless_store_agent_report_request_timing import HostingV1HeadlessStoreAgentReportRequestTiming

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1HeadlessStoreAgentReportRequestTiming from a JSON string
hosting_v1_headless_store_agent_report_request_timing_instance = HostingV1HeadlessStoreAgentReportRequestTiming.from_json(json)
# print the JSON string representation of the object
print(HostingV1HeadlessStoreAgentReportRequestTiming.to_json())

# convert the object into a dict
hosting_v1_headless_store_agent_report_request_timing_dict = hosting_v1_headless_store_agent_report_request_timing_instance.to_dict()
# create an instance of HostingV1HeadlessStoreAgentReportRequestTiming from a dict
hosting_v1_headless_store_agent_report_request_timing_from_dict = HostingV1HeadlessStoreAgentReportRequestTiming.from_dict(hosting_v1_headless_store_agent_report_request_timing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


