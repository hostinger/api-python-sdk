# hostinger_api.WordPressMaintenanceApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**show_maintenance_status_v1**](WordPressMaintenanceApi.md#show_maintenance_status_v1) | **GET** /api/hosting/v1/accounts/{username}/wordpress/{software}/maintenance/status | Show maintenance status
[**toggle_maintenance_mode_v1**](WordPressMaintenanceApi.md#toggle_maintenance_mode_v1) | **PATCH** /api/hosting/v1/accounts/{username}/wordpress/{software}/maintenance/toggle | Toggle maintenance mode


# **show_maintenance_status_v1**
> WordPressV1MaintenanceMaintenanceStatusResource show_maintenance_status_v1(username, software)

Show maintenance status

Show the maintenance mode status for the specified WordPress installation.

Provide the WordPress installation (software) identifier in the path. It can
be obtained from GET /api/hosting/v1/wordpress/installations (the `id` field).

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.word_press_v1_maintenance_maintenance_status_resource import WordPressV1MaintenanceMaintenanceStatusResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.WordPressMaintenanceApi(api_client)
    username = 'u123456789' # str | 
    software = '1232456789' # str | WordPress installation (software) identifier

    try:
        # Show maintenance status
        api_response = api_instance.show_maintenance_status_v1(username, software)
        print("The response of WordPressMaintenanceApi->show_maintenance_status_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WordPressMaintenanceApi->show_maintenance_status_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **software** | **str**| WordPress installation (software) identifier | 

### Return type

[**WordPressV1MaintenanceMaintenanceStatusResource**](WordPressV1MaintenanceMaintenanceStatusResource.md)

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

# **toggle_maintenance_mode_v1**
> CommonSuccessEmptyResource toggle_maintenance_mode_v1(username, software, word_press_v1_maintenance_toggle_maintenance_request)

Toggle maintenance mode

Enable or disable maintenance mode for the specified WordPress installation,
based on the `enabled` flag.

Provide the WordPress installation (software) identifier in the path. It can
be obtained from GET /api/hosting/v1/wordpress/installations (the `id` field).

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.common_success_empty_resource import CommonSuccessEmptyResource
from hostinger_api.models.word_press_v1_maintenance_toggle_maintenance_request import WordPressV1MaintenanceToggleMaintenanceRequest
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.WordPressMaintenanceApi(api_client)
    username = 'u123456789' # str | 
    software = '1232456789' # str | WordPress installation (software) identifier
    word_press_v1_maintenance_toggle_maintenance_request = hostinger_api.WordPressV1MaintenanceToggleMaintenanceRequest() # WordPressV1MaintenanceToggleMaintenanceRequest | 

    try:
        # Toggle maintenance mode
        api_response = api_instance.toggle_maintenance_mode_v1(username, software, word_press_v1_maintenance_toggle_maintenance_request)
        print("The response of WordPressMaintenanceApi->toggle_maintenance_mode_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WordPressMaintenanceApi->toggle_maintenance_mode_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **software** | **str**| WordPress installation (software) identifier | 
 **word_press_v1_maintenance_toggle_maintenance_request** | [**WordPressV1MaintenanceToggleMaintenanceRequest**](WordPressV1MaintenanceToggleMaintenanceRequest.md)|  | 

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

