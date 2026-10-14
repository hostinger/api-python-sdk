# HostingV1HeadlessStoreAgentReportRequestRun

The run the report is for

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**kind** | **str** |  | 
**skill** | **str** |  | [optional] 
**follow_ups** | **List[object]** |  | [optional] 

## Example

```python
from hostinger_api.models.hosting_v1_headless_store_agent_report_request_run import HostingV1HeadlessStoreAgentReportRequestRun

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1HeadlessStoreAgentReportRequestRun from a JSON string
hosting_v1_headless_store_agent_report_request_run_instance = HostingV1HeadlessStoreAgentReportRequestRun.from_json(json)
# print the JSON string representation of the object
print(HostingV1HeadlessStoreAgentReportRequestRun.to_json())

# convert the object into a dict
hosting_v1_headless_store_agent_report_request_run_dict = hosting_v1_headless_store_agent_report_request_run_instance.to_dict()
# create an instance of HostingV1HeadlessStoreAgentReportRequestRun from a dict
hosting_v1_headless_store_agent_report_request_run_from_dict = HostingV1HeadlessStoreAgentReportRequestRun.from_dict(hosting_v1_headless_store_agent_report_request_run_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


