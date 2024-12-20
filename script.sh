#!/bin/bash

clean_up_build_fragments() {
    rm quicko
    cp ./dist/quicko ./
}

replace_binary() {
    FILE_PATH="./quicko"

    # Check if the file exists
    if [ -e "$FILE_PATH" ]; then
        rm ~/bin/quicko
        cp quicko ~/bin
    else
        echo "Error: The binary does not exists."
    fi

}

# Run a specific function based on input
"$@"