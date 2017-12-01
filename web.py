#!/usr/bin/env python
import os
import sys
import subprocess
import signal

PORT = 8000

def start_fe():
  p = subprocess.Popen('npm run dev', cwd='fe', shell=True, close_fds=True)
  print 'fe process: %d'%p.pid
  return p

def start_server():
  cmd = 'python manage.py runserver 0.0.0.0:%d'%PORT
  p = subprocess.Popen(cmd, shell=True, close_fds=True)
  print 'server process: %d'%p.pid
  return p

def listen_input(p_fe, p_server):
  print 'what do you want ? (stop):'
  command = raw_input()
  if command == 'stop':
    if p_fe is not None:
      ret = os.system('kill -f %d'%p_fe.pid)
      print 'kill fe process ret:%d'%ret
    if p_server is not None:
      ret = os.system('kill -f %d'%p_server.pid)
      print 'kill server process ret:%d'%ret
    pass
  else:
    listen_input(p_fe, p_server)

def run():
  p_fe = start_fe()
  p_server = start_server()
  listen_input(p_fe, p_server)

run()
