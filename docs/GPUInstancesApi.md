# hostinger_api.GPUInstancesApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_instance_v1**](GPUInstancesApi.md#create_instance_v1) | **POST** /api/gpu/v1/instances | Create instance
[**delete_instance_v1**](GPUInstancesApi.md#delete_instance_v1) | **DELETE** /api/gpu/v1/instances/{instanceId} | Delete instance
[**get_instance_details_v1**](GPUInstancesApi.md#get_instance_details_v1) | **GET** /api/gpu/v1/instances/{instanceId} | Get instance details
[**get_instance_metrics_v1**](GPUInstancesApi.md#get_instance_metrics_v1) | **GET** /api/gpu/v1/instances/{instanceId}/metrics | Get instance metrics
[**get_instances_v1**](GPUInstancesApi.md#get_instances_v1) | **GET** /api/gpu/v1/instances | Get instances


# **create_instance_v1**
> CommonSuccessEmptyResource create_instance_v1(gpuv1_instance_store_request)

Create instance

Create a new GPU instance.

Pick `pool_instance_id` from the pool instance types list and `os_template_id` from the OS templates
available for that instance type. Your account must have enough credits to run the instance for its
first hour.

The instance is created asynchronously: a successful request returns immediately, and the instance
appears in the instance list while its `status` moves from `created` through `creating` to `running`.

Use this endpoint to provision GPU compute.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.common_success_empty_resource import CommonSuccessEmptyResource
from hostinger_api.models.gpuv1_instance_store_request import GPUV1InstanceStoreRequest
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.GPUInstancesApi(api_client)
    gpuv1_instance_store_request = hostinger_api.GPUV1InstanceStoreRequest() # GPUV1InstanceStoreRequest | 

    try:
        # Create instance
        api_response = api_instance.create_instance_v1(gpuv1_instance_store_request)
        print("The response of GPUInstancesApi->create_instance_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GPUInstancesApi->create_instance_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gpuv1_instance_store_request** | [**GPUV1InstanceStoreRequest**](GPUV1InstanceStoreRequest.md)|  | 

### Return type

[**CommonSuccessEmptyResource**](CommonSuccessEmptyResource.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success empty response |  -  |
**422** | Validation error response |  -  |
**401** | Unauthenticated response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_instance_v1**
> CommonSuccessEmptyResource delete_instance_v1(instance_id)

Delete instance

Delete a specified GPU instance.

The instance is destroyed asynchronously: a successful request returns immediately and the instance
`status` moves to `destroying`. Deleting fails while the instance is in `created`, `destroying`,
`destroyed` or `abuse` status, or while another action is in progress on it.

Use this endpoint to stop billing for a GPU instance you no longer need.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.common_success_empty_resource import CommonSuccessEmptyResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.GPUInstancesApi(api_client)
    instance_id = 6325 # int | GPU instance ID

    try:
        # Delete instance
        api_response = api_instance.delete_instance_v1(instance_id)
        print("The response of GPUInstancesApi->delete_instance_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GPUInstancesApi->delete_instance_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **int**| GPU instance ID | 

### Return type

[**CommonSuccessEmptyResource**](CommonSuccessEmptyResource.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success empty response |  -  |
**401** | Unauthenticated response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_instance_details_v1**
> GPUV1InstanceInstanceResource get_instance_details_v1(instance_id)

Get instance details

Retrieve detailed information about a specified GPU instance, including its SSH keys.

Use this endpoint to follow the instance `status` after creating or deleting it.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.gpuv1_instance_instance_resource import GPUV1InstanceInstanceResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.GPUInstancesApi(api_client)
    instance_id = 6325 # int | GPU instance ID

    try:
        # Get instance details
        api_response = api_instance.get_instance_details_v1(instance_id)
        print("The response of GPUInstancesApi->get_instance_details_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GPUInstancesApi->get_instance_details_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **int**| GPU instance ID | 

### Return type

[**GPUV1InstanceInstanceResource**](GPUV1InstanceInstanceResource.md)

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

# **get_instance_metrics_v1**
> List[GPUV1MetricsMetricsResource] get_instance_metrics_v1(instance_id)

Get instance metrics

Retrieve utilisation metrics of a specified GPU instance for the last hour.

Each data point contains CPU, memory and GPU utilisation, used GPU memory and GPU throughput.
The list is empty until the instance is provisioned.

Use this endpoint to monitor GPU instance load.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.gpuv1_metrics_metrics_resource import GPUV1MetricsMetricsResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.GPUInstancesApi(api_client)
    instance_id = 6325 # int | GPU instance ID

    try:
        # Get instance metrics
        api_response = api_instance.get_instance_metrics_v1(instance_id)
        print("The response of GPUInstancesApi->get_instance_metrics_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GPUInstancesApi->get_instance_metrics_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **int**| GPU instance ID | 

### Return type

[**List[GPUV1MetricsMetricsResource]**](GPUV1MetricsMetricsResource.md)

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

# **get_instances_v1**
> List[GPUV1InstanceInstanceListResource] get_instances_v1()

Get instances

Retrieve all GPU instances of your account.

Use this endpoint to view your GPU instances with their status, pool, instance type and OS template.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.gpuv1_instance_instance_list_resource import GPUV1InstanceInstanceListResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.GPUInstancesApi(api_client)

    try:
        # Get instances
        api_response = api_instance.get_instances_v1()
        print("The response of GPUInstancesApi->get_instances_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GPUInstancesApi->get_instances_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[GPUV1InstanceInstanceListResource]**](GPUV1InstanceInstanceListResource.md)

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

