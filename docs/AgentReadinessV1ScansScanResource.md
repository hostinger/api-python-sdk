# AgentReadinessV1ScansScanResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | Domain name that was scanned | 
**status** | **str** | Scan status. Result fields are null until the status is &#x60;completed&#x60;. | 
**score** | **int** | Agent readiness score from 0 to 100. Null unless completed, and null when unreachable. | 
**grade** | **str** | Letter grade for the score, from &#x60;A&#x60; to &#x60;F&#x60;. Null unless completed, and null when unreachable. | 
**is_unreachable** | **bool** | Whether the website homepage could not be fetched | 
**scanner_version** | **int** | Version of the scoring method that produced this scan | 
**is_outdated** | **bool** | Whether the scan was produced by an older scoring method than the current one | 
**scanned_at** | **datetime** | When the scan finished. Null unless completed. | 
**categories** | [**AgentReadinessV1ScansCategoriesResource**](AgentReadinessV1ScansCategoriesResource.md) |  | 
**unassessed_categories** | **List[str]** | Categories where no check could be counted. They still cost their full weight. Null unless completed. | 
**results** | [**List[AgentReadinessV1ScansCheckResultResource]**](AgentReadinessV1ScansCheckResultResource.md) | Result of every check. Null unless completed. | 

## Example

```python
from hostinger_api.models.agent_readiness_v1_scans_scan_resource import AgentReadinessV1ScansScanResource

# TODO update the JSON string below
json = "{}"
# create an instance of AgentReadinessV1ScansScanResource from a JSON string
agent_readiness_v1_scans_scan_resource_instance = AgentReadinessV1ScansScanResource.from_json(json)
# print the JSON string representation of the object
print(AgentReadinessV1ScansScanResource.to_json())

# convert the object into a dict
agent_readiness_v1_scans_scan_resource_dict = agent_readiness_v1_scans_scan_resource_instance.to_dict()
# create an instance of AgentReadinessV1ScansScanResource from a dict
agent_readiness_v1_scans_scan_resource_from_dict = AgentReadinessV1ScansScanResource.from_dict(agent_readiness_v1_scans_scan_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


