# hostinger_api.EcommerceShippingApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**set_store_shipping_v1**](EcommerceShippingApi.md#set_store_shipping_v1) | **POST** /api/ecommerce/v1/stores/{store_id}/shipping | Set store shipping


# **set_store_shipping_v1**
> EcommerceV1ShippingShippingResource set_store_shipping_v1(store_id, ecommerce_v1_shipping_set_shipping_request)

Set store shipping

Set the flat-rate shipping price for a store, creating the shipping zone if it does not exist yet.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.ecommerce_v1_shipping_set_shipping_request import EcommerceV1ShippingSetShippingRequest
from hostinger_api.models.ecommerce_v1_shipping_shipping_resource import EcommerceV1ShippingShippingResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.EcommerceShippingApi(api_client)
    store_id = 'store_01J8Z5F8W9K8M4A7B3C2D1E0FG' # str | The ID of the store to configure shipping for.
    ecommerce_v1_shipping_set_shipping_request = hostinger_api.EcommerceV1ShippingSetShippingRequest() # EcommerceV1ShippingSetShippingRequest | 

    try:
        # Set store shipping
        api_response = api_instance.set_store_shipping_v1(store_id, ecommerce_v1_shipping_set_shipping_request)
        print("The response of EcommerceShippingApi->set_store_shipping_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EcommerceShippingApi->set_store_shipping_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The ID of the store to configure shipping for. | 
 **ecommerce_v1_shipping_set_shipping_request** | [**EcommerceV1ShippingSetShippingRequest**](EcommerceV1ShippingSetShippingRequest.md)|  | 

### Return type

[**EcommerceV1ShippingShippingResource**](EcommerceV1ShippingShippingResource.md)

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

