# hostinger_api.VPSPTRRecordsApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_ptr_record_v1**](VPSPTRRecordsApi.md#create_ptr_record_v1) | **POST** /api/vps/v1/virtual-machines/{virtualMachineId}/ptr/{ipAddressId} | Create PTR record
[**delete_ptr_record_v1**](VPSPTRRecordsApi.md#delete_ptr_record_v1) | **DELETE** /api/vps/v1/virtual-machines/{virtualMachineId}/ptr/{ipAddressId} | Delete PTR record


# **create_ptr_record_v1**
> VPSV1ActionActionResource create_ptr_record_v1(virtual_machine_id, ip_address_id, vpsv1_virtual_machine_ptr_store_request)

Create PTR record

Create or update a PTR (Pointer) record for a specified virtual machine.

Use this endpoint to configure reverse DNS lookup for VPS IP addresses.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.vpsv1_action_action_resource import VPSV1ActionActionResource
from hostinger_api.models.vpsv1_virtual_machine_ptr_store_request import VPSV1VirtualMachinePTRStoreRequest
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.VPSPTRRecordsApi(api_client)
    virtual_machine_id = 1268054 # int | Virtual Machine ID
    ip_address_id = 246547 # int | IP Address ID
    vpsv1_virtual_machine_ptr_store_request = hostinger_api.VPSV1VirtualMachinePTRStoreRequest() # VPSV1VirtualMachinePTRStoreRequest | 

    try:
        # Create PTR record
        api_response = api_instance.create_ptr_record_v1(virtual_machine_id, ip_address_id, vpsv1_virtual_machine_ptr_store_request)
        print("The response of VPSPTRRecordsApi->create_ptr_record_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPSPTRRecordsApi->create_ptr_record_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **virtual_machine_id** | **int**| Virtual Machine ID | 
 **ip_address_id** | **int**| IP Address ID | 
 **vpsv1_virtual_machine_ptr_store_request** | [**VPSV1VirtualMachinePTRStoreRequest**](VPSV1VirtualMachinePTRStoreRequest.md)|  | 

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
**401** | Unauthenticated response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ptr_record_v1**
> VPSV1ActionActionResource delete_ptr_record_v1(virtual_machine_id, ip_address_id)

Delete PTR record

Delete a PTR (Pointer) record for a specified virtual machine.

Once deleted, reverse DNS lookups to the virtual machine's IP address will no longer return the previously configured hostname.

Use this endpoint to remove reverse DNS configuration from VPS instances.

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
    api_instance = hostinger_api.VPSPTRRecordsApi(api_client)
    virtual_machine_id = 1268054 # int | Virtual Machine ID
    ip_address_id = 246547 # int | IP Address ID

    try:
        # Delete PTR record
        api_response = api_instance.delete_ptr_record_v1(virtual_machine_id, ip_address_id)
        print("The response of VPSPTRRecordsApi->delete_ptr_record_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPSPTRRecordsApi->delete_ptr_record_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **virtual_machine_id** | **int**| Virtual Machine ID | 
 **ip_address_id** | **int**| IP Address ID | 

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
**401** | Unauthenticated response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

