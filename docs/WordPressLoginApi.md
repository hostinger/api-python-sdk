# hostinger_api.WordPressLoginApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_login_links_v1**](WordPressLoginApi.md#create_login_links_v1) | **POST** /api/hosting/v1/accounts/{username}/wordpress/{software}/login/links | Create login links


# **create_login_links_v1**
> WordPressV1LoginLoginLinksResource create_login_links_v1(username, software)

Create login links

Create temporary auto-login links for the specified WordPress installation.

Provide the WordPress installation (software) identifier in the path. It can
be obtained from GET /api/hosting/v1/wordpress/installations (the `id` field).

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.word_press_v1_login_login_links_resource import WordPressV1LoginLoginLinksResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.WordPressLoginApi(api_client)
    username = 'u123456789' # str | 
    software = '1232456789' # str | WordPress installation (software) identifier

    try:
        # Create login links
        api_response = api_instance.create_login_links_v1(username, software)
        print("The response of WordPressLoginApi->create_login_links_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WordPressLoginApi->create_login_links_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **software** | **str**| WordPress installation (software) identifier | 

### Return type

[**WordPressV1LoginLoginLinksResource**](WordPressV1LoginLoginLinksResource.md)

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

