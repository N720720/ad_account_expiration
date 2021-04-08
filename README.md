# ad_account_expiration

Set the expiration of Active Directory accounts to a specific date for all users in a txt file. The dates for the end of the winter semester(WS) and summer semester(SS) are calculated automatically, but you can also set a custom date. The program changes the regular names in the text file to user names expected by Active Directory.

## Usage

```console
python ad.py file_path [Options]
```

**Positional**:

* `file_path`     The Path to your file with the names of the employes
  
**Options**:

* `-WS`: Set the AD accounts expiration date to the end of the Wintersemester(WS).
* `-SS`: Set the AD accounts expiration date to the end of the Sommersemester(SS).
* `-D dd/mm/yyyy`: Set the AD accounts expiration date use dd/mm/yyyy e.g. 01/04/2021.
* `-h, --help`: Show this message and exit.

**File Structure:**

Enter the names for which you want to set a new expiration date in a txt file. For example, open Notepad, paste the names as below, and save them as `names.txt`.

***Note:***

German umlauts are OK and will be changed to ae, ue, etc. Middle names are removed by the script because they are not needed in this case. Upper case letters are changed to lower case letters.

```txt
First Lastname
First Middle Lastname
Max Mustermann
Mäx Müstermann
Mäx Klaus Michael ... Müstermann

```

The format of the user name is the first character of the first name plus the last name. E.g. flastname or mmustermann.
