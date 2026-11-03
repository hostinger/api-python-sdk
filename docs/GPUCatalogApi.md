# hostinger_api.GPUCatalogApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_pool_groups_v1**](GPUCatalogApi.md#get_pool_groups_v1) | **GET** /api/gpu/v1/pools/groups | Get pool groups
[**get_pool_instance_types_v1**](GPUCatalogApi.md#get_pool_instance_types_v1) | **GET** /api/gpu/v1/pools/{poolId}/instances | Get pool instance types
[**get_pool_list_v1**](GPUCatalogApi.md#get_pool_list_v1) | **GET** /api/gpu/v1/pools | Get pool list
[**get_pool_os_templates_v1**](GPUCatalogApi.md#get_pool_os_templates_v1) | **GET** /api/gpu/v1/pools/{poolId}/instances/{poolInstanceId}/os-templates | Get pool OS templates


# **get_pool_groups_v1**
> List[GPUV1PoolPoolGroupResource] get_pool_groups_v1(currency=currency)

Get pool groups

Retrieve GPU pool groups, ordered by name.

Each group bundles the pools of one GPU model and lists its currently available pools,
whether any of them is available and the lowest hourly price among its instance types.
The price is returned even when the group is out of stock.

Use this endpoint to show which GPU models can be ordered and from what price.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.gpuv1_pool_pool_group_resource import GPUV1PoolPoolGroupResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.GPUCatalogApi(api_client)
    currency = 'EUR' # str | Currency of the returned prices, `USD` by default (optional)

    try:
        # Get pool groups
        api_response = api_instance.get_pool_groups_v1(currency=currency)
        print("The response of GPUCatalogApi->get_pool_groups_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GPUCatalogApi->get_pool_groups_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| Currency of the returned prices, &#x60;USD&#x60; by default | [optional] 

### Return type

[**List[GPUV1PoolPoolGroupResource]**](GPUV1PoolPoolGroupResource.md)

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

# **get_pool_instance_types_v1**
> List[GPUV1PoolPoolInstanceResource] get_pool_instance_types_v1(pool_id)

Get pool instance types

Retrieve the instance types offered by a specified GPU pool, ordered by CPU core count.

Each instance type describes its CPU, memory and storage, and its hourly price.
Only instance types that can currently be ordered are returned.

Use this endpoint to choose the `pool_instance_id` for a new GPU instance.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.gpuv1_pool_pool_instance_resource import GPUV1PoolPoolInstanceResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.GPUCatalogApi(api_client)
    pool_id = 12 # int | GPU pool ID

    try:
        # Get pool instance types
        api_response = api_instance.get_pool_instance_types_v1(pool_id)
        print("The response of GPUCatalogApi->get_pool_instance_types_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GPUCatalogApi->get_pool_instance_types_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_id** | **int**| GPU pool ID | 

### Return type

[**List[GPUV1PoolPoolInstanceResource]**](GPUV1PoolPoolInstanceResource.md)

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

# **get_pool_list_v1**
> List[GPUV1PoolPoolResource] get_pool_list_v1()

Get pool list

Retrieve all available GPU pools, ordered by name.

A pool serves GPU accelerators of one model from a single region.

Use this endpoint to choose a pool before listing its instance types.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.gpuv1_pool_pool_resource import GPUV1PoolPoolResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.GPUCatalogApi(api_client)

    try:
        # Get pool list
        api_response = api_instance.get_pool_list_v1()
        print("The response of GPUCatalogApi->get_pool_list_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GPUCatalogApi->get_pool_list_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[GPUV1PoolPoolResource]**](GPUV1PoolPoolResource.md)

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

# **get_pool_os_templates_v1**
> List[GPUV1OsTemplateOsTemplateResource] get_pool_os_templates_v1(pool_id, pool_instance_id)

Get pool OS templates

Retrieve the OS templates that can be installed on a specified GPU pool instance type.

Use this endpoint to choose the `os_template_id` for a new GPU instance.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.gpuv1_os_template_os_template_resource import GPUV1OsTemplateOsTemplateResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.GPUCatalogApi(api_client)
    pool_id = 12 # int | GPU pool ID
    pool_instance_id = 232 # int | GPU pool instance type ID

    try:
        # Get pool OS templates
        api_response = api_instance.get_pool_os_templates_v1(pool_id, pool_instance_id)
        print("The response of GPUCatalogApi->get_pool_os_templates_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GPUCatalogApi->get_pool_os_templates_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_id** | **int**| GPU pool ID | 
 **pool_instance_id** | **int**| GPU pool instance type ID | 

### Return type

[**List[GPUV1OsTemplateOsTemplateResource]**](GPUV1OsTemplateOsTemplateResource.md)

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

