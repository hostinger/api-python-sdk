# hostinger_api.MailWebhooksApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_webhook_v1**](MailWebhooksApi.md#create_webhook_v1) | **POST** /api/mail/v1/mailboxes/{mailboxId}/webhooks | Create webhook


# **create_webhook_v1**
> MailV1WebhooksWebhookResource create_webhook_v1(mailbox_id, mail_v1_schema_create_webhook_request_schema)

Create webhook

Create a webhook for the given mailbox. The generated secret is
returned only in this response and is sent as a bearer token with
every delivery.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.mail_v1_schema_create_webhook_request_schema import MailV1SchemaCreateWebhookRequestSchema
from hostinger_api.models.mail_v1_webhooks_webhook_resource import MailV1WebhooksWebhookResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.MailWebhooksApi(api_client)
    mailbox_id = 'AC1a2b3c4d5e6f7g' # str | Mailbox resource ID
    mail_v1_schema_create_webhook_request_schema = hostinger_api.MailV1SchemaCreateWebhookRequestSchema() # MailV1SchemaCreateWebhookRequestSchema | 

    try:
        # Create webhook
        api_response = api_instance.create_webhook_v1(mailbox_id, mail_v1_schema_create_webhook_request_schema)
        print("The response of MailWebhooksApi->create_webhook_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailWebhooksApi->create_webhook_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mailbox_id** | **str**| Mailbox resource ID | 
 **mail_v1_schema_create_webhook_request_schema** | [**MailV1SchemaCreateWebhookRequestSchema**](MailV1SchemaCreateWebhookRequestSchema.md)|  | 

### Return type

[**MailV1WebhooksWebhookResource**](MailV1WebhooksWebhookResource.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created response |  -  |
**401** | Unauthenticated response |  -  |
**400** | Error response |  -  |
**404** | Error response |  -  |
**409** | Error response |  -  |
**422** | Error response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

