# ReachV1ProfilesFeaturesPlanFeatureResource

Whether a single plan feature can be used on the profile.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature** | **str** |  | [optional] 
**is_available** | **bool** | Whether the feature can be used right now. | [optional] 
**is_locked** | **bool** | Whether the feature sits outside the base plan and needs an upgrade. | [optional] 

## Example

```python
from hostinger_api.models.reach_v1_profiles_features_plan_feature_resource import ReachV1ProfilesFeaturesPlanFeatureResource

# TODO update the JSON string below
json = "{}"
# create an instance of ReachV1ProfilesFeaturesPlanFeatureResource from a JSON string
reach_v1_profiles_features_plan_feature_resource_instance = ReachV1ProfilesFeaturesPlanFeatureResource.from_json(json)
# print the JSON string representation of the object
print(ReachV1ProfilesFeaturesPlanFeatureResource.to_json())

# convert the object into a dict
reach_v1_profiles_features_plan_feature_resource_dict = reach_v1_profiles_features_plan_feature_resource_instance.to_dict()
# create an instance of ReachV1ProfilesFeaturesPlanFeatureResource from a dict
reach_v1_profiles_features_plan_feature_resource_from_dict = ReachV1ProfilesFeaturesPlanFeatureResource.from_dict(reach_v1_profiles_features_plan_feature_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


