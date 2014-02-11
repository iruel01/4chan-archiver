#!/bin/zsh

mkdir $2
cd $2
mkdir $3
cd $3
wget -O - $1 |
grep -Eo 'i.4cdn.org/[^"]+' |
uniq |
xargs wget
cd ../../
