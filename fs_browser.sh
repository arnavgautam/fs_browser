#!/bin/bash

echo "Welcome to the file browser! Where would you like to browse today? "
read folder_location
echo "Thank you, we'll get right on that!"
absolute_folder_location=$(python3 get_absolute_location.py $folder_location)
if [ -z "$absolute_folder_location" ]; then
    echo "The location provided, $folder_location, is not a valid directory"
    exit 1
fi
docker run -it --rm -p 3005:3005 --name fs-browser-flask -v $absolute_folder_location:/browsing_data fs_browser-flask