# hostinger_api.HostingCacheApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clear_website_cache_v1**](HostingCacheApi.md#clear_website_cache_v1) | **DELETE** /api/hosting/v1/accounts/{username}/websites/{domain}/cache/clear | Clear website cache
[**toggle_cacheless_mode_v1**](HostingCacheApi.md#toggle_cacheless_mode_v1) | **PATCH** /api/hosting/v1/accounts/{username}/websites/{domain}/cacheless-mode/toggle | Toggle cacheless mode
[**toggle_website_cache_v1**](HostingCacheApi.md#toggle_website_cache_v1) | **PATCH** /api/hosting/v1/accounts/{username}/websites/{domain}/cache/toggle | Toggle website cache


# **clear_website_cache_v1**
> CommonSuccessEmptyResource clear_website_cache_v1(username, domain, directory=directory)

Clear website cache

Permanently clears all server-side cache for the website at once. Use it when content was
updated and needs to be visible immediately, or after making major changes.

Also purges the Hostinger CDN cache when CDN is enabled on the website. For a WordPress
installation living in a subdirectory, pass the directory query parameter to clear its cache.

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
    api_instance = hostinger_api.HostingCacheApi(api_client)
    username = 'u123456789' # str | 
    domain = 'mydomain.tld' # str | Domain name
    directory = 'blog' # str | Directory of the website installation to clear, relative to the website root. Defaults to the website root. (optional)

    try:
        # Clear website cache
        api_response = api_instance.clear_website_cache_v1(username, domain, directory=directory)
        print("The response of HostingCacheApi->clear_website_cache_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingCacheApi->clear_website_cache_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **domain** | **str**| Domain name | 
 **directory** | **str**| Directory of the website installation to clear, relative to the website root. Defaults to the website root. | [optional] 

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

# **toggle_cacheless_mode_v1**
> CommonSuccessEmptyResource toggle_cacheless_mode_v1(username, domain, hosting_v1_cache_toggle_cacheless_mode_request)

Toggle cacheless mode

Turns development (cacheless) mode on or off, based on the enabled flag. When enabled, nothing
is cached, effectively turning off all caching for the website; use it while actively developing,
testing changes, debugging issues, or when real-time updates must be visible. Disable it after
finishing development work to restore the performance benefits of caching.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.common_success_empty_resource import CommonSuccessEmptyResource
from hostinger_api.models.hosting_v1_cache_toggle_cacheless_mode_request import HostingV1CacheToggleCachelessModeRequest
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.HostingCacheApi(api_client)
    username = 'u123456789' # str | 
    domain = 'mydomain.tld' # str | Domain name
    hosting_v1_cache_toggle_cacheless_mode_request = hostinger_api.HostingV1CacheToggleCachelessModeRequest() # HostingV1CacheToggleCachelessModeRequest | 

    try:
        # Toggle cacheless mode
        api_response = api_instance.toggle_cacheless_mode_v1(username, domain, hosting_v1_cache_toggle_cacheless_mode_request)
        print("The response of HostingCacheApi->toggle_cacheless_mode_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingCacheApi->toggle_cacheless_mode_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **domain** | **str**| Domain name | 
 **hosting_v1_cache_toggle_cacheless_mode_request** | [**HostingV1CacheToggleCachelessModeRequest**](HostingV1CacheToggleCachelessModeRequest.md)|  | 

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

# **toggle_website_cache_v1**
> CommonSuccessEmptyResource toggle_website_cache_v1(username, domain, hosting_v1_cache_toggle_cache_request)

Toggle website cache

Turns server-side caching for the website on or off, based on the enabled flag. Enable it for
faster page loads, reduced server load, and improved user experience; recommended for production
websites. Disabling may impact performance; to temporarily bypass caching while developing or
debugging, prefer toggling cacheless mode instead.

Does nothing if caching is already in the requested state.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.common_success_empty_resource import CommonSuccessEmptyResource
from hostinger_api.models.hosting_v1_cache_toggle_cache_request import HostingV1CacheToggleCacheRequest
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.HostingCacheApi(api_client)
    username = 'u123456789' # str | 
    domain = 'mydomain.tld' # str | Domain name
    hosting_v1_cache_toggle_cache_request = hostinger_api.HostingV1CacheToggleCacheRequest() # HostingV1CacheToggleCacheRequest | 

    try:
        # Toggle website cache
        api_response = api_instance.toggle_website_cache_v1(username, domain, hosting_v1_cache_toggle_cache_request)
        print("The response of HostingCacheApi->toggle_website_cache_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingCacheApi->toggle_website_cache_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **domain** | **str**| Domain name | 
 **hosting_v1_cache_toggle_cache_request** | [**HostingV1CacheToggleCacheRequest**](HostingV1CacheToggleCacheRequest.md)|  | 

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

