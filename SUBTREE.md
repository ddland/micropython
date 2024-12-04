# Working with subtrees

Notes to keep the sub-trees organised. 

## Add another (new) subtree
First add the remote:
```
git remote add -f HANDLE https://github.com/address/repo.git
```
then squash the remote into the repository:
```
git subtree add --prefix NEWDIR HANDLE main --squash
```

## Updates subs
Pull the updates into the overview repository without all the history (squash)
```
git subtree pull --prefix NEWDIR HANDLE main --squash
```
