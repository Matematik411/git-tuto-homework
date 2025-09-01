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

---

Checking the status  
`git status`

Shows which files are staged, unstaged, or untracked.  
Useful to see what will be committed.

---

Staging changes  
`git add <file>`

Adds the specified file to the staging area.  
Use `git add .` to stage all changes in the current directory.

---

Committing changes  
`git commit -m "your message"`

Creates a new commit with the staged changes and the given message.

---

Viewing commit history  
`git log`

Shows a list of previous commits in the current branch.  
Use `git log --oneline` for a shorter summary.

---

Discarding local changes  
`git checkout -- <file>`

Reverts the specified file to the last committed state.  
*Warning: This deletes local changes in that file.*