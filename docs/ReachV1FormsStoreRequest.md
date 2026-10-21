# ReachV1FormsStoreRequest

Create a draft form

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Form name. Letters, digits, spaces and - . &#39; _ only. | 

## Example

```python
from hostinger_api.models.reach_v1_forms_store_request import ReachV1FormsStoreRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReachV1FormsStoreRequest from a JSON string
reach_v1_forms_store_request_instance = ReachV1FormsStoreRequest.from_json(json)
# print the JSON string representation of the object
print(ReachV1FormsStoreRequest.to_json())

# convert the object into a dict
reach_v1_forms_store_request_dict = reach_v1_forms_store_request_instance.to_dict()
# create an instance of ReachV1FormsStoreRequest from a dict
reach_v1_forms_store_request_from_dict = ReachV1FormsStoreRequest.from_dict(reach_v1_forms_store_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


