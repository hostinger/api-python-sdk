# hostinger_api.VPSSnapshotsApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_snapshot_v1**](VPSSnapshotsApi.md#create_snapshot_v1) | **POST** /api/vps/v1/virtual-machines/{virtualMachineId}/snapshot | Create snapshot
[**delete_snapshot_v1**](VPSSnapshotsApi.md#delete_snapshot_v1) | **DELETE** /api/vps/v1/virtual-machines/{virtualMachineId}/snapshot | Delete snapshot
[**get_snapshot_v1**](VPSSnapshotsApi.md#get_snapshot_v1) | **GET** /api/vps/v1/virtual-machines/{virtualMachineId}/snapshot | Get snapshot
[**restore_snapshot_v1**](VPSSnapshotsApi.md#restore_snapshot_v1) | **POST** /api/vps/v1/virtual-machines/{virtualMachineId}/snapshot/restore | Restore snapshot


# **create_snapshot_v1**
> VPSV1ActionActionResource create_snapshot_v1(virtual_machine_id)

Create snapshot

Create a snapshot of a specified virtual machine.

A snapshot captures the state and data of the virtual machine at a specific point in time, 
allowing users to restore the virtual machine to that state if needed. 
This operation is useful for backup purposes, system recovery, 
and testing changes without affecting the current state of the virtual machine.

**Creating new snapshot will overwrite the existing snapshot!**

Use this endpoint to capture VPS state for backup and recovery purposes.

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
    api_instance = hostinger_api.VPSSnapshotsApi(api_client)
    virtual_machine_id = 1268054 # int | Virtual Machine ID

    try:
        # Create snapshot
        api_response = api_instance.create_snapshot_v1(virtual_machine_id)
        print("The response of VPSSnapshotsApi->create_snapshot_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPSSnapshotsApi->create_snapshot_v1: %s\n" % e)
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
**401** | Unauthenticated response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_snapshot_v1**
> VPSV1ActionActionResource delete_snapshot_v1(virtual_machine_id)

Delete snapshot

Delete a snapshot of a specified virtual machine.

Use this endpoint to remove VPS snapshots.

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
    api_instance = hostinger_api.VPSSnapshotsApi(api_client)
    virtual_machine_id = 1268054 # int | Virtual Machine ID

    try:
        # Delete snapshot
        api_response = api_instance.delete_snapshot_v1(virtual_machine_id)
        print("The response of VPSSnapshotsApi->delete_snapshot_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPSSnapshotsApi->delete_snapshot_v1: %s\n" % e)
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
**401** | Unauthenticated response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_snapshot_v1**
> VPSV1SnapshotSnapshotResource get_snapshot_v1(virtual_machine_id)

Get snapshot

Retrieve snapshot for a specified virtual machine.

Use this endpoint to view current VPS snapshot information.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.vpsv1_snapshot_snapshot_resource import VPSV1SnapshotSnapshotResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.VPSSnapshotsApi(api_client)
    virtual_machine_id = 1268054 # int | Virtual Machine ID

    try:
        # Get snapshot
        api_response = api_instance.get_snapshot_v1(virtual_machine_id)
        print("The response of VPSSnapshotsApi->get_snapshot_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPSSnapshotsApi->get_snapshot_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **virtual_machine_id** | **int**| Virtual Machine ID | 

### Return type

[**VPSV1SnapshotSnapshotResource**](VPSV1SnapshotSnapshotResource.md)

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

# **restore_snapshot_v1**
> VPSV1ActionActionResource restore_snapshot_v1(virtual_machine_id)

Restore snapshot

Restore a specified virtual machine to a previous state using a snapshot.

Restoring from a snapshot allows users to revert the virtual machine to that state, which is useful for system recovery, undoing changes, or testing.

Use this endpoint to revert VPS instances to previous saved states.

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
    api_instance = hostinger_api.VPSSnapshotsApi(api_client)
    virtual_machine_id = 1268054 # int | Virtual Machine ID

    try:
        # Restore snapshot
        api_response = api_instance.restore_snapshot_v1(virtual_machine_id)
        print("The response of VPSSnapshotsApi->restore_snapshot_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPSSnapshotsApi->restore_snapshot_v1: %s\n" % e)
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
**401** | Unauthenticated response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

