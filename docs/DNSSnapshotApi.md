# hostinger_api.DNSSnapshotApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_dns_snapshot_list_v1**](DNSSnapshotApi.md#get_dns_snapshot_list_v1) | **GET** /api/dns/v1/snapshots/{domain} | Get DNS snapshot list
[**get_dns_snapshot_v1**](DNSSnapshotApi.md#get_dns_snapshot_v1) | **GET** /api/dns/v1/snapshots/{domain}/{snapshotId} | Get DNS snapshot
[**restore_dns_snapshot_v1**](DNSSnapshotApi.md#restore_dns_snapshot_v1) | **POST** /api/dns/v1/snapshots/{domain}/{snapshotId}/restore | Restore DNS snapshot


# **get_dns_snapshot_list_v1**
> List[DNSV1SnapshotSnapshotResource] get_dns_snapshot_list_v1(domain)

Get DNS snapshot list

Retrieve DNS snapshots for a domain.

Use this endpoint to view available DNS backup points for restoration.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.dnsv1_snapshot_snapshot_resource import DNSV1SnapshotSnapshotResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.DNSSnapshotApi(api_client)
    domain = 'mydomain.tld' # str | Domain name

    try:
        # Get DNS snapshot list
        api_response = api_instance.get_dns_snapshot_list_v1(domain)
        print("The response of DNSSnapshotApi->get_dns_snapshot_list_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DNSSnapshotApi->get_dns_snapshot_list_v1: %s\n" % e)
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
**401** | Unauthenticated response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dns_snapshot_v1**
> DNSV1SnapshotSnapshotWithContentResource get_dns_snapshot_v1(domain, snapshot_id)

Get DNS snapshot

Retrieve particular DNS snapshot with contents of DNS zone records.

Use this endpoint to view historical DNS configurations for domains.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.dnsv1_snapshot_snapshot_with_content_resource import DNSV1SnapshotSnapshotWithContentResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.DNSSnapshotApi(api_client)
    domain = 'mydomain.tld' # str | Domain name
    snapshot_id = 53513053 # int | Snapshot ID

    try:
        # Get DNS snapshot
        api_response = api_instance.get_dns_snapshot_v1(domain, snapshot_id)
        print("The response of DNSSnapshotApi->get_dns_snapshot_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DNSSnapshotApi->get_dns_snapshot_v1: %s\n" % e)
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
**401** | Unauthenticated response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_dns_snapshot_v1**
> CommonSuccessEmptyResource restore_dns_snapshot_v1(domain, snapshot_id)

Restore DNS snapshot

Restore DNS zone to the selected snapshot.

Use this endpoint to revert domain DNS to a previous configuration.

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
    api_instance = hostinger_api.DNSSnapshotApi(api_client)
    domain = 'mydomain.tld' # str | Domain name
    snapshot_id = 53513053 # int | Snapshot ID

    try:
        # Restore DNS snapshot
        api_response = api_instance.restore_dns_snapshot_v1(domain, snapshot_id)
        print("The response of DNSSnapshotApi->restore_dns_snapshot_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DNSSnapshotApi->restore_dns_snapshot_v1: %s\n" % e)
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
**401** | Unauthenticated response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

