[app]

# (str) Title of your application
title = Analyzer

# (str) Package name
package.name = analyzer

# (str) Package domain (reverse domain notation)
package.domain = org.test

# (str) Source code directory
source.dir = .

# (str) List of included file extensions
source.include_exts = py,png,jpg,kv,atlas

# (str) Application version
version = 0.1

# (list) Python requirements
requirements = python3==3.9,kivy,pyjnius,openssl,pyopenssl,certifi,pillow

# (str) Orientation: portrait, landscape, all
orientation = portrait

# (int) Fullscreen: 0 for no, 1 for yes
fullscreen = 0

# (list) Android permissions
android.permissions = android.permission.INTERNET, android.permission.ACCESS_NETWORK_STATE, android.permission.ACCESS_WIFI_STATE

# --- Android toolchain settings ---

# (int) Android API target
android.api = 33

# (int) Minimum Android API your app supports
android.minapi = 21

# NDK version
android.ndk = 25b
android.ndk_api = 21

# Accept SDK license automatically
android.accept_sdk_license = True

# Architectures to build (simpler + faster)
android.archs = arm64-v8a

# Allow app backup
android.allow_backup = True

# Debug artifact
android.debug_artifact = apk

# Use stable SDL2 bootstrap
p4a.bootstrap = sdl2
