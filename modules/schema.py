import random
from faker import Faker
from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from faker.providers import internet, address, company

fake = Faker()
fake.add_provider(internet)
fake.add_provider(address)
fake.add_provider(company)

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

@dataclass_json
@dataclass
class Blog:
  id:       int = field(default_factory=lambda: random.randint(1, 9999))
  title:    str = field(default_factory=lambda: fake.text(60))
  author:   str = field(default_factory=lambda: fake.name())
  date:     str = field(default_factory=lambda: str(fake.date_between()))
  category: str = field(default_factory=lambda: fake.word())
  content:  str = field(default_factory=lambda: fake.paragraph(10))
  image:    str = field(default_factory=lambda: fake.image_url())

@dataclass_json
@dataclass
class Product:
  id:           int = field(default_factory=lambda: random.randint(1, 9999))
  title:        str = field(default_factory=lambda: fake.text(20))
  price:        str = field(default_factory=lambda: fake.pricetag())
  tagline:      str = field(default_factory=lambda: fake.catch_phrase())
  category:     str = field(default_factory=lambda: fake.word())
  description:  str = field(default_factory=lambda: fake.paragraph(10))
  image:        str = field(default_factory=lambda: fake.image_url())