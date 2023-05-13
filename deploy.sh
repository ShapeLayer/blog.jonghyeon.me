theme=$(awk '/^theme/{print $3}' tools.conf)
theme_repo_url=$(awk '/^theme_repo_url/{print $3}' tools.conf)
sh tools/clone_theme_customizer.sh
cp -rf customizer/deploy .
rm -rf customizer
