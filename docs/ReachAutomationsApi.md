# hostinger_api.ReachAutomationsApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_automation_details_v1**](ReachAutomationsApi.md#get_automation_details_v1) | **GET** /api/reach/v1/profiles/{profileUuid}/automations/{automationUuid} | Get automation details
[**list_automation_steps_v1**](ReachAutomationsApi.md#list_automation_steps_v1) | **GET** /api/reach/v1/profiles/{profileUuid}/automations/{automationUuid}/steps | List automation steps
[**list_automations_v1**](ReachAutomationsApi.md#list_automations_v1) | **GET** /api/reach/v1/profiles/{profileUuid}/automations | List automations


# **get_automation_details_v1**
> ReachV1AutomationsAutomationResource get_automation_details_v1(profile_uuid, automation_uuid)

Get automation details

Get a single automation with the counts of contacts that entered it, are moving through it,
finished it or failed on the way.

This describes the automation itself. To see the workflow it runs, use the steps endpoint.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.reach_v1_automations_automation_resource import ReachV1AutomationsAutomationResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.ReachAutomationsApi(api_client)
    profile_uuid = '550e8400-e09b-41d4-a716-400055000000' # str | Profile uuid parameter
    automation_uuid = '550e8400-e09b-41d4-a716-400055000000' # str | Automation uuid parameter

    try:
        # Get automation details
        api_response = api_instance.get_automation_details_v1(profile_uuid, automation_uuid)
        print("The response of ReachAutomationsApi->get_automation_details_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReachAutomationsApi->get_automation_details_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_uuid** | **str**| Profile uuid parameter | 
 **automation_uuid** | **str**| Automation uuid parameter | 

### Return type

[**ReachV1AutomationsAutomationResource**](ReachV1AutomationsAutomationResource.md)

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

# **list_automation_steps_v1**
> List[ReachV1AutomationsStepsAutomationStepResource] list_automation_steps_v1(profile_uuid, automation_uuid)

List automation steps

Get the workflow of an automation as a flat list of steps.

The steps form a tree rather than a straight line: follow `parent_uuid` to reconstruct the
branches, and use `step_order` to order the steps that share a parent. An automation with no
steps yet returns an empty list.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.reach_v1_automations_steps_automation_step_resource import ReachV1AutomationsStepsAutomationStepResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.ReachAutomationsApi(api_client)
    profile_uuid = '550e8400-e09b-41d4-a716-400055000000' # str | Profile uuid parameter
    automation_uuid = '550e8400-e09b-41d4-a716-400055000000' # str | Automation uuid parameter

    try:
        # List automation steps
        api_response = api_instance.list_automation_steps_v1(profile_uuid, automation_uuid)
        print("The response of ReachAutomationsApi->list_automation_steps_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReachAutomationsApi->list_automation_steps_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_uuid** | **str**| Profile uuid parameter | 
 **automation_uuid** | **str**| Automation uuid parameter | 

### Return type

[**List[ReachV1AutomationsStepsAutomationStepResource]**](ReachV1AutomationsStepsAutomationStepResource.md)

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

# **list_automations_v1**
> ReachListAutomationsV1200Response list_automations_v1(profile_uuid, status=status, sort_direction=sort_direction, page=page, per_page=per_page)

List automations

Get a paginated list of the automations in a profile.

Every automation comes with the counts of contacts that entered it, are moving through it,
finished it or failed on the way. Those counts describe the contact journey and are not
email engagement metrics - for opens, clicks and unsubscribes use the campaign statistics
endpoint instead.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.reach_list_automations_v1200_response import ReachListAutomationsV1200Response
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.ReachAutomationsApi(api_client)
    profile_uuid = '550e8400-e09b-41d4-a716-400055000000' # str | Profile uuid parameter
    status = 'active' # str | Filter automations by status.  There is no `completed` status. An automation that has finished for every contact still reports `active`. (optional)
    sort_direction = 'desc' # str | Order automations by creation date. Newest first unless set to `asc`. (optional)
    page = 1 # int | Page number (optional)
    per_page = 25 # int | Number of items per page (optional) (default to 25)

    try:
        # List automations
        api_response = api_instance.list_automations_v1(profile_uuid, status=status, sort_direction=sort_direction, page=page, per_page=per_page)
        print("The response of ReachAutomationsApi->list_automations_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReachAutomationsApi->list_automations_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_uuid** | **str**| Profile uuid parameter | 
 **status** | **str**| Filter automations by status.  There is no &#x60;completed&#x60; status. An automation that has finished for every contact still reports &#x60;active&#x60;. | [optional] 
 **sort_direction** | **str**| Order automations by creation date. Newest first unless set to &#x60;asc&#x60;. | [optional] 
 **page** | **int**| Page number | [optional] 
 **per_page** | **int**| Number of items per page | [optional] [default to 25]

### Return type

[**ReachListAutomationsV1200Response**](ReachListAutomationsV1200Response.md)

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

