# ReachV1ProfilesPlanLimitsResource

What the plan allows and what is left of it for the current period.  `emails` counts every email sent. `recipients` counts the distinct contacts emailed - it is not the size of the contact list, a contact emailed three times counts once and a contact never emailed does not count at all. `ai_credits` counts the AI generations used, and its limit includes any extra credits bought on top of the plan.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**emails** | [**ReachV1ProfilesPlanLimitUsageResource**](ReachV1ProfilesPlanLimitUsageResource.md) |  | [optional] 
**recipients** | [**ReachV1ProfilesPlanLimitUsageResource**](ReachV1ProfilesPlanLimitUsageResource.md) |  | [optional] 
**ai_credits** | [**ReachV1ProfilesPlanLimitUsageResource**](ReachV1ProfilesPlanLimitUsageResource.md) |  | [optional] 
**period_start** | **datetime** | Start of the current period. Periods are calendar months rather than billing anniversaries, so the counters reset at midnight UTC on the 1st no matter when the subscription started. | [optional] 
**period_end** | **datetime** | End of the current period, that is the last moment of the calendar month. | [optional] 

## Example

```python
from hostinger_api.models.reach_v1_profiles_plan_limits_resource import ReachV1ProfilesPlanLimitsResource

# TODO update the JSON string below
json = "{}"
# create an instance of ReachV1ProfilesPlanLimitsResource from a JSON string
reach_v1_profiles_plan_limits_resource_instance = ReachV1ProfilesPlanLimitsResource.from_json(json)
# print the JSON string representation of the object
print(ReachV1ProfilesPlanLimitsResource.to_json())

# convert the object into a dict
reach_v1_profiles_plan_limits_resource_dict = reach_v1_profiles_plan_limits_resource_instance.to_dict()
# create an instance of ReachV1ProfilesPlanLimitsResource from a dict
reach_v1_profiles_plan_limits_resource_from_dict = ReachV1ProfilesPlanLimitsResource.from_dict(reach_v1_profiles_plan_limits_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


