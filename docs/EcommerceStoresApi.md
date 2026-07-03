# hostinger_api.EcommerceStoresApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_store_v1**](EcommerceStoresApi.md#create_store_v1) | **POST** /api/ecommerce/v1/stores | Create store
[**delete_store_v1**](EcommerceStoresApi.md#delete_store_v1) | **DELETE** /api/ecommerce/v1/stores/{store_id} | Delete store
[**get_store_metadata_v1**](EcommerceStoresApi.md#get_store_metadata_v1) | **GET** /api/ecommerce/v1/stores/{store_id}/metadata | Get store metadata
[**get_stores_v1**](EcommerceStoresApi.md#get_stores_v1) | **GET** /api/ecommerce/v1/stores | Get stores


# **create_store_v1**
> EcommerceV1StoreStoreCreationResource create_store_v1(ecommerce_v1_store_store_request)

Create store

Create a new store for your account.

A primary sales channel is created alongside the store.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.ecommerce_v1_store_store_creation_resource import EcommerceV1StoreStoreCreationResource
from hostinger_api.models.ecommerce_v1_store_store_request import EcommerceV1StoreStoreRequest
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.EcommerceStoresApi(api_client)
    ecommerce_v1_store_store_request = hostinger_api.EcommerceV1StoreStoreRequest() # EcommerceV1StoreStoreRequest | 

    try:
        # Create store
        api_response = api_instance.create_store_v1(ecommerce_v1_store_store_request)
        print("The response of EcommerceStoresApi->create_store_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EcommerceStoresApi->create_store_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ecommerce_v1_store_store_request** | [**EcommerceV1StoreStoreRequest**](EcommerceV1StoreStoreRequest.md)|  | 

### Return type

[**EcommerceV1StoreStoreCreationResource**](EcommerceV1StoreStoreCreationResource.md)

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

# **delete_store_v1**
> EcommerceV1StoreStoreDeleteResource delete_store_v1(store_id)

Delete store

Soft-delete a store owned by your account.

The underlying store data is preserved; only the store is marked as deleted.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.ecommerce_v1_store_store_delete_resource import EcommerceV1StoreStoreDeleteResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.EcommerceStoresApi(api_client)
    store_id = 'store_01J8Z5F8W9K8M4A7B3C2D1E0FG' # str | The ID of the store to delete.

    try:
        # Delete store
        api_response = api_instance.delete_store_v1(store_id)
        print("The response of EcommerceStoresApi->delete_store_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EcommerceStoresApi->delete_store_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The ID of the store to delete. | 

### Return type

[**EcommerceV1StoreStoreDeleteResource**](EcommerceV1StoreStoreDeleteResource.md)

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

# **get_store_metadata_v1**
> EcommerceV1StoreStoreMetadataResource get_store_metadata_v1(store_id)

Get store metadata

Get a store's readiness metadata: whether payment methods and shipping are configured,
plus its default currency. Useful to verify prerequisites before building a storefront.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.ecommerce_v1_store_store_metadata_resource import EcommerceV1StoreStoreMetadataResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.EcommerceStoresApi(api_client)
    store_id = 'store_01J8Z5F8W9K8M4A7B3C2D1E0FG' # str | The ID of the store to read metadata for.

    try:
        # Get store metadata
        api_response = api_instance.get_store_metadata_v1(store_id)
        print("The response of EcommerceStoresApi->get_store_metadata_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EcommerceStoresApi->get_store_metadata_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The ID of the store to read metadata for. | 

### Return type

[**EcommerceV1StoreStoreMetadataResource**](EcommerceV1StoreStoreMetadataResource.md)

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

# **get_stores_v1**
> EcommerceGetStoresV1200Response get_stores_v1(page=page)

Get stores

Retrieve the stores associated with your account.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.ecommerce_get_stores_v1200_response import EcommerceGetStoresV1200Response
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.EcommerceStoresApi(api_client)
    page = 1 # int | Page number (optional)

    try:
        # Get stores
        api_response = api_instance.get_stores_v1(page=page)
        print("The response of EcommerceStoresApi->get_stores_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EcommerceStoresApi->get_stores_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number | [optional] 

### Return type

[**EcommerceGetStoresV1200Response**](EcommerceGetStoresV1200Response.md)

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

