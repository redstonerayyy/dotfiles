# make config folders and folder for vim plugins
mkdir -p ~/.config/nvim
mkdir -p ~/.nvimplugs

# add sourcing to .*rc
echo 'source /usr/share/nvm/init-nvm.sh' >> ~/.zshrc
echo 'source /usr/share/nvm/init-nvm.sh' >> ~/.bashrc
