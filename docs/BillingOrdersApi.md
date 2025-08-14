# hostinger_api.BillingOrdersApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_service_order_v1**](BillingOrdersApi.md#create_service_order_v1) | **POST** /api/billing/v1/orders | Create service order


# **create_service_order_v1**
> BillingV1OrderOrderResource create_service_order_v1(billing_v1_order_store_request)

Create service order

Create a new service order. 

**DEPRECATED**

To purchase a domain, use [`POST /api/domains/v1/portfolio`](/#tag/domains-portfolio/POST/api/domains/v1/portfolio) instead.

To purchase a VPS, use [`POST /api/vps/v1/virtual-machines`](/#tag/vps-virtual-machine/POST/api/vps/v1/virtual-machines) instead.


To place order, you need to provide payment method ID and list of price items from the catalog endpoint together with quantity.
Coupons also can be provided during order creation.

Orders created using this endpoint will be set for automatic renewal.

Some `credit_card` payments might need additional verification, rendering purchase unprocessed.
We recommend use other payment methods than `credit_card` if you encounter this issue.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.billing_v1_order_order_resource import BillingV1OrderOrderResource
from hostinger_api.models.billing_v1_order_store_request import BillingV1OrderStoreRequest
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.BillingOrdersApi(api_client)
    billing_v1_order_store_request = hostinger_api.BillingV1OrderStoreRequest() # BillingV1OrderStoreRequest | 

    try:
        # Create service order
        api_response = api_instance.create_service_order_v1(billing_v1_order_store_request)
        print("The response of BillingOrdersApi->create_service_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingOrdersApi->create_service_order_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **billing_v1_order_store_request** | [**BillingV1OrderStoreRequest**](BillingV1OrderStoreRequest.md)|  | 

### Return type

[**BillingV1OrderOrderResource**](BillingV1OrderOrderResource.md)

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

