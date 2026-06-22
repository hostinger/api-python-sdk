# hostinger_api.ReachProfilesApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_profiles_v1**](ReachProfilesApi.md#list_profiles_v1) | **GET** /api/reach/v1/profiles | List Profiles


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

