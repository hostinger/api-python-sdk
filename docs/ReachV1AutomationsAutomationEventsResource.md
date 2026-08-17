# ReachV1AutomationsAutomationEventsResource

Counts of contacts moving through the automation.  These are not email engagement metrics. Automations expose no sent, open or click counters - use the campaign statistics endpoint for those.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**started** | **int** | Contacts that ever entered the automation, including those that already left it. | [optional] 
**in_progress** | **int** | Contacts currently moving through the automation, including those waiting on a delay step. | [optional] 
**completed** | **int** | Contacts that reached the end of the workflow. | [optional] 
**failed** | **int** | Contacts whose journey through the automation errored and stopped. | [optional] 

## Example

```python
from hostinger_api.models.reach_v1_automations_automation_events_resource import ReachV1AutomationsAutomationEventsResource

# TODO update the JSON string below
json = "{}"
# create an instance of ReachV1AutomationsAutomationEventsResource from a JSON string
reach_v1_automations_automation_events_resource_instance = ReachV1AutomationsAutomationEventsResource.from_json(json)
# print the JSON string representation of the object
print(ReachV1AutomationsAutomationEventsResource.to_json())

# convert the object into a dict
reach_v1_automations_automation_events_resource_dict = reach_v1_automations_automation_events_resource_instance.to_dict()
# create an instance of ReachV1AutomationsAutomationEventsResource from a dict
reach_v1_automations_automation_events_resource_from_dict = ReachV1AutomationsAutomationEventsResource.from_dict(reach_v1_automations_automation_events_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


