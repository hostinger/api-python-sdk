# MailV1OrdersPlanResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Machine name of the plan | [optional] 
**title** | **str** | Human-readable plan title | [optional] 
**domain** | [**MailV1OrdersPlanDomainResource**](MailV1OrdersPlanDomainResource.md) |  | [optional] 
**mailbox** | [**MailV1OrdersPlanMailboxResource**](MailV1OrdersPlanMailboxResource.md) |  | [optional] 

## Example

```python
from hostinger_api.models.mail_v1_orders_plan_resource import MailV1OrdersPlanResource

# TODO update the JSON string below
json = "{}"
# create an instance of MailV1OrdersPlanResource from a JSON string
mail_v1_orders_plan_resource_instance = MailV1OrdersPlanResource.from_json(json)
# print the JSON string representation of the object
print(MailV1OrdersPlanResource.to_json())

# convert the object into a dict
mail_v1_orders_plan_resource_dict = mail_v1_orders_plan_resource_instance.to_dict()
# create an instance of MailV1OrdersPlanResource from a dict
mail_v1_orders_plan_resource_from_dict = MailV1OrdersPlanResource.from_dict(mail_v1_orders_plan_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


