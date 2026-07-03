# hostinger_api.EcommerceSalesChannelsApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_a_custom_sales_channel_v1**](EcommerceSalesChannelsApi.md#create_a_custom_sales_channel_v1) | **POST** /api/ecommerce/v1/stores/{store_id}/sales-channels | Create a custom sales channel
[**list_sales_channels_v1**](EcommerceSalesChannelsApi.md#list_sales_channels_v1) | **GET** /api/ecommerce/v1/stores/{store_id}/sales-channels | List sales channels


# **create_a_custom_sales_channel_v1**
> EcommerceV1SalesChannelSalesChannelCreationResource create_a_custom_sales_channel_v1(store_id, ecommerce_v1_sales_channel_store_request)

Create a custom sales channel

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
        # Create a custom sales channel
        api_response = api_instance.create_a_custom_sales_channel_v1(store_id, ecommerce_v1_sales_channel_store_request)
        print("The response of EcommerceSalesChannelsApi->create_a_custom_sales_channel_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EcommerceSalesChannelsApi->create_a_custom_sales_channel_v1: %s\n" % e)
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

