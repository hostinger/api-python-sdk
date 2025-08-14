# hostinger_api.BillingPaymentMethodsApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_payment_method_v1**](BillingPaymentMethodsApi.md#delete_payment_method_v1) | **DELETE** /api/billing/v1/payment-methods/{paymentMethodId} | Delete payment method
[**get_payment_method_list_v1**](BillingPaymentMethodsApi.md#get_payment_method_list_v1) | **GET** /api/billing/v1/payment-methods | Get payment method list
[**set_default_payment_method_v1**](BillingPaymentMethodsApi.md#set_default_payment_method_v1) | **POST** /api/billing/v1/payment-methods/{paymentMethodId} | Set default payment method


# **delete_payment_method_v1**
> CommonSuccessEmptyResource delete_payment_method_v1(payment_method_id)

Delete payment method

Delete a payment method from your account.

Use this endpoint to remove unused payment methods from user accounts.

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
    api_instance = hostinger_api.BillingPaymentMethodsApi(api_client)
    payment_method_id = 9693613 # int | Payment method ID

    try:
        # Delete payment method
        api_response = api_instance.delete_payment_method_v1(payment_method_id)
        print("The response of BillingPaymentMethodsApi->delete_payment_method_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingPaymentMethodsApi->delete_payment_method_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_method_id** | **int**| Payment method ID | 

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

# **get_payment_method_list_v1**
> List[BillingV1PaymentMethodPaymentMethodResource] get_payment_method_list_v1()

Get payment method list

Retrieve available payment methods that can be used for placing new orders.

If you want to add new payment method, please use [hPanel](https://hpanel.hostinger.com/billing/payment-methods).

Use this endpoint to view available payment options before creating orders.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.billing_v1_payment_method_payment_method_resource import BillingV1PaymentMethodPaymentMethodResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.BillingPaymentMethodsApi(api_client)

    try:
        # Get payment method list
        api_response = api_instance.get_payment_method_list_v1()
        print("The response of BillingPaymentMethodsApi->get_payment_method_list_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingPaymentMethodsApi->get_payment_method_list_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[BillingV1PaymentMethodPaymentMethodResource]**](BillingV1PaymentMethodPaymentMethodResource.md)

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

# **set_default_payment_method_v1**
> CommonSuccessEmptyResource set_default_payment_method_v1(payment_method_id)

Set default payment method

Set the default payment method for your account.

Use this endpoint to configure the primary payment method for future orders.

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
    api_instance = hostinger_api.BillingPaymentMethodsApi(api_client)
    payment_method_id = 9693613 # int | Payment method ID

    try:
        # Set default payment method
        api_response = api_instance.set_default_payment_method_v1(payment_method_id)
        print("The response of BillingPaymentMethodsApi->set_default_payment_method_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingPaymentMethodsApi->set_default_payment_method_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_method_id** | **int**| Payment method ID | 

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

