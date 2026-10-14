# HostingV1HeadlessStoreAgentReportRequest

Headless build report (report.schema.json v1), as written by the headless skill at the end of a run. Send the report unchanged.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_version** | **str** | Report schema version | 
**generated_at** | **datetime** | When the report was written | 
**consent** | [**HostingV1HeadlessStoreAgentReportRequestConsent**](HostingV1HeadlessStoreAgentReportRequestConsent.md) |  | 
**run** | [**HostingV1HeadlessStoreAgentReportRequestRun**](HostingV1HeadlessStoreAgentReportRequestRun.md) |  | 
**info** | [**HostingV1HeadlessStoreAgentReportRequestInfo**](HostingV1HeadlessStoreAgentReportRequestInfo.md) |  | 
**timing** | [**HostingV1HeadlessStoreAgentReportRequestTiming**](HostingV1HeadlessStoreAgentReportRequestTiming.md) |  | 
**tokens** | **object** | Token usage, only when the tool reports its own usage | 
**issues** | **List[object]** | Problems hit during the run | 
**user_feedback** | **List[object]** | Feedback the user gave during the run | 
**skill_gaps** | **List[object]** | Places where the skill instructions were missing or wrong | 
**what_went_well** | **List[object]** | Things that worked well during the run | 
**logging_gaps** | **List[object]** | Where the run log is missing or unsure | [optional] 
**previous_runs** | **List[object]** | Earlier runs for the same website | 

## Example

```python
from hostinger_api.models.hosting_v1_headless_store_agent_report_request import HostingV1HeadlessStoreAgentReportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1HeadlessStoreAgentReportRequest from a JSON string
hosting_v1_headless_store_agent_report_request_instance = HostingV1HeadlessStoreAgentReportRequest.from_json(json)
# print the JSON string representation of the object
print(HostingV1HeadlessStoreAgentReportRequest.to_json())

# convert the object into a dict
hosting_v1_headless_store_agent_report_request_dict = hosting_v1_headless_store_agent_report_request_instance.to_dict()
# create an instance of HostingV1HeadlessStoreAgentReportRequest from a dict
hosting_v1_headless_store_agent_report_request_from_dict = HostingV1HeadlessStoreAgentReportRequest.from_dict(hosting_v1_headless_store_agent_report_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


