# hostinger_api.VPSPostInstallScriptsApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_post_install_script_v1**](VPSPostInstallScriptsApi.md#create_post_install_script_v1) | **POST** /api/vps/v1/post-install-scripts | Create post-install script
[**delete_a_post_install_script_v1**](VPSPostInstallScriptsApi.md#delete_a_post_install_script_v1) | **DELETE** /api/vps/v1/post-install-scripts/{postInstallScriptId} | Delete a post-install script
[**get_post_install_script_list_v1**](VPSPostInstallScriptsApi.md#get_post_install_script_list_v1) | **GET** /api/vps/v1/post-install-scripts | Get post-install script list
[**get_post_install_script_v1**](VPSPostInstallScriptsApi.md#get_post_install_script_v1) | **GET** /api/vps/v1/post-install-scripts/{postInstallScriptId} | Get post-install script
[**update_post_install_script_v1**](VPSPostInstallScriptsApi.md#update_post_install_script_v1) | **PUT** /api/vps/v1/post-install-scripts/{postInstallScriptId} | Update post-install script


# **create_post_install_script_v1**
> VPSV1PostInstallScriptPostInstallScriptResource create_post_install_script_v1(vpsv1_post_install_script_store_request)

Create post-install script

This endpoint allows you to add a new post-install script to your account, 
which can then be used run after the installation of a virtual machine instance.

The script contents will be saved to the file `/post_install` with executable attribute set and will be executed once virtual machine is installed.
The output of the script will be redirected to `/post_install.log`. Maximum script size is 48KB. 

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.vpsv1_post_install_script_post_install_script_resource import VPSV1PostInstallScriptPostInstallScriptResource
from hostinger_api.models.vpsv1_post_install_script_store_request import VPSV1PostInstallScriptStoreRequest
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.VPSPostInstallScriptsApi(api_client)
    vpsv1_post_install_script_store_request = hostinger_api.VPSV1PostInstallScriptStoreRequest() # VPSV1PostInstallScriptStoreRequest | 

    try:
        # Create post-install script
        api_response = api_instance.create_post_install_script_v1(vpsv1_post_install_script_store_request)
        print("The response of VPSPostInstallScriptsApi->create_post_install_script_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPSPostInstallScriptsApi->create_post_install_script_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vpsv1_post_install_script_store_request** | [**VPSV1PostInstallScriptStoreRequest**](VPSV1PostInstallScriptStoreRequest.md)|  | 

### Return type

[**VPSV1PostInstallScriptPostInstallScriptResource**](VPSV1PostInstallScriptPostInstallScriptResource.md)

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

# **delete_a_post_install_script_v1**
> CommonSuccessEmptyResource delete_a_post_install_script_v1(post_install_script_id)

Delete a post-install script

This endpoint deletes a post-install script from your account. 

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
    api_instance = hostinger_api.VPSPostInstallScriptsApi(api_client)
    post_install_script_id = 9568314 # int | Post-install script ID

    try:
        # Delete a post-install script
        api_response = api_instance.delete_a_post_install_script_v1(post_install_script_id)
        print("The response of VPSPostInstallScriptsApi->delete_a_post_install_script_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPSPostInstallScriptsApi->delete_a_post_install_script_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_install_script_id** | **int**| Post-install script ID | 

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

# **get_post_install_script_list_v1**
> VPSGetPostInstallScriptListV1200Response get_post_install_script_list_v1(page=page)

Get post-install script list

This endpoint retrieves a list of post-install scripts associated with your account.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.vps_get_post_install_script_list_v1200_response import VPSGetPostInstallScriptListV1200Response
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.VPSPostInstallScriptsApi(api_client)
    page = 1 # int | Page number (optional)

    try:
        # Get post-install script list
        api_response = api_instance.get_post_install_script_list_v1(page=page)
        print("The response of VPSPostInstallScriptsApi->get_post_install_script_list_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPSPostInstallScriptsApi->get_post_install_script_list_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number | [optional] 

### Return type

[**VPSGetPostInstallScriptListV1200Response**](VPSGetPostInstallScriptListV1200Response.md)

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

# **get_post_install_script_v1**
> VPSV1PostInstallScriptPostInstallScriptResource get_post_install_script_v1(post_install_script_id)

Get post-install script

This endpoint retrieves post-install script by its ID.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.vpsv1_post_install_script_post_install_script_resource import VPSV1PostInstallScriptPostInstallScriptResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.VPSPostInstallScriptsApi(api_client)
    post_install_script_id = 9568314 # int | Post-install script ID

    try:
        # Get post-install script
        api_response = api_instance.get_post_install_script_v1(post_install_script_id)
        print("The response of VPSPostInstallScriptsApi->get_post_install_script_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPSPostInstallScriptsApi->get_post_install_script_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_install_script_id** | **int**| Post-install script ID | 

### Return type

[**VPSV1PostInstallScriptPostInstallScriptResource**](VPSV1PostInstallScriptPostInstallScriptResource.md)

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

# **update_post_install_script_v1**
> VPSV1PostInstallScriptPostInstallScriptResource update_post_install_script_v1(post_install_script_id, vpsv1_post_install_script_store_request)

Update post-install script

This endpoint updates a specific post-install script.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.vpsv1_post_install_script_post_install_script_resource import VPSV1PostInstallScriptPostInstallScriptResource
from hostinger_api.models.vpsv1_post_install_script_store_request import VPSV1PostInstallScriptStoreRequest
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.VPSPostInstallScriptsApi(api_client)
    post_install_script_id = 9568314 # int | Post-install script ID
    vpsv1_post_install_script_store_request = hostinger_api.VPSV1PostInstallScriptStoreRequest() # VPSV1PostInstallScriptStoreRequest | 

    try:
        # Update post-install script
        api_response = api_instance.update_post_install_script_v1(post_install_script_id, vpsv1_post_install_script_store_request)
        print("The response of VPSPostInstallScriptsApi->update_post_install_script_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPSPostInstallScriptsApi->update_post_install_script_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_install_script_id** | **int**| Post-install script ID | 
 **vpsv1_post_install_script_store_request** | [**VPSV1PostInstallScriptStoreRequest**](VPSV1PostInstallScriptStoreRequest.md)|  | 

### Return type

[**VPSV1PostInstallScriptPostInstallScriptResource**](VPSV1PostInstallScriptPostInstallScriptResource.md)

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

