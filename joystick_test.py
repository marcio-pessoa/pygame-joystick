#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
---
name: joystick_test.py
description: Test Joystick package
copyright: 2019-2019 Márcio Pessoa
people:
  developers:
  - name: Márcio Pessoa
    email: marcio.pessoa@gmail.com
change-log:
  2019-08-31
  - version: 0.1
    added: timer tests
"""

import sys
import time
import json
import pygame
from joystick import Joystick, detect

# Detect and initialize joystick
JOYSTICK = Joystick()
for _ in range(10):
    if detect():
        JOYSTICK.identification(detect()[0])
        break
    time.sleep(10 / 1000)

# Exit if no joystick connected
if JOYSTICK.identification() is None:
    print("Joystick not found.")
    sys.exit(True)

# Display joystick configuration
print("Joystick configuration:")
print(json.dumps(JOYSTICK.configuration(),
                 indent=2,
                 separators=(", ", ": ")))

pygame.init()  # pylint: disable=no-member

# Loop until the user clicks the close button.
DONE = False

# Used to manage how fast the screen updates.
CLOCK = pygame.time.Clock()

while not DONE:
    # Check user actions
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # pylint: disable=no-member
            DONE = True
        elif event.type == pygame.KEYDOWN:  # pylint: disable=no-member
            print("*****************************")
            DONE = True
        elif event.type == pygame.JOYAXISMOTION:  # pylint: disable=no-member
            print(JOYSTICK.axis())
        elif event.type == pygame.JOYBALLMOTION:  # pylint: disable=no-member
            print(JOYSTICK.ball())
        elif event.type == pygame.JOYBUTTONDOWN:  # pylint: disable=no-member
            print(JOYSTICK.button())
        elif event.type == pygame.JOYBUTTONUP:  # pylint: disable=no-member
            print(JOYSTICK.button())
        elif event.type == pygame.JOYHATMOTION:  # pylint: disable=no-member
            print(JOYSTICK.hat())


        print(json.dumps(JOYSTICK.all(),
                         indent=2,
                         separators=(", ", ": ")))

    # Limit to 20 frames per second.
    CLOCK.tick(20)

pygame.quit()  # pylint: disable=no-member
