import json
import subprocess

from openpyxl import Workbook
import os

import orthagonal_operations


def update_environment_combinations(combinations, env_config_file="web_environment.json", output_file="web_environment_combinations.json"):
    with open(env_config_file, 'r') as f:
        env_config = json.load(f)

    updated_env = []

    for combination in combinations:
        env_key = combination['env'].lower()
        browser_key = combination['browser'].lower()
        if env_key in env_config['env'] and browser_key in env_config['browser']:
            updated_env.append({
                "env": env_config['env'][env_key],
                "browser": env_config['browser'][browser_key],
                "windows_height": env_config['window_height'],
                "window_width": env_config['window_width'],
                "receiver_email": env_config['receiver_email']
            })

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

















