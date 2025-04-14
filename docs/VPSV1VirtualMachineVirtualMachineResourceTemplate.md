# VPSV1VirtualMachineVirtualMachineResourceTemplate

OS template installed in virtual machine

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Template ID | [optional] 
**name** | **str** | Template name | [optional] 
**description** | **str** | Template description | [optional] 
**documentation** | **str** | Link to official OS documentation | [optional] 

## Example

```python
from hostinger-api.models.vpsv1_virtual_machine_virtual_machine_resource_template import VPSV1VirtualMachineVirtualMachineResourceTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of VPSV1VirtualMachineVirtualMachineResourceTemplate from a JSON string
vpsv1_virtual_machine_virtual_machine_resource_template_instance = VPSV1VirtualMachineVirtualMachineResourceTemplate.from_json(json)
# print the JSON string representation of the object
print(VPSV1VirtualMachineVirtualMachineResourceTemplate.to_json())

# convert the object into a dict
vpsv1_virtual_machine_virtual_machine_resource_template_dict = vpsv1_virtual_machine_virtual_machine_resource_template_instance.to_dict()
# create an instance of VPSV1VirtualMachineVirtualMachineResourceTemplate from a dict
vpsv1_virtual_machine_virtual_machine_resource_template_from_dict = VPSV1VirtualMachineVirtualMachineResourceTemplate.from_dict(vpsv1_virtual_machine_virtual_machine_resource_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


