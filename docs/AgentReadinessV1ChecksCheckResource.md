# AgentReadinessV1ChecksCheckResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Check ID, as used by &#x60;check_id&#x60; in scan results | 
**name** | **str** | Human-readable check name | 
**category** | **str** | Category the check belongs to | 
**category_label** | **str** | Human-readable category name | 
**weight** | **int** | Points this check can earn | 

## Example

```python
from hostinger_api.models.agent_readiness_v1_checks_check_resource import AgentReadinessV1ChecksCheckResource

# TODO update the JSON string below
json = "{}"
# create an instance of AgentReadinessV1ChecksCheckResource from a JSON string
agent_readiness_v1_checks_check_resource_instance = AgentReadinessV1ChecksCheckResource.from_json(json)
# print the JSON string representation of the object
print(AgentReadinessV1ChecksCheckResource.to_json())

# convert the object into a dict
agent_readiness_v1_checks_check_resource_dict = agent_readiness_v1_checks_check_resource_instance.to_dict()
# create an instance of AgentReadinessV1ChecksCheckResource from a dict
agent_readiness_v1_checks_check_resource_from_dict = AgentReadinessV1ChecksCheckResource.from_dict(agent_readiness_v1_checks_check_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


