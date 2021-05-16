# -*- coding: utf-8 -*-
from tratamento import tratamento
import os

shutdown = False
os.chdir('root')
while not( shutdown):

    tratamento(input())



