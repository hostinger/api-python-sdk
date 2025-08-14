# hostinger_api.VPSActionsApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_action_details_v1**](VPSActionsApi.md#get_action_details_v1) | **GET** /api/vps/v1/virtual-machines/{virtualMachineId}/actions/{actionId} | Get action details
[**get_actions_v1**](VPSActionsApi.md#get_actions_v1) | **GET** /api/vps/v1/virtual-machines/{virtualMachineId}/actions | Get actions


# **get_action_details_v1**
> VPSV1ActionActionResource get_action_details_v1(virtual_machine_id, action_id)

Get action details

Retrieve detailed information about a specific action performed on a specified virtual machine.

Use this endpoint to monitor specific VPS operation status and details.

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
    api_instance = hostinger_api.VPSActionsApi(api_client)
    virtual_machine_id = 1268054 # int | Virtual Machine ID
    action_id = 8123712 # int | Action ID

    try:
        # Get action details
        api_response = api_instance.get_action_details_v1(virtual_machine_id, action_id)
        print("The response of VPSActionsApi->get_action_details_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPSActionsApi->get_action_details_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **virtual_machine_id** | **int**| Virtual Machine ID | 
 **action_id** | **int**| Action ID | 

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

# **get_actions_v1**
> VPSGetActionsV1200Response get_actions_v1(virtual_machine_id, page=page)

Get actions

Retrieve actions performed on a specified virtual machine.

Actions are operations or events that have been executed on the virtual machine, such as starting, stopping, or modifying 
the machine. This endpoint allows you to view the history of these actions, providing details about each action, 
such as the action name, timestamp, and status.

Use this endpoint to view VPS operation history and troubleshoot issues.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.vps_get_actions_v1200_response import VPSGetActionsV1200Response
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.VPSActionsApi(api_client)
    virtual_machine_id = 1268054 # int | Virtual Machine ID
    page = 1 # int | Page number (optional)

    try:
        # Get actions
        api_response = api_instance.get_actions_v1(virtual_machine_id, page=page)
        print("The response of VPSActionsApi->get_actions_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPSActionsApi->get_actions_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **virtual_machine_id** | **int**| Virtual Machine ID | 
 **page** | **int**| Page number | [optional] 

### Return type

[**VPSGetActionsV1200Response**](VPSGetActionsV1200Response.md)

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

