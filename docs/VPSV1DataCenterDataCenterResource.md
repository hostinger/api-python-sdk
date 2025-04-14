# VPSV1DataCenterDataCenterResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Data center ID | [optional] 
**name** | **str** | Data center name | [optional] 
**location** | **str** | Data center location country (two letter code) | [optional] 
**city** | **str** | Data center location city | [optional] 
**continent** | **str** | Data center location continent | [optional] 

## Example

```python
from hostinger-api.models.vpsv1_data_center_data_center_resource import VPSV1DataCenterDataCenterResource

# TODO update the JSON string below
json = "{}"
# create an instance of VPSV1DataCenterDataCenterResource from a JSON string
vpsv1_data_center_data_center_resource_instance = VPSV1DataCenterDataCenterResource.from_json(json)
# print the JSON string representation of the object
print(VPSV1DataCenterDataCenterResource.to_json())

# convert the object into a dict
vpsv1_data_center_data_center_resource_dict = vpsv1_data_center_data_center_resource_instance.to_dict()
# create an instance of VPSV1DataCenterDataCenterResource from a dict
vpsv1_data_center_data_center_resource_from_dict = VPSV1DataCenterDataCenterResource.from_dict(vpsv1_data_center_data_center_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


