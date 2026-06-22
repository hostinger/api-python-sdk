# hostinger_api.HostingOrdersApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_orders_v1**](HostingOrdersApi.md#list_orders_v1) | **GET** /api/hosting/v1/orders | List orders


# **list_orders_v1**
> HostingListOrdersV1200Response list_orders_v1(page=page, per_page=per_page, statuses=statuses, order_ids=order_ids)

List orders

Retrieve a paginated list of orders accessible to the authenticated client.

This endpoint returns orders of your hosting accounts as well as orders
of other client hosting accounts that have shared access with you.

Use the available query parameters to filter results by order statuses
or specific order IDs for more targeted results.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.hosting_list_orders_v1200_response import HostingListOrdersV1200Response
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.HostingOrdersApi(api_client)
    page = 1 # int | Page number (optional)
    per_page = 25 # int | Number of items per page (optional) (default to 25)
    statuses = ['[\"active\",\"suspended\"]'] # List[str] | Filter by order statuses (optional)
    order_ids = [[12345,67890]] # List[int] | Filter by specific order IDs (optional)

    try:
        # List orders
        api_response = api_instance.list_orders_v1(page=page, per_page=per_page, statuses=statuses, order_ids=order_ids)
        print("The response of HostingOrdersApi->list_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingOrdersApi->list_orders_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number | [optional] 
 **per_page** | **int**| Number of items per page | [optional] [default to 25]
 **statuses** | [**List[str]**](str.md)| Filter by order statuses | [optional] 
 **order_ids** | [**List[int]**](int.md)| Filter by specific order IDs | [optional] 

### Return type

[**HostingListOrdersV1200Response**](HostingListOrdersV1200Response.md)

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

