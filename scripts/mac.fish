source common.fish

#set DEBUG "True"

echo "Making directories..."
run mkdir -p $HOME/dev/backpack
run mkdir -p $HOME/dev/megaproj

echo "Installing Rust toolkit..."
run rustup-init
run fish_add_path ~/.cargo/bin
    
echo "Installing Heroku and Firebase tools:"
echo "Heroku..."
run npm install -g heroku
echo "Firebase.."
run npm install -g firebase-tools

echo "Setting up Ruby..."
run fish_add_path /usr/local/opt/ruby/bin
run gem update --system
    
echo "Setting up fish shell..."
run mkdir -p $HOME/.config/fish
run cp -r fish $HOME/.config/fish