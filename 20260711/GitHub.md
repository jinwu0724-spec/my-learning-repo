# GitHub 远程仓库管理

## 0.简介

用 Git 把你电脑上的本地仓库（local）和 GitHub 网站上的仓库（remote）连接起来，然后进行同步管理。

[^]: 版本管理很重要的 V

### Conventional Commits

git commit -m "feat:  添加新功能"
git commit -m "fix:   修复BUG"
git commit -m "docs:  文档修改"
git commit -m "style: 样式/格式调整（不影响逻辑）"
git commit -m "refactor: 代码重构"
git commit -m "test: c测试内容"
git commit -m "chore: 杂项（构建、配置、依赖等）"

## 1.配置环境

### 1.1.安装 [Git](https://git-scm.com/)

官方资源：[Git Install](https://git-scm.com/install/)

安装教程：[Git 详细安装教程](https://blog.csdn.net/mukes/article/details/115693833)

[^]: 如果你只是一位初学者，全程“next”即可

### 1.2.创建 [GitHub](https://github.com/) 仓库

### 1.3.连接仓库资源

|  ID  |                          Connection                          |
| :--: | :----------------------------------------------------------: |
|  0   |     若你的GitHub上预先创建仓库，那么继续push你的项目即可     |
|  1   | 若你的GitHub上没有预先创建仓库，一般在你提交你的项目之后会默认创建 your-code-repo |

### 1.4.推送push内容

[^]: 如果有空余时间可以学习对应的git指令，可以“不会敲”，但需要“能看懂”

## 附录

### 参考博客（按照推荐优先级进行排序）

#### [GitHub 與 VS Code 新手連接教學](https://wiki.interaction.tw/index.php/Tool:VS_Code_%2B_GitHub)

#### [vscode如何连接github/gitee远程仓库详细步骤（ssh+https）最全最详细](https://blog.csdn.net/Bin_niB/article/details/135915738)

#### [在 Visual Studio Code 中使用 GitHub Codespaces](https://docs.github.com/zh/codespaces/developing-in-a-codespace/using-github-codespaces-in-visual-studio-code)

通过将Visual Studio Code扩展与GitHub Codespaces帐户连接，您可以直接在GitHub中开发您的代码空间。