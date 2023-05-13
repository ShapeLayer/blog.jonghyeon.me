theme=$(awk '/^theme/{print $3}' tools.conf)
theme_repo_url=$(awk '/^theme_repo_url/{print $3}' tools.conf)
# sh tools/clone_theme_customizer.sh
# cp -rf customizer/deploy docs
# rm -rf customizer
# mv docs/assets/lib/.gitkeep docs/assets/lib/.gitmodules
# rm docs/.gitmodules
sh tools/merge_with_theme.sh $theme $theme_repo_url
