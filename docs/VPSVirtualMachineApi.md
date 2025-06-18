# hostinger_api.VPSVirtualMachineApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_attached_public_keys_v1**](VPSVirtualMachineApi.md#get_attached_public_keys_v1) | **GET** /api/vps/v1/virtual-machines/{virtualMachineId}/public-keys | Get attached public keys
[**get_metrics_v1**](VPSVirtualMachineApi.md#get_metrics_v1) | **GET** /api/vps/v1/virtual-machines/{virtualMachineId}/metrics | Get metrics
[**get_virtual_machine_list_v1**](VPSVirtualMachineApi.md#get_virtual_machine_list_v1) | **GET** /api/vps/v1/virtual-machines | Get virtual machine list
[**get_virtual_machine_v1**](VPSVirtualMachineApi.md#get_virtual_machine_v1) | **GET** /api/vps/v1/virtual-machines/{virtualMachineId} | Get virtual machine
[**purchase_new_virtual_machine_v1**](VPSVirtualMachineApi.md#purchase_new_virtual_machine_v1) | **POST** /api/vps/v1/virtual-machines | Purchase new virtual machine
[**recreate_virtual_machine_v1**](VPSVirtualMachineApi.md#recreate_virtual_machine_v1) | **POST** /api/vps/v1/virtual-machines/{virtualMachineId}/recreate | Recreate virtual machine
[**reset_hostname_v1**](VPSVirtualMachineApi.md#reset_hostname_v1) | **DELETE** /api/vps/v1/virtual-machines/{virtualMachineId}/hostname | Reset hostname
[**restart_virtual_machine_v1**](VPSVirtualMachineApi.md#restart_virtual_machine_v1) | **POST** /api/vps/v1/virtual-machines/{virtualMachineId}/restart | Restart virtual machine
[**set_hostname_v1**](VPSVirtualMachineApi.md#set_hostname_v1) | **PUT** /api/vps/v1/virtual-machines/{virtualMachineId}/hostname | Set hostname
[**set_nameservers_v1**](VPSVirtualMachineApi.md#set_nameservers_v1) | **PUT** /api/vps/v1/virtual-machines/{virtualMachineId}/nameservers | Set nameservers
[**set_panel_password_v1**](VPSVirtualMachineApi.md#set_panel_password_v1) | **PUT** /api/vps/v1/virtual-machines/{virtualMachineId}/panel-password | Set panel password
[**set_root_password_v1**](VPSVirtualMachineApi.md#set_root_password_v1) | **PUT** /api/vps/v1/virtual-machines/{virtualMachineId}/root-password | Set root password
[**setup_new_virtual_machine_v1**](VPSVirtualMachineApi.md#setup_new_virtual_machine_v1) | **POST** /api/vps/v1/virtual-machines/{virtualMachineId}/setup | Setup new virtual machine
[**start_virtual_machine_v1**](VPSVirtualMachineApi.md#start_virtual_machine_v1) | **POST** /api/vps/v1/virtual-machines/{virtualMachineId}/start | Start virtual machine
[**stop_virtual_machine_v1**](VPSVirtualMachineApi.md#stop_virtual_machine_v1) | **POST** /api/vps/v1/virtual-machines/{virtualMachineId}/stop | Stop virtual machine


# **get_attached_public_keys_v1**
> VPSGetPublicKeyListV1200Response get_attached_public_keys_v1(virtual_machine_id, page=page)

Get attached public keys

This endpoint retrieves a list of public keys attached to a specified virtual machine.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.vps_get_public_key_list_v1200_response import VPSGetPublicKeyListV1200Response
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.VPSVirtualMachineApi(api_client)
    virtual_machine_id = 1268054 # int | Virtual Machine ID
    page = 1 # int | Page number (optional)

    try:
        # Get attached public keys
        api_response = api_instance.get_attached_public_keys_v1(virtual_machine_id, page=page)
        print("The response of VPSVirtualMachineApi->get_attached_public_keys_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPSVirtualMachineApi->get_attached_public_keys_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **virtual_machine_id** | **int**| Virtual Machine ID | 
 **page** | **int**| Page number | [optional] 

### Return type

[**VPSGetPublicKeyListV1200Response**](VPSGetPublicKeyListV1200Response.md)

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

# **get_metrics_v1**
> VPSV1MetricsMetricsCollection get_metrics_v1(virtual_machine_id, date_from, date_to)

Get metrics

This endpoint retrieves the historical metrics for a specified virtual machine.
It includes the following metrics: 
- CPU usage
- Memory usage
- Disk usage
- Network usage
- Uptime

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.vpsv1_metrics_metrics_collection import VPSV1MetricsMetricsCollection
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.VPSVirtualMachineApi(api_client)
    virtual_machine_id = 1268054 # int | Virtual Machine ID
    date_from = '2025-05-01T00:00Z' # datetime | 
    date_to = '2025-06-01T00:00Z' # datetime | 

    try:
        # Get metrics
        api_response = api_instance.get_metrics_v1(virtual_machine_id, date_from, date_to)
        print("The response of VPSVirtualMachineApi->get_metrics_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPSVirtualMachineApi->get_metrics_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **virtual_machine_id** | **int**| Virtual Machine ID | 
 **date_from** | **datetime**|  | 
 **date_to** | **datetime**|  | 

### Return type

[**VPSV1MetricsMetricsCollection**](VPSV1MetricsMetricsCollection.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success response |  -  |
**422** | Validation error response |  -  |
**401** | Unauthenticated response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_virtual_machine_list_v1**
> List[VPSV1VirtualMachineVirtualMachineResource] get_virtual_machine_list_v1()

Get virtual machine list

This endpoint retrieves a list of all available virtual machines.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.vpsv1_virtual_machine_virtual_machine_resource import VPSV1VirtualMachineVirtualMachineResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.VPSVirtualMachineApi(api_client)

    try:
        # Get virtual machine list
        api_response = api_instance.get_virtual_machine_list_v1()
        print("The response of VPSVirtualMachineApi->get_virtual_machine_list_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPSVirtualMachineApi->get_virtual_machine_list_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[VPSV1VirtualMachineVirtualMachineResource]**](VPSV1VirtualMachineVirtualMachineResource.md)

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

# **get_virtual_machine_v1**
> VPSV1VirtualMachineVirtualMachineResource get_virtual_machine_v1(virtual_machine_id)

Get virtual machine

This endpoint retrieves detailed information about a specified virtual machine.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.vpsv1_virtual_machine_virtual_machine_resource import VPSV1VirtualMachineVirtualMachineResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.VPSVirtualMachineApi(api_client)
    virtual_machine_id = 1268054 # int | Virtual Machine ID

    try:
        # Get virtual machine
        api_response = api_instance.get_virtual_machine_v1(virtual_machine_id)
        print("The response of VPSVirtualMachineApi->get_virtual_machine_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPSVirtualMachineApi->get_virtual_machine_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **virtual_machine_id** | **int**| Virtual Machine ID | 

### Return type

[**VPSV1VirtualMachineVirtualMachineResource**](VPSV1VirtualMachineVirtualMachineResource.md)

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

# **purchase_new_virtual_machine_v1**
> BillingV1OrderVirtualMachineOrderResource purchase_new_virtual_machine_v1(vpsv1_virtual_machine_purchase_request)

Purchase new virtual machine

This endpoint allows you to buy (purchase) and setup a new virtual machine.

If virtual machine setup fails for any reason, login to [hPanel](https://hpanel.hostinger.com/) and complete the setup manually.

If no payment method is provided, your default payment method will be used automatically.                        

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.billing_v1_order_virtual_machine_order_resource import BillingV1OrderVirtualMachineOrderResource
from hostinger_api.models.vpsv1_virtual_machine_purchase_request import VPSV1VirtualMachinePurchaseRequest
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.VPSVirtualMachineApi(api_client)
    vpsv1_virtual_machine_purchase_request = hostinger_api.VPSV1VirtualMachinePurchaseRequest() # VPSV1VirtualMachinePurchaseRequest | 

    try:
        # Purchase new virtual machine
        api_response = api_instance.purchase_new_virtual_machine_v1(vpsv1_virtual_machine_purchase_request)
        print("The response of VPSVirtualMachineApi->purchase_new_virtual_machine_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPSVirtualMachineApi->purchase_new_virtual_machine_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vpsv1_virtual_machine_purchase_request** | [**VPSV1VirtualMachinePurchaseRequest**](VPSV1VirtualMachinePurchaseRequest.md)|  | 

### Return type

[**BillingV1OrderVirtualMachineOrderResource**](BillingV1OrderVirtualMachineOrderResource.md)

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

# **recreate_virtual_machine_v1**
> VPSV1ActionActionResource recreate_virtual_machine_v1(virtual_machine_id, vpsv1_virtual_machine_recreate_request)

Recreate virtual machine

This endpoint will recreate a virtual machine from scratch. 
The recreation process involves reinstalling the operating system and resetting the virtual machine to its initial state.
Snapshots, if there are any, will be deleted.

## Password Requirements
Password will be checked against leaked password databases. 
Requirements for the password are:
- At least 8 characters long
- At least one uppercase letter
- At least one lowercase letter
- At least one number
- Is not leaked publicly

**This operation is irreversible and will result in the loss of all data stored on the virtual machine!**

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.vpsv1_action_action_resource import VPSV1ActionActionResource
from hostinger_api.models.vpsv1_virtual_machine_recreate_request import VPSV1VirtualMachineRecreateRequest
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.VPSVirtualMachineApi(api_client)
    virtual_machine_id = 1268054 # int | Virtual Machine ID
    vpsv1_virtual_machine_recreate_request = hostinger_api.VPSV1VirtualMachineRecreateRequest() # VPSV1VirtualMachineRecreateRequest | 

    try:
        # Recreate virtual machine
        api_response = api_instance.recreate_virtual_machine_v1(virtual_machine_id, vpsv1_virtual_machine_recreate_request)
        print("The response of VPSVirtualMachineApi->recreate_virtual_machine_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPSVirtualMachineApi->recreate_virtual_machine_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **virtual_machine_id** | **int**| Virtual Machine ID | 
 **vpsv1_virtual_machine_recreate_request** | [**VPSV1VirtualMachineRecreateRequest**](VPSV1VirtualMachineRecreateRequest.md)|  | 

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

# **reset_hostname_v1**
> VPSV1ActionActionResource reset_hostname_v1(virtual_machine_id)

Reset hostname

This endpoint resets the hostname and PTR record of a specified virtual machine to the default value.

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
    api_instance = hostinger_api.VPSVirtualMachineApi(api_client)
    virtual_machine_id = 1268054 # int | Virtual Machine ID

    try:
        # Reset hostname
        api_response = api_instance.reset_hostname_v1(virtual_machine_id)
        print("The response of VPSVirtualMachineApi->reset_hostname_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPSVirtualMachineApi->reset_hostname_v1: %s\n" % e)
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

# **restart_virtual_machine_v1**
> VPSV1ActionActionResource restart_virtual_machine_v1(virtual_machine_id)

Restart virtual machine

This endpoint restarts a specified virtual machine. This is equivalent to fully stopping and starting the virtual machine.
If the virtual machine was stopped, it will be started.

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
    api_instance = hostinger_api.VPSVirtualMachineApi(api_client)
    virtual_machine_id = 1268054 # int | Virtual Machine ID

    try:
        # Restart virtual machine
        api_response = api_instance.restart_virtual_machine_v1(virtual_machine_id)
        print("The response of VPSVirtualMachineApi->restart_virtual_machine_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPSVirtualMachineApi->restart_virtual_machine_v1: %s\n" % e)
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

# **set_hostname_v1**
> VPSV1ActionActionResource set_hostname_v1(virtual_machine_id, vpsv1_virtual_machine_hostname_update_request)

Set hostname

This endpoint sets the hostname for a specified virtual machine. 
Changing hostname does not update PTR record automatically.
If you want your virtual machine to be reachable by a hostname, 
you need to point your domain A/AAAA records to virtual machine IP as well.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.vpsv1_action_action_resource import VPSV1ActionActionResource
from hostinger_api.models.vpsv1_virtual_machine_hostname_update_request import VPSV1VirtualMachineHostnameUpdateRequest
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.VPSVirtualMachineApi(api_client)
    virtual_machine_id = 1268054 # int | Virtual Machine ID
    vpsv1_virtual_machine_hostname_update_request = hostinger_api.VPSV1VirtualMachineHostnameUpdateRequest() # VPSV1VirtualMachineHostnameUpdateRequest | 

    try:
        # Set hostname
        api_response = api_instance.set_hostname_v1(virtual_machine_id, vpsv1_virtual_machine_hostname_update_request)
        print("The response of VPSVirtualMachineApi->set_hostname_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPSVirtualMachineApi->set_hostname_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **virtual_machine_id** | **int**| Virtual Machine ID | 
 **vpsv1_virtual_machine_hostname_update_request** | [**VPSV1VirtualMachineHostnameUpdateRequest**](VPSV1VirtualMachineHostnameUpdateRequest.md)|  | 

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

# **set_nameservers_v1**
> VPSV1ActionActionResource set_nameservers_v1(virtual_machine_id, vpsv1_virtual_machine_nameservers_update_request)

Set nameservers

This endpoint sets the nameservers for a specified virtual machine.
Be aware, that improper nameserver configuration can lead to the virtual machine being unable to resolve domain names.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.vpsv1_action_action_resource import VPSV1ActionActionResource
from hostinger_api.models.vpsv1_virtual_machine_nameservers_update_request import VPSV1VirtualMachineNameserversUpdateRequest
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.VPSVirtualMachineApi(api_client)
    virtual_machine_id = 1268054 # int | Virtual Machine ID
    vpsv1_virtual_machine_nameservers_update_request = hostinger_api.VPSV1VirtualMachineNameserversUpdateRequest() # VPSV1VirtualMachineNameserversUpdateRequest | 

    try:
        # Set nameservers
        api_response = api_instance.set_nameservers_v1(virtual_machine_id, vpsv1_virtual_machine_nameservers_update_request)
        print("The response of VPSVirtualMachineApi->set_nameservers_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPSVirtualMachineApi->set_nameservers_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **virtual_machine_id** | **int**| Virtual Machine ID | 
 **vpsv1_virtual_machine_nameservers_update_request** | [**VPSV1VirtualMachineNameserversUpdateRequest**](VPSV1VirtualMachineNameserversUpdateRequest.md)|  | 

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

# **set_panel_password_v1**
> VPSV1ActionActionResource set_panel_password_v1(virtual_machine_id, vpsv1_virtual_machine_panel_password_update_request)

Set panel password

This endpoint sets the panel password for a specified virtual machine. 
If virtual machine does not use panel OS, the request will still be processed without any effect.
Requirements for the password is the same as in the [recreate virtual machine endpoint](/#tag/vps-virtual-machine/POST/api/vps/v1/virtual-machines/{virtualMachineId}/recreate).

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.vpsv1_action_action_resource import VPSV1ActionActionResource
from hostinger_api.models.vpsv1_virtual_machine_panel_password_update_request import VPSV1VirtualMachinePanelPasswordUpdateRequest
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.VPSVirtualMachineApi(api_client)
    virtual_machine_id = 1268054 # int | Virtual Machine ID
    vpsv1_virtual_machine_panel_password_update_request = hostinger_api.VPSV1VirtualMachinePanelPasswordUpdateRequest() # VPSV1VirtualMachinePanelPasswordUpdateRequest | 

    try:
        # Set panel password
        api_response = api_instance.set_panel_password_v1(virtual_machine_id, vpsv1_virtual_machine_panel_password_update_request)
        print("The response of VPSVirtualMachineApi->set_panel_password_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPSVirtualMachineApi->set_panel_password_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **virtual_machine_id** | **int**| Virtual Machine ID | 
 **vpsv1_virtual_machine_panel_password_update_request** | [**VPSV1VirtualMachinePanelPasswordUpdateRequest**](VPSV1VirtualMachinePanelPasswordUpdateRequest.md)|  | 

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

# **set_root_password_v1**
> VPSV1ActionActionResource set_root_password_v1(virtual_machine_id, vpsv1_virtual_machine_root_password_update_request)

Set root password

This endpoint sets the root password for a specified virtual machine. 
Requirements for the password is the same as in the [recreate virtual machine endpoint](/#tag/vps-virtual-machine/POST/api/vps/v1/virtual-machines/{virtualMachineId}/recreate).

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.vpsv1_action_action_resource import VPSV1ActionActionResource
from hostinger_api.models.vpsv1_virtual_machine_root_password_update_request import VPSV1VirtualMachineRootPasswordUpdateRequest
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.VPSVirtualMachineApi(api_client)
    virtual_machine_id = 1268054 # int | Virtual Machine ID
    vpsv1_virtual_machine_root_password_update_request = hostinger_api.VPSV1VirtualMachineRootPasswordUpdateRequest() # VPSV1VirtualMachineRootPasswordUpdateRequest | 

    try:
        # Set root password
        api_response = api_instance.set_root_password_v1(virtual_machine_id, vpsv1_virtual_machine_root_password_update_request)
        print("The response of VPSVirtualMachineApi->set_root_password_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPSVirtualMachineApi->set_root_password_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **virtual_machine_id** | **int**| Virtual Machine ID | 
 **vpsv1_virtual_machine_root_password_update_request** | [**VPSV1VirtualMachineRootPasswordUpdateRequest**](VPSV1VirtualMachineRootPasswordUpdateRequest.md)|  | 

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

# **setup_new_virtual_machine_v1**
> VPSV1VirtualMachineVirtualMachineResource setup_new_virtual_machine_v1(virtual_machine_id, vpsv1_virtual_machine_setup_request)

Setup new virtual machine

This endpoint will setup newly purchased virtual machine with `initial` state. 

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.vpsv1_virtual_machine_setup_request import VPSV1VirtualMachineSetupRequest
from hostinger_api.models.vpsv1_virtual_machine_virtual_machine_resource import VPSV1VirtualMachineVirtualMachineResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.VPSVirtualMachineApi(api_client)
    virtual_machine_id = 1268054 # int | Virtual Machine ID
    vpsv1_virtual_machine_setup_request = hostinger_api.VPSV1VirtualMachineSetupRequest() # VPSV1VirtualMachineSetupRequest | 

    try:
        # Setup new virtual machine
        api_response = api_instance.setup_new_virtual_machine_v1(virtual_machine_id, vpsv1_virtual_machine_setup_request)
        print("The response of VPSVirtualMachineApi->setup_new_virtual_machine_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPSVirtualMachineApi->setup_new_virtual_machine_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **virtual_machine_id** | **int**| Virtual Machine ID | 
 **vpsv1_virtual_machine_setup_request** | [**VPSV1VirtualMachineSetupRequest**](VPSV1VirtualMachineSetupRequest.md)|  | 

### Return type

[**VPSV1VirtualMachineVirtualMachineResource**](VPSV1VirtualMachineVirtualMachineResource.md)

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

# **start_virtual_machine_v1**
> VPSV1ActionActionResource start_virtual_machine_v1(virtual_machine_id)

Start virtual machine

This endpoint starts a specified virtual machine. 
If the virtual machine is already running, the request will still be processed without any effect.

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
    api_instance = hostinger_api.VPSVirtualMachineApi(api_client)
    virtual_machine_id = 1268054 # int | Virtual Machine ID

    try:
        # Start virtual machine
        api_response = api_instance.start_virtual_machine_v1(virtual_machine_id)
        print("The response of VPSVirtualMachineApi->start_virtual_machine_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPSVirtualMachineApi->start_virtual_machine_v1: %s\n" % e)
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

# **stop_virtual_machine_v1**
> VPSV1ActionActionResource stop_virtual_machine_v1(virtual_machine_id)

Stop virtual machine

This endpoint stops a specified virtual machine. 
If the virtual machine is already stopped, the request will still be processed without any effect.

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
    api_instance = hostinger_api.VPSVirtualMachineApi(api_client)
    virtual_machine_id = 1268054 # int | Virtual Machine ID

    try:
        # Stop virtual machine
        api_response = api_instance.stop_virtual_machine_v1(virtual_machine_id)
        print("The response of VPSVirtualMachineApi->stop_virtual_machine_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPSVirtualMachineApi->stop_virtual_machine_v1: %s\n" % e)
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

