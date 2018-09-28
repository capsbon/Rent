@set /p dotfile=Please input dot file name:
@set /p outfile=Please input result file name:
dot -Tpng %dotfile%.dot -o %outfile%.png

cmd
