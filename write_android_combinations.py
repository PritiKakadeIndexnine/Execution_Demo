import orthagonal_operations
import json

if __name__ == "__main__":
    with open("android_environment.json", 'r') as f:
        combined_env = json.load(f)

        factors = ["env", "device", "version"]
        levels = {
            "env": list(combined_env['android']['env'].values()),
            "device": list(combined_env['android']['device'].values()),
            "version": list(combined_env['android']['version'].values())
        }

        combinations = orthagonal_operations.generate_testing_combinations(factors, levels)
        orthagonal_operations.update_combinations(combinations)

        remote_url = "https://github.com/PritiKakadeIndexnine/Execution_Demo.git"

        orthagonal_operations.commit_and_push_changes("Android", remote_url)


