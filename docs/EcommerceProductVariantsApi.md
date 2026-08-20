# hostinger_api.EcommerceProductVariantsApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_a_product_variant_v1**](EcommerceProductVariantsApi.md#create_a_product_variant_v1) | **POST** /api/ecommerce/v1/stores/{store_id}/products/{product_id}/variants | Create a product variant
[**delete_a_product_variant_v1**](EcommerceProductVariantsApi.md#delete_a_product_variant_v1) | **DELETE** /api/ecommerce/v1/stores/{store_id}/products/{product_id}/variants/{variant_id} | Delete a product variant
[**list_product_variants_v1**](EcommerceProductVariantsApi.md#list_product_variants_v1) | **GET** /api/ecommerce/v1/stores/{store_id}/products/{product_id}/variants | List product variants
[**update_product_variants_in_batch_v1**](EcommerceProductVariantsApi.md#update_product_variants_in_batch_v1) | **PATCH** /api/ecommerce/v1/stores/{store_id}/products/{product_id}/variants/batch | Update product variants in batch


# **create_a_product_variant_v1**
> EcommerceV1VariantVariantResponseResource create_a_product_variant_v1(store_id, product_id, ecommerce_v1_variant_create_variant_request)

Create a product variant

Add a variant to a product along one or more option dimensions (e.g. Size, Color). Options
missing from the product are created automatically; provide a value for every option the
product already has. Prices are integers in the smallest currency unit and default to the
store currency. Returns the created variant.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.ecommerce_v1_variant_create_variant_request import EcommerceV1VariantCreateVariantRequest
from hostinger_api.models.ecommerce_v1_variant_variant_response_resource import EcommerceV1VariantVariantResponseResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.EcommerceProductVariantsApi(api_client)
    store_id = 'store_01J8Z5F8W9K8M4A7B3C2D1E0FG' # str | The ID of the store that owns the product.
    product_id = 'prod_01J8Z5F8W9K8M4A7B3C2D1E0FG' # str | The ID of the product to add the variant to.
    ecommerce_v1_variant_create_variant_request = hostinger_api.EcommerceV1VariantCreateVariantRequest() # EcommerceV1VariantCreateVariantRequest | 

    try:
        # Create a product variant
        api_response = api_instance.create_a_product_variant_v1(store_id, product_id, ecommerce_v1_variant_create_variant_request)
        print("The response of EcommerceProductVariantsApi->create_a_product_variant_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EcommerceProductVariantsApi->create_a_product_variant_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The ID of the store that owns the product. | 
 **product_id** | **str**| The ID of the product to add the variant to. | 
 **ecommerce_v1_variant_create_variant_request** | [**EcommerceV1VariantCreateVariantRequest**](EcommerceV1VariantCreateVariantRequest.md)|  | 

### Return type

[**EcommerceV1VariantVariantResponseResource**](EcommerceV1VariantVariantResponseResource.md)

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

# **delete_a_product_variant_v1**
> EcommerceV1VariantVariantDeletedResource delete_a_product_variant_v1(store_id, product_id, variant_id)

Delete a product variant

Delete a single variant from the product.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.ecommerce_v1_variant_variant_deleted_resource import EcommerceV1VariantVariantDeletedResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.EcommerceProductVariantsApi(api_client)
    store_id = 'store_01J8Z5F8W9K8M4A7B3C2D1E0FG' # str | The ID of the store that owns the product.
    product_id = 'prod_01J8Z5F8W9K8M4A7B3C2D1E0FG' # str | The ID of the product that owns the variant.
    variant_id = 'variant_01J8Z5F8W9K8M4A7B3C2D1E0FG' # str | The ID of the variant to delete.

    try:
        # Delete a product variant
        api_response = api_instance.delete_a_product_variant_v1(store_id, product_id, variant_id)
        print("The response of EcommerceProductVariantsApi->delete_a_product_variant_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EcommerceProductVariantsApi->delete_a_product_variant_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The ID of the store that owns the product. | 
 **product_id** | **str**| The ID of the product that owns the variant. | 
 **variant_id** | **str**| The ID of the variant to delete. | 

### Return type

[**EcommerceV1VariantVariantDeletedResource**](EcommerceV1VariantVariantDeletedResource.md)

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

# **list_product_variants_v1**
> EcommerceListProductVariantsV1200Response list_product_variants_v1(store_id, product_id, page=page)

List product variants

List a product's variants, ordered by rank, with their options, prices and inventory.
Prices are integers in the smallest currency unit and live on variants.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.ecommerce_list_product_variants_v1200_response import EcommerceListProductVariantsV1200Response
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.EcommerceProductVariantsApi(api_client)
    store_id = 'store_01J8Z5F8W9K8M4A7B3C2D1E0FG' # str | The ID of the store that owns the product.
    product_id = 'prod_01J8Z5F8W9K8M4A7B3C2D1E0FG' # str | The ID of the product to list variants for.
    page = 1 # int | Page number (optional)

    try:
        # List product variants
        api_response = api_instance.list_product_variants_v1(store_id, product_id, page=page)
        print("The response of EcommerceProductVariantsApi->list_product_variants_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EcommerceProductVariantsApi->list_product_variants_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The ID of the store that owns the product. | 
 **product_id** | **str**| The ID of the product to list variants for. | 
 **page** | **int**| Page number | [optional] 

### Return type

[**EcommerceListProductVariantsV1200Response**](EcommerceListProductVariantsV1200Response.md)

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

# **update_product_variants_in_batch_v1**
> EcommerceV1VariantVariantListResponseResource update_product_variants_in_batch_v1(store_id, product_id, ecommerce_v1_variant_batch_update_variants_request)

Update product variants in batch

Update up to 100 existing variants in place by id — title, inventory, stock tracking and
prices. Variants omitted from the request are left untouched. Prices replace the variant's
existing prices in full. Returns the updated variants.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.ecommerce_v1_variant_batch_update_variants_request import EcommerceV1VariantBatchUpdateVariantsRequest
from hostinger_api.models.ecommerce_v1_variant_variant_list_response_resource import EcommerceV1VariantVariantListResponseResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.EcommerceProductVariantsApi(api_client)
    store_id = 'store_01J8Z5F8W9K8M4A7B3C2D1E0FG' # str | The ID of the store that owns the product.
    product_id = 'prod_01J8Z5F8W9K8M4A7B3C2D1E0FG' # str | The ID of the product whose variants are being updated.
    ecommerce_v1_variant_batch_update_variants_request = hostinger_api.EcommerceV1VariantBatchUpdateVariantsRequest() # EcommerceV1VariantBatchUpdateVariantsRequest | 

    try:
        # Update product variants in batch
        api_response = api_instance.update_product_variants_in_batch_v1(store_id, product_id, ecommerce_v1_variant_batch_update_variants_request)
        print("The response of EcommerceProductVariantsApi->update_product_variants_in_batch_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EcommerceProductVariantsApi->update_product_variants_in_batch_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The ID of the store that owns the product. | 
 **product_id** | **str**| The ID of the product whose variants are being updated. | 
 **ecommerce_v1_variant_batch_update_variants_request** | [**EcommerceV1VariantBatchUpdateVariantsRequest**](EcommerceV1VariantBatchUpdateVariantsRequest.md)|  | 

### Return type

[**EcommerceV1VariantVariantListResponseResource**](EcommerceV1VariantVariantListResponseResource.md)

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

