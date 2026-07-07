# WordPressV1HostingerPluginsAiOptionStatusResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_llmstxt_enabled** | **bool** | Whether the llms.txt AI option is enabled. Present when the option is requested or when no specific option filter is provided. | [optional] 
**is_web2agent_enabled** | **bool** | Whether the Web2Agent AI option is enabled. Present when the option is requested or when no specific option filter is provided. | [optional] 

## Example

```python
from hostinger_api.models.word_press_v1_hostinger_plugins_ai_option_status_resource import WordPressV1HostingerPluginsAiOptionStatusResource

# TODO update the JSON string below
json = "{}"
# create an instance of WordPressV1HostingerPluginsAiOptionStatusResource from a JSON string
word_press_v1_hostinger_plugins_ai_option_status_resource_instance = WordPressV1HostingerPluginsAiOptionStatusResource.from_json(json)
# print the JSON string representation of the object
print(WordPressV1HostingerPluginsAiOptionStatusResource.to_json())

# convert the object into a dict
word_press_v1_hostinger_plugins_ai_option_status_resource_dict = word_press_v1_hostinger_plugins_ai_option_status_resource_instance.to_dict()
# create an instance of WordPressV1HostingerPluginsAiOptionStatusResource from a dict
word_press_v1_hostinger_plugins_ai_option_status_resource_from_dict = WordPressV1HostingerPluginsAiOptionStatusResource.from_dict(word_press_v1_hostinger_plugins_ai_option_status_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


