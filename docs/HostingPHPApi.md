# hostinger_api.HostingPHPApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_php_details_v1**](HostingPHPApi.md#get_php_details_v1) | **GET** /api/hosting/v1/accounts/{username}/websites/{domain}/php/details | Get PHP details
[**get_php_info_v1**](HostingPHPApi.md#get_php_info_v1) | **GET** /api/hosting/v1/accounts/{username}/websites/{domain}/php/php-info | Get PHP info
[**reset_php_extensions_v1**](HostingPHPApi.md#reset_php_extensions_v1) | **PATCH** /api/hosting/v1/accounts/{username}/websites/{domain}/php/extensions/reset | Reset PHP extensions
[**update_php_extensions_v1**](HostingPHPApi.md#update_php_extensions_v1) | **PATCH** /api/hosting/v1/accounts/{username}/websites/{domain}/php/extensions | Update PHP extensions
[**update_php_options_v1**](HostingPHPApi.md#update_php_options_v1) | **PATCH** /api/hosting/v1/accounts/{username}/websites/{domain}/php/options | Update PHP options
[**update_php_version_v1**](HostingPHPApi.md#update_php_version_v1) | **PATCH** /api/hosting/v1/accounts/{username}/websites/{domain}/php/version | Update PHP version


# **get_php_details_v1**
> HostingV1PhpPhpDetailsResource get_php_details_v1(username, domain)

Get PHP details

Returns the full PHP configuration for the website: current version, available versions
(supported and unsupported), enabled/disabled extensions, options with their current value,
default, type and the plan limit (`max`), and conflicting extension groups.

Use it to check the current PHP setup before updating the version, extensions or options.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.hosting_v1_php_php_details_resource import HostingV1PhpPhpDetailsResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.HostingPHPApi(api_client)
    username = 'u123456789' # str | 
    domain = 'mydomain.tld' # str | Domain name

    try:
        # Get PHP details
        api_response = api_instance.get_php_details_v1(username, domain)
        print("The response of HostingPHPApi->get_php_details_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingPHPApi->get_php_details_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **domain** | **str**| Domain name | 

### Return type

[**HostingV1PhpPhpDetailsResource**](HostingV1PhpPhpDetailsResource.md)

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

# **get_php_info_v1**
> HostingV1PhpPhpInfoResource get_php_info_v1(username, domain)

Get PHP info

Returns the full phpinfo page (HTML) for the website.

Use it to debug PHP issues or inspect the complete PHP environment of the website.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.hosting_v1_php_php_info_resource import HostingV1PhpPhpInfoResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.HostingPHPApi(api_client)
    username = 'u123456789' # str | 
    domain = 'mydomain.tld' # str | Domain name

    try:
        # Get PHP info
        api_response = api_instance.get_php_info_v1(username, domain)
        print("The response of HostingPHPApi->get_php_info_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingPHPApi->get_php_info_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **domain** | **str**| Domain name | 

### Return type

[**HostingV1PhpPhpInfoResource**](HostingV1PhpPhpInfoResource.md)

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

# **reset_php_extensions_v1**
> CommonSuccessEmptyResource reset_php_extensions_v1(username, domain)

Reset PHP extensions

Resets all PHP extensions of the website to their default state.

Use it to recover from extension conflicts or restore the original configuration.

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
    api_instance = hostinger_api.HostingPHPApi(api_client)
    username = 'u123456789' # str | 
    domain = 'mydomain.tld' # str | Domain name

    try:
        # Reset PHP extensions
        api_response = api_instance.reset_php_extensions_v1(username, domain)
        print("The response of HostingPHPApi->reset_php_extensions_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingPHPApi->reset_php_extensions_v1: %s\n" % e)
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

# **update_php_extensions_v1**
> CommonSuccessEmptyResource update_php_extensions_v1(username, domain, hosting_v1_php_update_php_extensions_request)

Update PHP extensions

Enables or disables PHP extensions (modules) for the website.

Use the Get PHP details endpoint to check the current extension states before changing them.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.common_success_empty_resource import CommonSuccessEmptyResource
from hostinger_api.models.hosting_v1_php_update_php_extensions_request import HostingV1PhpUpdatePhpExtensionsRequest
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.HostingPHPApi(api_client)
    username = 'u123456789' # str | 
    domain = 'mydomain.tld' # str | Domain name
    hosting_v1_php_update_php_extensions_request = hostinger_api.HostingV1PhpUpdatePhpExtensionsRequest() # HostingV1PhpUpdatePhpExtensionsRequest | 

    try:
        # Update PHP extensions
        api_response = api_instance.update_php_extensions_v1(username, domain, hosting_v1_php_update_php_extensions_request)
        print("The response of HostingPHPApi->update_php_extensions_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingPHPApi->update_php_extensions_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **domain** | **str**| Domain name | 
 **hosting_v1_php_update_php_extensions_request** | [**HostingV1PhpUpdatePhpExtensionsRequest**](HostingV1PhpUpdatePhpExtensionsRequest.md)|  | 

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

# **update_php_options_v1**
> CommonSuccessEmptyResource update_php_options_v1(username, domain, hosting_v1_php_update_php_options_request)

Update PHP options

Updates PHP options for the website (e.g. `memory_limit`, `max_execution_time`, `upload_max_filesize`).
Only provide the options you want to change, inside the `options` object.

Values above the account plan limit are silently capped to that limit, so the request can succeed
with a smaller applied value. Call the Get PHP details endpoint afterwards to read the applied value.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.common_success_empty_resource import CommonSuccessEmptyResource
from hostinger_api.models.hosting_v1_php_update_php_options_request import HostingV1PhpUpdatePhpOptionsRequest
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.HostingPHPApi(api_client)
    username = 'u123456789' # str | 
    domain = 'mydomain.tld' # str | Domain name
    hosting_v1_php_update_php_options_request = hostinger_api.HostingV1PhpUpdatePhpOptionsRequest() # HostingV1PhpUpdatePhpOptionsRequest | 

    try:
        # Update PHP options
        api_response = api_instance.update_php_options_v1(username, domain, hosting_v1_php_update_php_options_request)
        print("The response of HostingPHPApi->update_php_options_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingPHPApi->update_php_options_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **domain** | **str**| Domain name | 
 **hosting_v1_php_update_php_options_request** | [**HostingV1PhpUpdatePhpOptionsRequest**](HostingV1PhpUpdatePhpOptionsRequest.md)|  | 

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

# **update_php_version_v1**
> CommonSuccessEmptyResource update_php_version_v1(username, domain, hosting_v1_php_update_php_version_request)

Update PHP version

Changes the PHP version of the website.

Use the Get PHP details endpoint to see the versions available for the website.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.common_success_empty_resource import CommonSuccessEmptyResource
from hostinger_api.models.hosting_v1_php_update_php_version_request import HostingV1PhpUpdatePhpVersionRequest
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.HostingPHPApi(api_client)
    username = 'u123456789' # str | 
    domain = 'mydomain.tld' # str | Domain name
    hosting_v1_php_update_php_version_request = hostinger_api.HostingV1PhpUpdatePhpVersionRequest() # HostingV1PhpUpdatePhpVersionRequest | 

    try:
        # Update PHP version
        api_response = api_instance.update_php_version_v1(username, domain, hosting_v1_php_update_php_version_request)
        print("The response of HostingPHPApi->update_php_version_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingPHPApi->update_php_version_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **domain** | **str**| Domain name | 
 **hosting_v1_php_update_php_version_request** | [**HostingV1PhpUpdatePhpVersionRequest**](HostingV1PhpUpdatePhpVersionRequest.md)|  | 

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

