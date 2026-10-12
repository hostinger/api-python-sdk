# hostinger_api.ReachProfilesApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**connect_sending_domain_v1**](ReachProfilesApi.md#connect_sending_domain_v1) | **POST** /api/reach/v1/profiles/{profileUuid}/domains | Connect sending domain
[**delete_sending_domain_v1**](ReachProfilesApi.md#delete_sending_domain_v1) | **DELETE** /api/reach/v1/profiles/{profileUuid}/domains | Delete sending domain
[**get_connected_sending_domain_v1**](ReachProfilesApi.md#get_connected_sending_domain_v1) | **GET** /api/reach/v1/profiles/{profileUuid}/domains | Get connected sending domain
[**get_profile_domain_dns_status_v1**](ReachProfilesApi.md#get_profile_domain_dns_status_v1) | **GET** /api/reach/v1/profiles/{profileUuid}/domains/dns-status | Get profile domain DNS status
[**get_profile_settings_v1**](ReachProfilesApi.md#get_profile_settings_v1) | **GET** /api/reach/v1/profiles/{profileUuid}/settings | Get profile settings
[**get_remaining_plan_limits_v1**](ReachProfilesApi.md#get_remaining_plan_limits_v1) | **GET** /api/reach/v1/profiles/{profileUuid}/limits | Get remaining plan limits
[**list_plan_feature_access_v1**](ReachProfilesApi.md#list_plan_feature_access_v1) | **GET** /api/reach/v1/profiles/{profileUuid}/features | List plan feature access
[**list_profiles_v1**](ReachProfilesApi.md#list_profiles_v1) | **GET** /api/reach/v1/profiles | List Profiles
[**update_profile_settings_v1**](ReachProfilesApi.md#update_profile_settings_v1) | **PATCH** /api/reach/v1/profiles/{profileUuid}/settings | Update profile settings


# **connect_sending_domain_v1**
> CommonSuccessEmptyResource connect_sending_domain_v1(profile_uuid, reach_v1_profiles_domains_connect_request)

Connect sending domain

Connect a sending domain to the profile so emails can be sent from addresses on it.

Connecting does not make the domain ready to send: check the DNS status endpoint next for
records that are still missing. A domain the account owns or has already verified connects
immediately. Any other domain starts a TXT ownership verification and returns `409`;
complete the verification in Reach, then retry. Returns `422` when the profile or another
profile already has the domain, the domain is blocked, or its ownership cannot be verified.
An already connected domain is never replaced.

On success the sender address of draft and scheduled campaigns, and of published automation
and double opt-in emails, moves onto the new domain in the background, keeping the part
before the `@`.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.common_success_empty_resource import CommonSuccessEmptyResource
from hostinger_api.models.reach_v1_profiles_domains_connect_request import ReachV1ProfilesDomainsConnectRequest
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.ReachProfilesApi(api_client)
    profile_uuid = '550e8400-e09b-41d4-a716-400055000000' # str | Profile uuid parameter
    reach_v1_profiles_domains_connect_request = hostinger_api.ReachV1ProfilesDomainsConnectRequest() # ReachV1ProfilesDomainsConnectRequest | 

    try:
        # Connect sending domain
        api_response = api_instance.connect_sending_domain_v1(profile_uuid, reach_v1_profiles_domains_connect_request)
        print("The response of ReachProfilesApi->connect_sending_domain_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReachProfilesApi->connect_sending_domain_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_uuid** | **str**| Profile uuid parameter | 
 **reach_v1_profiles_domains_connect_request** | [**ReachV1ProfilesDomainsConnectRequest**](ReachV1ProfilesDomainsConnectRequest.md)|  | 

### Return type

[**CommonSuccessEmptyResource**](CommonSuccessEmptyResource.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success empty response |  -  |
**401** | Unauthenticated response |  -  |
**409** | Conflict response. &#x60;Retry-After&#x60;, when present, is the number of seconds to wait before retrying. |  * Retry-After - Seconds to wait before retrying the request <br>  |
**422** | Validation error response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sending_domain_v1**
> CommonSuccessEmptyResource delete_sending_domain_v1(profile_uuid, reach_v1_profiles_domains_disconnect_request)

Delete sending domain

Disconnect the sending domain from the profile.

The domain record is removed, so the profile has no sending domain afterwards and campaigns
cannot be sent until a domain is connected again. Sender addresses already stored on
campaigns, automations and settings are left untouched and keep pointing at the removed
domain. A domain that is not connected to the profile also succeeds, so success is not proof
that anything was deleted. DNS records at the DNS provider are not removed. To switch
domains, delete this one and connect the new one. Confirm the domain with the customer
before calling.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.common_success_empty_resource import CommonSuccessEmptyResource
from hostinger_api.models.reach_v1_profiles_domains_disconnect_request import ReachV1ProfilesDomainsDisconnectRequest
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.ReachProfilesApi(api_client)
    profile_uuid = '550e8400-e09b-41d4-a716-400055000000' # str | Profile uuid parameter
    reach_v1_profiles_domains_disconnect_request = hostinger_api.ReachV1ProfilesDomainsDisconnectRequest() # ReachV1ProfilesDomainsDisconnectRequest | 

    try:
        # Delete sending domain
        api_response = api_instance.delete_sending_domain_v1(profile_uuid, reach_v1_profiles_domains_disconnect_request)
        print("The response of ReachProfilesApi->delete_sending_domain_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReachProfilesApi->delete_sending_domain_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_uuid** | **str**| Profile uuid parameter | 
 **reach_v1_profiles_domains_disconnect_request** | [**ReachV1ProfilesDomainsDisconnectRequest**](ReachV1ProfilesDomainsDisconnectRequest.md)|  | 

### Return type

[**CommonSuccessEmptyResource**](CommonSuccessEmptyResource.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success empty response |  -  |
**422** | Validation error response |  -  |
**401** | Unauthenticated response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connected_sending_domain_v1**
> ReachV1ProfilesDomainsSendingDomainResource get_connected_sending_domain_v1(profile_uuid)

Get connected sending domain

Get the sending domain connected to the profile, its verification status and any suspended
sender addresses.

Campaigns only go out once a domain is connected and active, so this is the cheapest way to
check that precondition before building one. A profile with no domain connected returns the
same shape with every field set to `null`. For the individual MX, SPF, DKIM and DMARC records
behind the status, use the DNS status endpoint.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.reach_v1_profiles_domains_sending_domain_resource import ReachV1ProfilesDomainsSendingDomainResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.ReachProfilesApi(api_client)
    profile_uuid = '550e8400-e09b-41d4-a716-400055000000' # str | Profile uuid parameter

    try:
        # Get connected sending domain
        api_response = api_instance.get_connected_sending_domain_v1(profile_uuid)
        print("The response of ReachProfilesApi->get_connected_sending_domain_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReachProfilesApi->get_connected_sending_domain_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_uuid** | **str**| Profile uuid parameter | 

### Return type

[**ReachV1ProfilesDomainsSendingDomainResource**](ReachV1ProfilesDomainsSendingDomainResource.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success response |  -  |
**401** | Unauthenticated response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_profile_domain_dns_status_v1**
> ReachV1ProfilesDomainsDnsStatusResource get_profile_domain_dns_status_v1(profile_uuid)

Get profile domain DNS status

Retrieve the DNS configuration status for a profile's domain.

This endpoint reports the state of MX, SPF, DKIM and DMARC records, including the
actual records found and the suggested records required for correct email delivery.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.reach_v1_profiles_domains_dns_status_resource import ReachV1ProfilesDomainsDnsStatusResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.ReachProfilesApi(api_client)
    profile_uuid = '550e8400-e09b-41d4-a716-400055000000' # str | Profile uuid parameter

    try:
        # Get profile domain DNS status
        api_response = api_instance.get_profile_domain_dns_status_v1(profile_uuid)
        print("The response of ReachProfilesApi->get_profile_domain_dns_status_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReachProfilesApi->get_profile_domain_dns_status_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_uuid** | **str**| Profile uuid parameter | 

### Return type

[**ReachV1ProfilesDomainsDnsStatusResource**](ReachV1ProfilesDomainsDnsStatusResource.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success response |  -  |
**401** | Unauthenticated response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_profile_settings_v1**
> ReachV1ProfilesSettingsSettingsResource get_profile_settings_v1(profile_uuid)

Get profile settings

Get the profile's saved sender identity and brand details.

Read the default sender before creating a campaign instead of asking the customer, and
reuse the brand fields when generating email content. Any field can be `null` for a profile
that never filled its settings in. This does not check that the sending domain is
verified, use the connected sending domain endpoint for that.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.reach_v1_profiles_settings_settings_resource import ReachV1ProfilesSettingsSettingsResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.ReachProfilesApi(api_client)
    profile_uuid = '550e8400-e09b-41d4-a716-400055000000' # str | Profile uuid parameter

    try:
        # Get profile settings
        api_response = api_instance.get_profile_settings_v1(profile_uuid)
        print("The response of ReachProfilesApi->get_profile_settings_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReachProfilesApi->get_profile_settings_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_uuid** | **str**| Profile uuid parameter | 

### Return type

[**ReachV1ProfilesSettingsSettingsResource**](ReachV1ProfilesSettingsSettingsResource.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success response |  -  |
**401** | Unauthenticated response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_remaining_plan_limits_v1**
> ReachV1ProfilesPlanLimitsResource get_remaining_plan_limits_v1(profile_uuid)

Get remaining plan limits

Get how much of the plan is left for the current period.

Two things to keep in mind before you build alerting on this. The period is a calendar month
rather than a billing anniversary, so the counters reset on the 1st no matter when the
subscription started. And usage is tracked per order, so every profile on the same order shares
one pool and reports the same numbers here. Only the current period is available, past usage is
not kept.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.reach_v1_profiles_plan_limits_resource import ReachV1ProfilesPlanLimitsResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.ReachProfilesApi(api_client)
    profile_uuid = '550e8400-e09b-41d4-a716-400055000000' # str | Profile uuid parameter

    try:
        # Get remaining plan limits
        api_response = api_instance.get_remaining_plan_limits_v1(profile_uuid)
        print("The response of ReachProfilesApi->get_remaining_plan_limits_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReachProfilesApi->get_remaining_plan_limits_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_uuid** | **str**| Profile uuid parameter | 

### Return type

[**ReachV1ProfilesPlanLimitsResource**](ReachV1ProfilesPlanLimitsResource.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success response |  -  |
**401** | Unauthenticated response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_plan_feature_access_v1**
> List[ReachV1ProfilesFeaturesPlanFeatureResource] list_plan_feature_access_v1(profile_uuid)

List plan feature access

List which plan features the profile can use.

This is the feature lock matrix, not a usage quota. `available` means the feature can be
used right now and `locked` means it is not part of the base plan, so an upgrade is needed.
For remaining emails, recipients and AI credits use the limits endpoint instead.

Worth checking before building something that cannot be activated afterwards, such as an
automation on a plan without automation activation.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.reach_v1_profiles_features_plan_feature_resource import ReachV1ProfilesFeaturesPlanFeatureResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.ReachProfilesApi(api_client)
    profile_uuid = '550e8400-e09b-41d4-a716-400055000000' # str | Profile uuid parameter

    try:
        # List plan feature access
        api_response = api_instance.list_plan_feature_access_v1(profile_uuid)
        print("The response of ReachProfilesApi->list_plan_feature_access_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReachProfilesApi->list_plan_feature_access_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_uuid** | **str**| Profile uuid parameter | 

### Return type

[**List[ReachV1ProfilesFeaturesPlanFeatureResource]**](ReachV1ProfilesFeaturesPlanFeatureResource.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success response |  -  |
**401** | Unauthenticated response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_profiles_v1**
> List[ReachV1ProfilesProfileResource] list_profiles_v1()

List Profiles

This endpoint returns all profiles available to the client, including their basic information.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.reach_v1_profiles_profile_resource import ReachV1ProfilesProfileResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.ReachProfilesApi(api_client)

    try:
        # List Profiles
        api_response = api_instance.list_profiles_v1()
        print("The response of ReachProfilesApi->list_profiles_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReachProfilesApi->list_profiles_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ReachV1ProfilesProfileResource]**](ReachV1ProfilesProfileResource.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success response |  -  |
**401** | Unauthenticated response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_profile_settings_v1**
> ReachV1ProfilesSettingsSettingsResource update_profile_settings_v1(profile_uuid, reach_v1_profiles_settings_update_request)

Update profile settings

Change the profile's default sender and brand details.

Send only the fields to change: every omitted field keeps its value, and `null` or an empty
string clears a text field. The default sender is what campaigns created afterwards start
from; existing campaigns keep their own sender. `sender_email` is only the part before the
`@`, because Reach combines it with the profile's connected sending domain, so an address
outside that domain cannot be set. Connecting a sending domain is a separate endpoint and
a connected domain cannot be changed here. Returns the settings after the change.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.reach_v1_profiles_settings_settings_resource import ReachV1ProfilesSettingsSettingsResource
from hostinger_api.models.reach_v1_profiles_settings_update_request import ReachV1ProfilesSettingsUpdateRequest
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.ReachProfilesApi(api_client)
    profile_uuid = '550e8400-e09b-41d4-a716-400055000000' # str | Profile uuid parameter
    reach_v1_profiles_settings_update_request = hostinger_api.ReachV1ProfilesSettingsUpdateRequest() # ReachV1ProfilesSettingsUpdateRequest | 

    try:
        # Update profile settings
        api_response = api_instance.update_profile_settings_v1(profile_uuid, reach_v1_profiles_settings_update_request)
        print("The response of ReachProfilesApi->update_profile_settings_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReachProfilesApi->update_profile_settings_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_uuid** | **str**| Profile uuid parameter | 
 **reach_v1_profiles_settings_update_request** | [**ReachV1ProfilesSettingsUpdateRequest**](ReachV1ProfilesSettingsUpdateRequest.md)|  | 

### Return type

[**ReachV1ProfilesSettingsSettingsResource**](ReachV1ProfilesSettingsSettingsResource.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success response |  -  |
**422** | Validation error response |  -  |
**401** | Unauthenticated response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

