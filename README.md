## Overview
Simple Python CLI tool to create JSON files with dummy data to use for testing. Uses dataclasses to define schemas so it can be easily customized to create new data exports.

Uses Faker to generate the data as defined in the schema.

## Requirements
Python 3.7+

## Install Dependencies
`pip install faker dataclasses-json`

## Usage

`python generator.py --type [TYPE] --count [COUNT] [--output FILENAME]`

The example:

`python generator.py --type User --count 500`

Will generate a JSON file with 500 users with the default filename of "fakeUser-[timestamp].json"

## Schemas

Check the `modules/schema.py` file to see the default schemas of User, Blog, and Product. You can add any new schemas to this file and use the class name as the "Type" when running the generator.

```
@dataclass_json
@dataclass
class User:
  id:             int = field(default_factory=lambda: random.randint(1,9999))
  username:       str = field(default_factory=lambda: fake.user_name())
  first_name:     str = field(default_factory=lambda: fake.first_name())
  last_name:      str = field(default_factory=lambda: fake.last_name())
  email:          str = field(default_factory=lambda: fake.ascii_safe_email())
  street_address: str = field(default_factory=lambda: fake.street_address())
  city:           str = field(default_factory=lambda: fake.city())
  state:          str = field(default_factory=lambda: fake.state())
  postal_code:    str = field(default_factory=lambda: fake.postcode())
  country:        str = field(default_factory=lambda: fake.country())
```
The property default factories mostly use Faker library functions. [See the Faker documentation](https://faker.readthedocs.io/en/master/) for additional values you can generate.
