<!-- ![登录界面截图](./Logo.png)
## 项目界面展示（UI Preview）

### 登录界面
![登录界面截图](./preview/lonin.png)
### 首页界面
![首页界面截图](./preview/home.png)
### 功能界面
![功能界面截图](./preview/function.png)
### 充电界面
![充电界面截图](./preview/charging.png)
### 关于界面
![关于界面截图](./preview/about.png)

> *图：基于 Qt Widgets 的程序登录界面设计*

### 界面说明

* 本界面使用 **Qt Widgets Designer** 进行设计
* 采用 **Python + Qt6（PySide6）** 实现界面逻辑
* 界面整体风格简洁，突出功能入口

### 主要元素说明

* **项目名称展示**：

  * 中央显示项目名称 **Uang Asura**，用于标识程序身份

* **用户输入区域**：

  * 密钥输入框（支持密码隐藏显示）
  * 登录按钮，用于进入主程序界面

* **功能链接**：

  * “购买密钥”：引导用户获取测试用密钥（教学演示用途）
  * “官网”：用于跳转至项目相关页面（示例功能）

* **背景与图标**：

  * 使用本地资源文件加载背景图片
  * Logo 与界面资源通过 Qt 资源系统（`.qrc`）统一管理

---

## 界面设计说明

* 界面与业务逻辑分离

  * UI 由 `.ui` 文件负责
  * 行为逻辑在 Python 代码中实现

* 采用 **模块化设计思想**

  * 登录界面作为独立模块
  * 便于后续扩展权限验证、账号体系等功能

---

## 技术实现要点（UI 部分）

* Qt Widgets
* Qt Designer
* PySide6
* Qt 资源系统（QRC）
* Python 信号与槽机制 -->


<center> <img src="./logo.png" width="200"/> </center>

<center>
# 项目界面展示（UI Preview）

## 登录界面

<img src="./preview/lonin.png" width="400"/>

## 首页界面

<img src="./preview/home.png" width="400"/>

## 功能界面

<img src="./preview/function.png" width="400"/>

## 充电界面

<img src="./preview/charging.png" width="400"/>

## 关于界面

<img src="./preview/about.png" width="400"/>

> *图：基于 Qt Widgets 的程序登录界面设计*
</center>
---

## 界面说明

* **工具与框架**：Qt Widgets Designer + PySide6
* **界面风格**：简洁，突出功能入口
* **设计理念**：UI 与业务逻辑分离，模块化设计

---

## 主要元素

* **项目名称**：中央显示 **Uang Asura**
* **用户输入**：

  * 密钥输入框（支持密码隐藏/显示）
  * 登录按钮进入主程序
* **功能链接**：

  * “购买密钥”：获取测试密钥（教学演示）
  * “官网”：跳转项目主页
* **资源管理**：背景与图标通过 Qt 资源系统（`.qrc`）统一管理

---

## 技术要点

* Qt Widgets + Qt Designer
* PySide6 信号与槽
* 模块化界面设计（便于后续扩展账号体系与权限验证）

---

如果你需要，我可以帮你生成一个 **更紧凑的 PDF 预览文档**，包含压缩后的图片，方便展示给其他人。

你希望我直接生成这个 PDF 版本吗？
