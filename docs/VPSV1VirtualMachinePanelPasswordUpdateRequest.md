# VPSV1VirtualMachinePanelPasswordUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | Panel password for the virtual machine | 

## Example

```python
from hostinger_api.models.vpsv1_virtual_machine_panel_password_update_request import VPSV1VirtualMachinePanelPasswordUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VPSV1VirtualMachinePanelPasswordUpdateRequest from a JSON string
vpsv1_virtual_machine_panel_password_update_request_instance = VPSV1VirtualMachinePanelPasswordUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(VPSV1VirtualMachinePanelPasswordUpdateRequest.to_json())

# convert the object into a dict
vpsv1_virtual_machine_panel_password_update_request_dict = vpsv1_virtual_machine_panel_password_update_request_instance.to_dict()
# create an instance of VPSV1VirtualMachinePanelPasswordUpdateRequest from a dict
vpsv1_virtual_machine_panel_password_update_request_from_dict = VPSV1VirtualMachinePanelPasswordUpdateRequest.from_dict(vpsv1_virtual_machine_panel_password_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


