# hostinger_api.VPSRecoveryApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**start_recovery_mode_v1**](VPSRecoveryApi.md#start_recovery_mode_v1) | **POST** /api/vps/v1/virtual-machines/{virtualMachineId}/recovery | Start recovery mode
[**stop_recovery_mode_v1**](VPSRecoveryApi.md#stop_recovery_mode_v1) | **DELETE** /api/vps/v1/virtual-machines/{virtualMachineId}/recovery | Stop recovery mode


# **start_recovery_mode_v1**
> VPSV1ActionActionResource start_recovery_mode_v1(virtual_machine_id, vpsv1_virtual_machine_recovery_start_request)

Start recovery mode

This endpoint initiates the recovery mode for a specified virtual machine. 
Recovery mode is a special state that allows users to perform system rescue operations, 
such as repairing file systems, recovering data, or troubleshooting issues that prevent the virtual machine 
from booting normally. 

Virtual machine will boot recovery disk image and original disk image will be mounted in `/mnt` directory.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.vpsv1_action_action_resource import VPSV1ActionActionResource
from hostinger_api.models.vpsv1_virtual_machine_recovery_start_request import VPSV1VirtualMachineRecoveryStartRequest
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.VPSRecoveryApi(api_client)
    virtual_machine_id = 1268054 # int | Virtual Machine ID
    vpsv1_virtual_machine_recovery_start_request = hostinger_api.VPSV1VirtualMachineRecoveryStartRequest() # VPSV1VirtualMachineRecoveryStartRequest | 

    try:
        # Start recovery mode
        api_response = api_instance.start_recovery_mode_v1(virtual_machine_id, vpsv1_virtual_machine_recovery_start_request)
        print("The response of VPSRecoveryApi->start_recovery_mode_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPSRecoveryApi->start_recovery_mode_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **virtual_machine_id** | **int**| Virtual Machine ID | 
 **vpsv1_virtual_machine_recovery_start_request** | [**VPSV1VirtualMachineRecoveryStartRequest**](VPSV1VirtualMachineRecoveryStartRequest.md)|  | 

### Return type

[**VPSV1ActionActionResource**](VPSV1ActionActionResource.md)

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
**401** | Unauthenticated |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_recovery_mode_v1**
> VPSV1ActionActionResource stop_recovery_mode_v1(virtual_machine_id)

Stop recovery mode

This endpoint stops the recovery mode for a specified virtual machine. 
If virtual machine is not in recovery mode, this operation will fail.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.vpsv1_action_action_resource import VPSV1ActionActionResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.VPSRecoveryApi(api_client)
    virtual_machine_id = 1268054 # int | Virtual Machine ID

    try:
        # Stop recovery mode
        api_response = api_instance.stop_recovery_mode_v1(virtual_machine_id)
        print("The response of VPSRecoveryApi->stop_recovery_mode_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPSRecoveryApi->stop_recovery_mode_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **virtual_machine_id** | **int**| Virtual Machine ID | 

### Return type

[**VPSV1ActionActionResource**](VPSV1ActionActionResource.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success response |  -  |
**401** | Unauthenticated |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

