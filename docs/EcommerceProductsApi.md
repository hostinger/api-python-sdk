# hostinger_api.EcommerceProductsApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_digital_product_v1**](EcommerceProductsApi.md#create_digital_product_v1) | **POST** /api/ecommerce/v1/stores/{store_id}/products/digital | Create digital product
[**create_physical_product_v1**](EcommerceProductsApi.md#create_physical_product_v1) | **POST** /api/ecommerce/v1/stores/{store_id}/products/physical | Create physical product
[**upload_and_attach_a_product_image_v1**](EcommerceProductsApi.md#upload_and_attach_a_product_image_v1) | **POST** /api/ecommerce/v1/stores/{store_id}/products/{product_id}/images | Upload and attach a product image


# **create_digital_product_v1**
> EcommerceV1ProductProductCreationResource create_digital_product_v1(store_id, ecommerce_v1_product_create_digital_product_request)

Create digital product

Create a published digital product with a single variant and an optional external download link.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.ecommerce_v1_product_create_digital_product_request import EcommerceV1ProductCreateDigitalProductRequest
from hostinger_api.models.ecommerce_v1_product_product_creation_resource import EcommerceV1ProductProductCreationResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.EcommerceProductsApi(api_client)
    store_id = 'store_01J8Z5F8W9K8M4A7B3C2D1E0FG' # str | The ID of the store to create the product in.
    ecommerce_v1_product_create_digital_product_request = hostinger_api.EcommerceV1ProductCreateDigitalProductRequest() # EcommerceV1ProductCreateDigitalProductRequest | 

    try:
        # Create digital product
        api_response = api_instance.create_digital_product_v1(store_id, ecommerce_v1_product_create_digital_product_request)
        print("The response of EcommerceProductsApi->create_digital_product_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EcommerceProductsApi->create_digital_product_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The ID of the store to create the product in. | 
 **ecommerce_v1_product_create_digital_product_request** | [**EcommerceV1ProductCreateDigitalProductRequest**](EcommerceV1ProductCreateDigitalProductRequest.md)|  | 

### Return type

[**EcommerceV1ProductProductCreationResource**](EcommerceV1ProductProductCreationResource.md)

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

# **create_physical_product_v1**
> EcommerceV1ProductProductCreationResource create_physical_product_v1(store_id, ecommerce_v1_product_create_physical_product_request)

Create physical product

Create a published physical product with a single variant priced in the store currency.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.ecommerce_v1_product_create_physical_product_request import EcommerceV1ProductCreatePhysicalProductRequest
from hostinger_api.models.ecommerce_v1_product_product_creation_resource import EcommerceV1ProductProductCreationResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.EcommerceProductsApi(api_client)
    store_id = 'store_01J8Z5F8W9K8M4A7B3C2D1E0FG' # str | The ID of the store to create the product in.
    ecommerce_v1_product_create_physical_product_request = hostinger_api.EcommerceV1ProductCreatePhysicalProductRequest() # EcommerceV1ProductCreatePhysicalProductRequest | 

    try:
        # Create physical product
        api_response = api_instance.create_physical_product_v1(store_id, ecommerce_v1_product_create_physical_product_request)
        print("The response of EcommerceProductsApi->create_physical_product_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EcommerceProductsApi->create_physical_product_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The ID of the store to create the product in. | 
 **ecommerce_v1_product_create_physical_product_request** | [**EcommerceV1ProductCreatePhysicalProductRequest**](EcommerceV1ProductCreatePhysicalProductRequest.md)|  | 

### Return type

[**EcommerceV1ProductProductCreationResource**](EcommerceV1ProductProductCreationResource.md)

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

# **upload_and_attach_a_product_image_v1**
> EcommerceV1ProductProductImageUploadResource upload_and_attach_a_product_image_v1(store_id, product_id, ecommerce_v1_product_upload_product_image_request)

Upload and attach a product image

Upload a raster image (JPEG, PNG, GIF or WebP, max 15MB) and attach it to a product in a single call.
The image is virus-scanned and validated by content, then stored on the CDN. Set is_thumbnail to make
it the product's primary image.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.ecommerce_v1_product_product_image_upload_resource import EcommerceV1ProductProductImageUploadResource
from hostinger_api.models.ecommerce_v1_product_upload_product_image_request import EcommerceV1ProductUploadProductImageRequest
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.EcommerceProductsApi(api_client)
    store_id = 'store_01J8Z5F8W9K8M4A7B3C2D1E0FG' # str | The ID of the store the product belongs to.
    product_id = 'prod_01J8Z5F8W9K8M4A7B3C2D1E0FG' # str | The ID of the product to attach the image to.
    ecommerce_v1_product_upload_product_image_request = hostinger_api.EcommerceV1ProductUploadProductImageRequest() # EcommerceV1ProductUploadProductImageRequest | 

    try:
        # Upload and attach a product image
        api_response = api_instance.upload_and_attach_a_product_image_v1(store_id, product_id, ecommerce_v1_product_upload_product_image_request)
        print("The response of EcommerceProductsApi->upload_and_attach_a_product_image_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EcommerceProductsApi->upload_and_attach_a_product_image_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The ID of the store the product belongs to. | 
 **product_id** | **str**| The ID of the product to attach the image to. | 
 **ecommerce_v1_product_upload_product_image_request** | [**EcommerceV1ProductUploadProductImageRequest**](EcommerceV1ProductUploadProductImageRequest.md)|  | 

### Return type

[**EcommerceV1ProductProductImageUploadResource**](EcommerceV1ProductProductImageUploadResource.md)

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

