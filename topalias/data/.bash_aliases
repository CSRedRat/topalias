# aliases suggestion: https://github.com/CSRedRat/topalias/issues/29

# default
alias psgrep='ps aux | egrep -i $1' # process search
alias hh='history | egrep -i' # search in history
alias upd='sudo apt update && sudo apt full-upgrade -y' # update system to latest packages in release
alias grep='grep -i --color=auto'

# grc colored
alias cvs='grc --colour=auto cvs'
alias diff='grc --colour=auto diff'
alias esperanto='grc --colour=auto esperanto'
alias gcc='grc --colour=auto gcc'
alias irclog='grc --colour=auto irclog'
alias ldap='grc --colour=auto ldap'
alias log='grc --colour=auto log'
alias netstat='grc --colour=auto netstat'
alias ping='grc --colour=auto ping'
alias proftpd='grc --colour=auto proftpd'
alias traceroute='grc --colour=auto traceroute'
alias wdiff='grc --colour=auto wdiff'
alias dig='grc --colour=auto dig'
alias cat='grc --colour=auto cat'
alias zcat='grc --colour=auto zcat'
alias make='grc --colour=auto make'
alias gcc='grc --colour=auto gcc'
alias g++='grc --colour=auto g++'
alias head='grc --colour=auto head'
alias mount='grc --colour=auto mount'
alias ps='grc --colour=auto ps'
alias mtr='grc --colour=auto mtr'
alias zgrep='grc --colour=auto zgrep'
alias ll='grc --colour=auto ls -laFh --color=always'  
alias l='grc --colour=auto ls -CF --color=always'

# admin tooling
alias tcp='netstat -ltupn' # list open tcp port without sudo
alias port='sudo ss -altp' # list open tcp port with process name/PID
alias es='eval `ssh-agent -s` && ssh-add'

# docker
alias dgrep='docker ps | egrep -i $1' # docker process search
alias dcupd='docker-compose stop && docker-compose rm && docker-compose pull && docker-compose up -d' # restart & update service from docker-compose.yml config in current dir
alias dc='docker-compose'
alias dcl='docker-compose logs -f'
alias dcr='docker-compose stop && docker-compose up -d'
alias snd='sudo nano docker-compose.yml'
alias dcu='docker-compose up -d'
alias dcs='docker-compose stop'

# kubernetes
alias k='kubectl'
alias kgp='kubectl get pods,svc,ing --all-namespaces'

# git
alias gr='git rebase --continue'
