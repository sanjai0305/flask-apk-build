[app]
title = My Folder Tool
package.name = foldertool
package.domain = org.sanjai
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,html,css,js,txt,db
version = 0.1

# Requirements must include kivy and flask
requirements = python3,kivy==2.1.0,flask,flask-cors,android,requests

orientation = portrait
fullscreen = 0
android.permissions = INTERNET
android.api = 31
android.minapi = 21
android.entrypoint = org.kivy.android.PythonActivity

[buildozer]
log_level = 2
warn_on_root = 1