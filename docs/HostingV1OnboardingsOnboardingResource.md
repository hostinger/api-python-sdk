# HostingV1OnboardingsOnboardingResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | Domain of the website being set up. | 
**username** | **str** | Hosting account username. | 
**status** | **str** | &#x60;running&#x60; while the website is still being set up, &#x60;completed&#x60; once the setup has finished, &#x60;failed&#x60; when it stopped before finishing or has not reported progress for over an hour. | 
**created_at** | **datetime** | When the setup was requested. | 
**updated_at** | **datetime** | When the setup last reported progress. | 

## Example

```python
from hostinger_api.models.hosting_v1_onboardings_onboarding_resource import HostingV1OnboardingsOnboardingResource

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1OnboardingsOnboardingResource from a JSON string
hosting_v1_onboardings_onboarding_resource_instance = HostingV1OnboardingsOnboardingResource.from_json(json)
# print the JSON string representation of the object
print(HostingV1OnboardingsOnboardingResource.to_json())

# convert the object into a dict
hosting_v1_onboardings_onboarding_resource_dict = hosting_v1_onboardings_onboarding_resource_instance.to_dict()
# create an instance of HostingV1OnboardingsOnboardingResource from a dict
hosting_v1_onboardings_onboarding_resource_from_dict = HostingV1OnboardingsOnboardingResource.from_dict(hosting_v1_onboardings_onboarding_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


