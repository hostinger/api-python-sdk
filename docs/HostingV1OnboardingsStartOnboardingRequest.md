# HostingV1OnboardingsStartOnboardingRequest

Website type, domain and WordPress settings for a new website setup

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Website type. Omit or &#x60;null&#x60; for an empty website. &#x60;wordpress&#x60; installs WordPress in the website root and requires &#x60;wordpress&#x60;. The headless types (&#x60;headless_wordpress&#x60;, &#x60;headless_ecommerce&#x60;, &#x60;headless_pocketbase&#x60;) create a headless website; &#x60;headless_wordpress&#x60; additionally installs WordPress into the &#x60;cms&#x60; directory with generated credentials. | [optional] 
**domain** | **str** | Customer-owned domain. Cannot start with \&quot;www.\&quot;. Omit or &#x60;null&#x60; to set the website up on a generated temporary free subdomain. | [optional] 
**wordpress** | [**HostingV1OnboardingsStartOnboardingRequestWordpress**](HostingV1OnboardingsStartOnboardingRequestWordpress.md) |  | [optional] 

## Example

```python
from hostinger_api.models.hosting_v1_onboardings_start_onboarding_request import HostingV1OnboardingsStartOnboardingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1OnboardingsStartOnboardingRequest from a JSON string
hosting_v1_onboardings_start_onboarding_request_instance = HostingV1OnboardingsStartOnboardingRequest.from_json(json)
# print the JSON string representation of the object
print(HostingV1OnboardingsStartOnboardingRequest.to_json())

# convert the object into a dict
hosting_v1_onboardings_start_onboarding_request_dict = hosting_v1_onboardings_start_onboarding_request_instance.to_dict()
# create an instance of HostingV1OnboardingsStartOnboardingRequest from a dict
hosting_v1_onboardings_start_onboarding_request_from_dict = HostingV1OnboardingsStartOnboardingRequest.from_dict(hosting_v1_onboardings_start_onboarding_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


