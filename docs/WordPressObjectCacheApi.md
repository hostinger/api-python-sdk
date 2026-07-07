# hostinger_api.WordPressObjectCacheApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**show_memcached_object_cache_status_v1**](WordPressObjectCacheApi.md#show_memcached_object_cache_status_v1) | **GET** /api/hosting/v1/accounts/{username}/wordpress/{software}/memcached/status | Show Memcached object cache status
[**toggle_memcached_object_cache_v1**](WordPressObjectCacheApi.md#toggle_memcached_object_cache_v1) | **PATCH** /api/hosting/v1/accounts/{username}/wordpress/{software}/memcached/toggle | Toggle Memcached object cache


# **show_memcached_object_cache_status_v1**
> WordPressV1MemcachedMemcachedStatusResource show_memcached_object_cache_status_v1(username, software)

Show Memcached object cache status

Show the Memcached object cache status for the specified WordPress
installation.

Provide the WordPress installation (software) identifier in the path. It can
be obtained from GET /api/hosting/v1/wordpress/installations (the `id` field).

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.word_press_v1_memcached_memcached_status_resource import WordPressV1MemcachedMemcachedStatusResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.WordPressObjectCacheApi(api_client)
    username = 'u123456789' # str | 
    software = '1232456789' # str | WordPress installation (software) identifier

    try:
        # Show Memcached object cache status
        api_response = api_instance.show_memcached_object_cache_status_v1(username, software)
        print("The response of WordPressObjectCacheApi->show_memcached_object_cache_status_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WordPressObjectCacheApi->show_memcached_object_cache_status_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **software** | **str**| WordPress installation (software) identifier | 

### Return type

[**WordPressV1MemcachedMemcachedStatusResource**](WordPressV1MemcachedMemcachedStatusResource.md)

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

# **toggle_memcached_object_cache_v1**
> CommonSuccessEmptyResource toggle_memcached_object_cache_v1(username, software, word_press_v1_memcached_toggle_memcached_request)

Toggle Memcached object cache

Activate or deactivate the Memcached object cache for the specified WordPress
installation, based on the `enabled` flag.

Provide the WordPress installation (software) identifier in the path. It can
be obtained from GET /api/hosting/v1/wordpress/installations (the `id` field).

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.common_success_empty_resource import CommonSuccessEmptyResource
from hostinger_api.models.word_press_v1_memcached_toggle_memcached_request import WordPressV1MemcachedToggleMemcachedRequest
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.WordPressObjectCacheApi(api_client)
    username = 'u123456789' # str | 
    software = '1232456789' # str | WordPress installation (software) identifier
    word_press_v1_memcached_toggle_memcached_request = hostinger_api.WordPressV1MemcachedToggleMemcachedRequest() # WordPressV1MemcachedToggleMemcachedRequest | 

    try:
        # Toggle Memcached object cache
        api_response = api_instance.toggle_memcached_object_cache_v1(username, software, word_press_v1_memcached_toggle_memcached_request)
        print("The response of WordPressObjectCacheApi->toggle_memcached_object_cache_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WordPressObjectCacheApi->toggle_memcached_object_cache_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **software** | **str**| WordPress installation (software) identifier | 
 **word_press_v1_memcached_toggle_memcached_request** | [**WordPressV1MemcachedToggleMemcachedRequest**](WordPressV1MemcachedToggleMemcachedRequest.md)|  | 

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

