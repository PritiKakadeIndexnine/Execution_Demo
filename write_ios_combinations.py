import orthagonal_operations
import json
import subprocess

def update_combinations(combinations, output_file="ios_combinations.json"):
    with open(output_file, 'w') as json_file:
        json.dump(combinations, json_file, indent=4)


if __name__ == "__main__":
    with open("combined_environment.json", 'r') as f:
        combined_env = json.load(f)

        factors = ["env", "device", "version"]
        levels = {
            "env": list(combined_env['ios']['env'].values()),
            "device": list(combined_env['ios']['device'].values()),
            "version": list(combined_env['ios']['version'].values())
        }

        combinations = orthagonal_operations.generate_testing_combinations(factors, levels)
        update_combinations(combinations)

        remote_url = "https://github.com/PritiKakadeIndexnine/Execution_Demo.git"

        orthagonal_operations.commit_and_push_changes("IOS-execution", remote_url)


