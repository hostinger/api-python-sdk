# hostinger_api.WordPressPluginsApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_word_press_plugin_v1**](WordPressPluginsApi.md#activate_word_press_plugin_v1) | **POST** /api/hosting/v1/accounts/{username}/wordpress/{software}/plugins/activate | Activate WordPress plugin
[**check_if_woo_commerce_is_installed_v1**](WordPressPluginsApi.md#check_if_woo_commerce_is_installed_v1) | **GET** /api/hosting/v1/wordpress/plugins/is-woocommerce-installed | Check if WooCommerce is installed
[**deactivate_word_press_plugin_v1**](WordPressPluginsApi.md#deactivate_word_press_plugin_v1) | **POST** /api/hosting/v1/accounts/{username}/wordpress/{software}/plugins/deactivate | Deactivate WordPress plugin
[**install_word_press_plugins_v1**](WordPressPluginsApi.md#install_word_press_plugins_v1) | **POST** /api/hosting/v1/accounts/{username}/wordpress/{software}/plugins/install | Install WordPress plugins
[**list_available_word_press_plugins_v1**](WordPressPluginsApi.md#list_available_word_press_plugins_v1) | **GET** /api/hosting/v1/accounts/{username}/wordpress/{software}/plugins/available | List available WordPress plugins
[**list_installed_word_press_plugins_v1**](WordPressPluginsApi.md#list_installed_word_press_plugins_v1) | **GET** /api/hosting/v1/accounts/{username}/wordpress/{software}/plugins | List installed WordPress plugins
[**list_suggested_word_press_plugins_v1**](WordPressPluginsApi.md#list_suggested_word_press_plugins_v1) | **GET** /api/hosting/v1/wordpress/plugins/suggested | List suggested WordPress plugins
[**search_word_press_plugins_v1**](WordPressPluginsApi.md#search_word_press_plugins_v1) | **GET** /api/hosting/v1/wordpress/plugins | Search WordPress plugins
[**uninstall_word_press_plugins_v1**](WordPressPluginsApi.md#uninstall_word_press_plugins_v1) | **POST** /api/hosting/v1/accounts/{username}/wordpress/{software}/plugins/uninstall | Uninstall WordPress plugins
[**update_hostinger_word_press_plugin_v1**](WordPressPluginsApi.md#update_hostinger_word_press_plugin_v1) | **POST** /api/hosting/v1/accounts/{username}/wordpress/{software}/plugins/hostinger/update | Update Hostinger WordPress plugin
[**update_word_press_plugins_v1**](WordPressPluginsApi.md#update_word_press_plugins_v1) | **POST** /api/hosting/v1/accounts/{username}/wordpress/{software}/plugins/update | Update WordPress plugins


# **activate_word_press_plugin_v1**
> CommonSuccessEmptyResource activate_word_press_plugin_v1(username, software, word_press_v1_plugins_activate_plugin_request)

Activate WordPress plugin

Activate an installed plugin on a WordPress installation.

Provide the WordPress installation (software) identifier in the path. It can
be obtained from GET /api/hosting/v1/wordpress/installations (the `id` field).

This operation is asynchronous: a successful response only means the activation
job has been queued.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.common_success_empty_resource import CommonSuccessEmptyResource
from hostinger_api.models.word_press_v1_plugins_activate_plugin_request import WordPressV1PluginsActivatePluginRequest
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.WordPressPluginsApi(api_client)
    username = 'u123456789' # str | 
    software = '1232456789' # str | WordPress installation (software) identifier
    word_press_v1_plugins_activate_plugin_request = hostinger_api.WordPressV1PluginsActivatePluginRequest() # WordPressV1PluginsActivatePluginRequest | 

    try:
        # Activate WordPress plugin
        api_response = api_instance.activate_word_press_plugin_v1(username, software, word_press_v1_plugins_activate_plugin_request)
        print("The response of WordPressPluginsApi->activate_word_press_plugin_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WordPressPluginsApi->activate_word_press_plugin_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **software** | **str**| WordPress installation (software) identifier | 
 **word_press_v1_plugins_activate_plugin_request** | [**WordPressV1PluginsActivatePluginRequest**](WordPressV1PluginsActivatePluginRequest.md)|  | 

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

# **check_if_woo_commerce_is_installed_v1**
> WordPressV1PluginsWoocommerceInstalledResource check_if_woo_commerce_is_installed_v1(domain=domain)

Check if WooCommerce is installed

Check whether WooCommerce is installed on any WordPress installation of a
domain. Optionally filter by domain to scope the check.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.word_press_v1_plugins_woocommerce_installed_resource import WordPressV1PluginsWoocommerceInstalledResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.WordPressPluginsApi(api_client)
    domain = 'example.com' # str | Filter by domain name (exact match) (optional)

    try:
        # Check if WooCommerce is installed
        api_response = api_instance.check_if_woo_commerce_is_installed_v1(domain=domain)
        print("The response of WordPressPluginsApi->check_if_woo_commerce_is_installed_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WordPressPluginsApi->check_if_woo_commerce_is_installed_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Filter by domain name (exact match) | [optional] 

### Return type

[**WordPressV1PluginsWoocommerceInstalledResource**](WordPressV1PluginsWoocommerceInstalledResource.md)

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

# **deactivate_word_press_plugin_v1**
> CommonSuccessEmptyResource deactivate_word_press_plugin_v1(username, software, word_press_v1_plugins_deactivate_plugin_request)

Deactivate WordPress plugin

Deactivate an installed plugin on a WordPress installation.

Provide the WordPress installation (software) identifier in the path. It can
be obtained from GET /api/hosting/v1/wordpress/installations (the `id` field).

This operation is asynchronous: a successful response only means the
deactivation job has been queued.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.common_success_empty_resource import CommonSuccessEmptyResource
from hostinger_api.models.word_press_v1_plugins_deactivate_plugin_request import WordPressV1PluginsDeactivatePluginRequest
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.WordPressPluginsApi(api_client)
    username = 'u123456789' # str | 
    software = '1232456789' # str | WordPress installation (software) identifier
    word_press_v1_plugins_deactivate_plugin_request = hostinger_api.WordPressV1PluginsDeactivatePluginRequest() # WordPressV1PluginsDeactivatePluginRequest | 

    try:
        # Deactivate WordPress plugin
        api_response = api_instance.deactivate_word_press_plugin_v1(username, software, word_press_v1_plugins_deactivate_plugin_request)
        print("The response of WordPressPluginsApi->deactivate_word_press_plugin_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WordPressPluginsApi->deactivate_word_press_plugin_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **software** | **str**| WordPress installation (software) identifier | 
 **word_press_v1_plugins_deactivate_plugin_request** | [**WordPressV1PluginsDeactivatePluginRequest**](WordPressV1PluginsDeactivatePluginRequest.md)|  | 

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

# **install_word_press_plugins_v1**
> CommonSuccessEmptyResource install_word_press_plugins_v1(username, software, word_press_v1_plugins_install_plugins_request)

Install WordPress plugins

Install one or more plugins on an existing WordPress installation.

Provide the WordPress installation (software) identifier in the path. It can
be obtained from GET /api/hosting/v1/wordpress/installations (the `id`
field). Use GET /api/hosting/v1/wordpress/plugins to discover the plugin
slugs available for installation.

This operation is asynchronous: a successful response only means the install
job has been queued, not that the plugins are ready.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.common_success_empty_resource import CommonSuccessEmptyResource
from hostinger_api.models.word_press_v1_plugins_install_plugins_request import WordPressV1PluginsInstallPluginsRequest
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.WordPressPluginsApi(api_client)
    username = 'u123456789' # str | 
    software = '1232456789' # str | WordPress installation (software) identifier
    word_press_v1_plugins_install_plugins_request = hostinger_api.WordPressV1PluginsInstallPluginsRequest() # WordPressV1PluginsInstallPluginsRequest | 

    try:
        # Install WordPress plugins
        api_response = api_instance.install_word_press_plugins_v1(username, software, word_press_v1_plugins_install_plugins_request)
        print("The response of WordPressPluginsApi->install_word_press_plugins_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WordPressPluginsApi->install_word_press_plugins_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **software** | **str**| WordPress installation (software) identifier | 
 **word_press_v1_plugins_install_plugins_request** | [**WordPressV1PluginsInstallPluginsRequest**](WordPressV1PluginsInstallPluginsRequest.md)|  | 

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

# **list_available_word_press_plugins_v1**
> List[WordPressV1PluginsAvailablePluginResource] list_available_word_press_plugins_v1(username, software)

List available WordPress plugins

List plugins recommended for installation on a WordPress installation that are
not yet installed.

Provide the WordPress installation (software) identifier in the path. It can
be obtained from GET /api/hosting/v1/wordpress/installations (the `id` field).

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.word_press_v1_plugins_available_plugin_resource import WordPressV1PluginsAvailablePluginResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.WordPressPluginsApi(api_client)
    username = 'u123456789' # str | 
    software = '1232456789' # str | WordPress installation (software) identifier

    try:
        # List available WordPress plugins
        api_response = api_instance.list_available_word_press_plugins_v1(username, software)
        print("The response of WordPressPluginsApi->list_available_word_press_plugins_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WordPressPluginsApi->list_available_word_press_plugins_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **software** | **str**| WordPress installation (software) identifier | 

### Return type

[**List[WordPressV1PluginsAvailablePluginResource]**](WordPressV1PluginsAvailablePluginResource.md)

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

# **list_installed_word_press_plugins_v1**
> List[WordPressV1PluginsInstalledPluginResource] list_installed_word_press_plugins_v1(username, software, category=category)

List installed WordPress plugins

List plugins installed on a WordPress installation, including their status,
available updates and known vulnerabilities.

Provide the WordPress installation (software) identifier in the path. It can
be obtained from GET /api/hosting/v1/wordpress/installations (the `id` field).

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.word_press_v1_plugins_installed_plugin_resource import WordPressV1PluginsInstalledPluginResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.WordPressPluginsApi(api_client)
    username = 'u123456789' # str | 
    software = '1232456789' # str | WordPress installation (software) identifier
    category = 'cache' # str | Filter installed plugins by category. (optional)

    try:
        # List installed WordPress plugins
        api_response = api_instance.list_installed_word_press_plugins_v1(username, software, category=category)
        print("The response of WordPressPluginsApi->list_installed_word_press_plugins_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WordPressPluginsApi->list_installed_word_press_plugins_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **software** | **str**| WordPress installation (software) identifier | 
 **category** | **str**| Filter installed plugins by category. | [optional] 

### Return type

[**List[WordPressV1PluginsInstalledPluginResource]**](WordPressV1PluginsInstalledPluginResource.md)

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

# **list_suggested_word_press_plugins_v1**
> List[WordPressV1PluginsSuggestedPluginGroupResource] list_suggested_word_press_plugins_v1(order_id=order_id)

List suggested WordPress plugins

List curated plugin suggestions grouped by website type.

Use the returned `slug` values with
POST /api/hosting/v1/accounts/{username}/wordpress/{software}/plugins/install.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.word_press_v1_plugins_suggested_plugin_group_resource import WordPressV1PluginsSuggestedPluginGroupResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.WordPressPluginsApi(api_client)
    order_id = 123456 # int | Optionally scope suggestions to a specific order. (optional)

    try:
        # List suggested WordPress plugins
        api_response = api_instance.list_suggested_word_press_plugins_v1(order_id=order_id)
        print("The response of WordPressPluginsApi->list_suggested_word_press_plugins_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WordPressPluginsApi->list_suggested_word_press_plugins_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **int**| Optionally scope suggestions to a specific order. | [optional] 

### Return type

[**List[WordPressV1PluginsSuggestedPluginGroupResource]**](WordPressV1PluginsSuggestedPluginGroupResource.md)

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

# **search_word_press_plugins_v1**
> List[WordPressV1PluginsPluginResource] search_word_press_plugins_v1(search)

Search WordPress plugins

Search the WordPress.org plugin directory for plugins available to install.

Use the returned `slug` values with
POST /api/hosting/v1/accounts/{username}/wordpress/{software}/plugins/install.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.word_press_v1_plugins_plugin_resource import WordPressV1PluginsPluginResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.WordPressPluginsApi(api_client)
    search = 'seo' # str | Search term to match against plugin names. Minimum 3 characters.

    try:
        # Search WordPress plugins
        api_response = api_instance.search_word_press_plugins_v1(search)
        print("The response of WordPressPluginsApi->search_word_press_plugins_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WordPressPluginsApi->search_word_press_plugins_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Search term to match against plugin names. Minimum 3 characters. | 

### Return type

[**List[WordPressV1PluginsPluginResource]**](WordPressV1PluginsPluginResource.md)

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

# **uninstall_word_press_plugins_v1**
> CommonSuccessEmptyResource uninstall_word_press_plugins_v1(username, software, word_press_v1_plugins_uninstall_plugins_request)

Uninstall WordPress plugins

Uninstall one or more plugins from a WordPress installation.

Provide the WordPress installation (software) identifier in the path. It can
be obtained from GET /api/hosting/v1/wordpress/installations (the `id` field).

This operation is asynchronous: a successful response only means the uninstall
job has been queued.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.common_success_empty_resource import CommonSuccessEmptyResource
from hostinger_api.models.word_press_v1_plugins_uninstall_plugins_request import WordPressV1PluginsUninstallPluginsRequest
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.WordPressPluginsApi(api_client)
    username = 'u123456789' # str | 
    software = '1232456789' # str | WordPress installation (software) identifier
    word_press_v1_plugins_uninstall_plugins_request = hostinger_api.WordPressV1PluginsUninstallPluginsRequest() # WordPressV1PluginsUninstallPluginsRequest | 

    try:
        # Uninstall WordPress plugins
        api_response = api_instance.uninstall_word_press_plugins_v1(username, software, word_press_v1_plugins_uninstall_plugins_request)
        print("The response of WordPressPluginsApi->uninstall_word_press_plugins_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WordPressPluginsApi->uninstall_word_press_plugins_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **software** | **str**| WordPress installation (software) identifier | 
 **word_press_v1_plugins_uninstall_plugins_request** | [**WordPressV1PluginsUninstallPluginsRequest**](WordPressV1PluginsUninstallPluginsRequest.md)|  | 

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

# **update_hostinger_word_press_plugin_v1**
> CommonSuccessEmptyResource update_hostinger_word_press_plugin_v1(username, software, word_press_v1_plugins_update_hostinger_plugin_request)

Update Hostinger WordPress plugin

Update a Hostinger plugin to its latest version on a WordPress installation.

Provide the WordPress installation (software) identifier in the path. It can
be obtained from GET /api/hosting/v1/wordpress/installations (the `id` field).

This operation is asynchronous: a successful response only means the update job
has been queued.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.common_success_empty_resource import CommonSuccessEmptyResource
from hostinger_api.models.word_press_v1_plugins_update_hostinger_plugin_request import WordPressV1PluginsUpdateHostingerPluginRequest
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.WordPressPluginsApi(api_client)
    username = 'u123456789' # str | 
    software = '1232456789' # str | WordPress installation (software) identifier
    word_press_v1_plugins_update_hostinger_plugin_request = hostinger_api.WordPressV1PluginsUpdateHostingerPluginRequest() # WordPressV1PluginsUpdateHostingerPluginRequest | 

    try:
        # Update Hostinger WordPress plugin
        api_response = api_instance.update_hostinger_word_press_plugin_v1(username, software, word_press_v1_plugins_update_hostinger_plugin_request)
        print("The response of WordPressPluginsApi->update_hostinger_word_press_plugin_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WordPressPluginsApi->update_hostinger_word_press_plugin_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **software** | **str**| WordPress installation (software) identifier | 
 **word_press_v1_plugins_update_hostinger_plugin_request** | [**WordPressV1PluginsUpdateHostingerPluginRequest**](WordPressV1PluginsUpdateHostingerPluginRequest.md)|  | 

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

# **update_word_press_plugins_v1**
> CommonSuccessEmptyResource update_word_press_plugins_v1(username, software, word_press_v1_plugins_update_plugins_request)

Update WordPress plugins

Update one or more installed plugins to their latest version on a WordPress
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
from hostinger_api.models.word_press_v1_plugins_update_plugins_request import WordPressV1PluginsUpdatePluginsRequest
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.WordPressPluginsApi(api_client)
    username = 'u123456789' # str | 
    software = '1232456789' # str | WordPress installation (software) identifier
    word_press_v1_plugins_update_plugins_request = hostinger_api.WordPressV1PluginsUpdatePluginsRequest() # WordPressV1PluginsUpdatePluginsRequest | 

    try:
        # Update WordPress plugins
        api_response = api_instance.update_word_press_plugins_v1(username, software, word_press_v1_plugins_update_plugins_request)
        print("The response of WordPressPluginsApi->update_word_press_plugins_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WordPressPluginsApi->update_word_press_plugins_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **software** | **str**| WordPress installation (software) identifier | 
 **word_press_v1_plugins_update_plugins_request** | [**WordPressV1PluginsUpdatePluginsRequest**](WordPressV1PluginsUpdatePluginsRequest.md)|  | 

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

