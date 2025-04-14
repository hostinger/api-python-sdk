# VPSV1VirtualMachineRecoveryStartRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**root_password** | **str** | Temporary root password for recovery mode | 

## Example

```python
from hostinger_api.models.vpsv1_virtual_machine_recovery_start_request import VPSV1VirtualMachineRecoveryStartRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VPSV1VirtualMachineRecoveryStartRequest from a JSON string
vpsv1_virtual_machine_recovery_start_request_instance = VPSV1VirtualMachineRecoveryStartRequest.from_json(json)
# print the JSON string representation of the object
print(VPSV1VirtualMachineRecoveryStartRequest.to_json())

# convert the object into a dict
vpsv1_virtual_machine_recovery_start_request_dict = vpsv1_virtual_machine_recovery_start_request_instance.to_dict()
# create an instance of VPSV1VirtualMachineRecoveryStartRequest from a dict
vpsv1_virtual_machine_recovery_start_request_from_dict = VPSV1VirtualMachineRecoveryStartRequest.from_dict(vpsv1_virtual_machine_recovery_start_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


