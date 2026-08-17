# hostinger_api.AgencyHostingPHPApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_available_php_versions_for_a_website_v1**](AgencyHostingPHPApi.md#list_available_php_versions_for_a_website_v1) | **GET** /api/agency-hosting/v1/websites/{website_uid}/php-settings/versions | List available PHP versions for a website
[**list_available_php_versions_for_an_order_v1**](AgencyHostingPHPApi.md#list_available_php_versions_for_an_order_v1) | **GET** /api/agency-hosting/v1/orders/{order_id}/websites/php-settings/versions | List available PHP versions for an order
[**list_php_extensions_for_a_website_v1**](AgencyHostingPHPApi.md#list_php_extensions_for_a_website_v1) | **GET** /api/agency-hosting/v1/websites/{website_uid}/php-settings/extensions | List PHP extensions for a website
[**list_php_options_for_a_website_v1**](AgencyHostingPHPApi.md#list_php_options_for_a_website_v1) | **GET** /api/agency-hosting/v1/websites/{website_uid}/php-settings/options | List PHP options for a website
[**replace_website_php_extensions_v1**](AgencyHostingPHPApi.md#replace_website_php_extensions_v1) | **PUT** /api/agency-hosting/v1/websites/{website_uid}/php-settings/extensions | Replace website PHP extensions
[**replace_website_php_options_v1**](AgencyHostingPHPApi.md#replace_website_php_options_v1) | **PUT** /api/agency-hosting/v1/websites/{website_uid}/php-settings/options | Replace website PHP options
[**update_website_php_version_v1**](AgencyHostingPHPApi.md#update_website_php_version_v1) | **PATCH** /api/agency-hosting/v1/websites/{website_uid}/php-settings/version | Update website PHP version


# **list_available_php_versions_for_a_website_v1**
> List[AgencyHostingV1PhpVersionResource] list_available_php_versions_for_a_website_v1(website_uid)

List available PHP versions for a website

Lists the PHP versions an Agency Plan website can be switched to. The version the website is currently running is returned as settings.php.version by the website details endpoint.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.agency_hosting_v1_php_version_resource import AgencyHostingV1PhpVersionResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.AgencyHostingPHPApi(api_client)
    website_uid = 'zpwlGlp19' # str | Agency Plan website UID

    try:
        # List available PHP versions for a website
        api_response = api_instance.list_available_php_versions_for_a_website_v1(website_uid)
        print("The response of AgencyHostingPHPApi->list_available_php_versions_for_a_website_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgencyHostingPHPApi->list_available_php_versions_for_a_website_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website_uid** | **str**| Agency Plan website UID | 

### Return type

[**List[AgencyHostingV1PhpVersionResource]**](AgencyHostingV1PhpVersionResource.md)

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

# **list_available_php_versions_for_an_order_v1**
> List[AgencyHostingV1PhpVersionResource] list_available_php_versions_for_an_order_v1(order_id)

List available PHP versions for an order

Lists the PHP versions available to websites created under an Agency Plan order, determined by the server the order is hosted on. Use this before creating a website; for a website that already exists, call the website-scoped versions endpoint instead.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.agency_hosting_v1_php_version_resource import AgencyHostingV1PhpVersionResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.AgencyHostingPHPApi(api_client)
    order_id = 123456 # int | Agency Plan order ID

    try:
        # List available PHP versions for an order
        api_response = api_instance.list_available_php_versions_for_an_order_v1(order_id)
        print("The response of AgencyHostingPHPApi->list_available_php_versions_for_an_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgencyHostingPHPApi->list_available_php_versions_for_an_order_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **int**| Agency Plan order ID | 

### Return type

[**List[AgencyHostingV1PhpVersionResource]**](AgencyHostingV1PhpVersionResource.md)

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

# **list_php_extensions_for_a_website_v1**
> List[AgencyHostingV1PhpExtensionResource] list_php_extensions_for_a_website_v1(website_uid)

List PHP extensions for a website

Lists every PHP extension available to an Agency Plan website and whether it is currently enabled.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.agency_hosting_v1_php_extension_resource import AgencyHostingV1PhpExtensionResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.AgencyHostingPHPApi(api_client)
    website_uid = 'zpwlGlp19' # str | Agency Plan website UID

    try:
        # List PHP extensions for a website
        api_response = api_instance.list_php_extensions_for_a_website_v1(website_uid)
        print("The response of AgencyHostingPHPApi->list_php_extensions_for_a_website_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgencyHostingPHPApi->list_php_extensions_for_a_website_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website_uid** | **str**| Agency Plan website UID | 

### Return type

[**List[AgencyHostingV1PhpExtensionResource]**](AgencyHostingV1PhpExtensionResource.md)

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

# **list_php_options_for_a_website_v1**
> List[AgencyHostingV1PhpOptionResource] list_php_options_for_a_website_v1(website_uid)

List PHP options for a website

Lists the php.ini directives that can be configured for an Agency Plan website, each with its default, the value currently in effect, and the values it accepts.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.agency_hosting_v1_php_option_resource import AgencyHostingV1PhpOptionResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.AgencyHostingPHPApi(api_client)
    website_uid = 'zpwlGlp19' # str | Agency Plan website UID

    try:
        # List PHP options for a website
        api_response = api_instance.list_php_options_for_a_website_v1(website_uid)
        print("The response of AgencyHostingPHPApi->list_php_options_for_a_website_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgencyHostingPHPApi->list_php_options_for_a_website_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website_uid** | **str**| Agency Plan website UID | 

### Return type

[**List[AgencyHostingV1PhpOptionResource]**](AgencyHostingV1PhpOptionResource.md)

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

# **replace_website_php_extensions_v1**
> CommonSuccessEmptyResource replace_website_php_extensions_v1(website_uid, agency_hosting_v1_php_update_extensions_request)

Replace website PHP extensions

Replaces the set of PHP extensions enabled on an Agency Plan website with the ones provided. Any toggleable extension not in the request is disabled, so call the extensions endpoint first and send the full desired set. Extensions compiled into PHP, reported with the "built-in" state, are always active and are unaffected.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.agency_hosting_v1_php_update_extensions_request import AgencyHostingV1PhpUpdateExtensionsRequest
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
    api_instance = hostinger_api.AgencyHostingPHPApi(api_client)
    website_uid = 'zpwlGlp19' # str | Agency Plan website UID
    agency_hosting_v1_php_update_extensions_request = hostinger_api.AgencyHostingV1PhpUpdateExtensionsRequest() # AgencyHostingV1PhpUpdateExtensionsRequest | 

    try:
        # Replace website PHP extensions
        api_response = api_instance.replace_website_php_extensions_v1(website_uid, agency_hosting_v1_php_update_extensions_request)
        print("The response of AgencyHostingPHPApi->replace_website_php_extensions_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgencyHostingPHPApi->replace_website_php_extensions_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website_uid** | **str**| Agency Plan website UID | 
 **agency_hosting_v1_php_update_extensions_request** | [**AgencyHostingV1PhpUpdateExtensionsRequest**](AgencyHostingV1PhpUpdateExtensionsRequest.md)|  | 

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

# **replace_website_php_options_v1**
> CommonSuccessEmptyResource replace_website_php_options_v1(website_uid, agency_hosting_v1_php_update_options_request)

Replace website PHP options

Replaces the custom php.ini values on an Agency Plan website with the ones provided. Any option not in the request is reset to its default, so call the options endpoint first and send the full desired set. Sending an empty array resets every option to its default.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.agency_hosting_v1_php_update_options_request import AgencyHostingV1PhpUpdateOptionsRequest
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
    api_instance = hostinger_api.AgencyHostingPHPApi(api_client)
    website_uid = 'zpwlGlp19' # str | Agency Plan website UID
    agency_hosting_v1_php_update_options_request = hostinger_api.AgencyHostingV1PhpUpdateOptionsRequest() # AgencyHostingV1PhpUpdateOptionsRequest | 

    try:
        # Replace website PHP options
        api_response = api_instance.replace_website_php_options_v1(website_uid, agency_hosting_v1_php_update_options_request)
        print("The response of AgencyHostingPHPApi->replace_website_php_options_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgencyHostingPHPApi->replace_website_php_options_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website_uid** | **str**| Agency Plan website UID | 
 **agency_hosting_v1_php_update_options_request** | [**AgencyHostingV1PhpUpdateOptionsRequest**](AgencyHostingV1PhpUpdateOptionsRequest.md)|  | 

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

# **update_website_php_version_v1**
> CommonSuccessEmptyResource update_website_php_version_v1(website_uid, agency_hosting_v1_php_update_version_request)

Update website PHP version

Switches an Agency Plan website to a different PHP version. Call the available versions endpoint first to see which versions can be selected. The website restarts on the new version, so requests served during the switch may fail and code that is incompatible with the target version will break.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.agency_hosting_v1_php_update_version_request import AgencyHostingV1PhpUpdateVersionRequest
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
    api_instance = hostinger_api.AgencyHostingPHPApi(api_client)
    website_uid = 'zpwlGlp19' # str | Agency Plan website UID
    agency_hosting_v1_php_update_version_request = hostinger_api.AgencyHostingV1PhpUpdateVersionRequest() # AgencyHostingV1PhpUpdateVersionRequest | 

    try:
        # Update website PHP version
        api_response = api_instance.update_website_php_version_v1(website_uid, agency_hosting_v1_php_update_version_request)
        print("The response of AgencyHostingPHPApi->update_website_php_version_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgencyHostingPHPApi->update_website_php_version_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website_uid** | **str**| Agency Plan website UID | 
 **agency_hosting_v1_php_update_version_request** | [**AgencyHostingV1PhpUpdateVersionRequest**](AgencyHostingV1PhpUpdateVersionRequest.md)|  | 

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

