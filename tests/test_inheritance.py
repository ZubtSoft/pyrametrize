from src.pyrametrize.inheritance import merge_configurations


def test_2_level_string_dictionary_inheritance_merge():
    parent_config = {
        "field1": "parent_val1",
        "field2": "child_val2",
        "field4": {
            "field5": "parent_val5",
            "field6": "child_val6",
            "field7": "child_val7",
        },
    }

    child_config = {
        "field2": "child_val2",
        "field3": "child_val3",
        "field4": {
            "field6": "child_val6",
            "field7": "child_val7",
        },
    }

    expected = {
        "field1": "parent_val1",
        "field2": "child_val2",
        "field3": "child_val3",
        "field4": {
            "field5": "parent_val5",
            "field6": "child_val6",
            "field7": "child_val7",
        },
    }

    actual = merge_configurations(parent_config, child_config)

    assert actual == expected
