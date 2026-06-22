# ReachV1ProfilesProfileResourceLimits


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ai_messages_limit** | **int** |  | [optional] 
**subscribers_limit** | **int** |  | [optional] 
**emails_monthly_limit** | **int** |  | [optional] 
**ai_messages_additional** | **int** |  | [optional] 

## Example

```python
from hostinger_api.models.reach_v1_profiles_profile_resource_limits import ReachV1ProfilesProfileResourceLimits

# TODO update the JSON string below
json = "{}"
# create an instance of ReachV1ProfilesProfileResourceLimits from a JSON string
reach_v1_profiles_profile_resource_limits_instance = ReachV1ProfilesProfileResourceLimits.from_json(json)
# print the JSON string representation of the object
print(ReachV1ProfilesProfileResourceLimits.to_json())

# convert the object into a dict
reach_v1_profiles_profile_resource_limits_dict = reach_v1_profiles_profile_resource_limits_instance.to_dict()
# create an instance of ReachV1ProfilesProfileResourceLimits from a dict
reach_v1_profiles_profile_resource_limits_from_dict = ReachV1ProfilesProfileResourceLimits.from_dict(reach_v1_profiles_profile_resource_limits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


