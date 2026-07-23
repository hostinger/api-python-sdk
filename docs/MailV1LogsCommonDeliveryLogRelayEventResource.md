# MailV1LogsCommonDeliveryLogRelayEventResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_to** | **str** |  | [optional] 
**relay** | **str** |  | [optional] 
**delay** | **str** |  | [optional] 
**dsn** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**response** | **str** |  | [optional] 
**time** | **datetime** |  | [optional] 

## Example

```python
from hostinger_api.models.mail_v1_logs_common_delivery_log_relay_event_resource import MailV1LogsCommonDeliveryLogRelayEventResource

# TODO update the JSON string below
json = "{}"
# create an instance of MailV1LogsCommonDeliveryLogRelayEventResource from a JSON string
mail_v1_logs_common_delivery_log_relay_event_resource_instance = MailV1LogsCommonDeliveryLogRelayEventResource.from_json(json)
# print the JSON string representation of the object
print(MailV1LogsCommonDeliveryLogRelayEventResource.to_json())

# convert the object into a dict
mail_v1_logs_common_delivery_log_relay_event_resource_dict = mail_v1_logs_common_delivery_log_relay_event_resource_instance.to_dict()
# create an instance of MailV1LogsCommonDeliveryLogRelayEventResource from a dict
mail_v1_logs_common_delivery_log_relay_event_resource_from_dict = MailV1LogsCommonDeliveryLogRelayEventResource.from_dict(mail_v1_logs_common_delivery_log_relay_event_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


