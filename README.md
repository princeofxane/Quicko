# ReadMe

## Description
Quicko is a client to fetch notes from storage location and opens in vim.

## Setup
### Config file.
Place the config file at below location for quicko to pick it up.
Else it will build the default configuration from the map present in *config.py*

* location: `/home/{user}/.config/quicko/config.yaml`

## Print the list
To list out the list of notes present use this command.
```
quicko list
```

## Fetching a note.
To fetch python note.
```
quicko python -n
```
## Fetching doubts.
To fetch python note.
```
quicko python -d
```


## Building binary
`make build` creates the binary to deletes the files and folder the build process leaves behind.
Cleaning the files may slow down the build process. If testing remove the `clean` command.
