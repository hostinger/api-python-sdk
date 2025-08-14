# hostinger_api.VPSDataCentersApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_data_center_list_v1**](VPSDataCentersApi.md#get_data_center_list_v1) | **GET** /api/vps/v1/data-centers | Get data center list


# **get_data_center_list_v1**
> List[VPSV1DataCenterDataCenterResource] get_data_center_list_v1()

Get data center list

Retrieve all available data centers.

Use this endpoint to view location options before deploying VPS instances.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.vpsv1_data_center_data_center_resource import VPSV1DataCenterDataCenterResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.VPSDataCentersApi(api_client)

    try:
        # Get data center list
        api_response = api_instance.get_data_center_list_v1()
        print("The response of VPSDataCentersApi->get_data_center_list_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPSDataCentersApi->get_data_center_list_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[VPSV1DataCenterDataCenterResource]**](VPSV1DataCenterDataCenterResource.md)

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

