# MailV1OrdersOrderResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Order resource ID | [optional] 
**status** | **str** | Order status | [optional] 
**is_trial** | **bool** | Whether the order is currently in a trial period | [optional] 
**seats** | **int** | Number of mailbox seats purchased with the order | [optional] 
**domain** | [**MailV1OrdersOrderDomainResource**](MailV1OrdersOrderDomainResource.md) |  | [optional] 
**plan** | [**MailV1OrdersOrderPlanResource**](MailV1OrdersOrderPlanResource.md) |  | [optional] 
**has_pending_upgrade** | **bool** | Whether an upgrade is currently pending for the order | [optional] 
**created_at** | **datetime** |  | [optional] 
**expires_at** | **datetime** |  | [optional] 

## Example

```python
from hostinger_api.models.mail_v1_orders_order_resource import MailV1OrdersOrderResource

# TODO update the JSON string below
json = "{}"
# create an instance of MailV1OrdersOrderResource from a JSON string
mail_v1_orders_order_resource_instance = MailV1OrdersOrderResource.from_json(json)
# print the JSON string representation of the object
print(MailV1OrdersOrderResource.to_json())

# convert the object into a dict
mail_v1_orders_order_resource_dict = mail_v1_orders_order_resource_instance.to_dict()
# create an instance of MailV1OrdersOrderResource from a dict
mail_v1_orders_order_resource_from_dict = MailV1OrdersOrderResource.from_dict(mail_v1_orders_order_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


