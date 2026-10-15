# AgentReadinessV1ScansCategoryScoreResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**score** | **int** | Points this category contributes to the 0-100 total score | 
**weight** | **int** | Maximum points this category can contribute | 
**earned** | **int** | Points earned by the counted checks in this category | 
**possible** | **int** | Points possible for the counted checks in this category | 

## Example

```python
from hostinger_api.models.agent_readiness_v1_scans_category_score_resource import AgentReadinessV1ScansCategoryScoreResource

# TODO update the JSON string below
json = "{}"
# create an instance of AgentReadinessV1ScansCategoryScoreResource from a JSON string
agent_readiness_v1_scans_category_score_resource_instance = AgentReadinessV1ScansCategoryScoreResource.from_json(json)
# print the JSON string representation of the object
print(AgentReadinessV1ScansCategoryScoreResource.to_json())

# convert the object into a dict
agent_readiness_v1_scans_category_score_resource_dict = agent_readiness_v1_scans_category_score_resource_instance.to_dict()
# create an instance of AgentReadinessV1ScansCategoryScoreResource from a dict
agent_readiness_v1_scans_category_score_resource_from_dict = AgentReadinessV1ScansCategoryScoreResource.from_dict(agent_readiness_v1_scans_category_score_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


