# hostinger_api.VPSBackupsApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_backups_v1**](VPSBackupsApi.md#get_backups_v1) | **GET** /api/vps/v1/virtual-machines/{virtualMachineId}/backups | Get backups
[**restore_backup_v1**](VPSBackupsApi.md#restore_backup_v1) | **POST** /api/vps/v1/virtual-machines/{virtualMachineId}/backups/{backupId}/restore | Restore backup


# **get_backups_v1**
> VPSGetBackupsV1200Response get_backups_v1(virtual_machine_id, page=page)

Get backups

Retrieve backups for a specified virtual machine.

Use this endpoint to view available backup points for VPS data recovery.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.vps_get_backups_v1200_response import VPSGetBackupsV1200Response
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.VPSBackupsApi(api_client)
    virtual_machine_id = 1268054 # int | Virtual Machine ID
    page = 1 # int | Page number (optional)

    try:
        # Get backups
        api_response = api_instance.get_backups_v1(virtual_machine_id, page=page)
        print("The response of VPSBackupsApi->get_backups_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPSBackupsApi->get_backups_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **virtual_machine_id** | **int**| Virtual Machine ID | 
 **page** | **int**| Page number | [optional] 

### Return type

[**VPSGetBackupsV1200Response**](VPSGetBackupsV1200Response.md)

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

# **restore_backup_v1**
> VPSV1ActionActionResource restore_backup_v1(virtual_machine_id, backup_id)

Restore backup

Restore a backup for a specified virtual machine.

The system will then initiate the restore process, which may take some time depending on the size of the backup.

**All data on the virtual machine will be overwritten with the data from the backup.**

Use this endpoint to recover VPS data from backup points.

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
    api_instance = hostinger_api.VPSBackupsApi(api_client)
    virtual_machine_id = 1268054 # int | Virtual Machine ID
    backup_id = 8676502 # int | Backup ID

    try:
        # Restore backup
        api_response = api_instance.restore_backup_v1(virtual_machine_id, backup_id)
        print("The response of VPSBackupsApi->restore_backup_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPSBackupsApi->restore_backup_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **virtual_machine_id** | **int**| Virtual Machine ID | 
 **backup_id** | **int**| Backup ID | 

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

