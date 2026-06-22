# hostinger_api.DomainAccessVerifierVerificationsApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_domain_verifications_direct**](DomainAccessVerifierVerificationsApi.md#get_domain_verifications_direct) | **GET** /api/v2/direct/verifications/active | Get domain verifications


# **get_domain_verifications_direct**
> DomainAccessVerifierV2VerificationsActiveVerificationsCollection get_domain_verifications_direct(domain_access_verifier_v2_verifications_list_request)

Get domain verifications

Retrieve a list of pending and completed domain verifications.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.domain_access_verifier_v2_verifications_active_verifications_collection import DomainAccessVerifierV2VerificationsActiveVerificationsCollection
from hostinger_api.models.domain_access_verifier_v2_verifications_list_request import DomainAccessVerifierV2VerificationsListRequest
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.DomainAccessVerifierVerificationsApi(api_client)
    domain_access_verifier_v2_verifications_list_request = hostinger_api.DomainAccessVerifierV2VerificationsListRequest() # DomainAccessVerifierV2VerificationsListRequest | 

    try:
        # Get domain verifications
        api_response = api_instance.get_domain_verifications_direct(domain_access_verifier_v2_verifications_list_request)
        print("The response of DomainAccessVerifierVerificationsApi->get_domain_verifications_direct:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainAccessVerifierVerificationsApi->get_domain_verifications_direct: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_access_verifier_v2_verifications_list_request** | [**DomainAccessVerifierV2VerificationsListRequest**](DomainAccessVerifierV2VerificationsListRequest.md)|  | 

### Return type

[**DomainAccessVerifierV2VerificationsActiveVerificationsCollection**](DomainAccessVerifierV2VerificationsActiveVerificationsCollection.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success response |  -  |
**401** | Unauthenticated response |  -  |
**422** | Validation error response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

