# BillingV1OrderVirtualMachineOrderResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order** | [**BillingV1OrderOrderResource**](BillingV1OrderOrderResource.md) |  | [optional] 
**virtual_machine** | [**VPSV1VirtualMachineVirtualMachineResource**](VPSV1VirtualMachineVirtualMachineResource.md) |  | [optional] 

## Example

```python
from hostinger_api.models.billing_v1_order_virtual_machine_order_resource import BillingV1OrderVirtualMachineOrderResource

# TODO update the JSON string below
json = "{}"
# create an instance of BillingV1OrderVirtualMachineOrderResource from a JSON string
billing_v1_order_virtual_machine_order_resource_instance = BillingV1OrderVirtualMachineOrderResource.from_json(json)
# print the JSON string representation of the object
print(BillingV1OrderVirtualMachineOrderResource.to_json())

# convert the object into a dict
billing_v1_order_virtual_machine_order_resource_dict = billing_v1_order_virtual_machine_order_resource_instance.to_dict()
# create an instance of BillingV1OrderVirtualMachineOrderResource from a dict
billing_v1_order_virtual_machine_order_resource_from_dict = BillingV1OrderVirtualMachineOrderResource.from_dict(billing_v1_order_virtual_machine_order_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


