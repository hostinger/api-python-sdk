# hostinger_api.AgentReadinessChecksApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_checks_v1**](AgentReadinessChecksApi.md#list_checks_v1) | **GET** /api/agent-readiness/v1/checks | List checks


# **list_checks_v1**
> List[AgentReadinessV1ChecksCheckResource] list_checks_v1()

List checks

List every check an agent readiness scan runs, with its name, category and weight.\n
Use it to show the human-readable name of each `check_id` in a scan's results.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.agent_readiness_v1_checks_check_resource import AgentReadinessV1ChecksCheckResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.AgentReadinessChecksApi(api_client)

    try:
        # List checks
        api_response = api_instance.list_checks_v1()
        print("The response of AgentReadinessChecksApi->list_checks_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentReadinessChecksApi->list_checks_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[AgentReadinessV1ChecksCheckResource]**](AgentReadinessV1ChecksCheckResource.md)

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

