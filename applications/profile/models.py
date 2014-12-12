# -*- coding: utf-8 -*-
# TODO Add module docstring

from django.db import models
from django.contrib.auth.models import User

from common.base_models import TimeStampedModel


class Profile(TimeStampedModel):
    """
    # TODO add model docstring
    fields:
    user(oo)
    description
    mobile
    following_count
    follower_count
    """

class ProfileImage(TimeStampedModel):
    """
    # TODO add model docstring
    user(fk)
    image
    show
    """

class Follow(TimeStampedModel):
    """
    # TODO add model docstring

    following(f-user)
    follower(f-user)
    """
