# hostinger_api.HostingRedirectsApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_website_redirect_v1**](HostingRedirectsApi.md#create_website_redirect_v1) | **POST** /api/hosting/v1/accounts/{username}/websites/{domain}/redirects | Create website redirect
[**delete_website_redirect_v1**](HostingRedirectsApi.md#delete_website_redirect_v1) | **DELETE** /api/hosting/v1/accounts/{username}/websites/{domain}/redirects | Delete website redirect
[**list_website_redirects_v1**](HostingRedirectsApi.md#list_website_redirects_v1) | **GET** /api/hosting/v1/accounts/{username}/websites/{domain}/redirects | List website redirects


# **create_website_redirect_v1**
> HostingV1RedirectsRedirectResource create_website_redirect_v1(username, domain, hosting_v1_redirects_create_redirect_request)

Create website redirect

Creates a redirect from a URL on the selected website to another URL or IP address.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.hosting_v1_redirects_create_redirect_request import HostingV1RedirectsCreateRedirectRequest
from hostinger_api.models.hosting_v1_redirects_redirect_resource import HostingV1RedirectsRedirectResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.HostingRedirectsApi(api_client)
    username = 'u123456789' # str | 
    domain = 'mydomain.tld' # str | Domain name
    hosting_v1_redirects_create_redirect_request = hostinger_api.HostingV1RedirectsCreateRedirectRequest() # HostingV1RedirectsCreateRedirectRequest | 

    try:
        # Create website redirect
        api_response = api_instance.create_website_redirect_v1(username, domain, hosting_v1_redirects_create_redirect_request)
        print("The response of HostingRedirectsApi->create_website_redirect_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingRedirectsApi->create_website_redirect_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **domain** | **str**| Domain name | 
 **hosting_v1_redirects_create_redirect_request** | [**HostingV1RedirectsCreateRedirectRequest**](HostingV1RedirectsCreateRedirectRequest.md)|  | 

### Return type

[**HostingV1RedirectsRedirectResource**](HostingV1RedirectsRedirectResource.md)

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

# **delete_website_redirect_v1**
> CommonSuccessEmptyResource delete_website_redirect_v1(username, domain, var_from)

Delete website redirect

Permanently deletes the redirect identified by its source URL.

Pass the `from` value exactly as returned by the list redirects endpoint.

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
    api_instance = hostinger_api.HostingRedirectsApi(api_client)
    username = 'u123456789' # str | 
    domain = 'mydomain.tld' # str | Domain name
    var_from = 'https://example.com/old-page' # str | Source URL returned by the list redirects endpoint.

    try:
        # Delete website redirect
        api_response = api_instance.delete_website_redirect_v1(username, domain, var_from)
        print("The response of HostingRedirectsApi->delete_website_redirect_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingRedirectsApi->delete_website_redirect_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **domain** | **str**| Domain name | 
 **var_from** | **str**| Source URL returned by the list redirects endpoint. | 

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
**422** | Validation error response |  -  |
**401** | Unauthenticated response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_website_redirects_v1**
> HostingListWebsiteRedirectsV1200Response list_website_redirects_v1(username, domain, page=page, per_page=per_page)

List website redirects

Returns a paginated list of redirects configured for the selected website.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.hosting_list_website_redirects_v1200_response import HostingListWebsiteRedirectsV1200Response
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.HostingRedirectsApi(api_client)
    username = 'u123456789' # str | 
    domain = 'mydomain.tld' # str | Domain name
    page = 1 # int | Page number (optional)
    per_page = 25 # int | Number of items per page (optional) (default to 25)

    try:
        # List website redirects
        api_response = api_instance.list_website_redirects_v1(username, domain, page=page, per_page=per_page)
        print("The response of HostingRedirectsApi->list_website_redirects_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingRedirectsApi->list_website_redirects_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **domain** | **str**| Domain name | 
 **page** | **int**| Page number | [optional] 
 **per_page** | **int**| Number of items per page | [optional] [default to 25]

### Return type

[**HostingListWebsiteRedirectsV1200Response**](HostingListWebsiteRedirectsV1200Response.md)

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

