# EcommerceV1OrderOrderDetailResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The order ID. | [optional] 
**display_id** | **int** | The order number. | [optional] 
**status** | **str** | The order status. | [optional] 
**payment_status** | **str** | The payment status. | [optional] 
**fulfillment_status** | **str** | The fulfilment status. | [optional] 
**total** | **int** | Order total in the smallest currency unit. | [optional] 
**currency_code** | **str** | The order currency code. | [optional] 
**customer_email** | **str** | The customer email. | [optional] 
**item_count** | **int** | Number of distinct line items. | [optional] 
**created_at** | **datetime** | ISO timestamp of when the order was created. | [optional] 
**merchant_note** | **str** | Internal note visible only to the merchant. | [optional] 
**subtotal** | **int** | Subtotal in the smallest currency unit. | [optional] 
**discount_total** | **int** | Discount total in the smallest currency unit. | [optional] 
**tax_total** | **int** | Tax total in the smallest currency unit. | [optional] 
**shipping_total** | **int** | Shipping total in the smallest currency unit. | [optional] 
**paid_total** | **int** | Amount paid in the smallest currency unit. | [optional] 
**refunded_total** | **int** | Amount refunded in the smallest currency unit. | [optional] 
**shipping_address** | [**EcommerceV1OrderOrderDetailResourceShippingAddress**](EcommerceV1OrderOrderDetailResourceShippingAddress.md) |  | [optional] 
**billing_address** | [**EcommerceV1OrderOrderDetailResourceBillingAddress**](EcommerceV1OrderOrderDetailResourceBillingAddress.md) |  | [optional] 
**items** | [**List[EcommerceV1OrderOrderDetailResourceItemsInner]**](EcommerceV1OrderOrderDetailResourceItemsInner.md) | The order line items. | [optional] 
**fulfillments** | [**List[EcommerceV1OrderOrderDetailResourceFulfillmentsInner]**](EcommerceV1OrderOrderDetailResourceFulfillmentsInner.md) | The order fulfilments with tracking. | [optional] 

## Example

```python
from hostinger_api.models.ecommerce_v1_order_order_detail_resource import EcommerceV1OrderOrderDetailResource

# TODO update the JSON string below
json = "{}"
# create an instance of EcommerceV1OrderOrderDetailResource from a JSON string
ecommerce_v1_order_order_detail_resource_instance = EcommerceV1OrderOrderDetailResource.from_json(json)
# print the JSON string representation of the object
print(EcommerceV1OrderOrderDetailResource.to_json())

# convert the object into a dict
ecommerce_v1_order_order_detail_resource_dict = ecommerce_v1_order_order_detail_resource_instance.to_dict()
# create an instance of EcommerceV1OrderOrderDetailResource from a dict
ecommerce_v1_order_order_detail_resource_from_dict = EcommerceV1OrderOrderDetailResource.from_dict(ecommerce_v1_order_order_detail_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


