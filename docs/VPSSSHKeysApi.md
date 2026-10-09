# hostinger_api.VPSSSHKeysApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_virtual_machine_ssh_keys_v1**](VPSSSHKeysApi.md#add_virtual_machine_ssh_keys_v1) | **POST** /api/vps/v1/virtual-machines/{virtualMachineId}/ssh-keys | Add virtual machine SSH keys
[**list_virtual_machine_ssh_keys_v1**](VPSSSHKeysApi.md#list_virtual_machine_ssh_keys_v1) | **GET** /api/vps/v1/virtual-machines/{virtualMachineId}/ssh-keys | List virtual machine SSH keys
[**remove_virtual_machine_ssh_keys_v1**](VPSSSHKeysApi.md#remove_virtual_machine_ssh_keys_v1) | **DELETE** /api/vps/v1/virtual-machines/{virtualMachineId}/ssh-keys | Remove virtual machine SSH keys


# **add_virtual_machine_ssh_keys_v1**
> List[VPSV1SshKeySshKeyResource] add_virtual_machine_ssh_keys_v1(virtual_machine_id, vpsv1_ssh_key_store_request)

Add virtual machine SSH keys

Add one or more SSH public keys to a specified virtual machine.

Keys are added to the `root` user and can be used for passwordless SSH authentication.
Returns the complete list of SSH keys currently configured on the virtual machine.

Use this endpoint to enable SSH key authentication for VPS instances.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.vpsv1_ssh_key_ssh_key_resource import VPSV1SshKeySshKeyResource
from hostinger_api.models.vpsv1_ssh_key_store_request import VPSV1SshKeyStoreRequest
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.VPSSSHKeysApi(api_client)
    virtual_machine_id = 1268054 # int | Virtual Machine ID
    vpsv1_ssh_key_store_request = hostinger_api.VPSV1SshKeyStoreRequest() # VPSV1SshKeyStoreRequest | 

    try:
        # Add virtual machine SSH keys
        api_response = api_instance.add_virtual_machine_ssh_keys_v1(virtual_machine_id, vpsv1_ssh_key_store_request)
        print("The response of VPSSSHKeysApi->add_virtual_machine_ssh_keys_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPSSSHKeysApi->add_virtual_machine_ssh_keys_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **virtual_machine_id** | **int**| Virtual Machine ID | 
 **vpsv1_ssh_key_store_request** | [**VPSV1SshKeyStoreRequest**](VPSV1SshKeyStoreRequest.md)|  | 

### Return type

[**List[VPSV1SshKeySshKeyResource]**](VPSV1SshKeySshKeyResource.md)

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

# **list_virtual_machine_ssh_keys_v1**
> List[VPSV1SshKeySshKeyResource] list_virtual_machine_ssh_keys_v1(virtual_machine_id)

List virtual machine SSH keys

Retrieve SSH public keys currently configured on a specified virtual machine.

Only keys of the `root` user are listed.

Use this endpoint to view SSH keys that can be used for authentication on VPS instances.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.vpsv1_ssh_key_ssh_key_resource import VPSV1SshKeySshKeyResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.VPSSSHKeysApi(api_client)
    virtual_machine_id = 1268054 # int | Virtual Machine ID

    try:
        # List virtual machine SSH keys
        api_response = api_instance.list_virtual_machine_ssh_keys_v1(virtual_machine_id)
        print("The response of VPSSSHKeysApi->list_virtual_machine_ssh_keys_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPSSSHKeysApi->list_virtual_machine_ssh_keys_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **virtual_machine_id** | **int**| Virtual Machine ID | 

### Return type

[**List[VPSV1SshKeySshKeyResource]**](VPSV1SshKeySshKeyResource.md)

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

# **remove_virtual_machine_ssh_keys_v1**
> List[VPSV1SshKeySshKeyResource] remove_virtual_machine_ssh_keys_v1(virtual_machine_id, vpsv1_ssh_key_destroy_request)

Remove virtual machine SSH keys

Remove one or more SSH public keys from a specified virtual machine.

Removed keys can no longer be used to authenticate via SSH as the `root` user.
Returns the remaining list of SSH keys configured on the virtual machine.

Use this endpoint to revoke SSH key access to VPS instances.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.vpsv1_ssh_key_destroy_request import VPSV1SshKeyDestroyRequest
from hostinger_api.models.vpsv1_ssh_key_ssh_key_resource import VPSV1SshKeySshKeyResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.VPSSSHKeysApi(api_client)
    virtual_machine_id = 1268054 # int | Virtual Machine ID
    vpsv1_ssh_key_destroy_request = hostinger_api.VPSV1SshKeyDestroyRequest() # VPSV1SshKeyDestroyRequest | 

    try:
        # Remove virtual machine SSH keys
        api_response = api_instance.remove_virtual_machine_ssh_keys_v1(virtual_machine_id, vpsv1_ssh_key_destroy_request)
        print("The response of VPSSSHKeysApi->remove_virtual_machine_ssh_keys_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPSSSHKeysApi->remove_virtual_machine_ssh_keys_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **virtual_machine_id** | **int**| Virtual Machine ID | 
 **vpsv1_ssh_key_destroy_request** | [**VPSV1SshKeyDestroyRequest**](VPSV1SshKeyDestroyRequest.md)|  | 

### Return type

[**List[VPSV1SshKeySshKeyResource]**](VPSV1SshKeySshKeyResource.md)

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

