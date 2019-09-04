from localities.models import Locality, City, State
from industries.models import Category, SubCategory
from campaigns.models import Entity, Size


entity = Entity.objects.create(name="Logo", order=1)

size = Size.objects.create(name="Size 1", length="2.8", height="1.0")
size.entities.add(entity)
size.save()

state = State.objects.create(name="Maharashtra", short_name="MH")

city = City.objects.create(name="Pune", state=state)
locality = Locality.objects.create(city=city, name="Kondhwa", postal_code="411048")

category = Category.objects.create(name="IT", popularity="HI")

sub_category = SubCategory.objects.create(category=category, name="BPO")
