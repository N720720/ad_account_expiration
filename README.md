# ad_account_expiration
Set Active Directory account expiration to a specific date for all users in a txt file. 
## Usage
```console
ad.py file_path [Options]
```
**Positional**:
`file_path`     The Path to your file with the names of the employes
  
**Options**:

* `-WS`: Set the AD accounts expiration date to the end of the Wintersemester(WS).
* `-SS`: Set the AD accounts expiration date to the end of the Sommersemester(SS).
* `-D dd/mm/yyyy`: Set the AD accounts expiration date use dd/mm/yyyy e.g. 01/04/2021.
* `-h, --help`: Show this message and exit.
