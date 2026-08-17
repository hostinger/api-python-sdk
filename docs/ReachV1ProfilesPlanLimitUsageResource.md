# ReachV1ProfilesPlanLimitUsageResource

Allowance, consumption and headroom of a single plan limit for the current period.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | The allowance for the current period. | [optional] 
**used** | **int** | How much of the allowance has been consumed so far. | [optional] 
**remaining** | **int** | Headroom left. Floors at 0, so it never reports a negative overage. | [optional] 

## Example

```python
from hostinger_api.models.reach_v1_profiles_plan_limit_usage_resource import ReachV1ProfilesPlanLimitUsageResource

# TODO update the JSON string below
json = "{}"
# create an instance of ReachV1ProfilesPlanLimitUsageResource from a JSON string
reach_v1_profiles_plan_limit_usage_resource_instance = ReachV1ProfilesPlanLimitUsageResource.from_json(json)
# print the JSON string representation of the object
print(ReachV1ProfilesPlanLimitUsageResource.to_json())

# convert the object into a dict
reach_v1_profiles_plan_limit_usage_resource_dict = reach_v1_profiles_plan_limit_usage_resource_instance.to_dict()
# create an instance of ReachV1ProfilesPlanLimitUsageResource from a dict
reach_v1_profiles_plan_limit_usage_resource_from_dict = ReachV1ProfilesPlanLimitUsageResource.from_dict(reach_v1_profiles_plan_limit_usage_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


