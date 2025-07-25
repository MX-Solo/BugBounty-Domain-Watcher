import argparse
from mymongo import MongoOperations

def main():
    parser = argparse.ArgumentParser(description="Domain Management Tool")
    parser.add_argument("-d", "--domain", help="Specify the domain.")
    parser.add_argument("-a", "--add", action="store_true", help="Add a new domain.")
    parser.add_argument("-r", "--remove", action="store_true", help="Remove a domain.")
    parser.add_argument("-s", "--status", nargs='?', const=True, default=False, help="Filter by status.")
    parser.add_argument("-t", "--tech", nargs='?', const=True, default=False, help="Filter by technologies.")
    parser.add_argument("-sc", "--status-changed", action="store_true", help="Filter by status change.")
    parser.add_argument("-tc", "--tech-changed", action="store_true", help="Filter by technology change.")
    parser.add_argument("-f", "--fresh", action="store_true", help="Filter by freshness.")
    parser.add_argument("-os", "--only-sub", action="store_true", help="Retrieve only subdomains.")
    parser.add_argument("-ac", "--active", action="store_true", help="Scan active subdomains.")

    args = parser.parse_args()

    if not args.domain:
        print("Please provide a domain using the -d option.")
        return

    mongo_ops = MongoOperations(args.domain)

    if args.add:
        mongo_ops.add_domain(args.active)
    elif args.remove:
        mongo_ops.remove_domain()
    elif args.fresh:
        mongo_ops.get_fresh(args.only_sub)
    elif args.status_changed:
        mongo_ops.get_status_changed(args.only_sub)
    elif args.tech_changed:
        mongo_ops.get_tech_changed(args.only_sub)
    elif args.status:
        mongo_ops.filter_status(args.status, args.only_sub)
    elif args.tech:
        mongo_ops.filter_tech(args.tech, args.only_sub)
    else:
        mongo_ops.get_full(args.only_sub)

if __name__ == "__main__":
    main()
