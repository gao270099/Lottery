[app]

# 应用基本信息
title = LotteryApp
package.name = lotteryapp
package.domain = org.lottery

# 包含的文件类型
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,csv,txt

version = 1.0.0

# 运行依赖
requirements = python3,kivy,requests

orientation = portrait
fullscreen = 0

# 权限设置
android.permissions = INTERNET,ACCESS_NETWORK_STATE,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

# 核心参数：自动接受 SDK 许可协议（必须开启）
android.accept_sdk_license = True

# 保持稳定兼容版本
android.api = 33
android.minapi = 21
android.ndk = 25b

# 仅构建 64 位架构（大幅提高编译成功率与速度，适配绝大多数安卓手机）
android.archs = arm64-v8a
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1
