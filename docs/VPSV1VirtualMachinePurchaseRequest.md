# VPSV1VirtualMachinePurchaseRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_id** | **str** | Catalog price item ID | 
**payment_method_id** | **int** | Payment method ID, default will be used if not provided | [optional] 
**setup** | [**VPSV1VirtualMachineSetupRequest**](VPSV1VirtualMachineSetupRequest.md) |  | 
**coupons** | **List[object]** | Discount coupon codes | [optional] 

## Example

```python
from hostinger_api.models.vpsv1_virtual_machine_purchase_request import VPSV1VirtualMachinePurchaseRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VPSV1VirtualMachinePurchaseRequest from a JSON string
vpsv1_virtual_machine_purchase_request_instance = VPSV1VirtualMachinePurchaseRequest.from_json(json)
# print the JSON string representation of the object
print(VPSV1VirtualMachinePurchaseRequest.to_json())

# convert the object into a dict
vpsv1_virtual_machine_purchase_request_dict = vpsv1_virtual_machine_purchase_request_instance.to_dict()
# create an instance of VPSV1VirtualMachinePurchaseRequest from a dict
vpsv1_virtual_machine_purchase_request_from_dict = VPSV1VirtualMachinePurchaseRequest.from_dict(vpsv1_virtual_machine_purchase_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


