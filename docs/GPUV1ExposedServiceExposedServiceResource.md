# GPUV1ExposedServiceExposedServiceResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Exposed service ID | [optional] 
**name** | **str** |  | [optional] 
**hostname** | **str** | Public hostname or IP address of the service | [optional] 
**internal_port** | **int** | Port the service listens on inside the instance | [optional] 
**external_port** | **int** | Public port the service is reachable on | [optional] 
**protocol** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from hostinger_api.models.gpuv1_exposed_service_exposed_service_resource import GPUV1ExposedServiceExposedServiceResource

# TODO update the JSON string below
json = "{}"
# create an instance of GPUV1ExposedServiceExposedServiceResource from a JSON string
gpuv1_exposed_service_exposed_service_resource_instance = GPUV1ExposedServiceExposedServiceResource.from_json(json)
# print the JSON string representation of the object
print(GPUV1ExposedServiceExposedServiceResource.to_json())

# convert the object into a dict
gpuv1_exposed_service_exposed_service_resource_dict = gpuv1_exposed_service_exposed_service_resource_instance.to_dict()
# create an instance of GPUV1ExposedServiceExposedServiceResource from a dict
gpuv1_exposed_service_exposed_service_resource_from_dict = GPUV1ExposedServiceExposedServiceResource.from_dict(gpuv1_exposed_service_exposed_service_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


