!# /usr/bin/bash

sudo dnf install xorg-x11-server-Xorg xorg-x11-xinit
sudo dnf nano python pip
sudo dnf install bspwm sxhkd polybar picom dmenu rofi
sudo dnf install nitrogen thunar firefox geany

mkdir .config
mkdir polybar

git clone --depth=1 https://github.com/adi1090x/polybar-themes.git
cd polybar-themes
chmod +x setup.sh
./setup.sh

rm -R polybar

cd mydots
cp -R mydots/config/* .config/

chmod +x bspwm/bspwmrc
chmod +x sxhkd/sxhkdrc

echo "exec bspwm" > .xinitrc



