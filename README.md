# 2026blog - 超级简单版

这是一个不需要密钥、不需要 Cloudflare、不需要网页登录配置的个人博客。

完整的傻瓜操作与原理说明在：[2026blog-超级简单操作手册.pdf](./output/pdf/2026blog-超级简单操作手册.pdf)

## 你只要认识三个文件

| 双击哪个文件 | 它做什么 |
| --- | --- |
| `①-双击预览网站.cmd` | 在这台电脑上打开博客，先看效果。 |
| `②-停止本地预览.cmd` | 关闭刚才的本机博客。 |
| `③-双击发布到GitHub.cmd` | 把博客上传到 GitHub；GitHub 会自动更新公开网站。 |

不要双击 `node_modules`、`src` 或 `scripts` 里的任何文件。

## 第一次使用

1. 双击 `③-双击发布到GitHub.cmd`。
2. 浏览器会打开 GitHub 新建仓库页面。仓库名必须是 **DSlandhou.github.io**，选择 **Public**，不要添加 README、`.gitignore` 或 License。
3. 创建完成后，回到这个文件夹，再双击一次 `③-双击发布到GitHub.cmd`。
4. 第一次 Git 可能会让你在浏览器登录 GitHub；完成登录后，如果窗口提示失败，再双击一次即可。
5. 打开 GitHub 的新仓库 → **Settings** → **Pages** → Source 选择 **GitHub Actions**。
6. 约一分钟后，你的网站地址是 `https://dslandhou.github.io/`。

## 最简单的写笔记方法

1. 双击 `①-双击预览网站.cmd`。
2. 浏览器打开后点击右上角“写一条”。
3. 写标题和正文，点击“下载笔记文件”。
4. 打开 Windows 的“下载”文件夹，把刚下载的 `.md` 文件拖进 `2026blog/src/content/notes`。
5. 双击 `③-双击发布到GitHub.cmd`。

## 换一台电脑也能写

不用安装任何软件：登录 GitHub → 打开 `DSlandhou/DSlandhou.github.io` 仓库 → 进入 `src/content/notes` → **Add file** → **Create new file**。文件名写成 `2026-07-28-note.md`，粘贴手册里的 Markdown 模板，点击 **Commit changes**。一分钟后网站会自动更新。

## 想改简历

在 VS Code 中只打开并修改 `src/data/profile.ts`，保存后双击预览网站。满意后双击发布文件。

## 这个版本刻意没有的功能

“在公开网页上直接发布到 GitHub”需要服务器、登录授权和密钥。为了让你放心上手，这个版本把它改成了“网页写作 → 下载笔记 → 拖进文件夹 → 双击发布”。这是更稳定、也更容易理解的第一步。
