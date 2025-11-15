import argparse
from sync_manager import sync_folders


def main():
    parser = argparse.ArgumentParser(description="Synchronyze content of two folders (source and destination)")
    parser.add_argument(
        "--source",
        required = True,
        help = "Type source folder path"
    )
    parser.add_argument(
        "--dest",
        required = True,
        help = "Type destination folder path"
    )
    parser.add_argument(
        "--delete",
        action =  "store_true", #If the --delete flag is specified in the command line, then args.delete = True.
        help = "Delete all file in destination folder that no longer exists"
    )

    args = parser.parse_args()
    sync_folders(args.source, args.dest, args.delete)


if __name__ == "__main__":
    main()