import json, argparse, time
import modules.schema as schema

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--t", "--type", help="Type of data as per the dataclass defined in schema.py. The default available options are: Blog, Product, User. You can define additional schemas in that file as well.")
    parser.add_argument("--c", "--count", help="Number of records to create. Default is 10.")
    parser.add_argument("--o", "--output", help="Filename to save the records as. The default is fake[Type]-[timestamp].json")
    args = parser.parse_args()

    if args.t is None:
        exit("Error: Missing required type")

    if args.c is None:
        args.c = 10

    class_ = getattr(schema, args.t)

    rjson = []
    if args.o is None:
        filename = "fake" + args.t + "-" + str(time.time()) + ".json";
    else:
        filename = args.o
        
    for _ in range(int(args.c)):
        obj = class_()
        rjson.append(obj.to_dict())

    json_string = json.dumps(rjson)
    with open(filename, "w") as file:
        file.write(json_string)
        
if __name__ == "__main__":
    main()