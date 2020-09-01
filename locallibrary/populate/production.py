from populate import base
from users.models import User

print('create admin account')
User.objects.create_superuser(username='ch3coch3',password='ch3coch3hpt',email=None,fullname='管理者')
print('done')
