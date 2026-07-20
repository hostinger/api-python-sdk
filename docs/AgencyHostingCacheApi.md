# hostinger_api.AgencyHostingCacheApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clear_agency_plan_website_cache_v1**](AgencyHostingCacheApi.md#clear_agency_plan_website_cache_v1) | **DELETE** /api/agency-hosting/v1/websites/{website_uid}/cache | Clear Agency Plan website cache


# **clear_agency_plan_website_cache_v1**
> CommonSuccessEmptyResource clear_agency_plan_website_cache_v1(website_uid)

Clear Agency Plan website cache

Clears cache for all domains associated with an Agency Plan website, including its preview domain.

This operation clears all cache types for the website.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.common_success_empty_resource import CommonSuccessEmptyResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.AgencyHostingCacheApi(api_client)
    website_uid = 'zpwlGlp19' # str | Agency Plan website UID

    try:
        # Clear Agency Plan website cache
        api_response = api_instance.clear_agency_plan_website_cache_v1(website_uid)
        print("The response of AgencyHostingCacheApi->clear_agency_plan_website_cache_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgencyHostingCacheApi->clear_agency_plan_website_cache_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website_uid** | **str**| Agency Plan website UID | 

### Return type

[**CommonSuccessEmptyResource**](CommonSuccessEmptyResource.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success empty response |  -  |
**401** | Unauthenticated response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

