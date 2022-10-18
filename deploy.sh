theme=$(awk '/^theme/{print $3}' tools.conf)
theme_repo_url=$(awk '/^theme_repo_url/{print $3}' tools.conf)
sh tools/merge_with_theme.sh $theme $theme_repo_url
