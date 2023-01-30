# get oh-my-zsh, be careful if link is working
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

# install znap, zsh managing tool
git clone --depth 1 -- https://github.com/marlonrichert/zsh-snap.git
source zsh-snap/install.zsh

