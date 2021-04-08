import argparse
import subprocess
from datetime import date
from pathlib import Path
from time import sleep
from typing import Dict, List, Tuple

from dateutil.relativedelta import relativedelta


def parsing() -> Tuple[str, str]:
    parser = argparse.ArgumentParser(
        description="Set the AD account expiration date to the end of the Wintersemester(WS) or Sommersemester(SS)"
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "-WS",
        action="store_true",
        help="Set the AD accounts expiration date to the end of the Wintersemester(WS)",
    )
    group.add_argument(
        "-SS",
        action="store_true",
        help="Set the AD accounts expiration date to the end of the Sommersemester(SS)",
    )
    group.add_argument(
        "-D",
        type=str,
        metavar="dd/mm/yyyy",
        help="Set the AD accounts expiration date use dd/mm/yyyy e.g. 01/04/2021",
    )
    parser.add_argument(
        "file_path",
        type=Path,
        help="The Path to your file with the names of the employes",
    )

    args = parser.parse_args()
    filename: str = args.file_path

    if args.WS:
        today_year = date.today().year
        plus_one_year = date(today_year, 10, 1) + relativedelta(years=1)
        end_date = plus_one_year.strftime("%d/%m/%Y")

    elif args.SS:
        today_year = date.today().year
        end_date = date(today_year, 4, 1).strftime("%d/%m/%Y")

    elif args.D:
        end_date = args.D
    else:
        print("Use -WS,-SS or -D flag to set the expiration date")
        exit()

    return filename, end_date


def make_umlaut_map() -> Dict[int, str]:
    umlautDictionary: Dict[str, str] = {
        "Ä": "Ae",
        "Ö": "Oe",
        "Ü": "Ue",
        "ä": "ae",
        "ö": "oe",
        "ü": "ue",
        "ß": "ss",
    }

    umap: Dict[int, str] = {ord(key): val for key, val in umlautDictionary.items()}
    return umap


def get_usernames(filename: str, umap: Dict[int, str]) -> List[str]:
    # remove umlauts and middle names, all lower caps and join the first charakter of the first name with the lastname

    flastname_list = []
    with open(filename, "r") as names:
        for line in names:
            no_umlauts = line.translate(umap)
            f_l_no_middle = [no_umlauts.rstrip("\n").split()[e] for e in (0, -1)]
            # print(f_l_no_middle)
            f_plus_l_no_middle_lower = (
                f_l_no_middle[0][0].lower() + f_l_no_middle[1].lower()
            )
            flastname_list.append(f_plus_l_no_middle_lower)
    return flastname_list


def set_expiration(users: List[str], end_date: str) -> None:
    # Set Account Expiration for user in list.The date is not inclusive, that is 01.10.2021 is 30.09.2021
    len_user = len(users)
    print(f"Set account expiration to {end_date}")
    for index, user in enumerate(users, 1):
        print(f"Prosessing {user}")
        subprocess.call(
            f"powershell.exe Set-ADAccountExpiration {user} -DateTime {end_date}",
            shell=True,
        )
        sleep(1)
        print(f"{index}/{len_user} Done")


def main(filename, end_date) -> None:
    umap = make_umlaut_map()
    users = get_usernames(filename, umap)
    set_expiration(users, end_date)


if __name__ == "__main__":
    filename, end_date = parsing()
    main(filename, end_date)
