import json
import subprocess

from openpyxl import Workbook
import os

import orthagonal_operations


def update_environment_combinations(combinations, env_config_file="web_environment.json", output_file="web_environment_combinations.json"):
    # Load the existing configuration
    with open(env_config_file, 'r') as file:
        config = json.load(file)

    # Prepare the results container
    results = []

    # Debug: Print loaded config
    print("Loaded configuration:")
    print(json.dumps(config, indent=4))

    # Iterate over each combination
    for combination in combinations:
        # Extract factors and their values
        env_key = combination.get('env', '').lower()
        browser_key = combination.get('browser', '').capitalize()

        # Debug: Print current combination being processed
        print(f"Processing combination: env={env_key}, browser={browser_key}")

        # Map factors to their corresponding values
        env_url = config['env'].get(env_key, '')
        browser_name = config['browser'].get(browser_key, '')

        # Debug: Print extracted values
        print(f"Extracted values: env_url={env_url}, browser_name={browser_name}")

        # Create a new dictionary with updated values
        updated_combination = {
            'env': combination.get('env', ''),
            'env_url': env_url,
            'browser': browser_name,
            'platform': config['platform']['Windows 10'],
            'window_height': config['window_height'],
            'window_width': config['window_width'],
            'receiver_email': config['receiver_email']
        }

        # Append to the results list
        results.append(updated_combination)

    # Write the results to a new JSON file
    with open(output_file, 'w') as file:
        json.dump(results, file, indent=4)

    print(f"Updated environment combinations have been written to '{output_file}'.")


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

















