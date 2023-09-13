#!/bin/bash
for filename in ./*.png; do
  echo "${filename}" | cut -d. -f-2
  if [[ "$filename" == *"SCENE"* ]]; then
    foldname="$(cut -d. -f-2 <<<$filename)/"
    echo $foldname
    mkdir -p "$foldname" && cp "$filename" "$foldname"
  fi
done
