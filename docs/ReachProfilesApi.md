# hostinger_api.ReachProfilesApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_connected_sending_domain_v1**](ReachProfilesApi.md#get_connected_sending_domain_v1) | **GET** /api/reach/v1/profiles/{profileUuid}/domains | Get connected sending domain
[**get_profile_domain_dns_status_v1**](ReachProfilesApi.md#get_profile_domain_dns_status_v1) | **GET** /api/reach/v1/profiles/{profileUuid}/domains/dns-status | Get profile domain DNS status
[**get_remaining_plan_limits_v1**](ReachProfilesApi.md#get_remaining_plan_limits_v1) | **GET** /api/reach/v1/profiles/{profileUuid}/limits | Get remaining plan limits
[**list_plan_feature_access_v1**](ReachProfilesApi.md#list_plan_feature_access_v1) | **GET** /api/reach/v1/profiles/{profileUuid}/features | List plan feature access
[**list_profiles_v1**](ReachProfilesApi.md#list_profiles_v1) | **GET** /api/reach/v1/profiles | List Profiles


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

