if type "xrandr"; then
  for m in $(xrandr --query | grep " connected" | cut -d" " -f1); do
    MONITOR=$m polybar --reload -c /home/blackpant/.config/polybar/config.ini main &
  done
else
  polybar --reload -c /home/blackpant/.config/polybar/config.ini main &
fi
