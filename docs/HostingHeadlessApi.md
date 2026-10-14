# hostinger_api.HostingHeadlessApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**submit_headless_build_report_v1**](HostingHeadlessApi.md#submit_headless_build_report_v1) | **POST** /api/hosting/v1/headless/agent-reports | Submit headless build report


# **submit_headless_build_report_v1**
> HostingV1HeadlessAgentReportResource submit_headless_build_report_v1(hosting_v1_headless_store_agent_report_request)

Submit headless build report

Submits the build report the headless skill writes at the end of a run (including early
stops), so Hostinger can learn where builds get stuck. Send one report per call, with the
report JSON as the request body, unchanged. Only send a report when the user agreed to it.

The report must match report.schema.json v1; an invalid report returns 422 and is not
stored. The report is linked to the authenticated account, so do not add account details
to it.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.hosting_v1_headless_agent_report_resource import HostingV1HeadlessAgentReportResource
from hostinger_api.models.hosting_v1_headless_store_agent_report_request import HostingV1HeadlessStoreAgentReportRequest
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.HostingHeadlessApi(api_client)
    hosting_v1_headless_store_agent_report_request = hostinger_api.HostingV1HeadlessStoreAgentReportRequest() # HostingV1HeadlessStoreAgentReportRequest | 

    try:
        # Submit headless build report
        api_response = api_instance.submit_headless_build_report_v1(hosting_v1_headless_store_agent_report_request)
        print("The response of HostingHeadlessApi->submit_headless_build_report_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingHeadlessApi->submit_headless_build_report_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hosting_v1_headless_store_agent_report_request** | [**HostingV1HeadlessStoreAgentReportRequest**](HostingV1HeadlessStoreAgentReportRequest.md)|  | 

### Return type

[**HostingV1HeadlessAgentReportResource**](HostingV1HeadlessAgentReportResource.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created response |  -  |
**422** | Validation error response |  -  |
**401** | Unauthenticated response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

