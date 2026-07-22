# MailV1OrdersOrderDomainResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Domain resource ID | [optional] 
**name** | **str** | Domain name | [optional] 

## Example

```python
from hostinger_api.models.mail_v1_orders_order_domain_resource import MailV1OrdersOrderDomainResource

# TODO update the JSON string below
json = "{}"
# create an instance of MailV1OrdersOrderDomainResource from a JSON string
mail_v1_orders_order_domain_resource_instance = MailV1OrdersOrderDomainResource.from_json(json)
# print the JSON string representation of the object
print(MailV1OrdersOrderDomainResource.to_json())

# convert the object into a dict
mail_v1_orders_order_domain_resource_dict = mail_v1_orders_order_domain_resource_instance.to_dict()
# create an instance of MailV1OrdersOrderDomainResource from a dict
mail_v1_orders_order_domain_resource_from_dict = MailV1OrdersOrderDomainResource.from_dict(mail_v1_orders_order_domain_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


