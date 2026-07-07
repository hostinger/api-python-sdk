# hostinger_api.WordPressLiteSpeedCacheApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**purge_lite_speed_cache_v1**](WordPressLiteSpeedCacheApi.md#purge_lite_speed_cache_v1) | **POST** /api/hosting/v1/accounts/{username}/wordpress/{software}/litespeed-cache/purge | Purge LiteSpeed Cache
[**show_lite_speed_cache_status_v1**](WordPressLiteSpeedCacheApi.md#show_lite_speed_cache_status_v1) | **GET** /api/hosting/v1/accounts/{username}/wordpress/{software}/litespeed-cache/status | Show LiteSpeed Cache status


# **purge_lite_speed_cache_v1**
> CommonSuccessEmptyResource purge_lite_speed_cache_v1(username, software)

Purge LiteSpeed Cache

Purge the LiteSpeed Cache for the specified WordPress installation.

Provide the WordPress installation (software) identifier in the path. It can
be obtained from GET /api/hosting/v1/wordpress/installations (the `id` field).

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
    api_instance = hostinger_api.WordPressLiteSpeedCacheApi(api_client)
    username = 'u123456789' # str | 
    software = '1232456789' # str | WordPress installation (software) identifier

    try:
        # Purge LiteSpeed Cache
        api_response = api_instance.purge_lite_speed_cache_v1(username, software)
        print("The response of WordPressLiteSpeedCacheApi->purge_lite_speed_cache_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WordPressLiteSpeedCacheApi->purge_lite_speed_cache_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **software** | **str**| WordPress installation (software) identifier | 

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

# **show_lite_speed_cache_status_v1**
> WordPressV1LitespeedLitespeedCacheStatusResource show_lite_speed_cache_status_v1(username, software)

Show LiteSpeed Cache status

Show the LiteSpeed Cache status for the specified WordPress installation.

Provide the WordPress installation (software) identifier in the path. It can
be obtained from GET /api/hosting/v1/wordpress/installations (the `id` field).

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.word_press_v1_litespeed_litespeed_cache_status_resource import WordPressV1LitespeedLitespeedCacheStatusResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.WordPressLiteSpeedCacheApi(api_client)
    username = 'u123456789' # str | 
    software = '1232456789' # str | WordPress installation (software) identifier

    try:
        # Show LiteSpeed Cache status
        api_response = api_instance.show_lite_speed_cache_status_v1(username, software)
        print("The response of WordPressLiteSpeedCacheApi->show_lite_speed_cache_status_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WordPressLiteSpeedCacheApi->show_lite_speed_cache_status_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **software** | **str**| WordPress installation (software) identifier | 

### Return type

[**WordPressV1LitespeedLitespeedCacheStatusResource**](WordPressV1LitespeedLitespeedCacheStatusResource.md)

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

