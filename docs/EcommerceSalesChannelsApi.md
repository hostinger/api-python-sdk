# hostinger_api.EcommerceSalesChannelsApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_custom_sales_channel_v1**](EcommerceSalesChannelsApi.md#create_custom_sales_channel_v1) | **POST** /api/ecommerce/v1/stores/{store_id}/sales-channels | Create custom sales channel
[**list_sales_channels_v1**](EcommerceSalesChannelsApi.md#list_sales_channels_v1) | **GET** /api/ecommerce/v1/stores/{store_id}/sales-channels | List sales channels
[**update_sales_channel_v1**](EcommerceSalesChannelsApi.md#update_sales_channel_v1) | **PATCH** /api/ecommerce/v1/stores/{store_id}/sales-channels/{sales_channel_id} | Update sales channel


# **create_custom_sales_channel_v1**
> EcommerceV1SalesChannelSalesChannelCreationResource create_custom_sales_channel_v1(store_id, ecommerce_v1_sales_channel_store_request)

Create custom sales channel

Create a custom sales channel for a store. Build your own frontend and keep your catalog,
orders, shipping and payments in sync through the Ecommerce API.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.ecommerce_v1_sales_channel_sales_channel_creation_resource import EcommerceV1SalesChannelSalesChannelCreationResource
from hostinger_api.models.ecommerce_v1_sales_channel_store_request import EcommerceV1SalesChannelStoreRequest
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.EcommerceSalesChannelsApi(api_client)
    store_id = 'store_01J8Z5F8W9K8M4A7B3C2D1E0FG' # str | The ID of the store to create the sales channel for.
    ecommerce_v1_sales_channel_store_request = hostinger_api.EcommerceV1SalesChannelStoreRequest() # EcommerceV1SalesChannelStoreRequest | 

    try:
        # Create custom sales channel
        api_response = api_instance.create_custom_sales_channel_v1(store_id, ecommerce_v1_sales_channel_store_request)
        print("The response of EcommerceSalesChannelsApi->create_custom_sales_channel_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EcommerceSalesChannelsApi->create_custom_sales_channel_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The ID of the store to create the sales channel for. | 
 **ecommerce_v1_sales_channel_store_request** | [**EcommerceV1SalesChannelStoreRequest**](EcommerceV1SalesChannelStoreRequest.md)|  | 

### Return type

[**EcommerceV1SalesChannelSalesChannelCreationResource**](EcommerceV1SalesChannelSalesChannelCreationResource.md)

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

# **list_sales_channels_v1**
> EcommerceV1SalesChannelSalesChannelListResource list_sales_channels_v1(store_id)

List sales channels

List a store's active sales channels with their full metadata.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.ecommerce_v1_sales_channel_sales_channel_list_resource import EcommerceV1SalesChannelSalesChannelListResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.EcommerceSalesChannelsApi(api_client)
    store_id = 'store_01J8Z5F8W9K8M4A7B3C2D1E0FG' # str | The ID of the store to list sales channels for.

    try:
        # List sales channels
        api_response = api_instance.list_sales_channels_v1(store_id)
        print("The response of EcommerceSalesChannelsApi->list_sales_channels_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EcommerceSalesChannelsApi->list_sales_channels_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The ID of the store to list sales channels for. | 

### Return type

[**EcommerceV1SalesChannelSalesChannelListResource**](EcommerceV1SalesChannelSalesChannelListResource.md)

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

# **update_sales_channel_v1**
> EcommerceV1SalesChannelSalesChannelUpdateResource update_sales_channel_v1(store_id, sales_channel_id, ecommerce_v1_sales_channel_update_request)

Update sales channel

Update a custom sales channel. The merchant-facing `name` and the public `url`
(returned as the channel `domain`) can be changed. Pass `null` to clear a value.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.ecommerce_v1_sales_channel_sales_channel_update_resource import EcommerceV1SalesChannelSalesChannelUpdateResource
from hostinger_api.models.ecommerce_v1_sales_channel_update_request import EcommerceV1SalesChannelUpdateRequest
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.EcommerceSalesChannelsApi(api_client)
    store_id = 'store_01J8Z5F8W9K8M4A7B3C2D1E0FG' # str | The ID of the store that owns the sales channel.
    sales_channel_id = 'scha_01J8Z5F8W9K8M4A7B3C2D1E0FG' # str | The ID of the sales channel to update.
    ecommerce_v1_sales_channel_update_request = hostinger_api.EcommerceV1SalesChannelUpdateRequest() # EcommerceV1SalesChannelUpdateRequest | 

    try:
        # Update sales channel
        api_response = api_instance.update_sales_channel_v1(store_id, sales_channel_id, ecommerce_v1_sales_channel_update_request)
        print("The response of EcommerceSalesChannelsApi->update_sales_channel_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EcommerceSalesChannelsApi->update_sales_channel_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The ID of the store that owns the sales channel. | 
 **sales_channel_id** | **str**| The ID of the sales channel to update. | 
 **ecommerce_v1_sales_channel_update_request** | [**EcommerceV1SalesChannelUpdateRequest**](EcommerceV1SalesChannelUpdateRequest.md)|  | 

### Return type

[**EcommerceV1SalesChannelSalesChannelUpdateResource**](EcommerceV1SalesChannelSalesChannelUpdateResource.md)

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

