# AgentReadinessV1ScansCheckResultResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**check_id** | **str** | Check ID, as listed by the &#x60;List checks&#x60; operation | 
**category** | **str** | Category the check belongs to | 
**status** | **str** | Check outcome. &#x60;not_applicable&#x60; and &#x60;error&#x60; checks do not count towards the category score. | 
**earned** | **int** | Points earned by this check | 
**possible** | **int** | Points this check can earn | 
**evidence** | **str** | What the scanner observed | 
**fix** | **str** | How to improve the result, or null when there is nothing to fix | 

## Example

```python
from hostinger_api.models.agent_readiness_v1_scans_check_result_resource import AgentReadinessV1ScansCheckResultResource

# TODO update the JSON string below
json = "{}"
# create an instance of AgentReadinessV1ScansCheckResultResource from a JSON string
agent_readiness_v1_scans_check_result_resource_instance = AgentReadinessV1ScansCheckResultResource.from_json(json)
# print the JSON string representation of the object
print(AgentReadinessV1ScansCheckResultResource.to_json())

# convert the object into a dict
agent_readiness_v1_scans_check_result_resource_dict = agent_readiness_v1_scans_check_result_resource_instance.to_dict()
# create an instance of AgentReadinessV1ScansCheckResultResource from a dict
agent_readiness_v1_scans_check_result_resource_from_dict = AgentReadinessV1ScansCheckResultResource.from_dict(agent_readiness_v1_scans_check_result_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


