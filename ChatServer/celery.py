import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ChatServer.settings')

app = Celery('ChatServer')

# Load task modules from all registered Django app configs.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Discover tasks in Django apps automatically.
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

# Periodic task schedule
app.conf.beat_schedule = {
    'delete-expired-files-daily': {
        'task': 'messaging.tasks.delete_expired_files',
        'schedule': crontab(hour=0, minute=0),
    },
}
