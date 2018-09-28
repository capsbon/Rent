
@set /p dotfile=Please input dot file name:
dot -Tpng %dotfile% -o %dotfile:~0,-4%.png

cmd
