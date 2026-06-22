# hostinger_api.HostingWordpressApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**install_word_press_v1**](HostingWordpressApi.md#install_word_press_v1) | **POST** /api/hosting/v1/accounts/{username}/wordpress/installations | Install WordPress
[**list_word_press_installations_v1**](HostingWordpressApi.md#list_word_press_installations_v1) | **GET** /api/hosting/v1/wordpress/installations | List WordPress installations


# **install_word_press_v1**
> CommonSuccessEmptyResource install_word_press_v1(username, hosting_v1_wordpress_install_wordpress_request)

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
from hostinger_api.models.hosting_v1_wordpress_install_wordpress_request import HostingV1WordpressInstallWordpressRequest
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.HostingWordpressApi(api_client)
    username = 'u123456789' # str | 
    hosting_v1_wordpress_install_wordpress_request = hostinger_api.HostingV1WordpressInstallWordpressRequest() # HostingV1WordpressInstallWordpressRequest | 

    try:
        # Install WordPress
        api_response = api_instance.install_word_press_v1(username, hosting_v1_wordpress_install_wordpress_request)
        print("The response of HostingWordpressApi->install_word_press_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingWordpressApi->install_word_press_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **hosting_v1_wordpress_install_wordpress_request** | [**HostingV1WordpressInstallWordpressRequest**](HostingV1WordpressInstallWordpressRequest.md)|  | 

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

# **list_word_press_installations_v1**
> List[HostingV1WordpressWordpressInstallationResource] list_word_press_installations_v1(username=username, domain=domain, ownership=ownership)

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
from hostinger_api.models.hosting_v1_wordpress_wordpress_installation_resource import HostingV1WordpressWordpressInstallationResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.HostingWordpressApi(api_client)
    username = 'cl_user123' # str | Filter by specific username (optional)
    domain = 'example.com' # str | Filter by domain name (exact match) (optional)
    ownership = 'owned' # str | Filter by ownership type. Defaults to \"owned\". Use \"all\" to include both owned and managed installations. (optional)

    try:
        # List WordPress installations
        api_response = api_instance.list_word_press_installations_v1(username=username, domain=domain, ownership=ownership)
        print("The response of HostingWordpressApi->list_word_press_installations_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingWordpressApi->list_word_press_installations_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Filter by specific username | [optional] 
 **domain** | **str**| Filter by domain name (exact match) | [optional] 
 **ownership** | **str**| Filter by ownership type. Defaults to \&quot;owned\&quot;. Use \&quot;all\&quot; to include both owned and managed installations. | [optional] 

### Return type

[**List[HostingV1WordpressWordpressInstallationResource]**](HostingV1WordpressWordpressInstallationResource.md)

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

