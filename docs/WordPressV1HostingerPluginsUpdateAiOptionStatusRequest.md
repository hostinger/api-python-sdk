# WordPressV1HostingerPluginsUpdateAiOptionStatusRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**option** | **str** | AI option name | 
**enable** | **bool** | Enable (true) or disable (false) the AI option. | 

## Example

```python
from hostinger_api.models.word_press_v1_hostinger_plugins_update_ai_option_status_request import WordPressV1HostingerPluginsUpdateAiOptionStatusRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WordPressV1HostingerPluginsUpdateAiOptionStatusRequest from a JSON string
word_press_v1_hostinger_plugins_update_ai_option_status_request_instance = WordPressV1HostingerPluginsUpdateAiOptionStatusRequest.from_json(json)
# print the JSON string representation of the object
print(WordPressV1HostingerPluginsUpdateAiOptionStatusRequest.to_json())

# convert the object into a dict
word_press_v1_hostinger_plugins_update_ai_option_status_request_dict = word_press_v1_hostinger_plugins_update_ai_option_status_request_instance.to_dict()
# create an instance of WordPressV1HostingerPluginsUpdateAiOptionStatusRequest from a dict
word_press_v1_hostinger_plugins_update_ai_option_status_request_from_dict = WordPressV1HostingerPluginsUpdateAiOptionStatusRequest.from_dict(word_press_v1_hostinger_plugins_update_ai_option_status_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


