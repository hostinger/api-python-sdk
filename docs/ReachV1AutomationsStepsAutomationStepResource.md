# ReachV1AutomationsStepsAutomationStepResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [optional] 
**parent_uuid** | **str** | The step this one branches from. Null for the entry point of the workflow. | [optional] 
**step_order** | **int** | Position of this step among the steps sharing its parent. | [optional] 
**type** | **str** | Role of the step in the workflow. A &#x60;conditional&#x60; step branches into several children. | [optional] 
**value** | **str** | The concrete trigger, action, decision or delay this step performs. | [optional] 
**config** | **object** | Step configuration. The shape depends on the value, and is empty for steps that take none. | [optional] 

## Example

```python
from hostinger_api.models.reach_v1_automations_steps_automation_step_resource import ReachV1AutomationsStepsAutomationStepResource

# TODO update the JSON string below
json = "{}"
# create an instance of ReachV1AutomationsStepsAutomationStepResource from a JSON string
reach_v1_automations_steps_automation_step_resource_instance = ReachV1AutomationsStepsAutomationStepResource.from_json(json)
# print the JSON string representation of the object
print(ReachV1AutomationsStepsAutomationStepResource.to_json())

# convert the object into a dict
reach_v1_automations_steps_automation_step_resource_dict = reach_v1_automations_steps_automation_step_resource_instance.to_dict()
# create an instance of ReachV1AutomationsStepsAutomationStepResource from a dict
reach_v1_automations_steps_automation_step_resource_from_dict = ReachV1AutomationsStepsAutomationStepResource.from_dict(reach_v1_automations_steps_automation_step_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


