# EcommerceV1OrderCancelRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notify_customer** | **bool** | Whether to email the customer about the cancellation. Defaults to true. | [optional] 

## Example

```python
from hostinger_api.models.ecommerce_v1_order_cancel_request import EcommerceV1OrderCancelRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EcommerceV1OrderCancelRequest from a JSON string
ecommerce_v1_order_cancel_request_instance = EcommerceV1OrderCancelRequest.from_json(json)
# print the JSON string representation of the object
print(EcommerceV1OrderCancelRequest.to_json())

# convert the object into a dict
ecommerce_v1_order_cancel_request_dict = ecommerce_v1_order_cancel_request_instance.to_dict()
# create an instance of EcommerceV1OrderCancelRequest from a dict
ecommerce_v1_order_cancel_request_from_dict = EcommerceV1OrderCancelRequest.from_dict(ecommerce_v1_order_cancel_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


