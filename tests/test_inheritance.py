from src.pyrametrize.inheritance import merge_configurations


def test_1_level_string_dictionary_inheritance_merge():
    parent_config = {"field1": "parent_val1", "field2": "parent_val2"}

    child_config = {"field2": "child_val2", "field3": "child_val3"}

    expected = {"field1": "parent_val1", "field2": "child_val2", "field3": "child_val3"}

    actual = merge_configurations(parent_config, child_config)

    assert actual == expected


def test_2_level_string_dictionary_inheritance_merge():
    parent_config = {
        "field1": {
            "field2": "parent_val2",
            "field3": "parent_val3",
            "field4": "parent_val4",
        }
    }

    child_config = {"field1": {"field3": "child_val3", "field4": "child_val4"}}

    expected = {
        "field1": {
            "field2": "parent_val2",
            "field3": "child_val3",
            "field4": "child_val4",
        }
    }

    actual = merge_configurations(parent_config, child_config)

    assert actual == expected
