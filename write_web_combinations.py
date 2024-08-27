import json
import subprocess

from openpyxl import Workbook
import os

import orthagonal_operations


def update_environment_combinations(combinations, env_config_file="web_environment.json", output_file="web_environment_combinations.json"):
    with open(env_config_file, 'r') as f:
        env_config = json.load(f)

    updated_env = []

    with open(output_file, 'w') as json_file:
        json.dump(combinations, json_file, indent=4)

    with open(output_file, 'w') as f:
        json.dump(updated_env, f, indent=2)

    print(f"Updated environment combinations written to '{output_file}'")



if __name__ == "__main__":
    factors = ["env", "browser"]
    levels = {
        "env": ["QA", "Staging", "Prod"],
        "browser": ["chrome", "firefox", "edge"]
    }

    test_combinations = orthagonal_operations.generate_testing_combinations(factors, levels)

    update_environment_combinations(test_combinations)

    remote_url = "https://github.com/PritiKakadeIndexnine/Execution_Demo.git"

    orthagonal_operations.commit_and_push_changes("web-execution", remote_url)

















