# VPSV1VirtualMachineVirtualMachineResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Virtual machine ID | [optional] 
**firewall_group_id** | **int** | Active firewall ID, &#x60;null&#x60; if disabled | [optional] 
**subscription_id** | **str** | Subscription ID | [optional] 
**plan** | **str** | VPS plan name | [optional] 
**hostname** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**actions_lock** | **str** |  | [optional] 
**cpus** | **int** | CPUs count assigned to virtual machine | [optional] 
**memory** | **int** | Memory available to virtual machine (in megabytes) | [optional] 
**disk** | **int** | Virtual machine disk size (in megabytes) | [optional] 
**bandwidth** | **int** | Monthly internet traffic available to virtual machine (in megabytes) | [optional] 
**ns1** | **str** | Primary DNS resolver | [optional] 
**ns2** | **str** | Secondary DNS resolver | [optional] 
**ipv4** | [**VPSV1VirtualMachineVirtualMachineResourceIpv4**](VPSV1VirtualMachineVirtualMachineResourceIpv4.md) |  | [optional] 
**ipv6** | [**VPSV1VirtualMachineVirtualMachineResourceIpv6**](VPSV1VirtualMachineVirtualMachineResourceIpv6.md) |  | [optional] 
**template** | [**VPSV1VirtualMachineVirtualMachineResourceTemplate**](VPSV1VirtualMachineVirtualMachineResourceTemplate.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from hostinger_api.models.vpsv1_virtual_machine_virtual_machine_resource import VPSV1VirtualMachineVirtualMachineResource

# TODO update the JSON string below
json = "{}"
# create an instance of VPSV1VirtualMachineVirtualMachineResource from a JSON string
vpsv1_virtual_machine_virtual_machine_resource_instance = VPSV1VirtualMachineVirtualMachineResource.from_json(json)
# print the JSON string representation of the object
print(VPSV1VirtualMachineVirtualMachineResource.to_json())

# convert the object into a dict
vpsv1_virtual_machine_virtual_machine_resource_dict = vpsv1_virtual_machine_virtual_machine_resource_instance.to_dict()
# create an instance of VPSV1VirtualMachineVirtualMachineResource from a dict
vpsv1_virtual_machine_virtual_machine_resource_from_dict = VPSV1VirtualMachineVirtualMachineResource.from_dict(vpsv1_virtual_machine_virtual_machine_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


