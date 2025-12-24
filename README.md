你希望我直接生成这个 PDF 版本吗？ -->
## ? 项目界面展示（UI Preview）

<p align="center">
    <img src="./Logo.png" width="200"/>
</p>

---

## ?? 界面预览
### ? 登录界面

<p align="center">
    <img src="./preview/lonin.png" width="420"/>
</p>

### ? 首页界面

<p align="center">
    <img src="./preview/home.png" width="420"/>
</p>

### ? 功能界面

<p align="center">
    <img src="./preview/function.png" width="420"/>
</p>

### ? 充电界面

<p align="center">
    <img src="./preview/charging.png" width="420"/>
</p>

### ?? 关于界面

<p align="center">
    <img src="./preview/about.png" width="420"/>
</p>

> 图示：基于 **Qt Widgets + PySide6** 构建的桌面应用界面

---

## ? 界面概述

* **开发工具**：Qt Widgets Designer + PySide6
* **整体风格**：简洁直观，突出核心功能入口
* **设计原则**：

  * UI 与业务逻辑解耦
  * 模块化界面结构，便于维护与扩展

---

## ? 主要界面元素

### ? 核心信息

* **项目名称**：`Uang Asura`（居中展示）
* **统一视觉风格**：图标与背景资源通过 Qt 资源系统统一管理

### ? 登录模块

* 密钥输入框（支持 **密码隐藏 / 显示切换**）
* 登录按钮（校验通过后进入主程序）

### ? 功能入口

* **购买密钥**：跳转获取测试密钥（教学 / 演示用途）
* **官方网站**：通过超链接跳转至项目主页

---

## ?? 技术实现要点

* Qt Widgets + Qt Designer 可视化设计
* PySide6 信号与槽机制
* 界面模块化拆分（便于后期扩展账号体系、权限验证等功能）
* 资源统一管理（`.qrc`）