# hostinger-api.DNSSnapshotApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_snapshot_list_v1**](DNSSnapshotApi.md#get_snapshot_list_v1) | **GET** /api/dns/v1/snapshots/{domain} | Get snapshot list
[**get_snapshot_v1**](DNSSnapshotApi.md#get_snapshot_v1) | **GET** /api/dns/v1/snapshots/{domain}/{snapshotId} | Get snapshot
[**restore_snapshot_v1**](DNSSnapshotApi.md#restore_snapshot_v1) | **POST** /api/dns/v1/snapshots/{domain}/{snapshotId} | Restore snapshot


# **get_snapshot_list_v1**
> List[DNSV1SnapshotSnapshotResource] get_snapshot_list_v1(domain)

Get snapshot list

This endpoint retrieves list of DNS snapshots.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger-api
from hostinger-api.models.dnsv1_snapshot_snapshot_resource import DNSV1SnapshotSnapshotResource
from hostinger-api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger-api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger-api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger-api.DNSSnapshotApi(api_client)
    domain = 'mydomain.tld' # str | Domain name

    try:
        # Get snapshot list
        api_response = api_instance.get_snapshot_list_v1(domain)
        print("The response of DNSSnapshotApi->get_snapshot_list_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DNSSnapshotApi->get_snapshot_list_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Domain name | 

### Return type

[**List[DNSV1SnapshotSnapshotResource]**](DNSV1SnapshotSnapshotResource.md)

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

# **get_snapshot_v1**
> DNSV1SnapshotSnapshotWithContentResource get_snapshot_v1(domain, snapshot_id)

Get snapshot

This endpoint retrieves particular DNS snapshot with the contents of DNS zone records.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger-api
from hostinger-api.models.dnsv1_snapshot_snapshot_with_content_resource import DNSV1SnapshotSnapshotWithContentResource
from hostinger-api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger-api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger-api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger-api.DNSSnapshotApi(api_client)
    domain = 'mydomain.tld' # str | Domain name
    snapshot_id = 53513053 # int | Snapshot ID

    try:
        # Get snapshot
        api_response = api_instance.get_snapshot_v1(domain, snapshot_id)
        print("The response of DNSSnapshotApi->get_snapshot_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DNSSnapshotApi->get_snapshot_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Domain name | 
 **snapshot_id** | **int**| Snapshot ID | 

### Return type

[**DNSV1SnapshotSnapshotWithContentResource**](DNSV1SnapshotSnapshotWithContentResource.md)

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

# **restore_snapshot_v1**
> CommonSuccessEmptyResource restore_snapshot_v1(domain, snapshot_id)

Restore snapshot

This endpoint restores DNS zone to the selected snapshot.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger-api
from hostinger-api.models.common_success_empty_resource import CommonSuccessEmptyResource
from hostinger-api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger-api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger-api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger-api.DNSSnapshotApi(api_client)
    domain = 'mydomain.tld' # str | Domain name
    snapshot_id = 53513053 # int | Snapshot ID

    try:
        # Restore snapshot
        api_response = api_instance.restore_snapshot_v1(domain, snapshot_id)
        print("The response of DNSSnapshotApi->restore_snapshot_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DNSSnapshotApi->restore_snapshot_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Domain name | 
 **snapshot_id** | **int**| Snapshot ID | 

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
**200** | Success response |  -  |
**401** | Unauthenticated |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

