# hostinger_api.EcommerceProductsApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_a_product_image_upload_urlv1**](EcommerceProductsApi.md#create_a_product_image_upload_urlv1) | **POST** /api/ecommerce/v1/stores/{store_id}/products/{product_id}/images/upload-url | Create a product image upload URL
[**create_digital_product_v1**](EcommerceProductsApi.md#create_digital_product_v1) | **POST** /api/ecommerce/v1/stores/{store_id}/products/digital | Create digital product
[**create_physical_product_v1**](EcommerceProductsApi.md#create_physical_product_v1) | **POST** /api/ecommerce/v1/stores/{store_id}/products/physical | Create physical product
[**delete_a_product_v1**](EcommerceProductsApi.md#delete_a_product_v1) | **DELETE** /api/ecommerce/v1/stores/{store_id}/products/{product_id} | Delete a product
[**list_products_v1**](EcommerceProductsApi.md#list_products_v1) | **GET** /api/ecommerce/v1/stores/{store_id}/products | List products
[**update_a_product_v1**](EcommerceProductsApi.md#update_a_product_v1) | **PATCH** /api/ecommerce/v1/stores/{store_id}/products/{product_id} | Update a product
[**upload_and_attach_a_product_image_v1**](EcommerceProductsApi.md#upload_and_attach_a_product_image_v1) | **POST** /api/ecommerce/v1/stores/{store_id}/products/{product_id}/images | Upload and attach a product image


# **create_a_product_image_upload_urlv1**
> EcommerceV1ProductProductImageUploadUrlResource create_a_product_image_upload_urlv1(store_id, product_id)

Create a product image upload URL

Returns a signed URL to upload a product image to (multipart/form-data POST). Then call the
attach-image endpoint with the returned object_name to scan and attach it to the product.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.ecommerce_v1_product_product_image_upload_url_resource import EcommerceV1ProductProductImageUploadUrlResource
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
    product_id = 'prod_01J8Z5F8W9K8M4A7B3C2D1E0FG' # str | The ID of the product the image will be attached to.

    try:
        # Create a product image upload URL
        api_response = api_instance.create_a_product_image_upload_urlv1(store_id, product_id)
        print("The response of EcommerceProductsApi->create_a_product_image_upload_urlv1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EcommerceProductsApi->create_a_product_image_upload_urlv1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The ID of the store the product belongs to. | 
 **product_id** | **str**| The ID of the product the image will be attached to. | 

### Return type

[**EcommerceV1ProductProductImageUploadUrlResource**](EcommerceV1ProductProductImageUploadUrlResource.md)

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

# **delete_a_product_v1**
> EcommerceV1ProductProductDeletedResource delete_a_product_v1(store_id, product_id)

Delete a product

Delete a product and its variants from the store. A subscription product with active
subscribers is archived instead of deleted so its data stays available.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.ecommerce_v1_product_product_deleted_resource import EcommerceV1ProductProductDeletedResource
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
    store_id = 'store_01J8Z5F8W9K8M4A7B3C2D1E0FG' # str | The ID of the store that owns the product.
    product_id = 'prod_01J8Z5F8W9K8M4A7B3C2D1E0FG' # str | The ID of the product to delete.

    try:
        # Delete a product
        api_response = api_instance.delete_a_product_v1(store_id, product_id)
        print("The response of EcommerceProductsApi->delete_a_product_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EcommerceProductsApi->delete_a_product_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The ID of the store that owns the product. | 
 **product_id** | **str**| The ID of the product to delete. | 

### Return type

[**EcommerceV1ProductProductDeletedResource**](EcommerceV1ProductProductDeletedResource.md)

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

# **list_products_v1**
> EcommerceListProductsV1200Response list_products_v1(store_id, product_ids=product_ids, status=status, q=q, include=include, page=page)

List products

List a store's products newest first as lean summaries (name, status, thumbnail, variant
count and price range). Prices are integers in the smallest currency unit and live on
variants. Filter by status, free text or a set of product ids. Use include=variants to
embed each product's variants with prices and inventory, and include=media to embed its media.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.ecommerce_list_products_v1200_response import EcommerceListProductsV1200Response
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
    store_id = 'store_01J8Z5F8W9K8M4A7B3C2D1E0FG' # str | The ID of the store to list products for.
    product_ids = ['product_ids_example'] # List[str] | Restrict to these product ids. Doubles as a single-product lookup. Up to 200 ids. (optional)
    status = ['status_example'] # List[str] | Product statuses to include. (optional)
    q = 'blue shirt' # str | Free-text search over product title and SKU. (optional)
    include = ['include_example'] # List[str] | Opt-in heavy data: \"variants\" embeds each product's variants; \"media\" embeds its media. (optional)
    page = 1 # int | Page number (optional)

    try:
        # List products
        api_response = api_instance.list_products_v1(store_id, product_ids=product_ids, status=status, q=q, include=include, page=page)
        print("The response of EcommerceProductsApi->list_products_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EcommerceProductsApi->list_products_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The ID of the store to list products for. | 
 **product_ids** | [**List[str]**](str.md)| Restrict to these product ids. Doubles as a single-product lookup. Up to 200 ids. | [optional] 
 **status** | [**List[str]**](str.md)| Product statuses to include. | [optional] 
 **q** | **str**| Free-text search over product title and SKU. | [optional] 
 **include** | [**List[str]**](str.md)| Opt-in heavy data: \&quot;variants\&quot; embeds each product&#39;s variants; \&quot;media\&quot; embeds its media. | [optional] 
 **page** | **int**| Page number | [optional] 

### Return type

[**EcommerceListProductsV1200Response**](EcommerceListProductsV1200Response.md)

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

# **update_a_product_v1**
> EcommerceV1ProductProductResponseResource update_a_product_v1(store_id, product_id, ecommerce_v1_product_update_request)

Update a product

Update a product's name, description or status. Set status to published to make it buyable,
draft to hide it, or archived to retire it. Variants, prices and inventory are managed
through the variant endpoints, not here. Returns the updated product summary.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.ecommerce_v1_product_product_response_resource import EcommerceV1ProductProductResponseResource
from hostinger_api.models.ecommerce_v1_product_update_request import EcommerceV1ProductUpdateRequest
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
    store_id = 'store_01J8Z5F8W9K8M4A7B3C2D1E0FG' # str | The ID of the store that owns the product.
    product_id = 'prod_01J8Z5F8W9K8M4A7B3C2D1E0FG' # str | The ID of the product to update.
    ecommerce_v1_product_update_request = hostinger_api.EcommerceV1ProductUpdateRequest() # EcommerceV1ProductUpdateRequest | 

    try:
        # Update a product
        api_response = api_instance.update_a_product_v1(store_id, product_id, ecommerce_v1_product_update_request)
        print("The response of EcommerceProductsApi->update_a_product_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EcommerceProductsApi->update_a_product_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The ID of the store that owns the product. | 
 **product_id** | **str**| The ID of the product to update. | 
 **ecommerce_v1_product_update_request** | [**EcommerceV1ProductUpdateRequest**](EcommerceV1ProductUpdateRequest.md)|  | 

### Return type

[**EcommerceV1ProductProductResponseResource**](EcommerceV1ProductProductResponseResource.md)

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

# **upload_and_attach_a_product_image_v1**
> EcommerceV1ProductProductImageUploadResource upload_and_attach_a_product_image_v1(store_id, product_id, ecommerce_v1_product_upload_product_image_request)

Upload and attach a product image

Fetch a raster image (JPEG, PNG, GIF or WebP, max 15MB) from a URL and attach it to a product in a
single call. The image is virus-scanned and validated by content, then stored on the CDN. Set
is_thumbnail to make it the product's primary image.

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

