# -*- coding: utf-8 -*-
# TODO docstring
from django.db import models

from common.base_models import TimeStampedModel


class Post(TimeStampedModel):
    """
    # TODO add model docstring
    user(f=user)
    image
    tags(mm-user)
    likes_count
    """

class Like(TimeStampedModel):
    """
    # TODO add model docstring

    post
    user
    """

