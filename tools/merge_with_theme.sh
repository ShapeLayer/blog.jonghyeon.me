echo 'Pulling theme repository.'
git clone $2
echo 'Pulling done.'
echo 'Merging theme file to documentations.'
rm -rf $1/.git
cp -rf $1/* .
rm -rf $1
echo 'Merging done.'