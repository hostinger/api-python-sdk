# hostinger_api.BillingOrdersApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_purchase_order_v1**](BillingOrdersApi.md#create_purchase_order_v1) | **POST** /api/billing/v1/orders | Create purchase order


# **create_purchase_order_v1**
> BillingV1OrderOrderResource create_purchase_order_v1(billing_v1_order_purchase_request)

Create purchase order

Create a purchase order for any Hostinger product.

This unified endpoint places an order for one or more catalog items and
works across all Hostinger products, leveraging the existing billing
infrastructure. Use the [catalog endpoint](#tag/billing-catalog) to look
up the `item_id` values available for purchase.

If no payment method is provided, your default payment method will be used automatically.

This endpoint only places the order. Product-specific provisioning
(e.g. VPS setup or domain registration) is not performed here — once the
order completes, use the relevant product endpoints or
[hPanel](https://hpanel.hostinger.com/) to finalize setup.

Use this endpoint to purchase any product available in the catalog.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.billing_v1_order_order_resource import BillingV1OrderOrderResource
from hostinger_api.models.billing_v1_order_purchase_request import BillingV1OrderPurchaseRequest
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
    billing_v1_order_purchase_request = hostinger_api.BillingV1OrderPurchaseRequest() # BillingV1OrderPurchaseRequest | 

    try:
        # Create purchase order
        api_response = api_instance.create_purchase_order_v1(billing_v1_order_purchase_request)
        print("The response of BillingOrdersApi->create_purchase_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingOrdersApi->create_purchase_order_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **billing_v1_order_purchase_request** | [**BillingV1OrderPurchaseRequest**](BillingV1OrderPurchaseRequest.md)|  | 

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

