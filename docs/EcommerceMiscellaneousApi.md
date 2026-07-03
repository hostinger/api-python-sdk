# hostinger_api.EcommerceMiscellaneousApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_custom_storefront_setup_instructions_v1**](EcommerceMiscellaneousApi.md#get_custom_storefront_setup_instructions_v1) | **GET** /api/ecommerce/v1/miscellaneous/custom-storefront-instructions | Get custom storefront setup instructions


# **get_custom_storefront_setup_instructions_v1**
> EcommerceV1MiscellaneousCustomStorefrontInstructionsResource get_custom_storefront_setup_instructions_v1()

Get custom storefront setup instructions

Retrieve step-by-step setup instructions, formatted as Markdown, for connecting a custom sales
channel to your store and keeping your catalog, orders, shipping and payments in sync through
the Ecommerce API.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.ecommerce_v1_miscellaneous_custom_storefront_instructions_resource import EcommerceV1MiscellaneousCustomStorefrontInstructionsResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.EcommerceMiscellaneousApi(api_client)

    try:
        # Get custom storefront setup instructions
        api_response = api_instance.get_custom_storefront_setup_instructions_v1()
        print("The response of EcommerceMiscellaneousApi->get_custom_storefront_setup_instructions_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EcommerceMiscellaneousApi->get_custom_storefront_setup_instructions_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**EcommerceV1MiscellaneousCustomStorefrontInstructionsResource**](EcommerceV1MiscellaneousCustomStorefrontInstructionsResource.md)

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

