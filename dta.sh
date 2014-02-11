#!/bin/zsh

dta() {
  wget -O - $1 |
  grep -Eo 'i.4cdn.org/[^"]+' |
  uniq |
  xargs wget
};

dta $1