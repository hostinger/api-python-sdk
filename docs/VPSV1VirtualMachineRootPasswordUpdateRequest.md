# VPSV1VirtualMachineRootPasswordUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | Root password | 

## Example

```python
from hostinger_api.models.vpsv1_virtual_machine_root_password_update_request import VPSV1VirtualMachineRootPasswordUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VPSV1VirtualMachineRootPasswordUpdateRequest from a JSON string
vpsv1_virtual_machine_root_password_update_request_instance = VPSV1VirtualMachineRootPasswordUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(VPSV1VirtualMachineRootPasswordUpdateRequest.to_json())

# convert the object into a dict
vpsv1_virtual_machine_root_password_update_request_dict = vpsv1_virtual_machine_root_password_update_request_instance.to_dict()
# create an instance of VPSV1VirtualMachineRootPasswordUpdateRequest from a dict
vpsv1_virtual_machine_root_password_update_request_from_dict = VPSV1VirtualMachineRootPasswordUpdateRequest.from_dict(vpsv1_virtual_machine_root_password_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


