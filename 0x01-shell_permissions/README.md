This project involves working with shell permissions. The list below shows each shell file.
1. 0-iam_betty -- Create a script that switches the current user to the user betty.
You should use exactly 8 characters for your command (+1 character for the new line)
You can assume that the user betty will exist when we will run your script

2. 1-whoa_am_i -- a script that prints the effective username of the current user.

3. 2-groups --  a script that prints all the groups the current user is part of.

4. 3-new_owner -- a script that changes the owner of the file hello to the user betty.

5. 4-empty -- a script that creates an empty file called hello.

6. 5-execute -- a script that adds execute permission to the owner of the file hello.

7. 6-multiple_permissions -- a script that adds execute permission to the owner and the group owner, and read permission to other users, to the file hello.
The file hello will be in the working directory

8. 7-everybody -- a script that adds execution permission to the owner, the group owner and the other users, to the file hello. The file hello will be in the working directory. You are not allowed to use commas for this script

9. 8-James_Bond -- a script that sets the permission to the file hello as follows:
Owner: no permission at all
Group: no permission at all
Other users: all the permissions
The file hello will be in the working directory You are not allowed to use commas for this script

10. 9-John_Doe -- a script that sets the mode of the file hello to this.

11. 10-mirror_permissions -- a script that sets the mode of the file hello the same as olleh’s mode. The file hello will be in the working directory. The file olleh will be in the working directory

12. 11-directories_permissions -- a script that adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users. Regular files should not be changed.

13. 12-directory_permissions -- a script that creates a directory called my_dir with permissions 751 in the working directory.

14. 13-change_group -- a script that changes the group owner to school for the file hello
The file hello will be in the working directory.

15. 100-change_owner_and_group -- a script that changes the owner to vincent and the group owner to staff for all the files and directories in the working directory.

16. 101-symbolic_link_permissions -- a script that changes the owner and the group owner of _hello to vincent and staff respectively. The file _hello is in the working directory. The file _hello is a symbolic link

17. 102-if_only -- a script that changes the owner of the file hello to betty only if it is owned by the user guillaume. The file hello will be in the working directory.

18. 103-Star_Wars -- a script that will play the StarWars IV episode in the terminal.