#!/bin/bash

clean_up_build_fragments() {
    rm quicko
    cp ./dist/quicko ./
}

replace_binary() {
    OLD_FILE="~/bin/quicko"
    NEW_FILE="./quicko"

    if [ -e "$OLD_FILE" ]; then
        rm ~/bin/quicko
    fi
    
    if [ -e "$NEW_FILE" ]; then
        cp quicko ~/bin
    else
        echo "Error: The binary does not exists."
    fi

}

# Run a specific function based on input
"$@"