# Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.zshrc.
# Initialization code that may require console input (password prompts, [y/n]
# confirmations, etc.) must go above this block; everything else may go below.

# powerlevel10k
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

# some default configure for zsh
HISTFILE=~/.histfile
HISTSIZE=1000
SAVEHIST=1000
bindkey -v



export EDITOR="nvim"
export VISUAL="nvim"

### SET MANPAGER
#### Uncomment only one of these! 

#### "bat" as manpager 
export MANPAGER="sh -c 'col -bx | bat -l man -p'" 

#### "vim" as manpager 
# export MANPAGER='/bin/bash -c "vim -MRn -c \"set buftype=nofile showtabline=0 ft=man ts=8 nomod nolist norelativenumber nonu noma\" -c \"normal L\" -c \"nmap q :qa<CR>\"</dev/tty <(col -b)"' 

#### "nvim" as manpager 
# export MANPAGER="nvim -c 'set ft=man' -"

# Aliases
# ----->>> !!! thier is no spaces when you write an alias
alias toxclip='xclip -selection c'
alias powersaving='sudo cpupower frequency-set -g powersave'
alias ls='ls --color=auto'
alias grep='grep --color=auto'
alias paci='sudo pacman -S'
alias pacu='sudo pacman -R'
alias pacs='sudo pacman -Ss'
alias icat='kitty +kitten icat'
# alias shutdown='sudo shutdown now'
alias shutdown='shutdown now'
alias reboot='reboot'
# alias reboot='sudo reboot'
alias u='sudo pacman -Syu'
alias cpf='copyfile'
alias cpd='copypath'
alias nd='neovide'
alias cd='z'
alias paclist='sudo pacman -Qm'
alias go='google-chrome-stable'
# alias cat='bat'

# --->> plugins section 

# loading powerlevel10
source ~/powerlevel10k/powerlevel10k.zsh-theme

# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh

# zsh-completion-settings
source /home/mahmoud/zsh-plugins/completion.zsh

# zsh-syntax-highlighting
source /home/mahmoud/zsh-plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh

# zsh-autosuggestions
source /home/mahmoud/zsh-plugins/zsh-autosuggestions/zsh-autosuggestions.zsh

# changing the cursor mode in vi-mode zsh
# cursor_mode plugin
source /home/mahmoud/zsh-plugins/cursor_mode.zsh

# zsh copypath 
source /home/mahmoud/zsh-plugins/copypath.plugin.zsh

# zsh-websearch
source /home/mahmoud/zsh-plugins/web_search.zsh
 
# zsh-sudo-plugin
source /home/mahmoud/zsh-plugins/sudo.plugin.zsh

# zsh-copyfile-plugin
source /home/mahmoud/zsh-plugins/copyfile.plugin.zsh


# dealing with fzf
source /usr/share/fzf/completion.zsh
source /usr/share/fzf/key-bindings.zsh

# zoxide-utility
export _ZO_ECHO=1
eval "$(zoxide init zsh)"

# Gem
path+=('/home/mahmoud/.local/share/gem/ruby/3.0.0/bin')
export PATH
