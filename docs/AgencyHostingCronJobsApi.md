# hostinger_api.AgencyHostingCronJobsApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_agency_plan_website_cron_job_v1**](AgencyHostingCronJobsApi.md#create_agency_plan_website_cron_job_v1) | **POST** /api/agency-hosting/v1/websites/{website_uid}/cron-jobs | Create Agency Plan website cron job
[**delete_agency_plan_website_cron_job_v1**](AgencyHostingCronJobsApi.md#delete_agency_plan_website_cron_job_v1) | **DELETE** /api/agency-hosting/v1/websites/{website_uid}/cron-jobs/{uuid} | Delete Agency Plan website cron job
[**list_agency_plan_website_cron_jobs_v1**](AgencyHostingCronJobsApi.md#list_agency_plan_website_cron_jobs_v1) | **GET** /api/agency-hosting/v1/websites/{website_uid}/cron-jobs | List Agency Plan website cron jobs


# **create_agency_plan_website_cron_job_v1**
> AgencyHostingV1WebsitesCronJobsCronJobResource create_agency_plan_website_cron_job_v1(website_uid, agency_hosting_v1_websites_cron_jobs_create_cron_job_request)

Create Agency Plan website cron job

Creates a cron job for an Agency Plan website from a schedule expression and a command.

Returns the created cron job, including its uuid, which is required to delete the cron job.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.agency_hosting_v1_websites_cron_jobs_create_cron_job_request import AgencyHostingV1WebsitesCronJobsCreateCronJobRequest
from hostinger_api.models.agency_hosting_v1_websites_cron_jobs_cron_job_resource import AgencyHostingV1WebsitesCronJobsCronJobResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.AgencyHostingCronJobsApi(api_client)
    website_uid = 'zpwlGlp19' # str | Agency Plan website UID
    agency_hosting_v1_websites_cron_jobs_create_cron_job_request = hostinger_api.AgencyHostingV1WebsitesCronJobsCreateCronJobRequest() # AgencyHostingV1WebsitesCronJobsCreateCronJobRequest | 

    try:
        # Create Agency Plan website cron job
        api_response = api_instance.create_agency_plan_website_cron_job_v1(website_uid, agency_hosting_v1_websites_cron_jobs_create_cron_job_request)
        print("The response of AgencyHostingCronJobsApi->create_agency_plan_website_cron_job_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgencyHostingCronJobsApi->create_agency_plan_website_cron_job_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website_uid** | **str**| Agency Plan website UID | 
 **agency_hosting_v1_websites_cron_jobs_create_cron_job_request** | [**AgencyHostingV1WebsitesCronJobsCreateCronJobRequest**](AgencyHostingV1WebsitesCronJobsCreateCronJobRequest.md)|  | 

### Return type

[**AgencyHostingV1WebsitesCronJobsCronJobResource**](AgencyHostingV1WebsitesCronJobsCronJobResource.md)

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

# **delete_agency_plan_website_cron_job_v1**
> CommonSuccessEmptyResource delete_agency_plan_website_cron_job_v1(website_uid, uuid)

Delete Agency Plan website cron job

Permanently deletes the cron job identified by its uuid from an Agency Plan website.

The operation is idempotent: deleting a cron job that does not exist succeeds without error.

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
    api_instance = hostinger_api.AgencyHostingCronJobsApi(api_client)
    website_uid = 'zpwlGlp19' # str | Agency Plan website UID
    uuid = '01931d6f-68f5-7b72-8d9e-09c6e1e6aa0e' # str | Unique identifier of the cron job as returned by the list cron jobs endpoint.

    try:
        # Delete Agency Plan website cron job
        api_response = api_instance.delete_agency_plan_website_cron_job_v1(website_uid, uuid)
        print("The response of AgencyHostingCronJobsApi->delete_agency_plan_website_cron_job_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgencyHostingCronJobsApi->delete_agency_plan_website_cron_job_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website_uid** | **str**| Agency Plan website UID | 
 **uuid** | **str**| Unique identifier of the cron job as returned by the list cron jobs endpoint. | 

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

# **list_agency_plan_website_cron_jobs_v1**
> AgencyHostingListAgencyPlanWebsiteCronJobsV1200Response list_agency_plan_website_cron_jobs_v1(website_uid, page=page, per_page=per_page)

List Agency Plan website cron jobs

Returns a paginated list of cron jobs configured for an Agency Plan website.

Each entry includes the schedule expression and the command executed on that schedule.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.agency_hosting_list_agency_plan_website_cron_jobs_v1200_response import AgencyHostingListAgencyPlanWebsiteCronJobsV1200Response
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.AgencyHostingCronJobsApi(api_client)
    website_uid = 'zpwlGlp19' # str | Agency Plan website UID
    page = 1 # int | Page number (optional)
    per_page = 25 # int | Number of items per page (optional) (default to 25)

    try:
        # List Agency Plan website cron jobs
        api_response = api_instance.list_agency_plan_website_cron_jobs_v1(website_uid, page=page, per_page=per_page)
        print("The response of AgencyHostingCronJobsApi->list_agency_plan_website_cron_jobs_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgencyHostingCronJobsApi->list_agency_plan_website_cron_jobs_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website_uid** | **str**| Agency Plan website UID | 
 **page** | **int**| Page number | [optional] 
 **per_page** | **int**| Number of items per page | [optional] [default to 25]

### Return type

[**AgencyHostingListAgencyPlanWebsiteCronJobsV1200Response**](AgencyHostingListAgencyPlanWebsiteCronJobsV1200Response.md)

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

