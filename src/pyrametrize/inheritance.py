from typing import Dict


def merge_configurations(parent_config: Dict, child_config: Dict) -> Dict:
    parent_config.update(child_config)
