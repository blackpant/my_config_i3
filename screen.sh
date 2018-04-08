#!/bin/bash


CMD=maim -i $(xdotool getactivewindow)| xclip -selection clipboard -t image/png | notify-send "SCREENSHOT" "screenshot taken of the active window"

case $BLOCK_BUTTON in
    1) echo "$CMD" | echo "Clicked";;
    *) echo "$CMD" ;;
esac
