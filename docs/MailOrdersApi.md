# hostinger_api.MailOrdersApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_mail_order_list_v1**](MailOrdersApi.md#get_mail_order_list_v1) | **GET** /api/mail/v1/orders | Get mail order list


# **get_mail_order_list_v1**
> MailGetMailOrderListV1200Response get_mail_order_list_v1(domain=domain, status=status, is_trial=is_trial, sort=sort, page=page, per_page=per_page)

Get mail order list

Retrieve a paginated list of mail orders associated with your account.

Use this endpoint to monitor your mail services, including their status,
plan, attached domain, and expiration details.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.mail_get_mail_order_list_v1200_response import MailGetMailOrderListV1200Response
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
        # Get mail order list
        api_response = api_instance.get_mail_order_list_v1(domain=domain, status=status, is_trial=is_trial, sort=sort, page=page, per_page=per_page)
        print("The response of MailOrdersApi->get_mail_order_list_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailOrdersApi->get_mail_order_list_v1: %s\n" % e)
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

[**MailGetMailOrderListV1200Response**](MailGetMailOrderListV1200Response.md)

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

