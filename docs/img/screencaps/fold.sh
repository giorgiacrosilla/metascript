#!/bin/bash
for filename in ../last_screencaps/*.png; do
  base_dir="$(dirname "$filename")"
  filename="$(basename "$filename" .png)"
  foldname="$(echo "$filename" | cut -d'.' -f1)"
  folder_path="./${foldname}/"
  if find $folder_path -type f -name "$filename.jpg" -print -quit | grep -q .; then
    echo "File $filename found."
  else
    mkdir "$folder_path"
    cp "$base_dir/$filename.png" "$folder_path"
    echo "File $filename not found in $folder_path"
  fi

done
