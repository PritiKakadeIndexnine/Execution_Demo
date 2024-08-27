import json
import subprocess

from openpyxl import Workbook
import os

import orthagonal_operations


def update_environment_combinations(combinations, env_config_file="web_environment.json", output_file="web_environment_combinations.json"):
    # Load the existing configuration
    with open('web_environment.json', 'r') as file:
        config = json.load(file)

    # Extracting relevant configurations
    env_urls = config['env']
    browsers = config['browser']
    window_height = config['window_height']
    window_width = config['window_width']
    receiver_email = config['receiver_email']

    # Iterate over each combination
    for combination in test_combinations:
        # Extract factors and their values
        env = combination.get('env')
        browser = combination.get('browser')

        # Map factors to their corresponding values
        env_url = env_urls.get(env.lower(), '')
        browser_name = browsers.get(browser.capitalize(), '')




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

















