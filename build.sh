echo "Activating virtual environment ..."
source .venv/Scripts/activate

function build() {
echo "Building python source files ..."
pyinstaller.exe --onefile $1 --name $2 --add-data ".venv/Lib/site-packages/riscv_assembler/data/*;data" --clean

echo "Deleting temporary files ..."
[ -d "__pycache__" ] && rm __pycache__ -fr
[ -d "build" ] && rm build -fr
[ -f *.spec ] && basename *.spec | xargs rm

echo "----------[DONE]----------"
}

echo $#
if [ $# -eq 0 ]
then
    # if there is only one python file, use that name as the exe output name
    if [ "$(ls -lr ./*.py | wc -l)" -eq 1 ]
    then
        FILENAME="$(basename *.py)"
        build $FILENAME "${FILENAME%.*}"
    else
        echo "Please specify the entry file of the python script"
        exit 1
    fi
fi

if [ $# -eq 1 ]
then
    if [ -f $1 ] 
    then
        build $1 "${1%.*}"
    else
        echo "There is no python file with this name"
        exit 1
    fi
fi

if [ $# -eq 2 ] 
then
    if [ -f $1 ] 
    then
        build $1 "${2%.*}"
    else
        echo "There is no python file with this name"
        exit 1
    fi

fi
