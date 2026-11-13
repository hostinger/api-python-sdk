# GPUV1ExposedServiceStoreRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Service name, unique within the instance | 
**internal_port** | **int** | Port the service listens on inside the instance, unique within the instance | 
**protocol** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from hostinger_api.models.gpuv1_exposed_service_store_request import GPUV1ExposedServiceStoreRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GPUV1ExposedServiceStoreRequest from a JSON string
gpuv1_exposed_service_store_request_instance = GPUV1ExposedServiceStoreRequest.from_json(json)
# print the JSON string representation of the object
print(GPUV1ExposedServiceStoreRequest.to_json())

# convert the object into a dict
gpuv1_exposed_service_store_request_dict = gpuv1_exposed_service_store_request_instance.to_dict()
# create an instance of GPUV1ExposedServiceStoreRequest from a dict
gpuv1_exposed_service_store_request_from_dict = GPUV1ExposedServiceStoreRequest.from_dict(gpuv1_exposed_service_store_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


