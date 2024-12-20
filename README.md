# ReadMe

## Description
Quicko is a client to fetch notes from storage location and opens in vim.


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

