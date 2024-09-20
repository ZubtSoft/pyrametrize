from typing import Dict


class ConfigurationMergeException(Exception):
    pass


def merge_configurations(parent_config: Dict, child_config: Dict) -> Dict:
    merge_result = {}

    child_only_keys = child_config.keys() - parent_config.keys()
    for key in child_only_keys:
        merge_result[key] = child_config[key]

    parent_only_keys = parent_config.keys() - child_config.keys()
    for key in parent_only_keys:
        merge_result[key] = parent_config[key]

    common_keys = parent_config.keys() & child_config.keys()
    for key in common_keys:
        pck = parent_config[key]
        cck = child_config[key]
        if isinstance(pck, str) and isinstance(cck, str):
            merge_result[key] = (
                cck  # TODO: here can be a customization of merge behavior
            )
        elif isinstance(pck, dict) and isinstance(cck, dict):
            merge_result[key] = merge_configurations(pck, cck)
        else:
            raise ConfigurationMergeException("Can't merge ", pck, cck)

    return merge_result
