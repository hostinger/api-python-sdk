# EcommerceV1OrderOrderResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The order ID, required by every other order endpoint. | [optional] 
**display_id** | **int** | The order number the merchant and customer see. | [optional] 
**status** | **str** | The order status. | [optional] 
**payment_status** | **str** | The payment status. A paid order is \&quot;captured\&quot;. | [optional] 
**fulfillment_status** | **str** | The fulfilment status. | [optional] 
**total** | **int** | Order total in the smallest currency unit. | [optional] 
**currency_code** | **str** | The order currency code. | [optional] 
**customer_email** | **str** | The customer email. | [optional] 
**item_count** | **int** | Number of distinct line items. Retrieve the order for the items themselves. | [optional] 
**created_at** | **datetime** | ISO timestamp of when the order was created. | [optional] 

## Example

```python
from hostinger_api.models.ecommerce_v1_order_order_resource import EcommerceV1OrderOrderResource

# TODO update the JSON string below
json = "{}"
# create an instance of EcommerceV1OrderOrderResource from a JSON string
ecommerce_v1_order_order_resource_instance = EcommerceV1OrderOrderResource.from_json(json)
# print the JSON string representation of the object
print(EcommerceV1OrderOrderResource.to_json())

# convert the object into a dict
ecommerce_v1_order_order_resource_dict = ecommerce_v1_order_order_resource_instance.to_dict()
# create an instance of EcommerceV1OrderOrderResource from a dict
ecommerce_v1_order_order_resource_from_dict = EcommerceV1OrderOrderResource.from_dict(ecommerce_v1_order_order_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


