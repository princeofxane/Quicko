# ReadMe

Quicko is a client to fetch notes from storage location and opens in vim.

## Config file.
Place the config file at below location for quicko to pick it up.
We do it because the binary does not support to have a config file embedded so far. 

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

## Makefile targets
`make build` creates the binary to deletes the files and folder the build process leaves behind.
Cleaning the files may slow down the build process. If testing remove the `clean` command.

`deposit` removes current binary from ~/bin/ and place newly built binary here.

