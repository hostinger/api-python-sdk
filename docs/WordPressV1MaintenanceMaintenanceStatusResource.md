# WordPressV1MaintenanceMaintenanceStatusResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Current maintenance mode status for the WordPress installation | [optional] 

## Example

```python
from hostinger_api.models.word_press_v1_maintenance_maintenance_status_resource import WordPressV1MaintenanceMaintenanceStatusResource

# TODO update the JSON string below
json = "{}"
# create an instance of WordPressV1MaintenanceMaintenanceStatusResource from a JSON string
word_press_v1_maintenance_maintenance_status_resource_instance = WordPressV1MaintenanceMaintenanceStatusResource.from_json(json)
# print the JSON string representation of the object
print(WordPressV1MaintenanceMaintenanceStatusResource.to_json())

# convert the object into a dict
word_press_v1_maintenance_maintenance_status_resource_dict = word_press_v1_maintenance_maintenance_status_resource_instance.to_dict()
# create an instance of WordPressV1MaintenanceMaintenanceStatusResource from a dict
word_press_v1_maintenance_maintenance_status_resource_from_dict = WordPressV1MaintenanceMaintenanceStatusResource.from_dict(word_press_v1_maintenance_maintenance_status_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


