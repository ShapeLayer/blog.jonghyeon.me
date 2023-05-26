theme=$(awk '/^theme/{print $3}' deploy.conf)
theme_repo_url=$(awk '/^theme_repo_url/{print $3}' deploy.conf)
theme_repo_branch=$(awk '/^theme_repo_branch/{print $3}' deploy.conf)
theme_clone_cache=theme
theme_path=$theme_clone_cache/"$theme"_deploy

echo 'Pulling theme repository.'
git clone -b $theme_repo_branch $theme_repo_url $theme_clone_cache
echo 'Pulling done.'
if [ -d $theme_path ]; then
  echo 'Merging Start.'
  rm -rf $theme_path/deploy/.git
  cp -rf $theme_path/deploy/* .
  rm -rf $theme_path
  echo 'Merging End.'
else
  echo 'Theme not found.'
fi
