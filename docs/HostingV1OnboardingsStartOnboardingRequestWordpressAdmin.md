# HostingV1OnboardingsStartOnboardingRequestWordpressAdmin

WordPress administrator account

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | **str** | WordPress admin username (letters, numbers, and underscore) | 
**password** | **str** | WordPress admin password (8-50 characters, mixed case, a digit, and not compromised) | 
**email** | **str** | WordPress admin email address | 

## Example

```python
from hostinger_api.models.hosting_v1_onboardings_start_onboarding_request_wordpress_admin import HostingV1OnboardingsStartOnboardingRequestWordpressAdmin

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1OnboardingsStartOnboardingRequestWordpressAdmin from a JSON string
hosting_v1_onboardings_start_onboarding_request_wordpress_admin_instance = HostingV1OnboardingsStartOnboardingRequestWordpressAdmin.from_json(json)
# print the JSON string representation of the object
print(HostingV1OnboardingsStartOnboardingRequestWordpressAdmin.to_json())

# convert the object into a dict
hosting_v1_onboardings_start_onboarding_request_wordpress_admin_dict = hosting_v1_onboardings_start_onboarding_request_wordpress_admin_instance.to_dict()
# create an instance of HostingV1OnboardingsStartOnboardingRequestWordpressAdmin from a dict
hosting_v1_onboardings_start_onboarding_request_wordpress_admin_from_dict = HostingV1OnboardingsStartOnboardingRequestWordpressAdmin.from_dict(hosting_v1_onboardings_start_onboarding_request_wordpress_admin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


