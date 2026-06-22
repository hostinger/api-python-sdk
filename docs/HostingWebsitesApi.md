# hostinger_api.HostingWebsitesApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_website_v1**](HostingWebsitesApi.md#create_website_v1) | **POST** /api/hosting/v1/websites | Create website
[**list_websites_v1**](HostingWebsitesApi.md#list_websites_v1) | **GET** /api/hosting/v1/websites | List websites


# **create_website_v1**
> CommonSuccessEmptyResource create_website_v1(hosting_v1_websites_create_website_request)

Create website

Create a new website for the authenticated client.

Provide the domain name and associated order ID to create a new website.
The datacenter_code parameter is required when creating the first website
on a new hosting plan - this will set up and configure new hosting account
in the selected datacenter.

Subsequent websites will be hosted on the same datacenter automatically.

Website creation takes up to a few minutes to complete. Check the
websites list endpoint to see when your new website becomes available.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.common_success_empty_resource import CommonSuccessEmptyResource
from hostinger_api.models.hosting_v1_websites_create_website_request import HostingV1WebsitesCreateWebsiteRequest
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.HostingWebsitesApi(api_client)
    hosting_v1_websites_create_website_request = hostinger_api.HostingV1WebsitesCreateWebsiteRequest() # HostingV1WebsitesCreateWebsiteRequest | 

    try:
        # Create website
        api_response = api_instance.create_website_v1(hosting_v1_websites_create_website_request)
        print("The response of HostingWebsitesApi->create_website_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingWebsitesApi->create_website_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hosting_v1_websites_create_website_request** | [**HostingV1WebsitesCreateWebsiteRequest**](HostingV1WebsitesCreateWebsiteRequest.md)|  | 

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

# **list_websites_v1**
> HostingListWebsitesV1200Response list_websites_v1(page=page, per_page=per_page, username=username, order_id=order_id, is_enabled=is_enabled, domain=domain)

List websites

Retrieve a paginated list of websites (main and addon types) accessible to the authenticated client.

This endpoint returns websites from your hosting accounts as well as
websites from other client hosting accounts that have shared access
with you.

Use the available query parameters to filter results by username,
order ID, enabled status, or domain name for more targeted results.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.hosting_list_websites_v1200_response import HostingListWebsitesV1200Response
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.HostingWebsitesApi(api_client)
    page = 1 # int | Page number (optional)
    per_page = 25 # int | Number of items per page (optional) (default to 25)
    username = 'cl_user123' # str | Filter by specific username (optional)
    order_id = 123 # int | Order ID (optional)
    is_enabled = true # bool | Filter by enabled status (optional)
    domain = 'example.com' # str | Filter by domain name (exact match) (optional)

    try:
        # List websites
        api_response = api_instance.list_websites_v1(page=page, per_page=per_page, username=username, order_id=order_id, is_enabled=is_enabled, domain=domain)
        print("The response of HostingWebsitesApi->list_websites_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingWebsitesApi->list_websites_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number | [optional] 
 **per_page** | **int**| Number of items per page | [optional] [default to 25]
 **username** | **str**| Filter by specific username | [optional] 
 **order_id** | **int**| Order ID | [optional] 
 **is_enabled** | **bool**| Filter by enabled status | [optional] 
 **domain** | **str**| Filter by domain name (exact match) | [optional] 

### Return type

[**HostingListWebsitesV1200Response**](HostingListWebsitesV1200Response.md)

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

