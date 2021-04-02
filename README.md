# Dots - Backup [WIP]

A simple python script to take backup of application config files. Sorry but this is messy i worked on this to learn python. This script will only work on **unix** based operating systems which follows **xdg-home** structure.

## Usage

> python3 main.py [options]

where options can be
  ```
  backup    - To backup config to $HOME/.dotfiles
  restore   - To restore existing backup
  git [url] - To upload the backup to github
  ```
  
## To-Do
- [x] Finish uploading backup to github
- [ ] Add restore from github
