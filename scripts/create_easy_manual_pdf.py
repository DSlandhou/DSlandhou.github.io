from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.platypus import KeepTogether, PageBreak, Paragraph, Preformatted, SimpleDocTemplate, Spacer, Table, TableStyle


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output" / "pdf" / "2026blog-超级简单操作手册.pdf"
OUTPUT.parent.mkdir(parents=True, exist_ok=True)

pdfmetrics.registerFont(UnicodeCIDFont("STSong-Light"))
PAPER = colors.HexColor("#F5F3EE")
INK = colors.HexColor("#151515")
MUTED = colors.HexColor("#66635D")
LINE = colors.HexColor("#D6D2CA")
LIME = colors.HexColor("#D9FF00")
SOFT = colors.HexColor("#ECE9E1")

styles = getSampleStyleSheet()
for style in [
    ParagraphStyle("Kicker", fontName="Helvetica-Bold", fontSize=9, leading=12, textColor=MUTED, spaceAfter=16),
    ParagraphStyle("Cover", fontName="STSong-Light", fontSize=34, leading=44, textColor=INK, spaceAfter=15),
    ParagraphStyle("H1", fontName="STSong-Light", fontSize=23, leading=31, textColor=INK, spaceAfter=15),
    ParagraphStyle("H2", fontName="STSong-Light", fontSize=15, leading=22, textColor=INK, spaceBefore=12, spaceAfter=7),
    ParagraphStyle("Body", fontName="STSong-Light", fontSize=10.4, leading=18, textColor=INK, spaceAfter=9),
    ParagraphStyle("Small", fontName="STSong-Light", fontSize=8.7, leading=14, textColor=MUTED, spaceAfter=7),
    ParagraphStyle("Table", fontName="STSong-Light", fontSize=9.1, leading=14, textColor=INK),
    ParagraphStyle("TableHead", fontName="STSong-Light", fontSize=9.1, leading=14, textColor=PAPER),
    ParagraphStyle("Callout", fontName="STSong-Light", fontSize=10.1, leading=17, textColor=INK),
]:
    styles.add(style)


def p(text, style="Body"):
    return Paragraph(text, styles[style])


def footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(LINE)
    canvas.setLineWidth(0.4)
    canvas.line(20 * mm, 15 * mm, A4[0] - 20 * mm, 15 * mm)
    canvas.setFillColor(MUTED)
    canvas.setFont("Helvetica", 7.5)
    canvas.drawString(20 * mm, 10 * mm, "2026BLOG / EASY MODE")
    canvas.drawRightString(A4[0] - 20 * mm, 10 * mm, str(doc.page))
    canvas.restoreState()


def title(number, name, subtitle):
    return [p(number, "Kicker"), p(name, "H1"), p(subtitle, "Small"), Spacer(1, 4)]


def step(number, name, text):
    return Table([[p(f"{number:02d}", "Small"), p(f"<b>{name}</b><br/>{text}")]], colWidths=[15 * mm, 155 * mm], style=TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LINEBELOW", (0, 0), (-1, -1), 0.5, LINE),
        ("TOPPADDING", (0, 0), (-1, -1), 6), ("BOTTOMPADDING", (0, 0), (-1, -1), 9),
    ]))


def tip(name, text):
    box = Table([[p(f"<b>{name}</b><br/>{text}", "Callout")]], colWidths=[170 * mm], style=TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#F0F8B4")),
        ("LINEBEFORE", (0, 0), (0, -1), 4, INK),
        ("LEFTPADDING", (0, 0), (-1, -1), 11), ("RIGHTPADDING", (0, 0), (-1, -1), 11),
        ("TOPPADDING", (0, 0), (-1, -1), 8), ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ]))
    return KeepTogether([box, Spacer(1, 5)])


def command(text):
    return Table([[Preformatted(text, ParagraphStyle("Code", fontName="Courier", fontSize=8.7, leading=13, textColor=INK))]], colWidths=[170 * mm], style=TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), SOFT), ("BOX", (0, 0), (-1, -1), 0.6, LINE),
        ("LEFTPADDING", (0, 0), (-1, -1), 10), ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 9), ("BOTTOMPADDING", (0, 0), (-1, -1), 9),
    ]))


def grid(rows, widths):
    wrapped = [[p(cell, "TableHead" if row_index == 0 else "Table") for cell in row] for row_index, row in enumerate(rows)]
    return Table(wrapped, colWidths=widths, style=TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), INK), ("GRID", (0, 0), (-1, -1), 0.45, LINE),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 8), ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 7), ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
    ]))


story = [
    Spacer(1, 29 * mm), p("2026BLOG / EASY MODE", "Kicker"), p("从双击文件开始", "Cover"),
    p("2026blog 超级简单操作手册", "Cover"), Spacer(1, 7 * mm),
    p("这是给第一次做网站的人写的版本。你不需要理解服务器、密钥或复杂命令；只需认识三个“可以双击”的文件，先让博客上线，再慢慢学习原理。", "Body"),
    Spacer(1, 18 * mm),
    Table([[p("最终目标", "Small"), p("写一条笔记 → 双击发布 → 一分钟后全世界都能看到", "Body")]], colWidths=[31 * mm, 139 * mm], style=TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), LIME), ("BOX", (0, 0), (-1, -1), 0.7, INK),
        ("LEFTPADDING", (0, 0), (-1, -1), 11), ("RIGHTPADDING", (0, 0), (-1, -1), 11),
        ("TOPPADDING", (0, 0), (-1, -1), 11), ("BOTTOMPADDING", (0, 0), (-1, -1), 11),
    ])),
    Spacer(1, 49 * mm), p("版本 2.0 · 简化版 · 2026-07-28", "Small"), PageBreak(),
]

story += title("先看结论", "这版到底简单在哪里？", "不再使用任何需要你保管的密码或服务器密钥。")
story += [grid([
    ["以前容易害怕的东西", "现在怎么处理"],
    ["Cloudflare、服务器、OAuth 登录", "全部移除。博客是纯静态网站，放在 GitHub Pages。"],
    ["在网页里直接上传 GitHub", "改成：网页写作 → 下载一个文件 → 拖进笔记文件夹 → 双击发布。"],
    ["输入一串 Git 命令", "改成双击“③-双击发布到GitHub.cmd”。"],
    ["换电脑后想写笔记", "直接用 GitHub 网页新增一个笔记文件，不用装任何软件。"],
], [61 * mm, 109 * mm]), Spacer(1, 14),
    tip("最重要的事实", "公开网站无法安全地把你的 GitHub 密码藏在网页里。把发布动作留在你自己的电脑或 GitHub 官方网页中，反而是最稳定、最安全的做法。"),
    p("不要着急看完全部。请从下一页开始，完成一个小动作就停下来确认一次。"), PageBreak(),
]

story += title("第 1 章", "从桌面打开文件夹", "这是你每次开始写博客的起点。")
story += [
    step(1, "回到桌面", "按键盘 Windows 键，或点击屏幕底部的 Windows 图标，选择“桌面”。找到黄色文件夹 <b>2026blog</b>。"),
    step(2, "不要先打开 VS Code", "双击 2026blog 文件夹。你会看到很多文件，但现在只需要找名称开头带圆圈数字的三个文件。"),
    step(3, "认准这三个文件", "<b>①-双击预览网站.cmd</b>、<b>②-停止本地预览.cmd</b>、<b>③-双击发布到GitHub.cmd</b>。它们是为你准备的按钮。"),
    step(4, "以后再用 VS Code", "只有想改简历资料时，才在文件夹空白处点右键 → 通过 Code 打开。平时写笔记根本不需要先打开 VS Code。"),
    tip("原理小课：.cmd 是什么？", ".cmd 是 Windows 的“小帮手脚本”。双击它时，电脑会按预先写好的顺序执行任务。你不必记住 Git 命令，但脚本仍在用 Git 做可靠的版本记录。"),
    PageBreak(),
]

story += title("第 2 章", "先把博客在本机打开", "这一步不会上传任何东西，也不会改变网站。")
story += [
    step(1, "双击第一个文件", "双击 <b>①-双击预览网站.cmd</b>。会出现一个黑色小窗口，请不要关闭它。"),
    step(2, "等待浏览器打开", "约 3 - 10 秒后，浏览器会自动打开 http://localhost:4321。看见你的主页就是成功。"),
    step(3, "随便看看", "点击简历、笔记、Now、写一条。这只是你电脑里的预览，其他人看不到。"),
    step(4, "结束时", "不用时，双击 <b>②-停止本地预览.cmd</b>。黑色窗口会关闭，浏览器页面也不再可用，这是正常的。"),
    tip("原理小课：localhost", "localhost 的意思是“这台电脑自己”。它像你在房间里摆了一块白板：只有你能看。等你发布后，GitHub Pages 才像把白板挂到公共展览墙上。"),
    PageBreak(),
]

story += title("第 3 章", "第一次把网站放上 GitHub", "这一章只需要做一次，以后只要双击发布文件。")
story += [
    step(1, "双击第三个文件", "双击 <b>③-双击发布到GitHub.cmd</b>。第一次时，它会自动打开 GitHub 的新建仓库页面。"),
    step(2, "按要求创建仓库", "Repository name 必须填 <b>DSlandhou.github.io</b>。选择 <b>Public</b>。不要勾选 Add a README、.gitignore 或 License。点击 Create repository。"),
    step(3, "回到文件夹再双击一次", "现在再双击 <b>③-双击发布到GitHub.cmd</b>。如果浏览器要求 Git 登录，请确认是 DSlandhou 账号后允许。"),
    step(4, "等窗口说成功", "看到“成功上传”就可以关闭窗口。第一次需要一两分钟是正常的。"),
    tip("为什么仓库名这么特别？", "GitHub 对“用户名.github.io”有一个特殊规则：它会把这个仓库直接变成你的个人网站首页。于是网站地址很好记：<b>https://dslandhou.github.io/</b>。"),
    PageBreak(),
]

story += title("第 4 章", "只点一次 GitHub Pages 设置", "这是 GitHub 的开关，让它知道要把仓库变成网站。")
story += [
    step(1, "打开新仓库", "浏览器打开 GitHub，进入 <b>DSlandhou/DSlandhou.github.io</b>。"),
    step(2, "进入设置", "点仓库上方的 <b>Settings</b>。如果屏幕较窄，可能藏在右侧或下拉菜单里。"),
    step(3, "找到 Pages", "在左边菜单找到 <b>Pages</b> 并点击。"),
    step(4, "选择 GitHub Actions", "在 Source（来源）选项中选择 <b>GitHub Actions</b>。做完后不用再设置。"),
    step(5, "等一会儿", "回到仓库上方的 Actions。绿色勾代表发布成功。约一分钟后访问 https://dslandhou.github.io/。"),
    tip("原理小课：自动发布", "每次你发布一个新版本，GitHub Actions 会自动运行项目里的发布说明，先生成静态网页，再替你放到 GitHub Pages。你不需要自己上传网站文件。"),
    PageBreak(),
]

story += title("第 5 章", "最简单的本机写笔记方法", "这是你平时最推荐使用的方式。")
story += [
    step(1, "预览网站", "双击 <b>①-双击预览网站.cmd</b>，等待浏览器打开。"),
    step(2, "进入写作页", "点击右上角的“写一条”。正常填写标题、标签和正文即可，不会有复杂的格式要求。"),
    step(3, "下载笔记", "点击“下载笔记文件”。浏览器会把一个名字像 <b>2026-07-28-note-120000.md</b> 的文件放进“下载”文件夹。"),
    step(4, "拖进博客", "按 Windows 键，搜索“下载”并打开。再打开桌面的 2026blog → src → content → notes。把刚下载的 .md 文件用鼠标拖到 notes 文件夹里。"),
    step(5, "先看效果，再发布", "刷新本机网站的笔记页面，确认文章出现；满意后双击 <b>③-双击发布到GitHub.cmd</b>。"),
    tip("原理小课：Markdown", ".md 是 Markdown 文件。它是普通文字文件，但开头的小资料能告诉博客文章的标题、日期和标签。它不像 Word 那样被某个软件锁住，十年后也能打开。"),
    PageBreak(),
]

story += title("第 6 章", "换一台电脑，也能直接写", "这种方法只需要浏览器和 GitHub 登录。")
story += [
    step(1, "登录 GitHub", "在任意电脑的浏览器打开 github.com，登录 DSlandhou。"),
    step(2, "进入笔记文件夹", "打开仓库 DSlandhou/DSlandhou.github.io → 依次点击 src → content → notes。"),
    step(3, "新建文件", "点击 Add file → Create new file。文件名写：<b>2026-07-28-note.md</b>。日期可换成当天，note 后面也可写英文小标题。"),
    step(4, "粘贴模板", "把下面模板复制进编辑器，替换标题、描述和正文。"),
    command('---\ntitle: "我的新笔记"\ndescription: "用一句话说这篇笔记。"\npublishedAt: 2026-07-28\ntags: ["随想"]\ndraft: false\n---\n\n从这里开始写正文。'),
    step(5, "提交并等待", "点击页面下方绿色的 Commit changes。约一分钟后刷新你的网站，文章就出现了。"),
    tip("原理小课：同一份真相", "不论你在自己电脑拖进文件，还是在 GitHub 网页新建文件，最终都是往同一个仓库放一份 .md 笔记。这就是两台电脑同步的原因。"),
    PageBreak(),
]

story += title("第 7 章", "改简历只改一个文件", "先写笔记，等熟悉后再慢慢改主页。")
story += [
    step(1, "打开项目", "在桌面打开 2026blog 文件夹，空白处点右键 → 通过 Code 打开。"),
    step(2, "只找 profile.ts", "左侧点开 src → data → <b>profile.ts</b>。只改引号里面的文字，例如 name、email、headline、currentFocus。"),
    step(3, "保存", "按 Ctrl + S。不要删除逗号、方括号、引号或大括号。"),
    step(4, "预览并发布", "双击第一个文件预览，觉得满意后双击第三个文件发布。"),
    tip("原理小课：资料与页面分开", "profile.ts 只存“你是谁、你想做什么”；网页负责把资料排成好看的样子。两者分开，能让你改资料时不伤到网站的外观。"),
    PageBreak(),
]

story += title("第 8 章", "三个最基本的原理", "懂一点点，就不会害怕。")
story += [grid([
    ["词语", "人话解释"],
    ["Git", "项目的时光机。每次发布都会留下一个可回退的版本。"],
    ["GitHub", "放在网上的项目保险箱，也是另一台电脑能访问到的共同文件夹。"],
    ["GitHub Pages", "把保险箱里的博客文件变成公开网站的服务。"],
    ["静态网站", "网页在发布前就做好了；访问的人只读取它，所以快、稳定、几乎不用维护。"],
    ["Markdown", "用普通文字写文章的小格式。你的每条笔记都是一份 .md 文件。"],
], [47 * mm, 123 * mm]), Spacer(1, 14),
    p("这版博客的路线只有一条：<b>笔记文件 → GitHub 仓库 → GitHub 自动生成网站 → 读者看到文章</b>。中间没有你需要保管的密码。"),
    tip("你真正需要形成的习惯", "写完先预览，再发布。每次只改一件小事。这样即使发生问题，也很容易知道刚才改了哪里。"),
    PageBreak(),
]

story += title("第 9 章", "不害怕报错的小守则", "红色文字不是失败，是电脑在说“我还差一点信息”。")
story += [grid([
    ["看到什么", "先怎么做"],
    ["预览网页打不开", "等 10 秒后刷新；确认黑色窗口没有被关闭；不行就双击②停止，再双击①预览。"],
    ["发布窗口说没有改动", "这是正常的：说明没有新文件。只有新增笔记或保存资料后才需要发布。"],
    ["发布窗口第一次打开 GitHub", "正常，登录 DSlandhou 并允许。完成后再双击③一次。"],
    ["GitHub 网站没更新", "去仓库的 Actions 看有没有绿色勾；通常等待 1 - 2 分钟后再刷新。"],
], [53 * mm, 117 * mm]), Spacer(1, 15),
    p("如果需要我帮忙，请发：1) 你双击的是哪一个文件；2) 黑色窗口里完整的红色文字截图；3) 你本来期待发生什么。<b>不要发送密码或 GitHub token。</b>"),
    Spacer(1, 20), p("今天只做第一步就很好。", "H2"),
    p("从桌面打开 2026blog，双击“①-双击预览网站.cmd”。看见首页，就已经在成为这个博客的主人了。"),
]

doc = SimpleDocTemplate(str(OUTPUT), pagesize=A4, rightMargin=20 * mm, leftMargin=20 * mm, topMargin=20 * mm, bottomMargin=22 * mm, title="2026blog 超级简单操作手册", author="Gatsby")
doc.build(story, onFirstPage=footer, onLaterPages=footer)
print(OUTPUT)
