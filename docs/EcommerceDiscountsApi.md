# hostinger_api.EcommerceDiscountsApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_a_discount_v1**](EcommerceDiscountsApi.md#create_a_discount_v1) | **POST** /api/ecommerce/v1/stores/{store_id}/discounts | Create a discount
[**list_discounts_v1**](EcommerceDiscountsApi.md#list_discounts_v1) | **GET** /api/ecommerce/v1/stores/{store_id}/discounts | List discounts


# **create_a_discount_v1**
> EcommerceV1DiscountDiscountResponseResource create_a_discount_v1(store_id, ecommerce_v1_discount_create_discount_request)

Create a discount

Create a discount for a store. Fixed discounts take an amount in the smallest currency
unit (e.g. $10 is 1000); percentage discounts take a whole-number value between 1 and 100.
Free-shipping discounts ignore value. Returns the created discount.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.ecommerce_v1_discount_create_discount_request import EcommerceV1DiscountCreateDiscountRequest
from hostinger_api.models.ecommerce_v1_discount_discount_response_resource import EcommerceV1DiscountDiscountResponseResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.EcommerceDiscountsApi(api_client)
    store_id = 'store_01J8Z5F8W9K8M4A7B3C2D1E0FG' # str | The ID of the store to create the discount for.
    ecommerce_v1_discount_create_discount_request = hostinger_api.EcommerceV1DiscountCreateDiscountRequest() # EcommerceV1DiscountCreateDiscountRequest | 

    try:
        # Create a discount
        api_response = api_instance.create_a_discount_v1(store_id, ecommerce_v1_discount_create_discount_request)
        print("The response of EcommerceDiscountsApi->create_a_discount_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EcommerceDiscountsApi->create_a_discount_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The ID of the store to create the discount for. | 
 **ecommerce_v1_discount_create_discount_request** | [**EcommerceV1DiscountCreateDiscountRequest**](EcommerceV1DiscountCreateDiscountRequest.md)|  | 

### Return type

[**EcommerceV1DiscountDiscountResponseResource**](EcommerceV1DiscountDiscountResponseResource.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created response |  -  |
**422** | Validation error response |  -  |
**401** | Unauthenticated response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_discounts_v1**
> EcommerceListDiscountsV1200Response list_discounts_v1(store_id, q=q, is_disabled=is_disabled, page=page)

List discounts

List a store's discounts. Filter by free text over code and name, or by disabled state.
Amounts for fixed discounts are integers in the smallest currency unit; percentage
discounts carry a whole-number value between 1 and 100.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.ecommerce_list_discounts_v1200_response import EcommerceListDiscountsV1200Response
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.EcommerceDiscountsApi(api_client)
    store_id = 'store_01J8Z5F8W9K8M4A7B3C2D1E0FG' # str | The ID of the store to list discounts for.
    q = 'blackfriday' # str | Free-text search over discount code and name. (optional)
    is_disabled = 'is_disabled_example' # str | Filter by disabled state. (optional)
    page = 1 # int | Page number (optional)

    try:
        # List discounts
        api_response = api_instance.list_discounts_v1(store_id, q=q, is_disabled=is_disabled, page=page)
        print("The response of EcommerceDiscountsApi->list_discounts_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EcommerceDiscountsApi->list_discounts_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The ID of the store to list discounts for. | 
 **q** | **str**| Free-text search over discount code and name. | [optional] 
 **is_disabled** | **str**| Filter by disabled state. | [optional] 
 **page** | **int**| Page number | [optional] 

### Return type

[**EcommerceListDiscountsV1200Response**](EcommerceListDiscountsV1200Response.md)

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

