# hostinger_api.HostingCronJobsApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_account_cron_job_v1**](HostingCronJobsApi.md#create_account_cron_job_v1) | **POST** /api/hosting/v1/accounts/{username}/cron-jobs | Create account cron job
[**delete_account_cron_job_v1**](HostingCronJobsApi.md#delete_account_cron_job_v1) | **DELETE** /api/hosting/v1/accounts/{username}/cron-jobs/{uid} | Delete account cron job
[**get_cron_job_output_v1**](HostingCronJobsApi.md#get_cron_job_output_v1) | **GET** /api/hosting/v1/accounts/{username}/cron-jobs/{uid}/output | Get cron job output
[**list_account_cron_jobs_v1**](HostingCronJobsApi.md#list_account_cron_jobs_v1) | **GET** /api/hosting/v1/accounts/{username}/cron-jobs | List account cron jobs


# **create_account_cron_job_v1**
> HostingV1CronJobsCronJobResource create_account_cron_job_v1(username, hosting_v1_cron_jobs_create_cron_job_request)

Create account cron job

Creates a cron job for the specified account from a schedule expression and a command.

Returns the created cron job, including its uid, which is required to delete the cron job or fetch its output.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.hosting_v1_cron_jobs_create_cron_job_request import HostingV1CronJobsCreateCronJobRequest
from hostinger_api.models.hosting_v1_cron_jobs_cron_job_resource import HostingV1CronJobsCronJobResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.HostingCronJobsApi(api_client)
    username = 'u123456789' # str | 
    hosting_v1_cron_jobs_create_cron_job_request = hostinger_api.HostingV1CronJobsCreateCronJobRequest() # HostingV1CronJobsCreateCronJobRequest | 

    try:
        # Create account cron job
        api_response = api_instance.create_account_cron_job_v1(username, hosting_v1_cron_jobs_create_cron_job_request)
        print("The response of HostingCronJobsApi->create_account_cron_job_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingCronJobsApi->create_account_cron_job_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **hosting_v1_cron_jobs_create_cron_job_request** | [**HostingV1CronJobsCreateCronJobRequest**](HostingV1CronJobsCreateCronJobRequest.md)|  | 

### Return type

[**HostingV1CronJobsCronJobResource**](HostingV1CronJobsCronJobResource.md)

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

# **delete_account_cron_job_v1**
> CommonSuccessEmptyResource delete_account_cron_job_v1(username, uid)

Delete account cron job

Permanently deletes the cron job identified by its uid.

The uid is returned by the list cron jobs endpoint.

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
    api_instance = hostinger_api.HostingCronJobsApi(api_client)
    username = 'u123456789' # str | 
    uid = 'cron_abc123' # str | Unique identifier of the cron job as returned by the list cron jobs endpoint.

    try:
        # Delete account cron job
        api_response = api_instance.delete_account_cron_job_v1(username, uid)
        print("The response of HostingCronJobsApi->delete_account_cron_job_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingCronJobsApi->delete_account_cron_job_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **uid** | **str**| Unique identifier of the cron job as returned by the list cron jobs endpoint. | 

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

# **get_cron_job_output_v1**
> HostingV1CronJobsCronJobOutputResource get_cron_job_output_v1(username, uid)

Get cron job output

Returns the output captured from the last execution of the cron job identified by its uid.

The uid is returned by the list cron jobs endpoint.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.hosting_v1_cron_jobs_cron_job_output_resource import HostingV1CronJobsCronJobOutputResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.HostingCronJobsApi(api_client)
    username = 'u123456789' # str | 
    uid = 'cron_abc123' # str | Unique identifier of the cron job as returned by the list cron jobs endpoint.

    try:
        # Get cron job output
        api_response = api_instance.get_cron_job_output_v1(username, uid)
        print("The response of HostingCronJobsApi->get_cron_job_output_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingCronJobsApi->get_cron_job_output_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **uid** | **str**| Unique identifier of the cron job as returned by the list cron jobs endpoint. | 

### Return type

[**HostingV1CronJobsCronJobOutputResource**](HostingV1CronJobsCronJobOutputResource.md)

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

# **list_account_cron_jobs_v1**
> List[HostingV1CronJobsCronJobResource] list_account_cron_jobs_v1(username)

List account cron jobs

Returns the list of cron jobs configured for the specified account, including their schedule and command.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.hosting_v1_cron_jobs_cron_job_resource import HostingV1CronJobsCronJobResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.HostingCronJobsApi(api_client)
    username = 'u123456789' # str | 

    try:
        # List account cron jobs
        api_response = api_instance.list_account_cron_jobs_v1(username)
        print("The response of HostingCronJobsApi->list_account_cron_jobs_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingCronJobsApi->list_account_cron_jobs_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 

### Return type

[**List[HostingV1CronJobsCronJobResource]**](HostingV1CronJobsCronJobResource.md)

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

