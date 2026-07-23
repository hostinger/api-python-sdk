# MailListAccessLogsV1200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[MailV1LogsAccessAccessLogResource]**](MailV1LogsAccessAccessLogResource.md) | Array of [&#x60;Mail.V1.Logs.Access.AccessLogResource&#x60;](#model/mailv1logsaccessaccesslogresource) | [optional] 
**meta** | [**CommonSchemaPaginationMetaSchema**](CommonSchemaPaginationMetaSchema.md) |  | [optional] 

## Example

```python
from hostinger_api.models.mail_list_access_logs_v1200_response import MailListAccessLogsV1200Response

# TODO update the JSON string below
json = "{}"
# create an instance of MailListAccessLogsV1200Response from a JSON string
mail_list_access_logs_v1200_response_instance = MailListAccessLogsV1200Response.from_json(json)
# print the JSON string representation of the object
print(MailListAccessLogsV1200Response.to_json())

# convert the object into a dict
mail_list_access_logs_v1200_response_dict = mail_list_access_logs_v1200_response_instance.to_dict()
# create an instance of MailListAccessLogsV1200Response from a dict
mail_list_access_logs_v1200_response_from_dict = MailListAccessLogsV1200Response.from_dict(mail_list_access_logs_v1200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


