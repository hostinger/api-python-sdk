# AgentReadinessV1ScansRunScanRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | Domain name or full URL of the website to scan. Only the host is used. | 

## Example

```python
from hostinger_api.models.agent_readiness_v1_scans_run_scan_request import AgentReadinessV1ScansRunScanRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AgentReadinessV1ScansRunScanRequest from a JSON string
agent_readiness_v1_scans_run_scan_request_instance = AgentReadinessV1ScansRunScanRequest.from_json(json)
# print the JSON string representation of the object
print(AgentReadinessV1ScansRunScanRequest.to_json())

# convert the object into a dict
agent_readiness_v1_scans_run_scan_request_dict = agent_readiness_v1_scans_run_scan_request_instance.to_dict()
# create an instance of AgentReadinessV1ScansRunScanRequest from a dict
agent_readiness_v1_scans_run_scan_request_from_dict = AgentReadinessV1ScansRunScanRequest.from_dict(agent_readiness_v1_scans_run_scan_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


