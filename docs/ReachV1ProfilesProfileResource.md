# ReachV1ProfilesProfileResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limits** | [**ReachV1ProfilesProfileResourceLimits**](ReachV1ProfilesProfileResourceLimits.md) |  | [optional] 
**is_trial** | **bool** |  | [optional] 
**expires_at** | **datetime** |  | [optional] 
**resource_id** | **int** |  | [optional] 
**status** | **str** |  | [optional] 
**profiles** | [**List[ReachV1ProfilesProfileResourceProfilesInner]**](ReachV1ProfilesProfileResourceProfilesInner.md) |  | [optional] 

## Example

```python
from hostinger_api.models.reach_v1_profiles_profile_resource import ReachV1ProfilesProfileResource

# TODO update the JSON string below
json = "{}"
# create an instance of ReachV1ProfilesProfileResource from a JSON string
reach_v1_profiles_profile_resource_instance = ReachV1ProfilesProfileResource.from_json(json)
# print the JSON string representation of the object
print(ReachV1ProfilesProfileResource.to_json())

# convert the object into a dict
reach_v1_profiles_profile_resource_dict = reach_v1_profiles_profile_resource_instance.to_dict()
# create an instance of ReachV1ProfilesProfileResource from a dict
reach_v1_profiles_profile_resource_from_dict = ReachV1ProfilesProfileResource.from_dict(reach_v1_profiles_profile_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


