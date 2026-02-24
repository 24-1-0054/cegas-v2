NOTE FOR PEARSON: code is incomplete, but should pass all Ps

# How to Use
Find hardware recommendations and libraries at: ./reports/physical-design.md

## Running (for users)
From this directory, enter this command through your terminal: 
`python3 app/src/cli.py`

Alternatively, it can be run from any directory without issues, as long as
the path is correct.

## Commands (for users)
The program will remind you of all commands in the beginning and after every
prompt. 

"Functions:"
"(1) Create student\n"
"(2) Enroll student\n"
"(3) Record score\n"
"(4) List reports\n"
"(5) Rank top-N by average%\n"
"(0) Exit\n"

The program takes IDs for all inputs. These can be seen in the csv datafiles.
Assuming a Linux system, your admin should have permissions for you to use the 
`less` command, which opens a file in read-only mode. Use this to find the IDs
you need as written in the schema and `.csv` files.

## Backups (for developers)
Windows support is in progress, but all .csv files can be now copied via 
`backup.sh`, a bash script.

Alternatively, one can copy all .csv files by hand.