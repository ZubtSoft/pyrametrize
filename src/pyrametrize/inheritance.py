from typing import Dict


class ConfigurationMergeException(Exception):
    pass


class ConfigurationMerger:
    def __get_merge_operator(self, parent_config_value, child_config_value):
        pass

    def merge_configurations(self, parent_config: Dict, child_config: Dict) -> Dict:
        merge_result = {}

        self.add_child_specific_keys(child_config, merge_result, parent_config)
        self.add_parent_specific_keys(child_config, merge_result, parent_config)
        common_keys = parent_config.keys() & child_config.keys()
        for key in common_keys:
            pcv = parent_config[key]
            ccv = child_config[key]
            if isinstance(pcv, str) and isinstance(ccv, str):
                merge_result[key] = (
                    ccv  # TODO: here can be a customization of merge behavior
                )
            elif isinstance(pcv, dict) and isinstance(ccv, dict):
                merge_result[key] = self.merge_configurations(pcv, ccv)
            else:
                raise ConfigurationMergeException("Can't merge ", pcv, ccv)

        return merge_result

    def add_parent_specific_keys(self, child_config, merge_result, parent_config):
        parent_only_keys = parent_config.keys() - child_config.keys()
        for key in parent_only_keys:
            merge_result[key] = parent_config[key]

    def add_child_specific_keys(self, child_config, merge_result, parent_config):
        child_only_keys = child_config.keys() - parent_config.keys()
        for key in child_only_keys:
            merge_result[key] = child_config[key]
