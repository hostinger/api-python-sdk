# hostinger_api.WordPressInstallationsApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_if_word_press_installations_are_valid_v1**](WordPressInstallationsApi.md#check_if_word_press_installations_are_valid_v1) | **POST** /api/hosting/v1/accounts/{username}/wordpress/installations/check-is-valid | Check if WordPress installations are valid
[**delete_word_press_installation_v1**](WordPressInstallationsApi.md#delete_word_press_installation_v1) | **DELETE** /api/hosting/v1/accounts/{username}/wordpress/{software} | Delete WordPress installation
[**detect_word_press_installations_v1**](WordPressInstallationsApi.md#detect_word_press_installations_v1) | **POST** /api/hosting/v1/accounts/{username}/wordpress/installations/detect | Detect WordPress installations
[**get_installation_jwt_token_v1**](WordPressInstallationsApi.md#get_installation_jwt_token_v1) | **GET** /api/hosting/v1/accounts/{username}/wordpress/{software}/jwt-token | Get installation JWT token
[**install_word_press_v1**](WordPressInstallationsApi.md#install_word_press_v1) | **POST** /api/hosting/v1/accounts/{username}/wordpress/installations | Install WordPress
[**list_available_word_press_core_updates_v1**](WordPressInstallationsApi.md#list_available_word_press_core_updates_v1) | **GET** /api/hosting/v1/accounts/{username}/wordpress/{software}/updates | List available WordPress core updates
[**list_word_press_installations_v1**](WordPressInstallationsApi.md#list_word_press_installations_v1) | **GET** /api/hosting/v1/wordpress/installations | List WordPress installations
[**show_word_press_core_version_v1**](WordPressInstallationsApi.md#show_word_press_core_version_v1) | **GET** /api/hosting/v1/accounts/{username}/wordpress/{software}/version | Show WordPress core version
[**update_word_press_core_v1**](WordPressInstallationsApi.md#update_word_press_core_v1) | **POST** /api/hosting/v1/accounts/{username}/wordpress/{software}/update | Update WordPress core


# **check_if_word_press_installations_are_valid_v1**
> List[WordPressV1InstallationsCheckIsValidResultResource] check_if_word_press_installations_are_valid_v1(username, word_press_v1_installations_check_is_valid_request)

Check if WordPress installations are valid

Check whether one or more WordPress installations are valid and working
correctly. Detects broken installations caused by missing files, broken
plugins, themes and similar issues.

Provide the WordPress installation (software) identifiers in the body. They
can be obtained from GET /api/hosting/v1/wordpress/installations (the `id`
field).

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.word_press_v1_installations_check_is_valid_request import WordPressV1InstallationsCheckIsValidRequest
from hostinger_api.models.word_press_v1_installations_check_is_valid_result_resource import WordPressV1InstallationsCheckIsValidResultResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.WordPressInstallationsApi(api_client)
    username = 'u123456789' # str | 
    word_press_v1_installations_check_is_valid_request = hostinger_api.WordPressV1InstallationsCheckIsValidRequest() # WordPressV1InstallationsCheckIsValidRequest | 

    try:
        # Check if WordPress installations are valid
        api_response = api_instance.check_if_word_press_installations_are_valid_v1(username, word_press_v1_installations_check_is_valid_request)
        print("The response of WordPressInstallationsApi->check_if_word_press_installations_are_valid_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WordPressInstallationsApi->check_if_word_press_installations_are_valid_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **word_press_v1_installations_check_is_valid_request** | [**WordPressV1InstallationsCheckIsValidRequest**](WordPressV1InstallationsCheckIsValidRequest.md)|  | 

### Return type

[**List[WordPressV1InstallationsCheckIsValidResultResource]**](WordPressV1InstallationsCheckIsValidResultResource.md)

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

# **delete_word_press_installation_v1**
> CommonSuccessEmptyResource delete_word_press_installation_v1(username, software, word_press_v1_installations_delete_installation_request)

Delete WordPress installation

Delete the specified WordPress installation, with optional file and database
removal. This removes all associated components including plugins, themes,
staging websites and any other related data.

Provide the WordPress installation (software) identifier in the path. It can
be obtained from GET /api/hosting/v1/wordpress/installations (the `id` field).

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.common_success_empty_resource import CommonSuccessEmptyResource
from hostinger_api.models.word_press_v1_installations_delete_installation_request import WordPressV1InstallationsDeleteInstallationRequest
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.WordPressInstallationsApi(api_client)
    username = 'u123456789' # str | 
    software = '1232456789' # str | WordPress installation (software) identifier
    word_press_v1_installations_delete_installation_request = hostinger_api.WordPressV1InstallationsDeleteInstallationRequest() # WordPressV1InstallationsDeleteInstallationRequest | 

    try:
        # Delete WordPress installation
        api_response = api_instance.delete_word_press_installation_v1(username, software, word_press_v1_installations_delete_installation_request)
        print("The response of WordPressInstallationsApi->delete_word_press_installation_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WordPressInstallationsApi->delete_word_press_installation_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **software** | **str**| WordPress installation (software) identifier | 
 **word_press_v1_installations_delete_installation_request** | [**WordPressV1InstallationsDeleteInstallationRequest**](WordPressV1InstallationsDeleteInstallationRequest.md)|  | 

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

# **detect_word_press_installations_v1**
> CommonSuccessEmptyResource detect_word_press_installations_v1(username)

Detect WordPress installations

Trigger a background scan to detect WordPress installations for the account.

This operation is asynchronous: a successful response only means the scan has
been queued. Poll GET /api/hosting/v1/wordpress/installations to fetch the
detected installations once the scan completes.

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
    api_instance = hostinger_api.WordPressInstallationsApi(api_client)
    username = 'u123456789' # str | 

    try:
        # Detect WordPress installations
        api_response = api_instance.detect_word_press_installations_v1(username)
        print("The response of WordPressInstallationsApi->detect_word_press_installations_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WordPressInstallationsApi->detect_word_press_installations_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 

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

# **get_installation_jwt_token_v1**
> WordPressV1InstallationsJwtTokenResource get_installation_jwt_token_v1(username, software)

Get installation JWT token

Return a JWT token used to authenticate requests against the specified
WordPress installation, including its MCP (Model Context Protocol) endpoint.

Provide the WordPress installation (software) identifier in the path. It can
be obtained from GET /api/hosting/v1/wordpress/installations (the `id` field).

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.word_press_v1_installations_jwt_token_resource import WordPressV1InstallationsJwtTokenResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.WordPressInstallationsApi(api_client)
    username = 'u123456789' # str | 
    software = '1232456789' # str | WordPress installation (software) identifier

    try:
        # Get installation JWT token
        api_response = api_instance.get_installation_jwt_token_v1(username, software)
        print("The response of WordPressInstallationsApi->get_installation_jwt_token_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WordPressInstallationsApi->get_installation_jwt_token_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **software** | **str**| WordPress installation (software) identifier | 

### Return type

[**WordPressV1InstallationsJwtTokenResource**](WordPressV1InstallationsJwtTokenResource.md)

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

# **install_word_press_v1**
> CommonSuccessEmptyResource install_word_press_v1(username, word_press_v1_installations_install_word_press_request)

Install WordPress

Install WordPress on an existing website.

The website must already exist before calling this endpoint. To create a new
website first, use POST /api/hosting/v1/websites and poll
GET /api/hosting/v1/websites until it appears.

Call GET /api/hosting/v1/wordpress/installations filtered by username and
domain before proceeding to check whether WordPress is already installed on
the target domain/path. If WordPress already exists and `overwrite` is false
(the default), the async job will fail.

This operation is asynchronous: a successful response only means the install
job has been queued, not that WordPress is ready. Installation typically
takes 1-2 minutes. Poll GET /api/hosting/v1/wordpress/installations filtered
by username and domain to track progress. When the installation appears in
that list, WordPress is ready.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.common_success_empty_resource import CommonSuccessEmptyResource
from hostinger_api.models.word_press_v1_installations_install_word_press_request import WordPressV1InstallationsInstallWordPressRequest
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.WordPressInstallationsApi(api_client)
    username = 'u123456789' # str | 
    word_press_v1_installations_install_word_press_request = hostinger_api.WordPressV1InstallationsInstallWordPressRequest() # WordPressV1InstallationsInstallWordPressRequest | 

    try:
        # Install WordPress
        api_response = api_instance.install_word_press_v1(username, word_press_v1_installations_install_word_press_request)
        print("The response of WordPressInstallationsApi->install_word_press_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WordPressInstallationsApi->install_word_press_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **word_press_v1_installations_install_word_press_request** | [**WordPressV1InstallationsInstallWordPressRequest**](WordPressV1InstallationsInstallWordPressRequest.md)|  | 

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

# **list_available_word_press_core_updates_v1**
> List[WordPressV1InstallationsUpdateResource] list_available_word_press_core_updates_v1(username, software)

List available WordPress core updates

List available WordPress core updates for the specified installation.

Provide the WordPress installation (software) identifier in the path. It can
be obtained from GET /api/hosting/v1/wordpress/installations (the `id` field).

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.word_press_v1_installations_update_resource import WordPressV1InstallationsUpdateResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.WordPressInstallationsApi(api_client)
    username = 'u123456789' # str | 
    software = '1232456789' # str | WordPress installation (software) identifier

    try:
        # List available WordPress core updates
        api_response = api_instance.list_available_word_press_core_updates_v1(username, software)
        print("The response of WordPressInstallationsApi->list_available_word_press_core_updates_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WordPressInstallationsApi->list_available_word_press_core_updates_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **software** | **str**| WordPress installation (software) identifier | 

### Return type

[**List[WordPressV1InstallationsUpdateResource]**](WordPressV1InstallationsUpdateResource.md)

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

# **list_word_press_installations_v1**
> List[WordPressV1InstallationsWordPressInstallationResource] list_word_press_installations_v1(username=username, domain=domain, ownership=ownership)

List WordPress installations

List WordPress installations accessible to the authenticated client.

Use this endpoint to discover existing WordPress installations and to poll
for installation status after calling the install endpoint. When a newly
requested installation appears in this list, WordPress is ready. Filter by
username and domain to narrow results to a specific website.

Each installation includes a `valid` flag and, when invalid, a
`validationError` describing why.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.word_press_v1_installations_word_press_installation_resource import WordPressV1InstallationsWordPressInstallationResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.WordPressInstallationsApi(api_client)
    username = 'cl_user123' # str | Filter by specific username (optional)
    domain = 'example.com' # str | Filter by domain name (exact match) (optional)
    ownership = 'owned' # str | Filter by ownership type. Defaults to \"owned\". Use \"all\" to include both owned and managed installations. (optional)

    try:
        # List WordPress installations
        api_response = api_instance.list_word_press_installations_v1(username=username, domain=domain, ownership=ownership)
        print("The response of WordPressInstallationsApi->list_word_press_installations_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WordPressInstallationsApi->list_word_press_installations_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Filter by specific username | [optional] 
 **domain** | **str**| Filter by domain name (exact match) | [optional] 
 **ownership** | **str**| Filter by ownership type. Defaults to \&quot;owned\&quot;. Use \&quot;all\&quot; to include both owned and managed installations. | [optional] 

### Return type

[**List[WordPressV1InstallationsWordPressInstallationResource]**](WordPressV1InstallationsWordPressInstallationResource.md)

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

# **show_word_press_core_version_v1**
> WordPressV1InstallationsVersionResource show_word_press_core_version_v1(username, software)

Show WordPress core version

Show the WordPress core version for the specified installation, along with
known vulnerabilities affecting it.

Provide the WordPress installation (software) identifier in the path. It can
be obtained from GET /api/hosting/v1/wordpress/installations (the `id` field).

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.word_press_v1_installations_version_resource import WordPressV1InstallationsVersionResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.WordPressInstallationsApi(api_client)
    username = 'u123456789' # str | 
    software = '1232456789' # str | WordPress installation (software) identifier

    try:
        # Show WordPress core version
        api_response = api_instance.show_word_press_core_version_v1(username, software)
        print("The response of WordPressInstallationsApi->show_word_press_core_version_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WordPressInstallationsApi->show_word_press_core_version_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **software** | **str**| WordPress installation (software) identifier | 

### Return type

[**WordPressV1InstallationsVersionResource**](WordPressV1InstallationsVersionResource.md)

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

# **update_word_press_core_v1**
> CommonSuccessEmptyResource update_word_press_core_v1(username, software, word_press_v1_installations_update_installation_request)

Update WordPress core

Update the WordPress core for the specified installation (minor update or a
specific version).

Provide the WordPress installation (software) identifier in the path. It can
be obtained from GET /api/hosting/v1/wordpress/installations (the `id` field).

This operation is asynchronous: a successful response only means the update
job has been queued.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.common_success_empty_resource import CommonSuccessEmptyResource
from hostinger_api.models.word_press_v1_installations_update_installation_request import WordPressV1InstallationsUpdateInstallationRequest
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.WordPressInstallationsApi(api_client)
    username = 'u123456789' # str | 
    software = '1232456789' # str | WordPress installation (software) identifier
    word_press_v1_installations_update_installation_request = hostinger_api.WordPressV1InstallationsUpdateInstallationRequest() # WordPressV1InstallationsUpdateInstallationRequest | 

    try:
        # Update WordPress core
        api_response = api_instance.update_word_press_core_v1(username, software, word_press_v1_installations_update_installation_request)
        print("The response of WordPressInstallationsApi->update_word_press_core_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WordPressInstallationsApi->update_word_press_core_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **software** | **str**| WordPress installation (software) identifier | 
 **word_press_v1_installations_update_installation_request** | [**WordPressV1InstallationsUpdateInstallationRequest**](WordPressV1InstallationsUpdateInstallationRequest.md)|  | 

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

