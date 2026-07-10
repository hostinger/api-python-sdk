# hostinger_api.AgencyHostingDatacentersApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_available_datacenters_for_an_agency_plan_order_v1**](AgencyHostingDatacentersApi.md#list_available_datacenters_for_an_agency_plan_order_v1) | **GET** /api/agency-hosting/v1/orders/{order_id}/datacenters | List available datacenters for an Agency Plan order


# **list_available_datacenters_for_an_agency_plan_order_v1**
> List[AgencyHostingV1DatacentersDatacenterResource] list_available_datacenters_for_an_agency_plan_order_v1(order_id)

List available datacenters for an Agency Plan order

Lists the datacenters available for provisioning a new website on the given Agency Plan
hosting order.

Each datacenter includes a `pinger_url` you can ping from the client to measure round-trip
latency; comparing the results across datacenters lets you pick the nearest one (lowest
ping) before choosing its `code` as the `datacenter_code` when creating a website setup.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.agency_hosting_v1_datacenters_datacenter_resource import AgencyHostingV1DatacentersDatacenterResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.AgencyHostingDatacentersApi(api_client)
    order_id = 123456 # int | Agency Plan order ID

    try:
        # List available datacenters for an Agency Plan order
        api_response = api_instance.list_available_datacenters_for_an_agency_plan_order_v1(order_id)
        print("The response of AgencyHostingDatacentersApi->list_available_datacenters_for_an_agency_plan_order_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgencyHostingDatacentersApi->list_available_datacenters_for_an_agency_plan_order_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **int**| Agency Plan order ID | 

### Return type

[**List[AgencyHostingV1DatacentersDatacenterResource]**](AgencyHostingV1DatacentersDatacenterResource.md)

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

