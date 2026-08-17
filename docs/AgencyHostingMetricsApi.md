# hostinger_api.AgencyHostingMetricsApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_agency_plan_order_disk_usage_metrics_v1**](AgencyHostingMetricsApi.md#list_agency_plan_order_disk_usage_metrics_v1) | **GET** /api/agency-hosting/v1/orders/{order_id}/disk-usage-metrics | List Agency Plan order disk usage metrics
[**list_order_resource_usage_metrics_v1**](AgencyHostingMetricsApi.md#list_order_resource_usage_metrics_v1) | **GET** /api/agency-hosting/v1/orders/{order_id}/resource-usage-metrics | List order resource usage metrics


# **list_agency_plan_order_disk_usage_metrics_v1**
> AgencyHostingV1OrdersDiskUsageMetricsMetricsResource list_agency_plan_order_disk_usage_metrics_v1(order_id, time_frame_days=time_frame_days)

List Agency Plan order disk usage metrics

Returns aggregated disk and inode usage for the Agency Plan order over the
selected time frame, plus the plan quotas. Figures cover the whole order
account. Values may be up to one hour stale. CPU, memory, and process usage
are on the resource-usage-metrics endpoint.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.agency_hosting_v1_orders_disk_usage_metrics_metrics_resource import AgencyHostingV1OrdersDiskUsageMetricsMetricsResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.AgencyHostingMetricsApi(api_client)
    order_id = 123456 # int | Agency Plan order ID
    time_frame_days = 1 # int | Length of the window in days, ending now. Bucket size grows with the window. (optional) (default to 1)

    try:
        # List Agency Plan order disk usage metrics
        api_response = api_instance.list_agency_plan_order_disk_usage_metrics_v1(order_id, time_frame_days=time_frame_days)
        print("The response of AgencyHostingMetricsApi->list_agency_plan_order_disk_usage_metrics_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgencyHostingMetricsApi->list_agency_plan_order_disk_usage_metrics_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **int**| Agency Plan order ID | 
 **time_frame_days** | **int**| Length of the window in days, ending now. Bucket size grows with the window. | [optional] [default to 1]

### Return type

[**AgencyHostingV1OrdersDiskUsageMetricsMetricsResource**](AgencyHostingV1OrdersDiskUsageMetricsMetricsResource.md)

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
**401** | Unauthenticated response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_order_resource_usage_metrics_v1**
> AgencyHostingV1OrdersResourceUsageMetricsMetricsResource list_order_resource_usage_metrics_v1(order_id, time_frame_hours=time_frame_hours)

List order resource usage metrics

Returns aggregated CPU, memory, and process usage for the Agency Plan order
over the selected time frame, plus the plan quotas and a per-website
breakdown. Each website is identified by uid. Suspended and deleted websites
are excluded from both the order totals and the per-website breakdown.
Values may be up to one hour stale. Disk and inode usage are on the
disk-usage-metrics endpoint.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.agency_hosting_v1_orders_resource_usage_metrics_metrics_resource import AgencyHostingV1OrdersResourceUsageMetricsMetricsResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.AgencyHostingMetricsApi(api_client)
    order_id = 123456 # int | Agency Plan order ID
    time_frame_hours = 24 # int | Length of the window in hours, ending now. Bucket size grows with the window. (optional) (default to 24)

    try:
        # List order resource usage metrics
        api_response = api_instance.list_order_resource_usage_metrics_v1(order_id, time_frame_hours=time_frame_hours)
        print("The response of AgencyHostingMetricsApi->list_order_resource_usage_metrics_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgencyHostingMetricsApi->list_order_resource_usage_metrics_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **int**| Agency Plan order ID | 
 **time_frame_hours** | **int**| Length of the window in hours, ending now. Bucket size grows with the window. | [optional] [default to 24]

### Return type

[**AgencyHostingV1OrdersResourceUsageMetricsMetricsResource**](AgencyHostingV1OrdersResourceUsageMetricsMetricsResource.md)

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
**401** | Unauthenticated response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

