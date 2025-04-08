# VPSV1VirtualMachineNameserversUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ns1** | **str** |  | 
**ns2** | **str** |  | [optional] 

## Example

```python
from hostinger_api.models.vpsv1_virtual_machine_nameservers_update_request import VPSV1VirtualMachineNameserversUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VPSV1VirtualMachineNameserversUpdateRequest from a JSON string
vpsv1_virtual_machine_nameservers_update_request_instance = VPSV1VirtualMachineNameserversUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(VPSV1VirtualMachineNameserversUpdateRequest.to_json())

# convert the object into a dict
vpsv1_virtual_machine_nameservers_update_request_dict = vpsv1_virtual_machine_nameservers_update_request_instance.to_dict()
# create an instance of VPSV1VirtualMachineNameserversUpdateRequest from a dict
vpsv1_virtual_machine_nameservers_update_request_from_dict = VPSV1VirtualMachineNameserversUpdateRequest.from_dict(vpsv1_virtual_machine_nameservers_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


