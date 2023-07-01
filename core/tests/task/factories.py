from factory.django import DjangoModelFactory
from factory import SubFactory
from factory.faker import Faker


from tests.accounts.factories import ProfileFactory
from enums.task import TaskPriority, TaskStatus
from tests.base import BaseFactory


class CategoryFactory(DjangoModelFactory, BaseFactory):
    name = Faker('name')

    class Meta:
        model = 'task.Category'


class TaskFactory(DjangoModelFactory, BaseFactory):
        
    author = SubFactory(ProfileFactory)
    title = Faker('text')
    content = Faker('sentence')
    status = TaskStatus.PUBLISHED
    category = SubFactory(CategoryFactory)
    priority = TaskPriority.LOW

    class Meta:
        model = 'task.Task'