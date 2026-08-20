# hostinger_api.EcommerceOrdersApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_an_order_v1**](EcommerceOrdersApi.md#cancel_an_order_v1) | **POST** /api/ecommerce/v1/stores/{store_id}/orders/{order_id}/cancel | Cancel an order
[**fulfil_an_order_v1**](EcommerceOrdersApi.md#fulfil_an_order_v1) | **POST** /api/ecommerce/v1/stores/{store_id}/orders/{order_id}/fulfill | Fulfil an order
[**list_orders_v1**](EcommerceOrdersApi.md#list_orders_v1) | **GET** /api/ecommerce/v1/stores/{store_id}/orders | List orders
[**retrieve_an_order_v1**](EcommerceOrdersApi.md#retrieve_an_order_v1) | **GET** /api/ecommerce/v1/stores/{store_id}/orders/{order_id} | Retrieve an order


# **cancel_an_order_v1**
> EcommerceV1OrderOrderResponseResource cancel_an_order_v1(store_id, order_id, ecommerce_v1_order_cancel_request)

Cancel an order

Cancel the order and optionally email the customer. Returns the updated order summary.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.ecommerce_v1_order_cancel_request import EcommerceV1OrderCancelRequest
from hostinger_api.models.ecommerce_v1_order_order_response_resource import EcommerceV1OrderOrderResponseResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.EcommerceOrdersApi(api_client)
    store_id = 'store_01J8Z5F8W9K8M4A7B3C2D1E0FG' # str | The ID of the store that owns the order.
    order_id = 'order_01J8Z5F8W9K8M4A7B3C2D1E0FG' # str | The ID of the order to cancel.
    ecommerce_v1_order_cancel_request = hostinger_api.EcommerceV1OrderCancelRequest() # EcommerceV1OrderCancelRequest | 

    try:
        # Cancel an order
        api_response = api_instance.cancel_an_order_v1(store_id, order_id, ecommerce_v1_order_cancel_request)
        print("The response of EcommerceOrdersApi->cancel_an_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EcommerceOrdersApi->cancel_an_order_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The ID of the store that owns the order. | 
 **order_id** | **str**| The ID of the order to cancel. | 
 **ecommerce_v1_order_cancel_request** | [**EcommerceV1OrderCancelRequest**](EcommerceV1OrderCancelRequest.md)|  | 

### Return type

[**EcommerceV1OrderOrderResponseResource**](EcommerceV1OrderOrderResponseResource.md)

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

# **fulfil_an_order_v1**
> EcommerceV1OrderOrderResponseResource fulfil_an_order_v1(store_id, order_id, ecommerce_v1_order_fulfill_request)

Fulfil an order

Create a fulfilment for the order and attach tracking in one call. Omit items to fulfil
every remaining unfulfilled item. Returns the updated order summary.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.ecommerce_v1_order_fulfill_request import EcommerceV1OrderFulfillRequest
from hostinger_api.models.ecommerce_v1_order_order_response_resource import EcommerceV1OrderOrderResponseResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.EcommerceOrdersApi(api_client)
    store_id = 'store_01J8Z5F8W9K8M4A7B3C2D1E0FG' # str | The ID of the store that owns the order.
    order_id = 'order_01J8Z5F8W9K8M4A7B3C2D1E0FG' # str | The ID of the order to fulfil.
    ecommerce_v1_order_fulfill_request = hostinger_api.EcommerceV1OrderFulfillRequest() # EcommerceV1OrderFulfillRequest | 

    try:
        # Fulfil an order
        api_response = api_instance.fulfil_an_order_v1(store_id, order_id, ecommerce_v1_order_fulfill_request)
        print("The response of EcommerceOrdersApi->fulfil_an_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EcommerceOrdersApi->fulfil_an_order_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The ID of the store that owns the order. | 
 **order_id** | **str**| The ID of the order to fulfil. | 
 **ecommerce_v1_order_fulfill_request** | [**EcommerceV1OrderFulfillRequest**](EcommerceV1OrderFulfillRequest.md)|  | 

### Return type

[**EcommerceV1OrderOrderResponseResource**](EcommerceV1OrderOrderResponseResource.md)

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

# **list_orders_v1**
> EcommerceListOrdersV1200Response list_orders_v1(store_id, status=status, payment_status=payment_status, fulfillment_status=fulfillment_status, email=email, display_id=display_id, q=q, created_at_from=created_at_from, created_at_to=created_at_to, page=page)

List orders

List a store's orders newest first as summaries. Filter by status, payment or fulfilment
status, customer email, order number or a free-text query. Amounts are in the smallest
currency unit. Retrieve a single order for its line items, addresses and fulfilments.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.ecommerce_list_orders_v1200_response import EcommerceListOrdersV1200Response
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.EcommerceOrdersApi(api_client)
    store_id = 'store_01J8Z5F8W9K8M4A7B3C2D1E0FG' # str | The ID of the store to list orders for.
    status = ['status_example'] # List[str] | Order statuses to include. (optional)
    payment_status = ['payment_status_example'] # List[str] | Payment statuses to include. A paid order is \"captured\". (optional)
    fulfillment_status = ['fulfillment_status_example'] # List[str] | Fulfilment statuses to include. (optional)
    email = 'buyer@example.com' # str | Customer email, matched exactly. (optional)
    display_id = '1042' # str | The order number the merchant and customer see. (optional)
    q = 'blue shirt' # str | Free-text search over customer name, email, order number and line items. (optional)
    created_at_from = '2026-01-01' # str | Earliest creation time to include, inclusive. Accepts a date or ISO date-time (UTC). (optional)
    created_at_to = '2026-01-31' # str | Latest creation time to include, inclusive. A bare date covers that whole day. (optional)
    page = 1 # int | Page number (optional)

    try:
        # List orders
        api_response = api_instance.list_orders_v1(store_id, status=status, payment_status=payment_status, fulfillment_status=fulfillment_status, email=email, display_id=display_id, q=q, created_at_from=created_at_from, created_at_to=created_at_to, page=page)
        print("The response of EcommerceOrdersApi->list_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EcommerceOrdersApi->list_orders_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The ID of the store to list orders for. | 
 **status** | [**List[str]**](str.md)| Order statuses to include. | [optional] 
 **payment_status** | [**List[str]**](str.md)| Payment statuses to include. A paid order is \&quot;captured\&quot;. | [optional] 
 **fulfillment_status** | [**List[str]**](str.md)| Fulfilment statuses to include. | [optional] 
 **email** | **str**| Customer email, matched exactly. | [optional] 
 **display_id** | **str**| The order number the merchant and customer see. | [optional] 
 **q** | **str**| Free-text search over customer name, email, order number and line items. | [optional] 
 **created_at_from** | **str**| Earliest creation time to include, inclusive. Accepts a date or ISO date-time (UTC). | [optional] 
 **created_at_to** | **str**| Latest creation time to include, inclusive. A bare date covers that whole day. | [optional] 
 **page** | **int**| Page number | [optional] 

### Return type

[**EcommerceListOrdersV1200Response**](EcommerceListOrdersV1200Response.md)

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

# **retrieve_an_order_v1**
> EcommerceV1OrderOrderDetailResponseResource retrieve_an_order_v1(store_id, order_id)

Retrieve an order

Retrieve one order in full: line items (each with the id the fulfil endpoint needs),
addresses, the totals breakdown and fulfilments with tracking. Amounts are in the
smallest currency unit.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.ecommerce_v1_order_order_detail_response_resource import EcommerceV1OrderOrderDetailResponseResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.EcommerceOrdersApi(api_client)
    store_id = 'store_01J8Z5F8W9K8M4A7B3C2D1E0FG' # str | The ID of the store that owns the order.
    order_id = 'order_01J8Z5F8W9K8M4A7B3C2D1E0FG' # str | The ID of the order to retrieve.

    try:
        # Retrieve an order
        api_response = api_instance.retrieve_an_order_v1(store_id, order_id)
        print("The response of EcommerceOrdersApi->retrieve_an_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EcommerceOrdersApi->retrieve_an_order_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The ID of the store that owns the order. | 
 **order_id** | **str**| The ID of the order to retrieve. | 

### Return type

[**EcommerceV1OrderOrderDetailResponseResource**](EcommerceV1OrderOrderDetailResponseResource.md)

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

