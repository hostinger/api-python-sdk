# hostinger_api.WordPressThemesApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_word_press_theme_v1**](WordPressThemesApi.md#activate_word_press_theme_v1) | **POST** /api/hosting/v1/accounts/{username}/wordpress/{software}/themes/activate | Activate WordPress theme
[**install_word_press_theme_v1**](WordPressThemesApi.md#install_word_press_theme_v1) | **POST** /api/hosting/v1/accounts/{username}/wordpress/{software}/themes/install | Install WordPress theme
[**list_installed_word_press_themes_v1**](WordPressThemesApi.md#list_installed_word_press_themes_v1) | **GET** /api/hosting/v1/accounts/{username}/wordpress/{software}/themes | List installed WordPress themes
[**list_word_press_themes_v1**](WordPressThemesApi.md#list_word_press_themes_v1) | **GET** /api/hosting/v1/wordpress/themes | List WordPress themes
[**uninstall_word_press_themes_v1**](WordPressThemesApi.md#uninstall_word_press_themes_v1) | **POST** /api/hosting/v1/accounts/{username}/wordpress/{software}/themes/uninstall | Uninstall WordPress themes
[**update_word_press_themes_v1**](WordPressThemesApi.md#update_word_press_themes_v1) | **POST** /api/hosting/v1/accounts/{username}/wordpress/{software}/themes/update | Update WordPress themes


# **activate_word_press_theme_v1**
> CommonSuccessEmptyResource activate_word_press_theme_v1(username, software, word_press_v1_themes_activate_theme_request)

Activate WordPress theme

Activate an installed theme on a WordPress installation.

Provide the WordPress installation (software) identifier in the path. It can
be obtained from GET /api/hosting/v1/wordpress/installations (the `id` field).

This operation is asynchronous: a successful response only means the activation
job has been queued.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.common_success_empty_resource import CommonSuccessEmptyResource
from hostinger_api.models.word_press_v1_themes_activate_theme_request import WordPressV1ThemesActivateThemeRequest
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.WordPressThemesApi(api_client)
    username = 'u123456789' # str | 
    software = '1232456789' # str | WordPress installation (software) identifier
    word_press_v1_themes_activate_theme_request = hostinger_api.WordPressV1ThemesActivateThemeRequest() # WordPressV1ThemesActivateThemeRequest | 

    try:
        # Activate WordPress theme
        api_response = api_instance.activate_word_press_theme_v1(username, software, word_press_v1_themes_activate_theme_request)
        print("The response of WordPressThemesApi->activate_word_press_theme_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WordPressThemesApi->activate_word_press_theme_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **software** | **str**| WordPress installation (software) identifier | 
 **word_press_v1_themes_activate_theme_request** | [**WordPressV1ThemesActivateThemeRequest**](WordPressV1ThemesActivateThemeRequest.md)|  | 

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

# **install_word_press_theme_v1**
> CommonSuccessEmptyResource install_word_press_theme_v1(username, software, word_press_v1_themes_install_theme_request)

Install WordPress theme

Install a theme on an existing WordPress installation.

Provide the WordPress installation (software) identifier in the path. It can
be obtained from GET /api/hosting/v1/wordpress/installations (the `id`
field).

When the theme is one of the Hostinger themes (hostinger-blog,
hostinger-affiliate-theme, hostinger-ai-theme), the optional `palette`,
`layout`, and `font` fields are forwarded to the custom installer (defaults:
palette1, layout1, default). For any other theme they are ignored.

This operation is asynchronous: a successful response only means the install
job has been queued, not that the theme is ready.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.common_success_empty_resource import CommonSuccessEmptyResource
from hostinger_api.models.word_press_v1_themes_install_theme_request import WordPressV1ThemesInstallThemeRequest
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.WordPressThemesApi(api_client)
    username = 'u123456789' # str | 
    software = '1232456789' # str | WordPress installation (software) identifier
    word_press_v1_themes_install_theme_request = hostinger_api.WordPressV1ThemesInstallThemeRequest() # WordPressV1ThemesInstallThemeRequest | 

    try:
        # Install WordPress theme
        api_response = api_instance.install_word_press_theme_v1(username, software, word_press_v1_themes_install_theme_request)
        print("The response of WordPressThemesApi->install_word_press_theme_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WordPressThemesApi->install_word_press_theme_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **software** | **str**| WordPress installation (software) identifier | 
 **word_press_v1_themes_install_theme_request** | [**WordPressV1ThemesInstallThemeRequest**](WordPressV1ThemesInstallThemeRequest.md)|  | 

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

# **list_installed_word_press_themes_v1**
> List[WordPressV1ThemesInstalledThemeResource] list_installed_word_press_themes_v1(username, software)

List installed WordPress themes

List themes installed on a WordPress installation, including their status,
available updates and known vulnerabilities.

Provide the WordPress installation (software) identifier in the path. It can
be obtained from GET /api/hosting/v1/wordpress/installations (the `id` field).

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.word_press_v1_themes_installed_theme_resource import WordPressV1ThemesInstalledThemeResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.WordPressThemesApi(api_client)
    username = 'u123456789' # str | 
    software = '1232456789' # str | WordPress installation (software) identifier

    try:
        # List installed WordPress themes
        api_response = api_instance.list_installed_word_press_themes_v1(username, software)
        print("The response of WordPressThemesApi->list_installed_word_press_themes_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WordPressThemesApi->list_installed_word_press_themes_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **software** | **str**| WordPress installation (software) identifier | 

### Return type

[**List[WordPressV1ThemesInstalledThemeResource]**](WordPressV1ThemesInstalledThemeResource.md)

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

# **list_word_press_themes_v1**
> List[WordPressV1ThemesThemeResource] list_word_press_themes_v1(order_id=order_id, search=search)

List WordPress themes

List WordPress themes available to install.

Use the returned `slug` values with
POST /api/hosting/v1/accounts/{username}/wordpress/{software}/themes/install.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.word_press_v1_themes_theme_resource import WordPressV1ThemesThemeResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.WordPressThemesApi(api_client)
    order_id = 123456 # int | Optionally scope themes to a specific order. (optional)
    search = 'blog' # str | Search term to match against theme names. (optional)

    try:
        # List WordPress themes
        api_response = api_instance.list_word_press_themes_v1(order_id=order_id, search=search)
        print("The response of WordPressThemesApi->list_word_press_themes_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WordPressThemesApi->list_word_press_themes_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **int**| Optionally scope themes to a specific order. | [optional] 
 **search** | **str**| Search term to match against theme names. | [optional] 

### Return type

[**List[WordPressV1ThemesThemeResource]**](WordPressV1ThemesThemeResource.md)

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

# **uninstall_word_press_themes_v1**
> CommonSuccessEmptyResource uninstall_word_press_themes_v1(username, software, word_press_v1_themes_uninstall_themes_request)

Uninstall WordPress themes

Uninstall one or more themes from a WordPress installation.

Provide the WordPress installation (software) identifier in the path. It can
be obtained from GET /api/hosting/v1/wordpress/installations (the `id` field).

This operation is asynchronous: a successful response only means the uninstall
job has been queued.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.common_success_empty_resource import CommonSuccessEmptyResource
from hostinger_api.models.word_press_v1_themes_uninstall_themes_request import WordPressV1ThemesUninstallThemesRequest
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.WordPressThemesApi(api_client)
    username = 'u123456789' # str | 
    software = '1232456789' # str | WordPress installation (software) identifier
    word_press_v1_themes_uninstall_themes_request = hostinger_api.WordPressV1ThemesUninstallThemesRequest() # WordPressV1ThemesUninstallThemesRequest | 

    try:
        # Uninstall WordPress themes
        api_response = api_instance.uninstall_word_press_themes_v1(username, software, word_press_v1_themes_uninstall_themes_request)
        print("The response of WordPressThemesApi->uninstall_word_press_themes_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WordPressThemesApi->uninstall_word_press_themes_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **software** | **str**| WordPress installation (software) identifier | 
 **word_press_v1_themes_uninstall_themes_request** | [**WordPressV1ThemesUninstallThemesRequest**](WordPressV1ThemesUninstallThemesRequest.md)|  | 

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

# **update_word_press_themes_v1**
> CommonSuccessEmptyResource update_word_press_themes_v1(username, software, word_press_v1_themes_update_themes_request)

Update WordPress themes

Update one or more installed themes to their latest version on a WordPress
installation.

Provide the WordPress installation (software) identifier in the path. It can
be obtained from GET /api/hosting/v1/wordpress/installations (the `id` field).

This operation is asynchronous: a successful response only means the update job
has been queued.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.common_success_empty_resource import CommonSuccessEmptyResource
from hostinger_api.models.word_press_v1_themes_update_themes_request import WordPressV1ThemesUpdateThemesRequest
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.WordPressThemesApi(api_client)
    username = 'u123456789' # str | 
    software = '1232456789' # str | WordPress installation (software) identifier
    word_press_v1_themes_update_themes_request = hostinger_api.WordPressV1ThemesUpdateThemesRequest() # WordPressV1ThemesUpdateThemesRequest | 

    try:
        # Update WordPress themes
        api_response = api_instance.update_word_press_themes_v1(username, software, word_press_v1_themes_update_themes_request)
        print("The response of WordPressThemesApi->update_word_press_themes_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WordPressThemesApi->update_word_press_themes_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **software** | **str**| WordPress installation (software) identifier | 
 **word_press_v1_themes_update_themes_request** | [**WordPressV1ThemesUpdateThemesRequest**](WordPressV1ThemesUpdateThemesRequest.md)|  | 

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

