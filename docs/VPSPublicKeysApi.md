# hostinger_api.VPSPublicKeysApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attach_public_key_v1**](VPSPublicKeysApi.md#attach_public_key_v1) | **POST** /api/vps/v1/public-keys/attach/{virtualMachineId} | Attach public key
[**create_public_key_v1**](VPSPublicKeysApi.md#create_public_key_v1) | **POST** /api/vps/v1/public-keys | Create public key
[**delete_public_key_v1**](VPSPublicKeysApi.md#delete_public_key_v1) | **DELETE** /api/vps/v1/public-keys/{publicKeyId} | Delete public key
[**get_public_keys_v1**](VPSPublicKeysApi.md#get_public_keys_v1) | **GET** /api/vps/v1/public-keys | Get public keys


# **attach_public_key_v1**
> VPSV1ActionActionResource attach_public_key_v1(virtual_machine_id, vpsv1_public_key_attach_request)

Attach public key

Attach existing public keys from your account to a specified virtual machine.

Multiple keys can be attached to a single virtual machine.

Use this endpoint to enable SSH key authentication for VPS instances.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.vpsv1_action_action_resource import VPSV1ActionActionResource
from hostinger_api.models.vpsv1_public_key_attach_request import VPSV1PublicKeyAttachRequest
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.VPSPublicKeysApi(api_client)
    virtual_machine_id = 1268054 # int | Virtual Machine ID
    vpsv1_public_key_attach_request = hostinger_api.VPSV1PublicKeyAttachRequest() # VPSV1PublicKeyAttachRequest | 

    try:
        # Attach public key
        api_response = api_instance.attach_public_key_v1(virtual_machine_id, vpsv1_public_key_attach_request)
        print("The response of VPSPublicKeysApi->attach_public_key_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPSPublicKeysApi->attach_public_key_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **virtual_machine_id** | **int**| Virtual Machine ID | 
 **vpsv1_public_key_attach_request** | [**VPSV1PublicKeyAttachRequest**](VPSV1PublicKeyAttachRequest.md)|  | 

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

# **create_public_key_v1**
> VPSV1PublicKeyPublicKeyResource create_public_key_v1(vpsv1_public_key_store_request)

Create public key

Add a new public key to your account.

Use this endpoint to register SSH keys for VPS authentication.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.vpsv1_public_key_public_key_resource import VPSV1PublicKeyPublicKeyResource
from hostinger_api.models.vpsv1_public_key_store_request import VPSV1PublicKeyStoreRequest
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.VPSPublicKeysApi(api_client)
    vpsv1_public_key_store_request = hostinger_api.VPSV1PublicKeyStoreRequest() # VPSV1PublicKeyStoreRequest | 

    try:
        # Create public key
        api_response = api_instance.create_public_key_v1(vpsv1_public_key_store_request)
        print("The response of VPSPublicKeysApi->create_public_key_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPSPublicKeysApi->create_public_key_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vpsv1_public_key_store_request** | [**VPSV1PublicKeyStoreRequest**](VPSV1PublicKeyStoreRequest.md)|  | 

### Return type

[**VPSV1PublicKeyPublicKeyResource**](VPSV1PublicKeyPublicKeyResource.md)

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

# **delete_public_key_v1**
> CommonSuccessEmptyResource delete_public_key_v1(public_key_id)

Delete public key

Delete a public key from your account. 

**Deleting public key from account does not remove it from virtual machine** 
       
Use this endpoint to remove unused SSH keys from account.

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
    api_instance = hostinger_api.VPSPublicKeysApi(api_client)
    public_key_id = 6672861 # int | Public Key ID

    try:
        # Delete public key
        api_response = api_instance.delete_public_key_v1(public_key_id)
        print("The response of VPSPublicKeysApi->delete_public_key_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPSPublicKeysApi->delete_public_key_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **public_key_id** | **int**| Public Key ID | 

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

# **get_public_keys_v1**
> VPSGetPublicKeysV1200Response get_public_keys_v1(page=page)

Get public keys

Retrieve public keys associated with your account.

Use this endpoint to view available SSH keys for VPS authentication.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.vps_get_public_keys_v1200_response import VPSGetPublicKeysV1200Response
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.VPSPublicKeysApi(api_client)
    page = 1 # int | Page number (optional)

    try:
        # Get public keys
        api_response = api_instance.get_public_keys_v1(page=page)
        print("The response of VPSPublicKeysApi->get_public_keys_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPSPublicKeysApi->get_public_keys_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number | [optional] 

### Return type

[**VPSGetPublicKeysV1200Response**](VPSGetPublicKeysV1200Response.md)

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

