# -*- coding: utf-8 -*-

from __future__ import division, unicode_literals


class Pet(object):
    def __init__(self, name, sound):
        super(Pet, self).__init__()
        try:
            self.name = name.encode('utf-8').decode('utf-8')
        except AttributeError:
            self.name = name
        try:
            self.sound = sound.encode('utf-8').decode('utf-8')
        except AttributeError:
            self.sound = sound

    def speak(self):
        return '{}!'.format(self.sound.upper())

    def come_here(self):
        return 'Here, {}, here!'.format(self.name)

    def __str__(self):
        return self.__unicode__()

    def __unicode__(self):
        return self.name


class Dog(Pet):
    def __init__(self, name, sound, age=None):
        super(Dog, self).__init__(name, sound)
        self.age = age

    @property
    def dog_years(self):
        return self.age / 7
