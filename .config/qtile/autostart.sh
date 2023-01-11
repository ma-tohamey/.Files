#!/bin/sh

function run {
  if ! pgrep $1 ;
  then
    $@&
  fi
}

run sxhkd &
run ksnip &
run nm-applet &
nitrogen --restore &
run picom --config .config/picom/picom.conf -b &
run aw-qt 
