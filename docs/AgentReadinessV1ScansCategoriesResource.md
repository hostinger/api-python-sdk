# AgentReadinessV1ScansCategoriesResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**crawl_permission** | [**AgentReadinessV1ScansCategoryScoreResource**](AgentReadinessV1ScansCategoryScoreResource.md) |  | 
**findability** | [**AgentReadinessV1ScansCategoryScoreResource**](AgentReadinessV1ScansCategoryScoreResource.md) |  | 
**readability** | [**AgentReadinessV1ScansCategoryScoreResource**](AgentReadinessV1ScansCategoryScoreResource.md) |  | 
**structured_meaning** | [**AgentReadinessV1ScansCategoryScoreResource**](AgentReadinessV1ScansCategoryScoreResource.md) |  | 
**commercial_legibility** | [**AgentReadinessV1ScansCategoryScoreResource**](AgentReadinessV1ScansCategoryScoreResource.md) |  | 
**agent_native_content** | [**AgentReadinessV1ScansCategoryScoreResource**](AgentReadinessV1ScansCategoryScoreResource.md) |  | 
**agent_interaction** | [**AgentReadinessV1ScansCategoryScoreResource**](AgentReadinessV1ScansCategoryScoreResource.md) |  | 

## Example

```python
from hostinger_api.models.agent_readiness_v1_scans_categories_resource import AgentReadinessV1ScansCategoriesResource

# TODO update the JSON string below
json = "{}"
# create an instance of AgentReadinessV1ScansCategoriesResource from a JSON string
agent_readiness_v1_scans_categories_resource_instance = AgentReadinessV1ScansCategoriesResource.from_json(json)
# print the JSON string representation of the object
print(AgentReadinessV1ScansCategoriesResource.to_json())

# convert the object into a dict
agent_readiness_v1_scans_categories_resource_dict = agent_readiness_v1_scans_categories_resource_instance.to_dict()
# create an instance of AgentReadinessV1ScansCategoriesResource from a dict
agent_readiness_v1_scans_categories_resource_from_dict = AgentReadinessV1ScansCategoriesResource.from_dict(agent_readiness_v1_scans_categories_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


