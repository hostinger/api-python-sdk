# VPSV1VirtualMachineRecreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_id** | **int** | Template ID | 
**password** | **str** | Password for the virtual machine. If not provided, random password will be generated. Password will not be shown in the response. | [optional] 
**post_install_script_id** | **int** | Post-install script ID | [optional] 

## Example

```python
from hostinger_api.models.vpsv1_virtual_machine_recreate_request import VPSV1VirtualMachineRecreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VPSV1VirtualMachineRecreateRequest from a JSON string
vpsv1_virtual_machine_recreate_request_instance = VPSV1VirtualMachineRecreateRequest.from_json(json)
# print the JSON string representation of the object
print(VPSV1VirtualMachineRecreateRequest.to_json())

# convert the object into a dict
vpsv1_virtual_machine_recreate_request_dict = vpsv1_virtual_machine_recreate_request_instance.to_dict()
# create an instance of VPSV1VirtualMachineRecreateRequest from a dict
vpsv1_virtual_machine_recreate_request_from_dict = VPSV1VirtualMachineRecreateRequest.from_dict(vpsv1_virtual_machine_recreate_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


