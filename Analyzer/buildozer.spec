[app]

title = Analyzer
package.name = analyzer
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1

requirements = python3,kivy,openssl,pyopenssl,certifi,pillow

orientation = portrait
fullscreen = 0

android.permissions = android.permission.INTERNET, android.permission.ACCESS_NETWORK_STATE, android.permission.ACCESS_WIFI_STATE

# Stable Android toolchain (IMPORTANT)
android.api = 30
android.minapi = 21
android.sdk = 30
android.ndk = 23b
android.ndk_api = 21
android.accept_sdk_license = True

# Build only one architecture (simpler + faster for CI)
android.archs = arm64-v8a

android.allow_backup = True
android.debug_artifact = apk

# Use stable bootstrap
p4a.bootstrap = sdl2
p4a.branch = master


[buildozer]

log_level = 2
warn_on_root = 1
