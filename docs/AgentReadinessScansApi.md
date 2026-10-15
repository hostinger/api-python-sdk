# hostinger_api.AgentReadinessScansApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_website_scan_v1**](AgentReadinessScansApi.md#get_website_scan_v1) | **GET** /api/agent-readiness/v1/scans/{domain} | Get website scan
[**run_website_scan_v1**](AgentReadinessScansApi.md#run_website_scan_v1) | **POST** /api/agent-readiness/v1/scans | Run website scan


# **get_website_scan_v1**
> AgentReadinessV1ScansScanResource get_website_scan_v1(domain)

Get website scan

Get the latest agent readiness scan of a website.\n
Scans started with the `Run website scan` operation are asynchronous. While the status is `pending`,
the result fields are null; wait a few seconds and call this operation again until the status is
`completed` or `failed`. A `failed` scan is not retried; run the scan again.\n
A completed scan has a 0-100 score, a letter grade, a score per category, and the result of every
check with the evidence found and how to fix it. Check names are listed by the `List checks` operation.\n
Returns 404 when the domain has never been scanned; use the `Run website scan` operation first.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.agent_readiness_v1_scans_scan_resource import AgentReadinessV1ScansScanResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.AgentReadinessScansApi(api_client)
    domain = 'example.com' # str | Domain name the scan was run for

    try:
        # Get website scan
        api_response = api_instance.get_website_scan_v1(domain)
        print("The response of AgentReadinessScansApi->get_website_scan_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentReadinessScansApi->get_website_scan_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Domain name the scan was run for | 

### Return type

[**AgentReadinessV1ScansScanResource**](AgentReadinessV1ScansScanResource.md)

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

# **run_website_scan_v1**
> AgentReadinessV1ScansScanResource run_website_scan_v1(agent_readiness_v1_scans_run_scan_request)

Run website scan

Start a scan of how ready a public website is for AI agents to discover, read and act on.\n
Scanning is asynchronous: this operation only starts the scan, and the returned scan is usually `pending`
with no results yet. To get the results, poll the `Get website scan` operation with the same domain every
few seconds until its status is `completed` or `failed`. The scan itself is limited to 60 seconds,
plus any time it waits in the queue. A `failed` scan is not retried; run this operation again.\n
Starting a scan for a domain that already has a pending scan from the last 5 minutes
returns that scan instead of starting a new one.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.agent_readiness_v1_scans_run_scan_request import AgentReadinessV1ScansRunScanRequest
from hostinger_api.models.agent_readiness_v1_scans_scan_resource import AgentReadinessV1ScansScanResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.AgentReadinessScansApi(api_client)
    agent_readiness_v1_scans_run_scan_request = hostinger_api.AgentReadinessV1ScansRunScanRequest() # AgentReadinessV1ScansRunScanRequest | 

    try:
        # Run website scan
        api_response = api_instance.run_website_scan_v1(agent_readiness_v1_scans_run_scan_request)
        print("The response of AgentReadinessScansApi->run_website_scan_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentReadinessScansApi->run_website_scan_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_readiness_v1_scans_run_scan_request** | [**AgentReadinessV1ScansRunScanRequest**](AgentReadinessV1ScansRunScanRequest.md)|  | 

### Return type

[**AgentReadinessV1ScansScanResource**](AgentReadinessV1ScansScanResource.md)

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

