import uuid

from app.models import TimestampedModel
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser, TimestampedModel):
    public_id = models.UUIDField(
        unique=True, editable=False, default=uuid.uuid4, db_index=True
    )
