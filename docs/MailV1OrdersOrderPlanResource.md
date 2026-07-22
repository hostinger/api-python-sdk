# MailV1OrdersOrderPlanResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Plan name | [optional] 
**title** | **str** | Plan title | [optional] 

## Example

```python
from hostinger_api.models.mail_v1_orders_order_plan_resource import MailV1OrdersOrderPlanResource

# TODO update the JSON string below
json = "{}"
# create an instance of MailV1OrdersOrderPlanResource from a JSON string
mail_v1_orders_order_plan_resource_instance = MailV1OrdersOrderPlanResource.from_json(json)
# print the JSON string representation of the object
print(MailV1OrdersOrderPlanResource.to_json())

# convert the object into a dict
mail_v1_orders_order_plan_resource_dict = mail_v1_orders_order_plan_resource_instance.to_dict()
# create an instance of MailV1OrdersOrderPlanResource from a dict
mail_v1_orders_order_plan_resource_from_dict = MailV1OrdersOrderPlanResource.from_dict(mail_v1_orders_order_plan_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


