# MailV1LogsCommonDeliveryLogResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **str** |  | [optional] 
**rcpt** | **str** |  | [optional] 
**rcpts** | **str** |  | [optional] 
**client_ip** | **str** |  | [optional] 
**var_from** | **str** |  | [optional] 
**nrcpt** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**relay_events** | [**List[MailV1LogsCommonDeliveryLogRelayEventResource]**](MailV1LogsCommonDeliveryLogRelayEventResource.md) |  | [optional] 
**status** | **str** |  | [optional] 
**is_spam** | **bool** |  | [optional] 

## Example

```python
from hostinger_api.models.mail_v1_logs_common_delivery_log_resource import MailV1LogsCommonDeliveryLogResource

# TODO update the JSON string below
json = "{}"
# create an instance of MailV1LogsCommonDeliveryLogResource from a JSON string
mail_v1_logs_common_delivery_log_resource_instance = MailV1LogsCommonDeliveryLogResource.from_json(json)
# print the JSON string representation of the object
print(MailV1LogsCommonDeliveryLogResource.to_json())

# convert the object into a dict
mail_v1_logs_common_delivery_log_resource_dict = mail_v1_logs_common_delivery_log_resource_instance.to_dict()
# create an instance of MailV1LogsCommonDeliveryLogResource from a dict
mail_v1_logs_common_delivery_log_resource_from_dict = MailV1LogsCommonDeliveryLogResource.from_dict(mail_v1_logs_common_delivery_log_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


