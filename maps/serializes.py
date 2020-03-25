from django.core.serializers import serialize
from maps.models import Person,PersonManager

data = serialize('json', Person.objects.all())
