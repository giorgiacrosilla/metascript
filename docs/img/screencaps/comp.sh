#!/bin/bash

find "./" -type f \( -iname "*.png" \) -print0 | while IFS= read -r -d $'\0' image; do
    filename="$(basename "$image")"
    filename_noext="${filename%.*}"
    foldname="$(echo "$filename_noext" | cut -d'.' -f1)"

    output_file="./$foldname/$filename_noext.jpg"

    convert -strip -interlace Plane -gaussian-blur 0.05 -quality 85% "$image" "$output_file"

    echo "Converted $image to $output_file"

done

