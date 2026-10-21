[app]

# 应用标题与包名
title = LotteryApp
package.name = lotteryapp
package.domain = org.lottery

# 包含的文件后缀
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,csv,txt

# 版本号
version = 1.0.0

# 所需依赖（根据项目实际需要的库添加）
requirements = python3,kivy,requests

# 屏幕方向 (portrait 为竖屏)
orientation = portrait
fullscreen = 0

# Android 权限与系统版本设置
android.permissions = INTERNET,ACCESS_NETWORK_STATE,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1
