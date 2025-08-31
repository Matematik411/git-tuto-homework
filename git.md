Reseting the branch 
`git reset #COMMIT`

The branch goes back to the `#COMMIT`, this can be commit id or just `HEAD~1` (or `~1`) for one commit back.

Reset can be 
- default keeps changes unstaged
- `--soft` changes are staged
- `--hard` changes are deleted


If the commits were pushed already, you need to 
`git push origin main --force`.
*Only do this if you’re sure no one else depends on that commit.*