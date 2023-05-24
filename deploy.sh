theme=$(awk '/^theme/{print $3}' tools.conf)
theme_repo_url=$(awk '/^theme_repo_url/{print $3}' tools.conf)
theme_repo_branch=$(awk '/^theme_repo_branch/{print $3}' tools.conf)
theme_clone_cache=theme

echo 'Pulling theme repository.'
git clone -b $theme_repo_branch $theme_repo_url $theme_clone_cache
echo 'Pulling done.'
echo 'Merging Start.'
rm -rf $theme_clone_cache/deploy/.git
cp -rf $theme_clone_cache/deploy/* .
rm -rf $theme_clone_cache
echo 'Merging End.'
