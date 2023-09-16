#!/bin/bash
for filename in ../screencaps_comp/*.png; do
  base_dir="$(dirname "$filename")"
  filename="$(basename "$filename")"
  foldname="$(echo "$filename" | cut -d'.' -f1)"
  if [[ "$filename" == *"SCENE"* ]]; then
    folder_path="./${foldname}/"
    if [ ! -d "$folder_path" ]; then
      echo "Creating folder: $folder_path"
      mkdir -p "$folder_path" && cp "$base_dir/$filename" "$folder_path"
    else
      echo "Folder already exists: $folder_path"
    fi
  fi

done
