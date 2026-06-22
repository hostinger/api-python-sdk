# hostinger_api.HostingDatacentersApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_available_datacenters_v1**](HostingDatacentersApi.md#list_available_datacenters_v1) | **GET** /api/hosting/v1/datacenters | List available datacenters


# **list_available_datacenters_v1**
> List[HostingV1DatacenterDatacenterResource] list_available_datacenters_v1(order_id)

List available datacenters

Retrieve a list of datacenters available for setting up hosting plans
based on available datacenter capacity and hosting plan of your order.
The first item in the list is the best match for your specific order
requirements.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.hosting_v1_datacenter_datacenter_resource import HostingV1DatacenterDatacenterResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.HostingDatacentersApi(api_client)
    order_id = 123 # int | Order ID

    try:
        # List available datacenters
        api_response = api_instance.list_available_datacenters_v1(order_id)
        print("The response of HostingDatacentersApi->list_available_datacenters_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingDatacentersApi->list_available_datacenters_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **int**| Order ID | 

### Return type

[**List[HostingV1DatacenterDatacenterResource]**](HostingV1DatacenterDatacenterResource.md)

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

