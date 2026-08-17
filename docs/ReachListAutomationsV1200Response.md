# ReachListAutomationsV1200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ReachV1AutomationsAutomationResource]**](ReachV1AutomationsAutomationResource.md) | Array of [&#x60;Reach.V1.Automations.AutomationResource&#x60;](#model/reachv1automationsautomationresource) | [optional] 
**meta** | [**CommonSchemaPaginationMetaSchema**](CommonSchemaPaginationMetaSchema.md) |  | [optional] 

## Example

```python
from hostinger_api.models.reach_list_automations_v1200_response import ReachListAutomationsV1200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ReachListAutomationsV1200Response from a JSON string
reach_list_automations_v1200_response_instance = ReachListAutomationsV1200Response.from_json(json)
# print the JSON string representation of the object
print(ReachListAutomationsV1200Response.to_json())

# convert the object into a dict
reach_list_automations_v1200_response_dict = reach_list_automations_v1200_response_instance.to_dict()
# create an instance of ReachListAutomationsV1200Response from a dict
reach_list_automations_v1200_response_from_dict = ReachListAutomationsV1200Response.from_dict(reach_list_automations_v1200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


