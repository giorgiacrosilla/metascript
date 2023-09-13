#!/bin/bash

# Function to generate JSON for a folder
function generate_json_for_folder() {
  local folder_path="$1"
  local folder_name="$(basename "$folder_path")"
  local json_output="{ \"$folder_name\": [] }"

  # Use find to list files and subdirectories in the folder
  while IFS= read -r -d '' item; do
    if [ -d "$item" ]; then
      # If it's a directory, recursively generate JSON for it
      subfolder_json="$(generate_json_for_folder "$item")"
      json_output="$(echo "$json_output" | jq --argjson value "$subfolder_json" '. += $value')"
    else
      # If it's a file, add it to the list of files
      file_name="$(basename "$item")"
      json_output="$(echo "$json_output" | jq ".[\"$folder_name\"] += [\"$file_name\"]")"
    fi
  done < <(find "$folder_path" -mindepth 1 -maxdepth 1 -print0)

  # Print the JSON for the folder
  echo "$json_output"
}

# Specify the root folder (change this to your desired path)
root_folder="."

# Generate JSON for the root folder
folder_structure_json="$(generate_json_for_folder "$root_folder")"

# Store the JSON in a file in the root folder
json_file="$root_folder/folder_structure.json"
echo "$folder_structure_json" > "$json_file"

# Print the path to the JSON file
echo "Folder structure JSON stored in: $json_file"

