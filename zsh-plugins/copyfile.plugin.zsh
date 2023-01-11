# Copies the contents of a given file to the system or X Windows clipboard
#
# copyfile <file>
function copyfile {
  emulate -L zsh
  xclip -selection c $1
}
