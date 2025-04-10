# hostinger_api.VPSFirewallApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_firewall_v1**](VPSFirewallApi.md#activate_firewall_v1) | **POST** /api/vps/v1/firewall/{firewallId}/activate/{virtualMachineId} | Activate firewall
[**create_firewall_rule_v1**](VPSFirewallApi.md#create_firewall_rule_v1) | **POST** /api/vps/v1/firewall/{firewallId}/rules | Create firewall rule
[**create_new_firewall_v1**](VPSFirewallApi.md#create_new_firewall_v1) | **POST** /api/vps/v1/firewall | Create new firewall
[**deactivate_firewall_v1**](VPSFirewallApi.md#deactivate_firewall_v1) | **POST** /api/vps/v1/firewall/{firewallId}/deactivate/{virtualMachineId} | Deactivate firewall
[**delete_firewall_rule_v1**](VPSFirewallApi.md#delete_firewall_rule_v1) | **DELETE** /api/vps/v1/firewall/{firewallId}/rules/{ruleId} | Delete firewall rule
[**delete_firewall_v1**](VPSFirewallApi.md#delete_firewall_v1) | **DELETE** /api/vps/v1/firewall/{firewallId} | Delete firewall
[**get_firewall_list_v1**](VPSFirewallApi.md#get_firewall_list_v1) | **GET** /api/vps/v1/firewall | Get firewall list
[**get_firewall_v1**](VPSFirewallApi.md#get_firewall_v1) | **GET** /api/vps/v1/firewall/{firewallId} | Get firewall
[**sync_firewall_v1**](VPSFirewallApi.md#sync_firewall_v1) | **POST** /api/vps/v1/firewall/{firewallId}/sync/{virtualMachineId} | Sync firewall
[**update_firewall_rule_v1**](VPSFirewallApi.md#update_firewall_rule_v1) | **PUT** /api/vps/v1/firewall/{firewallId}/rules/{ruleId} | Update firewall rule


# **activate_firewall_v1**
> VPSV1ActionActionResource activate_firewall_v1(firewall_id, virtual_machine_id)

Activate firewall

This endpoint activates a firewall for a specified virtual machine. 

Only one firewall can be active for a virtual machine at a time.

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
    api_instance = hostinger_api.VPSFirewallApi(api_client)
    firewall_id = 9449049 # int | Firewall ID
    virtual_machine_id = 1268054 # int | Virtual Machine ID

    try:
        # Activate firewall
        api_response = api_instance.activate_firewall_v1(firewall_id, virtual_machine_id)
        print("The response of VPSFirewallApi->activate_firewall_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPSFirewallApi->activate_firewall_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **firewall_id** | **int**| Firewall ID | 
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
**422** | Validation error response |  -  |
**401** | Unauthenticated |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_firewall_rule_v1**
> VPSV1FirewallFirewallRuleResource create_firewall_rule_v1(firewall_id, vpsv1_firewall_rules_store_request)

Create firewall rule

This endpoint creates new firewall rule from a specified firewall. 
By default, the firewall drops all incoming traffic, which means you must add accept rules for all ports you want to use.

Any virtual machine that has this firewall activated will loose sync with the firewall and will have to be synced again manually.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.vpsv1_firewall_firewall_rule_resource import VPSV1FirewallFirewallRuleResource
from hostinger_api.models.vpsv1_firewall_rules_store_request import VPSV1FirewallRulesStoreRequest
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.VPSFirewallApi(api_client)
    firewall_id = 9449049 # int | Firewall ID
    vpsv1_firewall_rules_store_request = hostinger_api.VPSV1FirewallRulesStoreRequest() # VPSV1FirewallRulesStoreRequest | 

    try:
        # Create firewall rule
        api_response = api_instance.create_firewall_rule_v1(firewall_id, vpsv1_firewall_rules_store_request)
        print("The response of VPSFirewallApi->create_firewall_rule_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPSFirewallApi->create_firewall_rule_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **firewall_id** | **int**| Firewall ID | 
 **vpsv1_firewall_rules_store_request** | [**VPSV1FirewallRulesStoreRequest**](VPSV1FirewallRulesStoreRequest.md)|  | 

### Return type

[**VPSV1FirewallFirewallRuleResource**](VPSV1FirewallFirewallRuleResource.md)

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

# **create_new_firewall_v1**
> VPSV1FirewallFirewallResource create_new_firewall_v1(vpsv1_firewall_store_request)

Create new firewall

This endpoint creates a new firewall.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.vpsv1_firewall_firewall_resource import VPSV1FirewallFirewallResource
from hostinger_api.models.vpsv1_firewall_store_request import VPSV1FirewallStoreRequest
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.VPSFirewallApi(api_client)
    vpsv1_firewall_store_request = hostinger_api.VPSV1FirewallStoreRequest() # VPSV1FirewallStoreRequest | 

    try:
        # Create new firewall
        api_response = api_instance.create_new_firewall_v1(vpsv1_firewall_store_request)
        print("The response of VPSFirewallApi->create_new_firewall_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPSFirewallApi->create_new_firewall_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vpsv1_firewall_store_request** | [**VPSV1FirewallStoreRequest**](VPSV1FirewallStoreRequest.md)|  | 

### Return type

[**VPSV1FirewallFirewallResource**](VPSV1FirewallFirewallResource.md)

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

# **deactivate_firewall_v1**
> VPSV1ActionActionResource deactivate_firewall_v1(firewall_id, virtual_machine_id)

Deactivate firewall

This endpoint deactivates a firewall for a specified virtual machine.

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
    api_instance = hostinger_api.VPSFirewallApi(api_client)
    firewall_id = 9449049 # int | Firewall ID
    virtual_machine_id = 1268054 # int | Virtual Machine ID

    try:
        # Deactivate firewall
        api_response = api_instance.deactivate_firewall_v1(firewall_id, virtual_machine_id)
        print("The response of VPSFirewallApi->deactivate_firewall_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPSFirewallApi->deactivate_firewall_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **firewall_id** | **int**| Firewall ID | 
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
**422** | Validation error response |  -  |
**401** | Unauthenticated |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_firewall_rule_v1**
> CommonSuccessEmptyResource delete_firewall_rule_v1(firewall_id, rule_id)

Delete firewall rule

This endpoint deletes a specific firewall rule from a specified firewall.

Any virtual machine that has this firewall activated will loose sync with the firewall and will have to be synced again manually.

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
    api_instance = hostinger_api.VPSFirewallApi(api_client)
    firewall_id = 9449049 # int | Firewall ID
    rule_id = 8941182 # int | Firewall Rule ID

    try:
        # Delete firewall rule
        api_response = api_instance.delete_firewall_rule_v1(firewall_id, rule_id)
        print("The response of VPSFirewallApi->delete_firewall_rule_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPSFirewallApi->delete_firewall_rule_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **firewall_id** | **int**| Firewall ID | 
 **rule_id** | **int**| Firewall Rule ID | 

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
**401** | Unauthenticated |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_firewall_v1**
> CommonSuccessEmptyResource delete_firewall_v1(firewall_id)

Delete firewall

This endpoint deletes a specified firewall. 

Any virtual machine that has this firewall activated will automatically have it deactivated.

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
    api_instance = hostinger_api.VPSFirewallApi(api_client)
    firewall_id = 9449049 # int | Firewall ID

    try:
        # Delete firewall
        api_response = api_instance.delete_firewall_v1(firewall_id)
        print("The response of VPSFirewallApi->delete_firewall_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPSFirewallApi->delete_firewall_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **firewall_id** | **int**| Firewall ID | 

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
**401** | Unauthenticated |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_firewall_list_v1**
> VPSGetFirewallListV1200Response get_firewall_list_v1(page=page)

Get firewall list

This endpoint retrieves a list of all firewalls available.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.vps_get_firewall_list_v1200_response import VPSGetFirewallListV1200Response
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.VPSFirewallApi(api_client)
    page = 1 # int | Page number (optional)

    try:
        # Get firewall list
        api_response = api_instance.get_firewall_list_v1(page=page)
        print("The response of VPSFirewallApi->get_firewall_list_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPSFirewallApi->get_firewall_list_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number | [optional] 

### Return type

[**VPSGetFirewallListV1200Response**](VPSGetFirewallListV1200Response.md)

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

# **get_firewall_v1**
> VPSV1FirewallFirewallResource get_firewall_v1(firewall_id)

Get firewall

This endpoint retrieves firewall by its ID and rules associated with it.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.vpsv1_firewall_firewall_resource import VPSV1FirewallFirewallResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.VPSFirewallApi(api_client)
    firewall_id = 9449049 # int | Firewall ID

    try:
        # Get firewall
        api_response = api_instance.get_firewall_v1(firewall_id)
        print("The response of VPSFirewallApi->get_firewall_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPSFirewallApi->get_firewall_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **firewall_id** | **int**| Firewall ID | 

### Return type

[**VPSV1FirewallFirewallResource**](VPSV1FirewallFirewallResource.md)

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

# **sync_firewall_v1**
> VPSV1ActionActionResource sync_firewall_v1(firewall_id, virtual_machine_id)

Sync firewall

This endpoint syncs a firewall for a specified virtual machine.

Firewall can loose sync with virtual machine if the firewall has new rules added, removed or updated.

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
    api_instance = hostinger_api.VPSFirewallApi(api_client)
    firewall_id = 9449049 # int | Firewall ID
    virtual_machine_id = 1268054 # int | Virtual Machine ID

    try:
        # Sync firewall
        api_response = api_instance.sync_firewall_v1(firewall_id, virtual_machine_id)
        print("The response of VPSFirewallApi->sync_firewall_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPSFirewallApi->sync_firewall_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **firewall_id** | **int**| Firewall ID | 
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
**422** | Validation error response |  -  |
**401** | Unauthenticated |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_firewall_rule_v1**
> VPSV1FirewallFirewallRuleResource update_firewall_rule_v1(firewall_id, rule_id, vpsv1_firewall_rules_store_request)

Update firewall rule

This endpoint updates a specific firewall rule from a specified firewall.

Any virtual machine that has this firewall activated will loose sync with the firewall and will have to be synced again manually.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.vpsv1_firewall_firewall_rule_resource import VPSV1FirewallFirewallRuleResource
from hostinger_api.models.vpsv1_firewall_rules_store_request import VPSV1FirewallRulesStoreRequest
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.VPSFirewallApi(api_client)
    firewall_id = 9449049 # int | Firewall ID
    rule_id = 8941182 # int | Firewall Rule ID
    vpsv1_firewall_rules_store_request = hostinger_api.VPSV1FirewallRulesStoreRequest() # VPSV1FirewallRulesStoreRequest | 

    try:
        # Update firewall rule
        api_response = api_instance.update_firewall_rule_v1(firewall_id, rule_id, vpsv1_firewall_rules_store_request)
        print("The response of VPSFirewallApi->update_firewall_rule_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPSFirewallApi->update_firewall_rule_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **firewall_id** | **int**| Firewall ID | 
 **rule_id** | **int**| Firewall Rule ID | 
 **vpsv1_firewall_rules_store_request** | [**VPSV1FirewallRulesStoreRequest**](VPSV1FirewallRulesStoreRequest.md)|  | 

### Return type

[**VPSV1FirewallFirewallRuleResource**](VPSV1FirewallFirewallRuleResource.md)

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

