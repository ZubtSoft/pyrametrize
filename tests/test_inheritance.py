from src.pyrametrize.inheritance import merge_configurations


def test_1_level_string_dictionary_inheritance_merge():
    modifiable_parent_config = {"field1": "parent_val1", "field2": "parent_val2"}

    child_config = {"field2": "child_val2", "field3": "child_val3"}

    expected = {"field1": "parent_val1", "field2": "child_val2", "field3": "child_val3"}

    merge_configurations(modifiable_parent_config, child_config)

    assert modifiable_parent_config == expected
