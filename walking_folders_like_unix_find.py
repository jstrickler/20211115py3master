import os
import pwd


starting_dir = "."
# starting_dir = os.path.abspath(starting_dir)

dirs_to_skip = ['__pycache__', '.git', '.idea']
for folder_name, dir_list, file_list in os.walk(starting_dir):
    for dir_name in dirs_to_skip:
        if dir_name in dir_list:
            dir_list.remove(dir_name)
    print(folder_name)
    for file_name in file_list:
        if file_name.endswith('.py'):
            file_path = os.path.join(folder_name, file_name)
            file_size = os.path.getsize(file_path)
            user_id = os.stat(file_path).st_uid
            group_id = os.stat(file_path).st_gid
            pw_info = pwd.getpwuid(user_id)
            user_name = pw_info.pw_name
            if file_size > 1000:
                print(f"    {file_size:6d} {file_name} {user_id} {user_name}")

# equal to id -Gn
import pwd, grp

def getgroups(user):
    gids = [g.gr_gid for g in grp.getgrall() if user in g.gr_mem]
    gid = pwd.getpwnam(user).pw_gid
    gids.append(grp.getgrgid(gid).gr_gid)
    return [grp.getgrgid(gid).gr_name for gid in gids]

print(getgroups("jstrick"))
