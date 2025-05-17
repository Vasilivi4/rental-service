import factory
from .models import Apartment
from faker import Faker
from apps.users.models import User  # Импорт кастомной модели

fake = Faker()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = factory.Faker("email")
    password = factory.PostGenerationMethodCall(
        "set_password",
        "defaultpassword"
    )
    # Другие поля модели, если есть


class ApartmentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Apartment

    name = factory.LazyAttribute(lambda x: fake.street_name() + " Apartment")
    slug = factory.Faker("slug")
    description = factory.LazyAttribute(lambda x: fake.text(max_nb_chars=200))
    price = factory.LazyAttribute(
        lambda x: round(fake.random_number(digits=6, fix_len=True) / 100, 2)
    )
    number_of_rooms = factory.LazyAttribute(
        lambda x: fake.random_int(min=1, max=5)
    )
    square = factory.LazyAttribute(
        lambda x: round(fake.random_number(digits=3, fix_len=True) / 10, 2)
    )
    availability = factory.LazyAttribute(lambda x: fake.boolean())
    owner = factory.SubFactory(UserFactory)
