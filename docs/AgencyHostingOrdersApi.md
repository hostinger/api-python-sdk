# hostinger_api.AgencyHostingOrdersApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_agency_plan_orders_v1**](AgencyHostingOrdersApi.md#list_agency_plan_orders_v1) | **GET** /api/agency-hosting/v1/orders | List Agency Plan orders


# **list_agency_plan_orders_v1**
> AgencyHostingListAgencyPlanOrdersV1200Response list_agency_plan_orders_v1(page=page, per_page=per_page)

List Agency Plan orders

Returns a paginated list of Agency Plan orders accessible to the authenticated client.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.agency_hosting_list_agency_plan_orders_v1200_response import AgencyHostingListAgencyPlanOrdersV1200Response
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.AgencyHostingOrdersApi(api_client)
    page = 1 # int | Page number (optional)
    per_page = 25 # int | Number of items per page (optional) (default to 25)

    try:
        # List Agency Plan orders
        api_response = api_instance.list_agency_plan_orders_v1(page=page, per_page=per_page)
        print("The response of AgencyHostingOrdersApi->list_agency_plan_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgencyHostingOrdersApi->list_agency_plan_orders_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number | [optional] 
 **per_page** | **int**| Number of items per page | [optional] [default to 25]

### Return type

[**AgencyHostingListAgencyPlanOrdersV1200Response**](AgencyHostingListAgencyPlanOrdersV1200Response.md)

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

