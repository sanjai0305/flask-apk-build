[app]
title = My App
package.name = myflaskapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,html,css,js,txt,db
version = 0.1
requirements = python3,kivy==2.1.0,flask,flask-cors,android
orientation = portrait
fullscreen = 0
android.permissions = INTERNET
android.api = 31
android.minapi = 21
android.entrypoint = org.kivy.android.PythonActivity

[buildozer]
log_level = 2
warn_on_root = 1