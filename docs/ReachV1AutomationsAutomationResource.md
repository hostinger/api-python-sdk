# ReachV1AutomationsAutomationResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**status** | **str** | There is no &#x60;completed&#x60; status. Use &#x60;events.completed&#x60; to see how many contacts finished. | [optional] 
**type** | **str** | What kind of workflow this is. &#x60;custom&#x60; automations are the ones built from scratch. | [optional] 
**config** | **object** | Trigger configuration of the automation. The shape depends on the type. | [optional] 
**events** | [**ReachV1AutomationsAutomationEventsResource**](ReachV1AutomationsAutomationEventsResource.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from hostinger_api.models.reach_v1_automations_automation_resource import ReachV1AutomationsAutomationResource

# TODO update the JSON string below
json = "{}"
# create an instance of ReachV1AutomationsAutomationResource from a JSON string
reach_v1_automations_automation_resource_instance = ReachV1AutomationsAutomationResource.from_json(json)
# print the JSON string representation of the object
print(ReachV1AutomationsAutomationResource.to_json())

# convert the object into a dict
reach_v1_automations_automation_resource_dict = reach_v1_automations_automation_resource_instance.to_dict()
# create an instance of ReachV1AutomationsAutomationResource from a dict
reach_v1_automations_automation_resource_from_dict = ReachV1AutomationsAutomationResource.from_dict(reach_v1_automations_automation_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


