import os
import sys
from os.path import isfile, join
import shutil
import getpass
from distutils.dir_util import copy_tree

username = getpass.getuser()
path = os.path.join(f'/home/{username}',".dotfiles")

if len(sys.argv) == 1:
    print(
        """\nPass an arguments to make code work\n 
        > python3 main.py backup    - To make backup
        > python3 main.py restore   - To restore a previous backup
        > python3 main.py git [url] - Upload backup to git [Pending] """
    )
    sys.exit()

else:
    if sys.argv[1]=="backup":
        try :
            os.makedirs(path)
        except FileExistsError:
            print('\nOops! You have a backup already done ^-^')
            sys.exit()

        #backup_dirs = [
        #    'neofetch', 'i3', 'bspwm', 'rofi', 'polybar', 
        #    'alacritty', 'picom', 'compton', 'dunst', 
        #    'dmenu', 'ncmpcpp', 'mpv', 'nvim', 
        #    'ranger', 'sxhkd', 'termite'
        #]
        backup_dirs = [f for f in os.listdir(f'/home/{username}/.config')]

        backup_config = [
            '.zshrc', '.xinitrc', '.vimrc',
            '.Xresources', '.nanorc' , '.bashrc'
        ]
        user_configs = os.listdir(f'/home/{username}/.config')
        user_configs.sort()
                    
        conf_path = os.path.join(f'/home/{username}/.dotfiles',".config")
        os.makedirs(conf_path)


        print(f'\n---------- backing up .config/ ----------\n')
        for i in user_configs:
            yes_no = input(f'You want to backup {i} (y/n): ')
            if yes_no == 'y':
                if isfile(join(f'/home/{username}/.config', i)):
                    shutil.copy(f'/home/{username}/.config/{i}', f'/home/{username}/.dotfiles/.config')
                    print(f'Backup for {i} created ! ')
                    print("")
                else:
                    src = os.path.join(f'/home/{username}/.config/',i)
                    des = os.path.join(f'/home/{username}/.dotfiles/.config/',i)
                    shutil.copytree(src,des,False,None)
                    print(f'Backup for {i} created ! ')
                    print("")

        home_conf = [f for f in os.listdir(f'/home/{username}') if isfile(join(f'/home/{username}', f))]
        home_conf.sort()

        print(f'\n---------- backing up rc files ----------\n')
        for conf in home_conf:
            if conf in backup_config:
                yes = input(f'You want to backup {conf} (y/n): ')
                if yes == 'y':
                    shutil.copy(f'/home/{username}/{conf}', f'/home/{username}/.dotfiles/')
                    print(f'Backed up {conf} !')
                    print("")

        print(f'\n----------  Thamks For Using!  ----------\n')
    
    elif sys.argv[1] == "restore":
        check_exist = [f for f in os.listdir(f'/home/{username}')]
        if ".config" in check_exist:
            print(f'restoring configs to /home/{username} ')
            os.system(f"cp -a /home/{username}/.dotfiles/. /home/{username}")
    
    elif sys.argv[1] == 'git':
        if len(sys.argv) == 2:
            print("""
                Baka ! you dont gave me a url 

                usage :
                    > python3 backup.py git https://github.com/ashzero2/sys-backup
            """)
        else:
            url = sys.argv[2]
            os.system(f'cd /home/{username}/.dotfiles && git init && git remote add origin {url} && git add --all && git commit -m "backup" && git push origin master')

    else:
        print(
            """ 
            \nPossible arguments are :\n
            backup    - To make a backup in /home/user/.dotfiles
            restore   - Restore a previous made backup
            git [url] - Pending :-/ """
        )