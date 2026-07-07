# hostinger_api.HostingCacheApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clear_website_cache_v1**](HostingCacheApi.md#clear_website_cache_v1) | **DELETE** /api/hosting/v1/accounts/{username}/websites/{domain}/cache/clear | Clear website cache
[**disable_cacheless_mode_v1**](HostingCacheApi.md#disable_cacheless_mode_v1) | **PATCH** /api/hosting/v1/accounts/{username}/websites/{domain}/cacheless-mode/disable | Disable cacheless mode
[**disable_website_cache_v1**](HostingCacheApi.md#disable_website_cache_v1) | **PATCH** /api/hosting/v1/accounts/{username}/websites/{domain}/cache/disable | Disable website cache
[**enable_cacheless_mode_v1**](HostingCacheApi.md#enable_cacheless_mode_v1) | **PATCH** /api/hosting/v1/accounts/{username}/websites/{domain}/cacheless-mode/enable | Enable cacheless mode
[**enable_website_cache_v1**](HostingCacheApi.md#enable_website_cache_v1) | **PATCH** /api/hosting/v1/accounts/{username}/websites/{domain}/cache/enable | Enable website cache


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

# **disable_cacheless_mode_v1**
> CommonSuccessEmptyResource disable_cacheless_mode_v1(username, domain)

Disable cacheless mode

Turns off development (cacheless) mode and returns the website to normal caching. Use it after
finishing development work to restore the performance benefits of caching.

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

    try:
        # Disable cacheless mode
        api_response = api_instance.disable_cacheless_mode_v1(username, domain)
        print("The response of HostingCacheApi->disable_cacheless_mode_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingCacheApi->disable_cacheless_mode_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **domain** | **str**| Domain name | 

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

# **disable_website_cache_v1**
> CommonSuccessEmptyResource disable_website_cache_v1(username, domain)

Disable website cache

Turns off server-side caching for the website until it is enabled again. May impact performance.
Use it when experiencing cache-related issues; to temporarily bypass caching while developing
or debugging, prefer enabling cacheless mode instead.

Does nothing if caching is already disabled.

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

    try:
        # Disable website cache
        api_response = api_instance.disable_website_cache_v1(username, domain)
        print("The response of HostingCacheApi->disable_website_cache_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingCacheApi->disable_website_cache_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **domain** | **str**| Domain name | 

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

# **enable_cacheless_mode_v1**
> CommonSuccessEmptyResource enable_cacheless_mode_v1(username, domain)

Enable cacheless mode

Enables development (cacheless) mode where nothing is cached, effectively turning off all
caching for the website. Use it while actively developing, testing changes, debugging issues,
or when real-time updates must be visible. Disable cacheless mode afterwards to restore
normal caching.

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

    try:
        # Enable cacheless mode
        api_response = api_instance.enable_cacheless_mode_v1(username, domain)
        print("The response of HostingCacheApi->enable_cacheless_mode_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingCacheApi->enable_cacheless_mode_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **domain** | **str**| Domain name | 

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

# **enable_website_cache_v1**
> CommonSuccessEmptyResource enable_website_cache_v1(username, domain)

Enable website cache

Turns on server-side caching for the website for better performance. Use it for faster page
loads, reduced server load, or improved user experience. Recommended for production websites.

Does nothing if caching is already enabled.

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

    try:
        # Enable website cache
        api_response = api_instance.enable_website_cache_v1(username, domain)
        print("The response of HostingCacheApi->enable_website_cache_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingCacheApi->enable_website_cache_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **domain** | **str**| Domain name | 

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

