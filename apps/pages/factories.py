import factory
from .models import News,Comments
from faker import Faker

fake = Faker()

class NewsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = News
    title = factory.Faker("sentence")
    description = factory.Faker("paragraph")
    status = factory.Faker("boolean")

class CommentsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Comments

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    comment_text = factory.Faker("text") 
    news = factory.SubFactory(NewsFactory)
    status = factory.Faker("boolean")