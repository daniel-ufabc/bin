#!/bin/bash 
for name in *.ogg; do ffmpeg -ab 192k -i "$name" "$(basename "$name" .ogg).mp3"; done;
 # "$name.mp3"; done;
