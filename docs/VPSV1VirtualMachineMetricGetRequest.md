# VPSV1VirtualMachineMetricGetRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_from** | **datetime** |  | 
**date_to** | **datetime** |  | 

## Example

```python
from hostinger-api.models.vpsv1_virtual_machine_metric_get_request import VPSV1VirtualMachineMetricGetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VPSV1VirtualMachineMetricGetRequest from a JSON string
vpsv1_virtual_machine_metric_get_request_instance = VPSV1VirtualMachineMetricGetRequest.from_json(json)
# print the JSON string representation of the object
print(VPSV1VirtualMachineMetricGetRequest.to_json())

# convert the object into a dict
vpsv1_virtual_machine_metric_get_request_dict = vpsv1_virtual_machine_metric_get_request_instance.to_dict()
# create an instance of VPSV1VirtualMachineMetricGetRequest from a dict
vpsv1_virtual_machine_metric_get_request_from_dict = VPSV1VirtualMachineMetricGetRequest.from_dict(vpsv1_virtual_machine_metric_get_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


