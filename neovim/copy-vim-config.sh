# install dependencies for syntax highlighting
pip install neovim
npm install -g neovim

# make config folders and folder for vim plugins
mkdir -p ~/.config/nvim
mkdir -p ~/.nvimplugs

# copy neovim config, either of these is possible
cp ./init.vim ~/.config/nvim/init.vim
# cp ./.vimrc ~/.vimrc

# add sourcing to .*rc
echo 'source /usr/share/nvm/init-nvm.sh' >> ~/.zshrc
echo 'source /usr/share/nvm/init-nvm.sh' >> ~/.bashrc