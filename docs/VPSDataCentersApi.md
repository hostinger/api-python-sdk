# hostinger-api.VPSDataCentersApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_data_centers_list_v1**](VPSDataCentersApi.md#get_data_centers_list_v1) | **GET** /api/vps/v1/data-centers | Get data centers list


# **get_data_centers_list_v1**
> List[VPSV1DataCenterDataCenterResource] get_data_centers_list_v1()

Get data centers list

This endpoint retrieves a list of all data centers available.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger-api
from hostinger-api.models.vpsv1_data_center_data_center_resource import VPSV1DataCenterDataCenterResource
from hostinger-api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://developers.hostinger.com
# See configuration.py for a list of all supported configuration parameters.
configuration = hostinger-api.Configuration(
    host = "https://developers.hostinger.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: apiToken
configuration = hostinger-api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger-api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger-api.VPSDataCentersApi(api_client)

    try:
        # Get data centers list
        api_response = api_instance.get_data_centers_list_v1()
        print("The response of VPSDataCentersApi->get_data_centers_list_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPSDataCentersApi->get_data_centers_list_v1: %s\n" % e)
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
**401** | Unauthenticated |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

