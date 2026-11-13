# hostinger_api.GPUExposedServicesApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_exposed_service_v1**](GPUExposedServicesApi.md#create_exposed_service_v1) | **POST** /api/gpu/v1/instances/{instanceId}/exposed-services | Create exposed service
[**delete_exposed_service_v1**](GPUExposedServicesApi.md#delete_exposed_service_v1) | **DELETE** /api/gpu/v1/instances/{instanceId}/exposed-services/{exposedServiceId} | Delete exposed service
[**get_exposed_services_v1**](GPUExposedServicesApi.md#get_exposed_services_v1) | **GET** /api/gpu/v1/instances/{instanceId}/exposed-services | Get exposed services


# **create_exposed_service_v1**
> CommonSuccessEmptyResource create_exposed_service_v1(instance_id, gpuv1_exposed_service_store_request)

Create exposed service

Expose a service running on a specified GPU instance to the internet.

The service is exposed asynchronously: a successful request returns immediately, and the service
appears in the exposed services list once it gets its public hostname and external port.
Fails when the instance already has the maximum of 4 exposed services.

Use this endpoint to make an application on your GPU instance publicly reachable.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.common_success_empty_resource import CommonSuccessEmptyResource
from hostinger_api.models.gpuv1_exposed_service_store_request import GPUV1ExposedServiceStoreRequest
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.GPUExposedServicesApi(api_client)
    instance_id = 6325 # int | GPU instance ID
    gpuv1_exposed_service_store_request = hostinger_api.GPUV1ExposedServiceStoreRequest() # GPUV1ExposedServiceStoreRequest | 

    try:
        # Create exposed service
        api_response = api_instance.create_exposed_service_v1(instance_id, gpuv1_exposed_service_store_request)
        print("The response of GPUExposedServicesApi->create_exposed_service_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GPUExposedServicesApi->create_exposed_service_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **int**| GPU instance ID | 
 **gpuv1_exposed_service_store_request** | [**GPUV1ExposedServiceStoreRequest**](GPUV1ExposedServiceStoreRequest.md)|  | 

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

# **delete_exposed_service_v1**
> CommonSuccessEmptyResource delete_exposed_service_v1(instance_id, exposed_service_id)

Delete exposed service

Delete a specified exposed service of a GPU instance.

The service is removed asynchronously: a successful request returns immediately and the service
stops being reachable from the internet shortly after.

Use this endpoint to close public access to a service on your GPU instance.

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
    api_instance = hostinger_api.GPUExposedServicesApi(api_client)
    instance_id = 6325 # int | GPU instance ID
    exposed_service_id = 3621 # int | Exposed service ID

    try:
        # Delete exposed service
        api_response = api_instance.delete_exposed_service_v1(instance_id, exposed_service_id)
        print("The response of GPUExposedServicesApi->delete_exposed_service_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GPUExposedServicesApi->delete_exposed_service_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **int**| GPU instance ID | 
 **exposed_service_id** | **int**| Exposed service ID | 

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

# **get_exposed_services_v1**
> List[GPUV1ExposedServiceExposedServiceResource] get_exposed_services_v1(instance_id)

Get exposed services

Retrieve the services exposed on a specified GPU instance.

A newly created service is listed once it gets its public hostname and external port.

Use this endpoint to find the public address of services running on your GPU instance.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.gpuv1_exposed_service_exposed_service_resource import GPUV1ExposedServiceExposedServiceResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.GPUExposedServicesApi(api_client)
    instance_id = 6325 # int | GPU instance ID

    try:
        # Get exposed services
        api_response = api_instance.get_exposed_services_v1(instance_id)
        print("The response of GPUExposedServicesApi->get_exposed_services_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GPUExposedServicesApi->get_exposed_services_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **int**| GPU instance ID | 

### Return type

[**List[GPUV1ExposedServiceExposedServiceResource]**](GPUV1ExposedServiceExposedServiceResource.md)

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

