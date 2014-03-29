  #!/bin/zsh
  wget -O - $1 |
  grep -Eo 'i.4cdn.org/[^"]+' |
  uniq |
  xargs wget