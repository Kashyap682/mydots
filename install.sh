!# /usr/bin/bash

sudo dnf install xorg-x11-server-Xorg xorg-x11-xinit
sudo dnf nano python pip
sudo dnf install bspwm sxhkd polybar picom dmenu rofi
sudo dnf install nitrogen thunar firefox geany

mkdir .config

git clone --depth=1 https://github.com/adi1090x/polybar-themes.git
cd polybar-themes
chmod +x setup.sh
./setup.sh

rm -R .config/polybar

cd mydots
mv -R mydots/config/* .config/

chmod +x .config/bspwm/bspwmrc
chmod +x .config/sxhkd/sxhkdrc

echo "exec bspwm" > .xinitrc

echo "Done."
