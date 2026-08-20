# EcommerceV1OrderOrderDetailResourceFulfillmentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The fulfilment ID. | [optional] 
**created_at** | **datetime** | ISO timestamp of when the fulfilment was created. | [optional] 
**shipped_at** | **datetime** | ISO timestamp of when the fulfilment shipped, if known. | [optional] 
**canceled_at** | **datetime** | ISO timestamp of when the fulfilment was canceled, if any. | [optional] 
**tracking** | [**List[EcommerceV1OrderOrderDetailResourceFulfillmentsInnerTrackingInner]**](EcommerceV1OrderOrderDetailResourceFulfillmentsInnerTrackingInner.md) | Tracking numbers attached to the fulfilment. | [optional] 

## Example

```python
from hostinger_api.models.ecommerce_v1_order_order_detail_resource_fulfillments_inner import EcommerceV1OrderOrderDetailResourceFulfillmentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of EcommerceV1OrderOrderDetailResourceFulfillmentsInner from a JSON string
ecommerce_v1_order_order_detail_resource_fulfillments_inner_instance = EcommerceV1OrderOrderDetailResourceFulfillmentsInner.from_json(json)
# print the JSON string representation of the object
print(EcommerceV1OrderOrderDetailResourceFulfillmentsInner.to_json())

# convert the object into a dict
ecommerce_v1_order_order_detail_resource_fulfillments_inner_dict = ecommerce_v1_order_order_detail_resource_fulfillments_inner_instance.to_dict()
# create an instance of EcommerceV1OrderOrderDetailResourceFulfillmentsInner from a dict
ecommerce_v1_order_order_detail_resource_fulfillments_inner_from_dict = EcommerceV1OrderOrderDetailResourceFulfillmentsInner.from_dict(ecommerce_v1_order_order_detail_resource_fulfillments_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


