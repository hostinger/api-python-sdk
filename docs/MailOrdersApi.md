# hostinger_api.MailOrdersApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_order_plan_v1**](MailOrdersApi.md#get_order_plan_v1) | **GET** /api/mail/v1/orders/{orderId}/plan | Get order plan
[**list_orders_v1**](MailOrdersApi.md#list_orders_v1) | **GET** /api/mail/v1/orders | List orders


# **get_order_plan_v1**
> MailV1OrdersPlanResource get_order_plan_v1(order_id)

Get order plan

Retrieve the plan the given mail order was purchased with, including
domain-level and mailbox-level quotas, limits, and protocol
availability.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.mail_v1_orders_plan_resource import MailV1OrdersPlanResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.MailOrdersApi(api_client)
    order_id = 'OR1a2b3c4d5e6f7g' # str | Order resource ID

    try:
        # Get order plan
        api_response = api_instance.get_order_plan_v1(order_id)
        print("The response of MailOrdersApi->get_order_plan_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailOrdersApi->get_order_plan_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| Order resource ID | 

### Return type

[**MailV1OrdersPlanResource**](MailV1OrdersPlanResource.md)

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
**404** | Error response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_orders_v1**
> MailListOrdersV1200Response list_orders_v1(domain=domain, status=status, is_trial=is_trial, sort=sort, page=page, per_page=per_page)

List orders

Retrieve a paginated list of mail orders associated with your account.

Use this endpoint to monitor your mail services, including their status,
plan, attached domain, and expiration details.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.mail_list_orders_v1200_response import MailListOrdersV1200Response
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.MailOrdersApi(api_client)
    domain = 'example.com' # str | Filter orders by domain name (exact match) (optional)
    status = 'active' # str | Filter orders by status (optional)
    is_trial = false # bool | Filter orders by trial state (optional)
    sort = -created_at # str | Sort orders by field. Prefix with `-` for descending order. (optional) (default to -created_at)
    page = 1 # int | Page number (optional)
    per_page = 25 # int | Number of items per page (optional) (default to 25)

    try:
        # List orders
        api_response = api_instance.list_orders_v1(domain=domain, status=status, is_trial=is_trial, sort=sort, page=page, per_page=per_page)
        print("The response of MailOrdersApi->list_orders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailOrdersApi->list_orders_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Filter orders by domain name (exact match) | [optional] 
 **status** | **str**| Filter orders by status | [optional] 
 **is_trial** | **bool**| Filter orders by trial state | [optional] 
 **sort** | **str**| Sort orders by field. Prefix with &#x60;-&#x60; for descending order. | [optional] [default to -created_at]
 **page** | **int**| Page number | [optional] 
 **per_page** | **int**| Number of items per page | [optional] [default to 25]

### Return type

[**MailListOrdersV1200Response**](MailListOrdersV1200Response.md)

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
**422** | Error response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

