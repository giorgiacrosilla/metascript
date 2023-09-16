#!/bin/bash

function generate_json_for_folder() {
  local folder_path="$1"
  local folder_name="$(basename "$folder_path")"
  local json_output="{ \"$folder_name\": [] }"

  while IFS= read -r -d '' item; do
    if [ -d "$item" ]; then
      subfolder_json="$(generate_json_for_folder "$item")"
      json_output="$(echo "$json_output" | jq --argjson value "$subfolder_json" '. += $value')"
    else
      file_name="$(basename "$item")"
      json_output="$(echo "$json_output" | jq ".[\"$folder_name\"] += [\"$file_name\"]")"
    fi
  done < <(find "$folder_path" -mindepth 1 -maxdepth 1 -print0)

  echo "$json_output"
}

root_folder="."

folder_structure_json="$(generate_json_for_folder "$root_folder")"

json_file="$root_folder/folder_structure.json"
echo "$folder_structure_json" > "$json_file"

echo "Folder structure JSON stored in: $json_file"

