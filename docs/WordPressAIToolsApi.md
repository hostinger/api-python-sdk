# hostinger_api.WordPressAIToolsApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**set_ai_option_status_v1**](WordPressAIToolsApi.md#set_ai_option_status_v1) | **PATCH** /api/hosting/v1/accounts/{username}/wordpress/{software}/hostinger-plugins/ai-option/status | Set AI option status
[**show_ai_option_status_v1**](WordPressAIToolsApi.md#show_ai_option_status_v1) | **GET** /api/hosting/v1/accounts/{username}/wordpress/{software}/hostinger-plugins/ai-option/status | Show AI option status


# **set_ai_option_status_v1**
> CommonSuccessEmptyResource set_ai_option_status_v1(username, software, word_press_v1_hostinger_plugins_update_ai_option_status_request)

Set AI option status

Enable or disable an AI option for the Hostinger Tools plugin on the specified
WordPress installation.

Provide the WordPress installation (software) identifier in the path. It can
be obtained from GET /api/hosting/v1/wordpress/installations (the `id` field).

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.common_success_empty_resource import CommonSuccessEmptyResource
from hostinger_api.models.word_press_v1_hostinger_plugins_update_ai_option_status_request import WordPressV1HostingerPluginsUpdateAiOptionStatusRequest
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.WordPressAIToolsApi(api_client)
    username = 'u123456789' # str | 
    software = '1232456789' # str | WordPress installation (software) identifier
    word_press_v1_hostinger_plugins_update_ai_option_status_request = hostinger_api.WordPressV1HostingerPluginsUpdateAiOptionStatusRequest() # WordPressV1HostingerPluginsUpdateAiOptionStatusRequest | 

    try:
        # Set AI option status
        api_response = api_instance.set_ai_option_status_v1(username, software, word_press_v1_hostinger_plugins_update_ai_option_status_request)
        print("The response of WordPressAIToolsApi->set_ai_option_status_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WordPressAIToolsApi->set_ai_option_status_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **software** | **str**| WordPress installation (software) identifier | 
 **word_press_v1_hostinger_plugins_update_ai_option_status_request** | [**WordPressV1HostingerPluginsUpdateAiOptionStatusRequest**](WordPressV1HostingerPluginsUpdateAiOptionStatusRequest.md)|  | 

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

# **show_ai_option_status_v1**
> WordPressV1HostingerPluginsAiOptionStatusResource show_ai_option_status_v1(username, software, option=option)

Show AI option status

Show the current AI option status for the Hostinger Tools plugin on the
specified WordPress installation. Filter by `option` to return a single
option, or omit it to return all options.

Provide the WordPress installation (software) identifier in the path. It can
be obtained from GET /api/hosting/v1/wordpress/installations (the `id` field).

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.word_press_v1_hostinger_plugins_ai_option_status_resource import WordPressV1HostingerPluginsAiOptionStatusResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.WordPressAIToolsApi(api_client)
    username = 'u123456789' # str | 
    software = '1232456789' # str | WordPress installation (software) identifier
    option = 'llmstxt' # str | Filter the status by a single AI option. (optional)

    try:
        # Show AI option status
        api_response = api_instance.show_ai_option_status_v1(username, software, option=option)
        print("The response of WordPressAIToolsApi->show_ai_option_status_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WordPressAIToolsApi->show_ai_option_status_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **software** | **str**| WordPress installation (software) identifier | 
 **option** | **str**| Filter the status by a single AI option. | [optional] 

### Return type

[**WordPressV1HostingerPluginsAiOptionStatusResource**](WordPressV1HostingerPluginsAiOptionStatusResource.md)

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

