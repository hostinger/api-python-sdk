# HostingV1HeadlessAgentReportResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Stored report ID | [optional] 
**run_id** | **str** | ID of the run the report is for | [optional] 
**created_at** | **datetime** | When the report was received | [optional] 

## Example

```python
from hostinger_api.models.hosting_v1_headless_agent_report_resource import HostingV1HeadlessAgentReportResource

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1HeadlessAgentReportResource from a JSON string
hosting_v1_headless_agent_report_resource_instance = HostingV1HeadlessAgentReportResource.from_json(json)
# print the JSON string representation of the object
print(HostingV1HeadlessAgentReportResource.to_json())

# convert the object into a dict
hosting_v1_headless_agent_report_resource_dict = hosting_v1_headless_agent_report_resource_instance.to_dict()
# create an instance of HostingV1HeadlessAgentReportResource from a dict
hosting_v1_headless_agent_report_resource_from_dict = HostingV1HeadlessAgentReportResource.from_dict(hosting_v1_headless_agent_report_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


