# HostingV1OnboardingsStartOnboardingRequestWordpress

WordPress install settings. Required when `type` is `wordpress`, not allowed otherwise. The site title is the domain.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language** | **str** | WordPress locale, for example &#x60;en_US&#x60; or &#x60;lt_LT&#x60;. Defaults to &#x60;en_US&#x60; when omitted. | [optional] 
**is_ai_builder** | **bool** | When &#x60;true&#x60;, installs the Hostinger AI theme (&#x60;hostinger-ai-theme&#x60;). Defaults to &#x60;false&#x60; when omitted. | [optional] 
**admin** | [**HostingV1OnboardingsStartOnboardingRequestWordpressAdmin**](HostingV1OnboardingsStartOnboardingRequestWordpressAdmin.md) |  | 

## Example

```python
from hostinger_api.models.hosting_v1_onboardings_start_onboarding_request_wordpress import HostingV1OnboardingsStartOnboardingRequestWordpress

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1OnboardingsStartOnboardingRequestWordpress from a JSON string
hosting_v1_onboardings_start_onboarding_request_wordpress_instance = HostingV1OnboardingsStartOnboardingRequestWordpress.from_json(json)
# print the JSON string representation of the object
print(HostingV1OnboardingsStartOnboardingRequestWordpress.to_json())

# convert the object into a dict
hosting_v1_onboardings_start_onboarding_request_wordpress_dict = hosting_v1_onboardings_start_onboarding_request_wordpress_instance.to_dict()
# create an instance of HostingV1OnboardingsStartOnboardingRequestWordpress from a dict
hosting_v1_onboardings_start_onboarding_request_wordpress_from_dict = HostingV1OnboardingsStartOnboardingRequestWordpress.from_dict(hosting_v1_onboardings_start_onboarding_request_wordpress_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


