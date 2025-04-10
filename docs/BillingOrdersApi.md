# @hostinger/api.BillingOrdersApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_new_service_order_v1**](BillingOrdersApi.md#create_new_service_order_v1) | **POST** /api/billing/v1/orders | Create new service order


# **create_new_service_order_v1**
> BillingV1OrderOrderResource create_new_service_order_v1(billing_v1_order_store_request)

Create new service order

This endpoint creates a new service order. 

To place order, you need to provide payment method ID and list of price items from the catalog endpoint together with quantity.
Coupons also can be provided during order creation.

Orders created using this endpoint will be set for automatically renewal.

### Example

* Bearer Authentication (apiToken):

```python
import @hostinger/api
from @hostinger/api.models.billing_v1_order_order_resource import BillingV1OrderOrderResource
from @hostinger/api.models.billing_v1_order_store_request import BillingV1OrderStoreRequest
from @hostinger/api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = @hostinger/api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with @hostinger/api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = @hostinger/api.BillingOrdersApi(api_client)
    billing_v1_order_store_request = @hostinger/api.BillingV1OrderStoreRequest() # BillingV1OrderStoreRequest | 

    try:
        # Create new service order
        api_response = api_instance.create_new_service_order_v1(billing_v1_order_store_request)
        print("The response of BillingOrdersApi->create_new_service_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingOrdersApi->create_new_service_order_v1: %s\n" % e)
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
**401** | Unauthenticated |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

