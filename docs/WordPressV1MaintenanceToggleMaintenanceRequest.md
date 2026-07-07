# WordPressV1MaintenanceToggleMaintenanceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Enable (true) or disable (false) maintenance mode for the WordPress installation. | 

## Example

```python
from hostinger_api.models.word_press_v1_maintenance_toggle_maintenance_request import WordPressV1MaintenanceToggleMaintenanceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WordPressV1MaintenanceToggleMaintenanceRequest from a JSON string
word_press_v1_maintenance_toggle_maintenance_request_instance = WordPressV1MaintenanceToggleMaintenanceRequest.from_json(json)
# print the JSON string representation of the object
print(WordPressV1MaintenanceToggleMaintenanceRequest.to_json())

# convert the object into a dict
word_press_v1_maintenance_toggle_maintenance_request_dict = word_press_v1_maintenance_toggle_maintenance_request_instance.to_dict()
# create an instance of WordPressV1MaintenanceToggleMaintenanceRequest from a dict
word_press_v1_maintenance_toggle_maintenance_request_from_dict = WordPressV1MaintenanceToggleMaintenanceRequest.from_dict(word_press_v1_maintenance_toggle_maintenance_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


