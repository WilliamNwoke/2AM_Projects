git add .

echo 'Enter the commit message: '
read commitMessage

git commit -m "$commitMessage"

echo 'Enter the name of the branch: '
read branch

# for azure push, enter branch name as azure-atlas-setup
# azure-atlas-setup
git push origin $branch