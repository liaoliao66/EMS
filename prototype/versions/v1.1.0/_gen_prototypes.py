# -*- coding: utf-8 -*-
"""Generate EMS v1.0.0 PC + WeCom H5 prototypes from PRD scope."""
from pathlib import Path
import html

ROOT = Path(__file__).resolve().parent
PAGES = ROOT / "pages"
WECOM = ROOT / "pages" / "wecom"
ASSETS = ROOT / "assets"
PAGES.mkdir(parents=True, exist_ok=True)
WECOM.mkdir(parents=True, exist_ok=True)
ASSETS.mkdir(parents=True, exist_ok=True)

NAV = [
    ("基础配置", [
        ("设备清单", "基础配置_设备清单_page.html", "fa-list"),
        ("保养标准", "基础配置_保养标准_page.html", "fa-clipboard-check"),
        ("点巡检标准", "基础配置_点巡检标准_page.html", "fa-tasks"),
        ("参数配置", "基础配置_参数配置_page.html", "fa-sliders"),
    ]),
    ("设备运营", [
        ("运营设备", "设备运营_运营设备_page.html", "fa-industry"),
        ("投保记录", "设备运营_投保记录_page.html", "fa-shield-halved"),
        ("理赔记录", "设备运营_理赔记录_page.html", "fa-file-invoice-dollar"),
        ("设备租赁", "设备运营_设备租赁_page.html", "fa-handshake"),
        ("设备报废", "设备运营_设备报废_page.html", "fa-recycle"),
        ("设备处置", "设备运营_设备处置_page.html", "fa-box-archive"),
    ]),
    ("点巡检管理", [
        ("点巡检区域", "点巡检_点巡检区域_page.html", "fa-map-location-dot"),
        ("点巡检记录", "点巡检_点巡检记录_page.html", "fa-clipboard-list"),
    ]),
    ("保养管理", [
        ("保养通知", "保养管理_保养通知_page.html", "fa-bell"),
        ("保养计划", "保养管理_保养计划_page.html", "fa-calendar-check"),
        ("保养完工", "保养管理_保养完工_page.html", "fa-flag-checkered"),
    ]),
    ("设备维修", [
        ("故障通知", "设备维修_故障通知_page.html", "fa-triangle-exclamation"),
        ("故障报修", "设备维修_故障报修_page.html", "fa-wrench"),
        ("维修计划", "设备维修_维修计划_page.html", "fa-calendar-days"),
        ("维修派工", "设备维修_维修派工_page.html", "fa-user-gear"),
        ("维修完工", "设备维修_维修完工_page.html", "fa-circle-check"),
    ]),
    ("运行管理", [
        ("加油记录", "运行管理_加油记录_page.html", "fa-gas-pump"),
    ]),
]


def badge(text, kind="muted"):
    return f'<span class="badge badge-{kind}">{text}</span>'


def pc_shell(title, active_file, body, extra_js=""):
    nav_html = []
    for group, items in NAV:
        nav_html.append(f'<div class="nav-group px-4 pt-4 pb-1 text-[11px] uppercase">{group}</div>')
        for name, file, icon in items:
            active = "active" if file == active_file else ""
            nav_html.append(
                f'<a class="nav-link {active} mx-2 mb-1 flex items-center gap-2 rounded-xl px-3 py-2 text-sm" href="{file}">'
                f'<i class="fa-solid {icon} w-4 text-center opacity-80"></i><span>{name}</span></a>'
            )
    nav = "\n".join(nav_html)
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
  <title>{title} · EMS v1.0.0</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css" />
  <link rel="stylesheet" href="../assets/common.css" />
</head>
<body class="min-h-screen">
  <div class="flex min-h-screen">
    <aside class="sidebar sticky top-0 flex h-screen w-60 shrink-0 flex-col overflow-y-auto text-white">
      <div class="border-b border-white/10 px-4 py-5">
        <div class="text-xs text-slate-400">智能设备管理 EMS</div>
        <div class="mt-1 text-base font-semibold">PC 业务端 · v1.0.0</div>
      </div>
      <nav class="flex-1 pb-6">{nav}</nav>
      <div class="border-t border-white/10 p-4 text-xs text-slate-400">
        <a class="hover:text-white" href="../index.html">返回版本入口</a>
      </div>
    </aside>
    <div class="flex min-w-0 flex-1 flex-col">
      <header class="sticky top-0 z-20 border-b border-slate-200 bg-white/90 backdrop-blur">
        <div class="mx-auto flex max-w-7xl items-center justify-between px-6 py-3">
          <div>
            <div class="text-sm font-semibold text-slate-900">{title}</div>
            <div class="text-xs text-slate-500">业务功能原型 · 不含消息/审批/权限页</div>
          </div>
          <div class="flex items-center gap-3">
            <div class="hidden md:block">
              <input class="input w-64" placeholder="业务内搜索编号/名称" />
            </div>
            <div class="flex h-9 w-9 items-center justify-center rounded-full bg-slate-100 text-slate-600">
              <i class="fa-solid fa-user text-sm"></i>
            </div>
          </div>
        </div>
      </header>
      <main class="flex-1 px-6 py-6">
        <div class="mx-auto max-w-7xl">{body}</div>
      </main>
    </div>
  </div>
  <div id="toast" class="toast"></div>
  <script src="../assets/common.js"></script>
  <script>{extra_js}</script>
</body>
</html>
"""


def filters(fields):
    items = []
    for f in fields:
        if f.get("type") == "select":
            opts = "".join(f'<option>{o}</option>' for o in f["options"])
            items.append(
                f'<div><label class="mb-1 block text-xs text-slate-500">{f["label"]}</label>'
                f'<select class="select">{opts}</select></div>'
            )
        else:
            items.append(
                f'<div><label class="mb-1 block text-xs text-slate-500">{f["label"]}</label>'
                f'<input class="input" placeholder="{f.get("ph","请输入")}" /></div>'
            )
    return (
        '<div class="card-soft mb-4 p-4">'
        '<div class="grid grid-cols-1 gap-3 md:grid-cols-4">'
        + "".join(items)
        + '</div>'
        '<div class="mt-3 flex gap-2">'
        '<button class="btn-brand px-4 py-2 text-sm" onclick="toast(\'已按条件筛选（原型）\')">查询</button>'
        '<button class="btn-ghost px-4 py-2 text-sm" onclick="toast(\'已重置\')">重置</button>'
        "</div></div>"
    )


def table_block(headers, rows, actions_note=""):
    th = "".join(f'<th class="px-3 py-3 font-semibold text-slate-600">{h}</th>' for h in headers)
    trs = []
    for r in rows:
        tds = "".join(f'<td class="px-3 py-3 text-slate-700">{c}</td>' for c in r)
        trs.append(f'<tr class="table-row border-t border-slate-100">{tds}</tr>')
    note = f'<div class="mt-2 text-xs text-slate-400">{actions_note}</div>' if actions_note else ""
    return f"""
    <div class="card-soft overflow-hidden">
      <div class="overflow-x-auto">
        <table class="w-full min-w-[880px] text-left text-sm">
          <thead class="bg-slate-50"><tr>{th}</tr></thead>
          <tbody>{''.join(trs)}</tbody>
        </table>
      </div>
      <div class="flex items-center justify-between border-t border-slate-100 px-4 py-3 text-sm text-slate-500">
        <span>共 {len(rows)} 条</span>
        <div class="flex gap-2">
          <button class="btn-ghost px-3 py-1.5 text-xs">上一页</button>
          <button class="btn-brand px-3 py-1.5 text-xs">1</button>
          <button class="btn-ghost px-3 py-1.5 text-xs">下一页</button>
        </div>
      </div>
    </div>{note}
    """


def _is_lightbox_target(label, href):
    if not href.endswith(".html"):
        return False
    keys = ("新增", "添加", "选择", "选取", "协议")
    return any(k in label or k in href for k in keys)


def page_header(title, desc, primary=None, secondary=None):
    btns = []
    for item, ghost in ((secondary, True), (primary, False)):
        if not item:
            continue
        label, action = item
        cls = "btn-ghost" if ghost else "btn-brand"
        if action.endswith(".html"):
            if _is_lightbox_target(label, action):
                btns.append(
                    f'<button type="button" class="{cls} px-4 py-2 text-sm" onclick="openLightbox(\'{action}\')">{label}</button>'
                )
            else:
                btns.append(f'<a class="{cls} px-4 py-2 text-sm" href="{action}">{label}</a>')
        else:
            onclick = action[3:] if action.startswith("js:") else action
            btns.append(
                f'<button type="button" class="{cls} px-4 py-2 text-sm" onclick="{onclick}">{label}</button>'
            )
    return f"""
    <div class="mb-4 flex flex-wrap items-end justify-between gap-3">
      <div>
        <h1 class="text-xl font-bold text-slate-900">{title}</h1>
        <p class="mt-1 text-sm text-slate-500">{desc}</p>
      </div>
      <div class="flex flex-wrap gap-2">{''.join(btns)}</div>
    </div>
    """


def ops(*links):
    parts = []
    for text, href in links:
        if href.startswith("js:"):
            parts.append(f'<button class="text-teal-700 hover:underline" onclick="{href[3:]}">{text}</button>')
        elif _is_lightbox_target(text, href) or ("编辑" in text and href.endswith(".html")):
            parts.append(
                f'<button class="text-teal-700 hover:underline" onclick="openLightbox(\'{href}\')">{text}</button>'
            )
        else:
            parts.append(f'<a class="text-teal-700 hover:underline" href="{href}">{text}</a>')
    return '<div class="flex flex-wrap gap-2">' + "".join(parts) + "</div>"


def modal_shell(title, body, back_url, extra_js=""):
    """新增/选择类页面：灯箱弹窗内容（iframe 内）或独立打开时的灯箱外观。"""
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
  <title>{title} · 弹窗 · EMS v1.0.0</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css" />
  <link rel="stylesheet" href="../assets/common.css" />
</head>
<body class="modal-page">
  <div id="root" class="modal-page-panel">
    <div class="sticky top-0 z-10 flex items-center justify-between border-b border-slate-100 bg-white px-5 py-3">
      <div>
        <div class="text-sm font-semibold text-slate-900">{title}</div>
        <div class="text-xs text-slate-500">弹窗 · 灯箱样式 · 不含审批/消息/权限</div>
      </div>
      <button type="button" class="lightbox-close static" onclick="closeModalOrBack('{back_url}')" aria-label="关闭">
        <i class="fa-solid fa-xmark"></i>
      </button>
    </div>
    <div class="flex-1 overflow-auto px-5 py-4">{body}</div>
  </div>
  <div id="toast" class="toast"></div>
  <script src="../assets/common.js"></script>
  <script>
    (function(){{
      const embed = new URLSearchParams(location.search).get('embed') === '1';
      if(!embed){{
        document.body.classList.add('standalone-lightbox');
        const root = document.getElementById('root');
        root.classList.add('standalone-panel');
        root.classList.remove('modal-page-panel');
      }}
    }})();
    {extra_js}
  </script>
</body>
</html>
"""


# ---------- Page definitions ----------
pages = {}

pages["基础配置_设备清单_page.html"] = page_header(
    "设备清单", "设备基础数据模板，供运营设备引用。",
    ("新增", "基础配置_设备清单_新增.html"),
) + filters([
    {"label": "搜索", "ph": "设备编号/名称"},
    {"label": "设备类型", "type": "select", "options": ["全部", "起重设备", "输送设备", "动力设备"]},
]) + table_block(
    ["设备编号", "设备名称", "设备类型", "设备属性", "创建时间", "操作"],
    [
        ["EQ-T-001", "门式起重机", "起重设备", "生产设备", "2026-03-01", ops(("查看", "js:toast('查看详情（原型）')"), ("编辑", "基础配置_设备清单_新增.html"), ("删除", "js:confirmDelete(false)"))],
        ["EQ-T-002", "皮带输送机", "输送设备", "生产设备", "2026-03-05", ops(("查看", "js:toast('查看详情（原型）')"), ("编辑", "基础配置_设备清单_新增.html"), ("删除", "js:confirmDelete(true)"))],
        ["EQ-T-003", "空压机组", "动力设备", "辅助设备", "2026-03-12", ops(("查看", "js:toast('查看详情（原型）')"), ("编辑", "基础配置_设备清单_新增.html"), ("删除", "js:confirmDelete(false)"))],
    ],
    "删除前校验是否被运营设备引用；被引用时 Toast：存在关联数据，无法删除。",
)

pages["基础配置_保养标准_page.html"] = page_header(
    "保养标准", "各类设备保养模板数据。",
    ("新增", "基础配置_保养标准_新增.html"),
) + filters([
    {"label": "搜索", "ph": "标准名称"},
    {"label": "设备类型", "type": "select", "options": ["全部", "起重设备", "输送设备"]},
]) + table_block(
    ["标准编号", "标准名称", "适用设备类型", "项目数", "创建时间", "操作"],
    [
        ["MS-001", "起重机月度保养", "起重设备", "6", "2026-02-18", ops(("查看", "js:toast('弹窗查看标准内容')"), ("编辑", "基础配置_保养标准_新增.html"), ("删除", "js:confirmAction()"))],
        ["MS-002", "输送机季度保养", "输送设备", "4", "2026-02-20", ops(("查看", "js:toast('弹窗查看标准内容')"), ("编辑", "基础配置_保养标准_新增.html"), ("删除", "js:confirmAction()"))],
    ],
)

pages["基础配置_点巡检标准_page.html"] = page_header(
    "点巡检标准", "定义巡检检查项，支持启停。",
    ("新增", "基础配置_点巡检标准_新增.html"),
) + filters([
    {"label": "启用状态", "type": "select", "options": ["全部", "启用", "禁用"]},
]) + table_block(
    ["标准编码", "标准名称", "检查项数", "启用状态", "创建时间", "操作"],
    [
        ["1001", "机械外观检查", "5", badge("启用", "ok"), "2026-01-10", ops(("查看", "js:toast('查看标准')"), ("编辑", "基础配置_点巡检标准_新增.html"), ("禁用", "js:toast('已禁用：新巡检可不填该标准')"), ("删除", "js:confirmDelete(true)"))],
        ["1002", "润滑与紧固", "3", badge("启用", "ok"), "2026-01-12", ops(("查看", "js:toast('查看标准')"), ("编辑", "基础配置_点巡检标准_新增.html"), ("禁用", "js:toast('已禁用')"), ("删除", "js:confirmDelete(false)"))],
        ["1003", "电气安全", "4", badge("禁用", "muted"), "2026-01-15", ops(("查看", "js:toast('查看标准')"), ("编辑", "基础配置_点巡检标准_新增.html"), ("启用", "js:toast('已启用')"), ("删除", "js:confirmDelete(false)"))],
    ],
)

pages["基础配置_参数配置_page.html"] = page_header(
    "参数配置", "配置点巡检/保养/故障业务通知参数；实际触达由平台消息中心执行。",
    ("保存", "js:toast('参数已保存（原型）')"),
) + """
<div class="grid grid-cols-1 gap-4 lg:grid-cols-3">
  <section class="card-soft p-5">
    <h2 class="font-semibold text-slate-900">点巡检通知</h2>
    <div class="mt-4 space-y-3 text-sm">
      <div><label class="mb-1 block text-xs text-slate-500">每日通知时间</label><input class="input" type="time" value="08:30" /></div>
      <div><label class="mb-1 block text-xs text-slate-500">通知人员</label><input class="input" value="张维保、李巡检" /></div>
      <div><label class="mb-1 block text-xs text-slate-500">渠道偏好</label>
        <select class="select"><option>站内信</option><option>企业微信</option><option>站内信+企业微信</option></select></div>
      <div class="flex items-center justify-between rounded-xl bg-slate-50 px-3 py-2"><span>通知状态</span><span class="badge badge-muted">默认关闭</span></div>
    </div>
  </section>
  <section class="card-soft p-5">
    <h2 class="font-semibold text-slate-900">保养通知</h2>
    <div class="mt-4 space-y-3 text-sm">
      <div><label class="mb-1 block text-xs text-slate-500">提前天数</label><input class="input" type="number" value="3" min="1" /></div>
      <div><label class="mb-1 block text-xs text-slate-500">通知详情模板</label><textarea class="textarea" rows="4">设备【运营设备名称】将于【下次保养日期】到期保养，请及时安排。</textarea></div>
    </div>
  </section>
  <section class="card-soft p-5">
    <h2 class="font-semibold text-slate-900">故障通知</h2>
    <div class="mt-4 space-y-3 text-sm">
      <div><label class="mb-1 block text-xs text-slate-500">通知详情模板</label><textarea class="textarea" rows="6">点巡检发现异常：【故障描述】，建议：【维修建议】，请关注设备【运营设备名称】。</textarea></div>
    </div>
  </section>
</div>
"""

# 运营设备
pages["设备运营_运营设备_page.html"] = page_header(
    "运营设备", "管理在场生产大型设备实例。",
    ("新增设备", "设备运营_运营设备_新增.html"),
    ("下载设备二维码", "js:toast('已打包下载：运营设备二维码+日期')"),
) + filters([
    {"label": "搜索", "ph": "运营设备编号/名称"},
    {"label": "设备类型", "type": "select", "options": ["全部", "起重设备", "输送设备", "动力设备"]},
    {"label": "设备来源", "type": "select", "options": ["全部", "自有", "租赁"]},
    {"label": "设备状态", "type": "select", "options": ["全部", "正常", "报废", "处置", "退租"]},
]) + table_block(
    ["运营设备编号", "名称", "类型", "来源", "设备状态", "运行状态", "维保负责人", "操作"],
    [
        ["OP-2026-001", "1号门吊", "起重设备", "自有", badge("正常", "ok"), badge("运行中", "info"), "王工",
         ops(("查看", "设备运营_运营设备_查看.html"), ("编辑", "设备运营_运营设备_新增.html"), ("复制", "js:confirmAction('确认复制该设备？将生成新编号')"), ("二维码", "js:toast('打开二维码预览')"), ("删除", "js:confirmDelete(true)"))],
        ["OP-2026-002", "2号输送线", "输送设备", "租赁", badge("正常", "ok"), badge("闲置中", "muted"), "赵工",
         ops(("查看", "设备运营_运营设备_查看.html"), ("编辑", "设备运营_运营设备_新增.html"), ("退租", "js:confirmAction('确定将此设备退租吗？此操作不可逆')"), ("二维码", "js:toast('打开二维码预览')"), ("删除", "js:confirmDelete(false)"))],
        ["OP-2025-088", "旧空压机", "动力设备", "自有", badge("报废", "danger"), "-", "钱工",
         ops(("查看", "设备运营_运营设备_查看.html"), ("删除", "js:confirmDelete(false)"))],
    ],
)

pages["设备运营_投保记录_page.html"] = page_header(
    "投保记录", "记录运营设备投保信息。", ("新增", "设备运营_投保记录_新增.html")
) + filters([
    {"label": "搜索", "ph": "投保单号/设备编号/名称"},
    {"label": "投保周期", "ph": "选择日期范围"},
]) + table_block(
    ["投保单号", "运营设备", "投保周期", "投保金额(元)", "创建时间", "操作"],
    [
        ["BX-2026-011", "OP-2026-001 / 1号门吊", "2026-01-01 至 2026-12-31", "128,000.00", "2026-01-05",
         ops(("查看", "js:toast('查看投保')"), ("编辑", "设备运营_投保记录_新增.html"), ("删除", "js:confirmDelete(true)"))],
        ["BX-2026-018", "OP-2026-002 / 2号输送线", "2026-03-01 至 2027-02-28", "56,500.00", "2026-03-02",
         ops(("查看", "js:toast('查看投保')"), ("编辑", "设备运营_投保记录_新增.html"), ("删除", "js:confirmDelete(false)"))],
    ],
)

pages["设备运营_理赔记录_page.html"] = page_header(
    "理赔记录", "基于投保记录登记理赔。", ("新增", "设备运营_理赔记录_新增.html")
) + filters([
    {"label": "搜索", "ph": "理赔单号/投保单号/设备"},
    {"label": "投保周期", "ph": "筛选投保周期"},
]) + table_block(
    ["理赔单号", "投保单号", "运营设备", "理赔日期", "理赔金额(元)", "操作"],
    [
        ["LP-2026-003", "BX-2026-011", "OP-2026-001 / 1号门吊", "2026-04-12", "8,600.00",
         ops(("查看", "js:toast('查看理赔')"), ("编辑", "设备运营_理赔记录_新增.html"), ("删除", "js:confirmAction()"))],
    ],
)

pages["设备运营_设备租赁_page.html"] = page_header(
    "设备租赁", "租赁业务单据与协议附件；提交后由平台审批回写状态。", ("新增", "设备运营_设备租赁_新增.html")
) + filters([
    {"label": "搜索", "ph": "租赁单号/设备编号/名称"},
    {"label": "业务状态", "type": "select", "options": ["全部", "草稿", "处理中", "已生效", "已驳回"]},
]) + table_block(
    ["租赁单号", "设备", "租赁周期", "数量", "租金(元)", "业务状态", "操作"],
    [
        ["ZL-2026-007", "皮带机模板 / 数量引用", "2026-05-01 至 2026-10-31", "2", "36,000.00", badge("已生效", "ok"),
         ops(("查看", "js:toast('查看租赁单')"), ("协议", "js:toast('打开协议上传（通用上传组件）')"))],
        ["ZL-2026-012", "临时叉车", "2026-06-01 至 2026-08-31", "1", "9,800.00", badge("草稿", "muted"),
         ops(("查看", "js:toast('查看')"), ("编辑", "设备运营_设备租赁_新增.html"), ("提交", "js:toast('已提交，进入平台审批')"), ("删除", "js:confirmAction()"))],
    ],
)

pages["设备运营_设备报废_page.html"] = page_header(
    "设备报废", "自有且正常设备的报废申请单据。", ("新增", "设备运营_设备报废_新增.html")
) + filters([
    {"label": "搜索", "ph": "报废编号/设备编号/名称"},
    {"label": "业务状态", "type": "select", "options": ["全部", "草稿", "处理中", "已生效", "已驳回"]},
]) + table_block(
    ["报废编号", "运营设备", "报废日期", "业务状态", "操作"],
    [
        ["BF-2026-002", "OP-2025-088 / 旧空压机", "2026-02-20", badge("已生效", "ok"),
         ops(("查看", "js:toast('查看报废单')"))],
        ["BF-2026-009", "OP-2026-001 / 1号门吊", "2026-07-01", badge("草稿", "muted"),
         ops(("查看", "js:toast('查看')"), ("编辑", "设备运营_设备报废_新增.html"), ("提交", "js:toast('已提交，进入平台审批')"), ("删除", "js:confirmAction()"))],
    ],
)

pages["设备运营_设备处置_page.html"] = page_header(
    "设备处置", "自有且正常设备的处置申请单据。", ("新增", "设备运营_设备处置_新增.html")
) + filters([
    {"label": "搜索", "ph": "处置单号/设备编号/名称"},
    {"label": "业务状态", "type": "select", "options": ["全部", "草稿", "处理中", "已生效", "已驳回"]},
]) + table_block(
    ["处置单号", "运营设备", "处置日期", "业务状态", "操作"],
    [
        ["CZ-2026-004", "OP-2024-055 / 退役卷扬", "2026-03-08", badge("已生效", "ok"),
         ops(("查看", "js:toast('查看处置单')"))],
    ],
)

pages["点巡检_点巡检区域_page.html"] = page_header(
    "点巡检区域", "区域编号映射老系统；区域二维码新增后永久不变。",
    ("新增", "点巡检_点巡检区域_新增.html"),
    ("下载点巡检二维码", "js:toast('已打包：点巡检二维码+日期')"),
) + filters([
    {"label": "搜索", "ph": "区域编号/名称、设备编号/名称"},
    {"label": "设备类型", "type": "select", "options": ["全部", "起重设备", "输送设备"]},
]) + table_block(
    ["区域编号", "区域名称", "运营设备", "启用", "操作"],
    [
        ["A-10086", "门吊行走机构", "OP-2026-001 / 1号门吊", badge("启用", "ok"),
         ops(("查看", "js:toast('查看区域')"), ("编辑", "点巡检_点巡检区域_新增.html"), ("二维码", "点巡检_点巡检区域_二维码.html"), ("删除", "js:confirmDelete(true)"))],
        ["A-10087", "输送驱动端", "OP-2026-002 / 2号输送线", badge("启用", "ok"),
         ops(("查看", "js:toast('查看区域')"), ("编辑", "点巡检_点巡检区域_新增.html"), ("二维码", "点巡检_点巡检区域_二维码.html"), ("删除", "js:confirmDelete(false)"))],
    ],
)

pages["点巡检_点巡检记录_page.html"] = page_header(
    "点巡检记录", "区分正常/异常；异常必传现场照片。",
    ("新增-正常", "点巡检_点巡检记录_新增正常.html"),
    ("新增-异常", "点巡检_点巡检记录_新增异常.html"),
) + filters([
    {"label": "搜索", "ph": "区域名称/设备编号/名称"},
    {"label": "点巡检结果", "type": "select", "options": ["全部", "正常", "异常"]},
    {"label": "业务状态", "type": "select", "options": ["全部", "草稿", "处理中", "已生效"]},
]) + table_block(
    ["巡检编号", "区域", "运营设备", "结果", "巡检时间", "业务状态", "操作"],
    [
        ["XJ-20260807-01", "门吊行走机构", "1号门吊", badge("正常", "ok"), "2026-08-07 07:40", badge("已生效", "ok"),
         ops(("查看", "js:toast('查看记录')"))],
        ["XJ-20260806-18", "输送驱动端", "2号输送线", badge("异常", "danger"), "2026-08-06 16:20", badge("已生效", "ok"),
         ops(("查看", "js:toast('查看记录')"), ("查看照片", "点巡检_点巡检记录_查看照片.html"))],
        ["XJ-20260807-09", "门吊行走机构", "1号门吊", badge("异常", "danger"), "2026-08-07 08:05", badge("草稿", "muted"),
         ops(("编辑", "点巡检_点巡检记录_新增异常.html"), ("提交", "js:toast('已提交，进入平台审批')"), ("删除", "js:confirmAction()"))],
    ],
)

pages["保养管理_保养通知_page.html"] = page_header(
    "保养通知", "业务汇总页（只读），非消息中心。"
) + filters([
    {"label": "搜索", "ph": "运营设备编号/名称"},
    {"label": "通知日期", "ph": "选择日期"},
]) + table_block(
    ["通知编号", "运营设备", "下次保养日期", "通知日期", "维保负责人", "操作"],
    [
        ["BN-20260805-01", "OP-2026-001 / 1号门吊", "2026-08-10", "2026-08-05", "王工",
         ops(("查看", "保养管理_保养通知_查看.html"))],
        ["BN-20260806-03", "OP-2026-002 / 2号输送线", "2026-08-12", "2026-08-06", "赵工",
         ops(("查看", "保养管理_保养通知_查看.html"))],
    ],
)

pages["保养管理_保养计划_page.html"] = page_header(
    "保养计划", "周期保养 / 专项保养。",
    ("新增-周期保养", "保养管理_保养计划_新增周期.html"),
    ("新增-专项保养", "保养管理_保养计划_新增专项.html"),
) + filters([
    {"label": "搜索", "ph": "计划单号/设备编号/名称"},
    {"label": "保养类型", "type": "select", "options": ["全部", "周期保养", "专项保养"]},
    {"label": "业务状态", "type": "select", "options": ["全部", "草稿", "处理中", "已生效"]},
]) + table_block(
    ["计划单号", "运营设备", "类型", "计划时间", "业务状态", "操作"],
    [
        ["BJ-2026-021", "1号门吊", "周期保养", "2026-08-10 09:00-12:00", badge("已生效", "ok"),
         ops(("查看", "js:toast('查看计划')"))],
        ["BJ-2026-028", "2号输送线", "专项保养", "2026-08-15 14:00-17:00", badge("草稿", "muted"),
         ops(("编辑", "保养管理_保养计划_新增专项.html"), ("提交", "js:toast('已提交，进入平台审批')"), ("删除", "js:confirmAction()"))],
    ],
)

pages["保养管理_保养完工_page.html"] = page_header(
    "保养完工", "派工登记与完工验收；作业时间不可交叉。",
    ("新增", "保养管理_保养完工_新增.html"),
) + filters([
    {"label": "搜索", "ph": "完工单号/计划单号/设备"},
    {"label": "保养类型", "type": "select", "options": ["全部", "周期保养", "专项保养"]},
]) + table_block(
    ["完工单号", "计划单号", "运营设备", "验收日期", "下次保养", "业务状态", "操作"],
    [
        ["BW-2026-015", "BJ-2026-021", "1号门吊", "2026-08-10", "2026-09-10", badge("已生效", "ok"),
         ops(("查看", "js:toast('查看完工单')"))],
        ["BW-2026-019", "BJ-2026-028", "2号输送线", "2026-08-07", "-", badge("草稿", "muted"),
         ops(("编辑", "保养管理_保养完工_新增.html"), ("提交", "js:toast('已提交，进入平台审批')"), ("删除", "js:confirmAction()"))],
    ],
)

pages["设备维修_故障通知_page.html"] = page_header(
    "故障通知", "本期来源：点巡检立即维修建议（只读汇总）。"
) + filters([
    {"label": "搜索", "ph": "运营设备编号/名称"},
    {"label": "通知时间", "ph": "选择日期"},
]) + table_block(
    ["通知编号", "来源", "运营设备", "通知时间", "摘要", "操作"],
    [
        ["GN-20260806-02", "点巡检-立即维修", "2号输送线", "2026-08-06 16:35", "驱动端异响，建议立即维修",
         ops(("查看", "设备维修_故障通知_查看.html"))],
    ],
)

pages["设备维修_故障报修_page.html"] = page_header(
    "故障报修", "驱动故障状态机：待计划→待维修→待派工→待验收→已完工。",
    ("新增", "设备维修_故障报修_新增.html"),
) + filters([
    {"label": "搜索", "ph": "运营设备编号/名称"},
    {"label": "故障状态", "type": "select", "options": ["全部", "待计划", "待维修", "待派工", "待验收", "已完工"]},
    {"label": "严重程度", "type": "select", "options": ["全部", "一般", "严重", "紧急"]},
]) + table_block(
    ["报修单号", "运营设备", "故障类型", "严重程度", "发生时间", "故障状态", "操作"],
    [
        ["GZ-2026-044", "2号输送线", "机械故障", badge("紧急", "danger"), "2026-08-06 16:10", badge("待派工", "warn"),
         ops(("查看", "js:toast('查看报修')"), ("删除", "js:confirmDelete(true)"))],
        ["GZ-2026-039", "1号门吊", "电气故障", badge("一般", "muted"), "2026-07-28 10:20", badge("已完工", "ok"),
         ops(("查看", "js:toast('查看报修')"))],
    ],
)

pages["设备维修_维修计划_page.html"] = page_header(
    "维修计划", "一故障可多计划；已派工不可作废。", ("新增", "设备维修_维修计划_新增.html")
) + filters([
    {"label": "搜索", "ph": "计划单号/设备编号/名称"},
    {"label": "状态", "type": "select", "options": ["全部", "草稿", "处理中", "已生效", "已作废"]},
]) + table_block(
    ["计划单号", "故障单号", "运营设备", "计划维修时间", "状态", "操作"],
    [
        ["WJ-2026-031", "GZ-2026-044", "2号输送线", "2026-08-07 09:00", badge("已生效", "ok"),
         ops(("查看", "js:toast('查看计划')"), ("作废", "js:toast('存在派工记录，无法作废')"))],
        ["WJ-2026-033", "GZ-2026-044", "2号输送线", "2026-08-08 14:00", badge("草稿", "muted"),
         ops(("编辑", "设备维修_维修计划_新增.html"), ("提交", "js:toast('已提交，进入平台审批')"), ("删除", "js:confirmAction()"))],
    ],
)

pages["设备维修_维修派工_page.html"] = page_header(
    "维修派工", "一计划一次派工。", ("新增", "设备维修_维修派工_新增.html")
) + filters([
    {"label": "搜索", "ph": "派工单号/计划单号/设备"},
    {"label": "维修时间", "ph": "时间范围"},
]) + table_block(
    ["派工单号", "维修计划", "运营设备", "维修时间", "操作"],
    [
        ["WP-2026-022", "WJ-2026-031", "2号输送线", "2026-08-07 09:00-11:30",
         ops(("查看", "js:toast('查看派工')"), ("编辑", "设备维修_维修派工_新增.html"), ("删除", "js:confirmDelete(false)"))],
    ],
)

pages["设备维修_维修完工_page.html"] = page_header(
    "维修完工", "一故障一次验收，回显关联计划与派工。", ("新增", "设备维修_维修完工_新增.html")
) + filters([
    {"label": "搜索", "ph": "完工单号/故障单号/设备"},
    {"label": "业务状态", "type": "select", "options": ["全部", "草稿", "处理中", "已生效"]},
]) + table_block(
    ["完工单号", "故障单号", "运营设备", "验收日期", "业务状态", "操作"],
    [
        ["WW-2026-017", "GZ-2026-039", "1号门吊", "2026-07-29", badge("已生效", "ok"),
         ops(("查看", "js:toast('查看完工')"))],
        ["WW-2026-021", "GZ-2026-044", "2号输送线", "2026-08-07", badge("草稿", "muted"),
         ops(("编辑", "设备维修_维修完工_新增.html"), ("提交", "js:toast('已提交，进入平台审批')"), ("删除", "js:confirmAction()"))],
    ],
)

pages["运行管理_加油记录_page.html"] = page_header(
    "加油记录", "可选正常/保养中/维修中设备。", ("新增", "运行管理_加油记录_新增.html")
) + filters([
    {"label": "搜索", "ph": "运营设备编号/名称"},
    {"label": "加油日期", "ph": "选择日期"},
]) + table_block(
    ["记录编号", "运营设备", "油类/油号", "加油日期", "业务状态", "操作"],
    [
        ["JY-2026-055", "1号门吊", "液压油 / 46#", "2026-08-01", badge("已生效", "ok"),
         ops(("查看", "js:toast('查看加油记录')"))],
        ["JY-2026-061", "2号输送线", "齿轮油 / 220#", "2026-08-06", badge("草稿", "muted"),
         ops(("编辑", "运行管理_加油记录_新增.html"), ("提交", "js:toast('已提交，进入平台审批')"), ("删除", "js:confirmAction()"))],
    ],
)


def form_page(title, back, fields_html, footer_note=""):
    body = f"""
    <div class="pb-2">
      <div class="grid grid-cols-1 gap-4 md:grid-cols-2">{fields_html}</div>
      <p class="mt-4 text-xs text-slate-400">{footer_note or '填写完成后保存；提交后由平台审批承接。'}</p>
      <div class="mt-6 flex justify-end gap-2 border-t border-slate-100 pt-4">
        <button type="button" class="btn-ghost px-4 py-2 text-sm" onclick="closeModalOrBack('{back}')">取消</button>
        <button type="button" class="btn-brand px-4 py-2 text-sm" onclick="saveAndClose('{back}')">保存 / 提交</button>
      </div>
    </div>
    """
    return ("__MODAL__", title, back, body, "")


def field(label, control):
    return f'<div><label class="mb-1 block text-xs text-slate-500">{label}</label>{control}</div>'


def pick_btn(label, href):
    return (
        f'<button type="button" class="btn-ghost block w-full px-3 py-2 text-left text-sm" '
        f'onclick="openLightbox(\'{href}\')">{label}</button>'
    )


# Form pages
pages["基础配置_设备清单_新增.html"] = form_page(
    "新增 / 编辑设备清单", "基础配置_设备清单_page.html",
    field("设备编号", '<input class="input" placeholder="唯一编号" />')
    + field("设备名称", '<input class="input" />')
    + field("设备类型", '<select class="select"><option>起重设备</option><option>输送设备</option><option>动力设备</option></select>')
    + field("设备属性", '<select class="select"><option>生产设备</option><option>辅助设备</option></select>')
    + field("设备图片", '<input class="input" type="file" />'),
    "编辑时编号不可改。",
)

pages["基础配置_保养标准_新增.html"] = form_page(
    "新增 / 编辑保养标准", "基础配置_保养标准_page.html",
    field("标准名称", '<input class="input" />')
    + field("适用设备类型", '<select class="select" multiple><option>起重设备</option><option>输送设备</option></select>')
    + """<div class="md:col-span-2">
      <div class="mb-2 flex items-center justify-between"><label class="text-xs text-slate-500">保养项目</label>
      <button class="btn-ghost px-3 py-1 text-xs" onclick="toast('已添加一行项目')">添加项目</button></div>
      <div class="overflow-hidden rounded-2xl border border-slate-200">
        <table class="w-full text-sm"><thead class="bg-slate-50"><tr>
          <th class="px-3 py-2 text-left">保养类别</th><th class="px-3 py-2 text-left">保养内容</th><th class="px-3 py-2">操作</th>
        </tr></thead><tbody>
          <tr class="border-t"><td class="px-3 py-2"><input class="input" value="润滑" /></td>
          <td class="px-3 py-2"><input class="input" value="检查并补充润滑油" /></td>
          <td class="px-3 py-2 text-center"><button class="text-slate-400" onclick="toast('至少保留一条完整项目')">删除</button></td></tr>
        </tbody></table>
      </div></div>""",
    "至少存在一条完整保养项目。",
)

pages["基础配置_点巡检标准_新增.html"] = form_page(
    "新增 / 编辑点巡检标准", "基础配置_点巡检标准_page.html",
    field("标准编码", '<input class="input" maxlength="4" placeholder="4位编码，唯一" />')
    + field("标准名称", '<input class="input" />')
    + field("启用", '<select class="select"><option>启用</option><option>禁用</option></select>')
    + field("检查说明", '<textarea class="textarea" rows="3"></textarea>'),
)

for name, title, back in [
    ("设备运营_投保记录_新增.html", "新增投保记录", "设备运营_投保记录_page.html"),
    ("设备运营_理赔记录_新增.html", "新增理赔记录", "设备运营_理赔记录_page.html"),
    ("设备运营_设备租赁_新增.html", "新增设备租赁", "设备运营_设备租赁_page.html"),
    ("设备运营_设备报废_新增.html", "新增设备报废", "设备运营_设备报废_page.html"),
    ("设备运营_设备处置_新增.html", "新增设备处置", "设备运营_设备处置_page.html"),
    ("点巡检_点巡检区域_新增.html", "新增点巡检区域", "点巡检_点巡检区域_page.html"),
    ("保养管理_保养计划_新增周期.html", "新增周期保养计划", "保养管理_保养计划_page.html"),
    ("保养管理_保养计划_新增专项.html", "新增专项保养计划", "保养管理_保养计划_page.html"),
    ("保养管理_保养完工_新增.html", "新增保养完工", "保养管理_保养完工_page.html"),
    ("设备维修_故障报修_新增.html", "新增故障报修", "设备维修_故障报修_page.html"),
    ("设备维修_维修计划_新增.html", "新增维修计划", "设备维修_维修计划_page.html"),
    ("设备维修_维修派工_新增.html", "新增维修派工", "设备维修_维修派工_page.html"),
    ("设备维修_维修完工_新增.html", "新增维修完工", "设备维修_维修完工_page.html"),
    ("运行管理_加油记录_新增.html", "新增加油记录", "运行管理_加油记录_page.html"),
]:
    extra = ""
    if "投保" in name:
        fields = field("运营设备", pick_btn('选择运营设备','通用_选择运营设备.html')) + field("投保单号", '<input class="input" />') + field("投保周期起", '<input class="input" type="date" />') + field("投保周期止", '<input class="input" type="date" />') + field("投保金额(元)", '<input class="input" placeholder="两位小数" />')
    elif "理赔" in name:
        fields = field("投保单号", pick_btn('选择投保单号','通用_选择投保单号.html')) + field("理赔单号", '<input class="input" />') + field("理赔日期", '<input class="input" type="date" />') + field("理赔金额(元)", '<input class="input" />')
    elif "租赁" in name:
        fields = field("清单/设备", pick_btn('选择设备','通用_选择设备清单.html')) + field("租赁周期起", '<input class="input" type="date" />') + field("租赁周期止", '<input class="input" type="date" />') + field("租赁数量", '<input class="input" type="number" min="1" value="1" />') + field("租金金额(元)", '<input class="input" />')
    elif "报废" in name or "处置" in name:
        fields = field("运营设备", pick_btn('选择自有且正常设备','通用_选择运营设备.html')) + field("日期", '<input class="input" type="date" />') + field("说明", '<textarea class="textarea" rows="3"></textarea>')
    elif "区域" in name:
        fields = field("运营设备", pick_btn('选择运营设备','通用_选择运营设备.html')) + field("区域编号", '<input class="input" placeholder="唯一，映射老系统" />') + field("区域名称", '<input class="input" />') + field("启用", '<select class="select"><option>启用</option><option>禁用</option></select>')
    elif "周期" in name:
        fields = field("运营设备", pick_btn('选择运营设备','通用_选择运营设备.html')) + field("保养类型", '<input class="input" value="周期保养" disabled />') + field("上次保养", '<input class="input" value="2026-07-10" disabled />') + field("计划时间起", '<input class="input" type="datetime-local" />') + field("计划时间止", '<input class="input" type="datetime-local" />') + field("保养人员", '<input class="input" placeholder="组织架构多选" />') + field("通知人员", '<input class="input" placeholder="组织架构多选" />')
    elif "专项" in name and "保养计划" in name:
        fields = field("运营设备", pick_btn('选择运营设备','通用_选择运营设备.html')) + field("专项项目", '<select class="select"><option>减速箱专项</option><option>电气专项</option></select>') + field("计划时间起", '<input class="input" type="datetime-local" />') + field("计划时间止", '<input class="input" type="datetime-local" />')
    elif "保养完工" in name:
        fields = field("保养计划", pick_btn('选择已生效未完工计划','通用_选择保养计划.html')) + field("验收日期", '<input class="input" type="date" value="2026-08-07" />') + field("下次保养", '<input class="input" value="按验收日+周期自动计算" disabled />') + field("验收人员", '<input class="input" />') + """<div class="md:col-span-2 rounded-2xl border border-dashed border-slate-200 p-4">
          <div class="mb-2 flex justify-between text-sm"><span class="font-medium">派工记录</span>
          <button class="btn-ghost px-3 py-1 text-xs" onclick="openLightbox('保养管理_保养完工_添加派工.html')">添加派工记录</button></div>
          <p class="text-xs text-slate-500">作业开始时间须晚于计划业务生效时间；同一计划下作业时间不得交叉。</p></div>"""
    elif "故障报修" in name:
        fields = field("运营设备", pick_btn('选择运营设备','通用_选择运营设备.html')) + field("故障类型", '<select class="select"><option>机械故障</option><option>电气故障</option><option>其他</option></select>') + field("严重程度", '<select class="select"><option>一般</option><option>严重</option><option>紧急</option></select>') + field("故障发生时间", '<input class="input" type="datetime-local" />') + field("故障描述", '<textarea class="textarea" rows="3"></textarea>')
    elif "维修计划" in name:
        fields = field("故障设备", pick_btn('选择未完工故障单','通用_选取故障设备.html')) + field("计划维修时间", '<input class="input" type="datetime-local" />') + field("通知人员", '<input class="input" />') + field("计划说明", '<textarea class="textarea" rows="3"></textarea>')
    elif "维修派工" in name:
        fields = field("维修计划", pick_btn('选择已生效未派工计划','通用_选取维修计划.html')) + field("维修时间起", '<input class="input" type="datetime-local" />') + field("维修时间止", '<input class="input" type="datetime-local" />') + field("维修人员", '<input class="input" />')
    elif "维修完工" in name:
        fields = field("故障设备", pick_btn('选择未完工故障单','通用_选取故障设备.html')) + field("完工验收日期", '<input class="input" type="date" value="2026-08-07" />') + field("验收人员", '<input class="input" />') + field("通知人员", '<input class="input" />') + '<div class="md:col-span-2 text-sm text-slate-500 rounded-2xl bg-slate-50 p-4">回显该故障关联的全部维修计划与派工记录（点击可预览）。</div>'
    else:  # 加油
        fields = field("运营设备", pick_btn('选择正常/保养中/维修中设备','通用_选择运营设备.html')) + field("油类", '<select class="select"><option>液压油</option><option>齿轮油</option></select>') + field("油号", '<select class="select"><option>46#</option><option>220#</option></select>') + field("加油日期", '<input class="input" type="date" />') + field("操作人员", '<input class="input" />')
    pages[name] = form_page(title, back, fields)

# Special pages — 新增三步也走灯箱弹窗
pages["设备运营_运营设备_新增.html"] = (
    "__MODAL__",
    "新增运营设备",
    "设备运营_运营设备_page.html",
    """
<div class="mb-6 flex flex-wrap items-center gap-4 text-sm">
  <div class="flex items-center gap-2"><span class="step-dot step-on">1</span><span>基础信息</span></div>
  <div class="h-px w-10 bg-slate-200"></div>
  <div class="flex items-center gap-2"><span class="step-dot step-off" id="s2">2</span><span>保养信息</span></div>
  <div class="h-px w-10 bg-slate-200"></div>
  <div class="flex items-center gap-2"><span class="step-dot step-off" id="s3">3</span><span>制造信息</span></div>
</div>
<div id="step1" class="grid grid-cols-1 gap-4 md:grid-cols-2">
  <div class="md:col-span-2"><button type="button" class="btn-ghost inline-flex px-4 py-2 text-sm" onclick="openLightbox('通用_选择设备清单.html')">选择设备清单数据</button></div>
  <div><label class="mb-1 block text-xs text-slate-500">运营设备编号</label><input class="input" placeholder="唯一性校验" /></div>
  <div><label class="mb-1 block text-xs text-slate-500">设备来源</label><select class="select"><option>自有</option><option>租赁</option></select></div>
  <div><label class="mb-1 block text-xs text-slate-500">设备状态</label><input class="input" value="正常" disabled /></div>
  <div><label class="mb-1 block text-xs text-slate-500">运行状态</label><select class="select"><option>闲置中</option><option>运行中</option></select></div>
  <div><label class="mb-1 block text-xs text-slate-500">安装日期</label><input class="input" type="date" /></div>
  <div><label class="mb-1 block text-xs text-slate-500">投用日期</label><input class="input" type="date" /></div>
</div>
<div id="step2" class="hidden space-y-4">
  <div class="grid grid-cols-1 gap-4 md:grid-cols-2">
    <div><label class="mb-1 block text-xs text-slate-500">维保负责人</label><input class="input" placeholder="组织架构单选" /></div>
    <div><label class="mb-1 block text-xs text-slate-500">保养周期（天）</label><input class="input" type="number" min="1" value="30" /></div>
  </div>
  <div class="rounded-2xl border border-slate-200 p-4">
    <div class="mb-2 flex justify-between text-sm"><span class="font-medium">定期保养项目</span>
      <button type="button" class="text-teal-700 hover:underline" onclick="openLightbox('通用_选择保养标准.html')">选择保养标准</button></div>
    <p class="text-xs text-slate-500">多次选择累加不覆盖；至少一条完整项目。</p>
  </div>
  <div class="rounded-2xl border border-dashed border-slate-200 p-4 text-sm text-slate-500">专项保养可多组，允许为空。</div>
</div>
<div id="step3" class="hidden grid grid-cols-1 gap-4 md:grid-cols-2">
  <div><label class="mb-1 block text-xs text-slate-500">出厂日期</label><input class="input" type="date" /></div>
  <div><label class="mb-1 block text-xs text-slate-500">联系方式</label><input class="input" placeholder="手机号" /></div>
  <div class="md:col-span-2"><label class="mb-1 block text-xs text-slate-500">制造商</label><input class="input" /></div>
</div>
<div class="mt-6 flex justify-between border-t border-slate-100 pt-4">
  <button class="btn-ghost px-4 py-2 text-sm" id="btnPrev" onclick="changeStep(-1)" disabled>上一步</button>
  <button class="btn-brand px-4 py-2 text-sm" id="btnNext" onclick="changeStep(1)">下一步</button>
</div>
""",
    "STEP_JS",
)

pages["设备运营_运营设备_查看.html"] = page_header(
    "查看运营设备", "基础信息 / 维保信息 / 制造信息 / 设备二维码。", ("返回", "设备运营_运营设备_page.html")
) + """
<div class="card-soft p-2">
  <div class="flex gap-2 border-b border-slate-100 px-2 pt-2 text-sm" id="tabs">
    <button class="tab-btn rounded-xl bg-slate-900 px-4 py-2 text-white" data-tab="t1">基础信息</button>
    <button class="tab-btn rounded-xl px-4 py-2 text-slate-600 hover:bg-slate-50" data-tab="t2">维保信息</button>
    <button class="tab-btn rounded-xl px-4 py-2 text-slate-600 hover:bg-slate-50" data-tab="t3">制造信息</button>
    <button class="tab-btn rounded-xl px-4 py-2 text-slate-600 hover:bg-slate-50" data-tab="t4">设备二维码</button>
  </div>
  <div class="p-5 text-sm">
    <div id="t1"><div class="grid grid-cols-2 gap-3 md:grid-cols-3">
      <div><div class="text-xs text-slate-400">运营设备编号</div><div>OP-2026-001</div></div>
      <div><div class="text-xs text-slate-400">名称</div><div>1号门吊</div></div>
      <div><div class="text-xs text-slate-400">设备状态 / 运行状态</div><div>正常 / 运行中</div></div>
      <div><div class="text-xs text-slate-400">来源</div><div>自有</div></div>
      <div><div class="text-xs text-slate-400">安装 / 投用</div><div>2025-11-01 / 2025-11-15</div></div>
    </div></div>
    <div id="t2" class="hidden"><p>维保负责人：王工；保养周期：30 天；保养项目完整展示（值快照）。</p></div>
    <div id="t3" class="hidden"><p>出厂日期：2025-08-01；联系方式：138****8000；制造商：示例重工。</p></div>
    <div id="t4" class="hidden text-center">
      <div class="mx-auto flex h-48 w-48 items-center justify-center rounded-2xl border border-slate-200 bg-slate-50">
        <i class="fa-solid fa-qrcode text-6xl text-slate-700"></i>
      </div>
      <p class="mt-3 text-slate-600">1号门吊 · OP-2026-001</p>
      <p class="text-xs text-slate-400">新增后二维码永久不变</p>
      <div class="mt-4 flex justify-center gap-2">
        <button class="btn-ghost px-3 py-1.5 text-xs" onclick="toast('上一台')">上一台</button>
        <button class="btn-brand px-3 py-1.5 text-xs" onclick="toast('已下载：编号+名称')">下载二维码</button>
        <button class="btn-ghost px-3 py-1.5 text-xs" onclick="toast('下一台')">下一台</button>
      </div>
    </div>
  </div>
</div>
<script>
document.querySelectorAll('.tab-btn').forEach(btn=>{
  btn.addEventListener('click',()=>{
    document.querySelectorAll('.tab-btn').forEach(b=>b.className='tab-btn rounded-xl px-4 py-2 text-slate-600 hover:bg-slate-50');
    btn.className='tab-btn rounded-xl bg-slate-900 px-4 py-2 text-white';
    ['t1','t2','t3','t4'].forEach(id=>document.getElementById(id).classList.add('hidden'));
    document.getElementById(btn.dataset.tab).classList.remove('hidden');
  });
});
</script>
"""

pages["点巡检_点巡检区域_二维码.html"] = page_header(
    "点巡检区域二维码", "区域新增后二维码永久不变。", ("返回", "点巡检_点巡检区域_page.html")
) + """
<div class="card-soft mx-auto max-w-lg p-8 text-center">
  <div class="mx-auto flex h-56 w-56 items-center justify-center rounded-2xl border border-slate-200 bg-white shadow-[0_4px_12px_rgba(0,0,0,0.05)]">
    <i class="fa-solid fa-qrcode text-7xl text-slate-800"></i>
  </div>
  <div class="mt-4 space-y-1 text-sm">
    <div>运营设备：1号门吊（OP-2026-001）</div>
    <div>区域名称：门吊行走机构</div>
    <div class="text-slate-400">区域编号：A-10086</div>
  </div>
  <div class="mt-5 flex justify-center gap-2">
    <button class="btn-ghost px-4 py-2 text-sm" onclick="toast('上一区域')">上一个</button>
    <button class="btn-brand px-4 py-2 text-sm" onclick="toast('已下载：设备名称+区域名称')">下载</button>
    <button class="btn-ghost px-4 py-2 text-sm" onclick="toast('下一区域')">下一个</button>
  </div>
</div>
"""

pages["点巡检_点巡检记录_新增正常.html"] = form_page(
    "新增点巡检记录（正常）",
    "点巡检_点巡检记录_page.html",
    field("点巡检区域", pick_btn("选择已启用区域", "通用_选择点巡检区域.html"))
    + field("巡检结果", '<input class="input" value="正常（全部项目默认正常）" disabled />')
    + field("巡检负责人", '<input class="input" value="当前用户" />')
    + field("巡检部门", '<input class="input" value="设备保障部" />')
    + '<div class="md:col-span-2 text-xs text-slate-500">点检项目全部展示；正常时现场照片非必传。</div>',
)

pages["点巡检_点巡检记录_新增异常.html"] = form_page(
    "新增点巡检记录（异常）",
    "点巡检_点巡检记录_page.html",
    field("点巡检区域", pick_btn("选择已启用区域", "通用_选择点巡检区域.html"))
    + field("维修建议", '<select class="select"><option>立即维修</option><option>计划维修</option><option>继续观察</option></select>')
    + field("巡检负责人", '<input class="input" value="当前用户" />')
    + field("现场照片", '<input class="input" type="file" multiple accept="image/png,image/jpeg" />')
    + '<div class="md:col-span-2 rounded-2xl bg-amber-50 px-4 py-3 text-sm text-amber-800">任一项非正常即为异常；异常必须上传现场照片，否则 Toast 拦截。</div>',
)

pages["点巡检_点巡检记录_查看照片.html"] = page_header(
    "查看现场照片", "支持大图逐张预览。", ("返回", "点巡检_点巡检记录_page.html")
) + """
<div class="grid grid-cols-1 gap-4 md:grid-cols-3">
  <a class="card-soft block overflow-hidden" href="https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?w=800&q=80" target="_blank">
    <img class="h-48 w-full object-cover" src="https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?w=600&q=80" alt="现场照片1" />
    <div class="p-3 text-sm">现场照片 1</div>
  </a>
  <a class="card-soft block overflow-hidden" href="https://images.unsplash.com/photo-1504328345606-18bbc8c9d7d1?w=800&q=80" target="_blank">
    <img class="h-48 w-full object-cover" src="https://images.unsplash.com/photo-1504328345606-18bbc8c9d7d1?w=600&q=80" alt="现场照片2" />
    <div class="p-3 text-sm">现场照片 2</div>
  </a>
</div>
"""

pages["保养管理_保养通知_查看.html"] = form_page(
    "保养通知详情", "保养管理_保养通知_page.html",
    field("通知编号", '<input class="input" value="BN-20260805-01" disabled />')
    + field("通知日期", '<input class="input" value="2026-08-05" disabled />')
    + field("运营设备", '<input class="input" value="OP-2026-001 / 1号门吊" disabled />')
    + field("维保负责人", '<input class="input" value="王工" disabled />')
    + field("下次保养日期", '<input class="input" value="2026-08-10" disabled />'),
    "只读业务汇总。",
)

pages["设备维修_故障通知_查看.html"] = form_page(
    "故障通知详情", "设备维修_故障通知_page.html",
    field("通知来源", '<input class="input" value="点巡检-立即维修建议" disabled />')
    + field("通知时间", '<input class="input" value="2026-08-06 16:35" disabled />')
    + field("运营设备", '<input class="input" value="2号输送线" disabled />')
    + field("描述", '<textarea class="textarea" rows="3" disabled>驱动端异响，建议立即维修</textarea>'),
)

pages["保养管理_保养完工_添加派工.html"] = form_page(
    "添加派工记录", "保养管理_保养完工_新增.html",
    field("作业开始时间", '<input class="input" type="datetime-local" />')
    + field("作业结束时间", '<input class="input" type="datetime-local" />')
    + field("保养人员", '<input class="input" />')
    + field("备注", '<textarea class="textarea" rows="3"></textarea>'),
    "开始时间需大于计划业务生效时间；同计划作业时间不得交叉。",
)

# Selector modals as pages
selector_pages = {
    "通用_选择设备清单.html": ("选择设备清单", "从基础配置设备清单中选择。", ["编号", "名称", "类型"], [["EQ-T-001", "门式起重机", "起重设备"], ["EQ-T-002", "皮带输送机", "输送设备"]]),
    "通用_选择运营设备.html": ("选择运营设备", "仅展示状态为正常的运营设备（部分场景另有过滤）。", ["编号", "名称", "状态"], [["OP-2026-001", "1号门吊", "正常"], ["OP-2026-002", "2号输送线", "正常"]]),
    "通用_选择保养标准.html": ("选择保养标准", "支持类型筛选与编号/名称搜索；多次选择累加。", ["编号", "名称", "类型"], [["MS-001", "起重机月度保养", "起重设备"], ["MS-002", "输送机季度保养", "输送设备"]]),
    "通用_选择点巡检区域.html": ("选择点巡检区域", "仅已启用区域。", ["区域编号", "区域名称", "设备"], [["A-10086", "门吊行走机构", "1号门吊"], ["A-10087", "输送驱动端", "2号输送线"]]),
    "通用_选择投保单号.html": ("选择投保单号", "来自投保记录。", ["投保单号", "设备", "周期"], [["BX-2026-011", "1号门吊", "2026全年"], ["BX-2026-018", "2号输送线", "2026-2027"]]),
    "通用_选择保养计划.html": ("选择保养计划", "已生效且未完工的计划。", ["计划单号", "设备", "类型"], [["BJ-2026-021", "1号门吊", "周期保养"], ["BJ-2026-028", "2号输送线", "专项保养"]]),
    "通用_选取故障设备.html": ("选取故障设备", "未发起完工验收的故障报修单。", ["故障单号", "设备", "状态"], [["GZ-2026-044", "2号输送线", "待派工"]]),
    "通用_选取维修计划.html": ("选取维修计划", "已生效、未派工、未作废且故障未完工。", ["计划单号", "故障单", "设备"], [["WJ-2026-031", "GZ-2026-044", "2号输送线"]]),
}

for fname, (title, desc, headers, rows) in selector_pages.items():
    row_html = []
    for r in rows:
        cells = "".join(f"<td class='px-3 py-3'>{c}</td>" for c in r)
        row_html.append(
            f"<tr class='table-row border-t border-slate-100'>{cells}"
            f"<td class='px-3 py-3'><button class='btn-brand px-3 py-1.5 text-xs' "
            f"onclick=\"toast('已选择：{r[0]}');closeLightbox()\">选择</button></td></tr>"
        )
    body = f"""
    <p class="mb-3 text-xs text-slate-500">{desc}</p>
    <div class="overflow-hidden rounded-2xl border border-slate-200">
      <div class="border-b border-slate-100 p-3"><input class="input" placeholder="搜索编号/名称" /></div>
      <table class="w-full text-sm"><thead class="bg-slate-50"><tr>
        {''.join(f'<th class="px-3 py-3 text-left">{h}</th>' for h in headers)}
        <th class="px-3 py-3 text-left">操作</th>
      </tr></thead><tbody>{''.join(row_html)}</tbody></table>
    </div>
    <div class="mt-4 flex justify-end">
      <button type="button" class="btn-ghost px-4 py-2 text-sm" onclick="closeLightbox()">关闭</button>
    </div>
    """
    pages[fname] = ("__MODAL__", title, "设备运营_运营设备_page.html", body, "")

STEP_JS = """
let step=1;
function changeStep(d){
  const next=step+d;
  if(next<1||next>3) return;
  if(d>0 && step===3){
    toast('运营设备已创建；二维码已固化（原型）');
    setTimeout(()=>closeModalOrBack('设备运营_运营设备_page.html'), 400);
    return;
  }
  step=next;
  ['step1','step2','step3'].forEach((id,i)=>document.getElementById(id).classList.toggle('hidden', i+1!==step));
  document.getElementById('s2').className='step-dot '+(step>=2?'step-on':'step-off');
  document.getElementById('s3').className='step-dot '+(step>=3?'step-on':'step-off');
  document.getElementById('btnPrev').disabled = step===1;
  document.getElementById('btnNext').textContent = step===3 ? '完成创建' : '下一步';
}
"""

# Write all PC pages（common.js 已独立维护，此处不再覆盖）
for fname, body in pages.items():
    if isinstance(body, tuple) and body and body[0] == "__MODAL__":
        _, title, back, content, extra_flag = body
        extra = STEP_JS if extra_flag == "STEP_JS" else ""
        html_doc = modal_shell(title, content, back, extra)
        (PAGES / fname).write_text(html_doc, encoding="utf-8")
        continue

    title = fname.replace("_page.html", "").replace(".html", "").replace("_", " · ")
    content = body
    active = fname if fname.endswith("_page.html") else ""
    if not fname.endswith("_page.html"):
        mapping = [
            ("基础配置_设备清单", "基础配置_设备清单_page.html"),
            ("基础配置_保养标准", "基础配置_保养标准_page.html"),
            ("基础配置_点巡检标准", "基础配置_点巡检标准_page.html"),
            ("设备运营_运营设备", "设备运营_运营设备_page.html"),
            ("设备运营_投保", "设备运营_投保记录_page.html"),
            ("设备运营_理赔", "设备运营_理赔记录_page.html"),
            ("设备运营_设备租赁", "设备运营_设备租赁_page.html"),
            ("设备运营_设备报废", "设备运营_设备报废_page.html"),
            ("设备运营_设备处置", "设备运营_设备处置_page.html"),
            ("点巡检_点巡检区域", "点巡检_点巡检区域_page.html"),
            ("点巡检_点巡检记录", "点巡检_点巡检记录_page.html"),
            ("保养管理_保养通知", "保养管理_保养通知_page.html"),
            ("保养管理_保养计划", "保养管理_保养计划_page.html"),
            ("保养管理_保养完工", "保养管理_保养完工_page.html"),
            ("设备维修_故障通知", "设备维修_故障通知_page.html"),
            ("设备维修_故障报修", "设备维修_故障报修_page.html"),
            ("设备维修_维修计划", "设备维修_维修计划_page.html"),
            ("设备维修_维修派工", "设备维修_维修派工_page.html"),
            ("设备维修_维修完工", "设备维修_维修完工_page.html"),
            ("运行管理_加油", "运行管理_加油记录_page.html"),
        ]
        for pref, list_page in mapping:
            if fname.startswith(pref):
                active = list_page
                break
    html_doc = pc_shell(title.split(" · ")[-1] if " · " in title else title, active, content, "")
    (PAGES / fname).write_text(html_doc, encoding="utf-8")

print(f"PC pages: {len(list(PAGES.glob('*.html')))}")

# ---------- WeCom H5 ----------
def wecom_shell(title, body, show_back=True):
    back = (
        f'<a href="wecom_入口.html" class="text-slate-700"><i class="fa-solid fa-chevron-left"></i></a>'
        if show_back
        else '<span class="w-4"></span>'
    )
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
  <title>{title} · 企微H5 · EMS v1.0.0</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css" />
  <style>
    body{{
      font-family:-apple-system,BlinkMacSystemFont,"SF Pro Text","Segoe UI",Roboto,"Helvetica Neue",sans-serif;
      line-height:1.6; margin:0; min-height:100vh;
      background:linear-gradient(160deg,#e2e8f0 0%,#f8fafc 45%,#cbd5e1 100%);
    }}
    .stage{{min-height:100vh;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:24px 16px;}}
    .phone{{
      width:390px; height:844px; border-radius:48px; border:10px solid #e5e7eb;
      background:#0f172a; box-shadow:0 24px 64px rgba(15,23,42,.22);
      position:relative; overflow:hidden; flex-shrink:0;
    }}
    .island{{
      position:absolute; top:12px; left:50%; transform:translateX(-50%);
      width:120px; height:32px; border-radius:20px; background:#0f172a; z-index:30;
    }}
    .phone-screen{{
      position:absolute; inset:0; margin:8px; border-radius:40px; overflow:hidden;
      background:#f8fafc; display:flex; flex-direction:column;
    }}
    .status-bar{{
      height:48px; padding:14px 20px 0; display:flex; justify-content:space-between;
      align-items:flex-start; font-size:12px; font-weight:600; color:#0f172a; flex-shrink:0;
    }}
    .nav-bar{{
      height:48px; display:flex; align-items:center; justify-content:space-between;
      padding:0 16px; background:#fff; border-bottom:1px solid #e2e8f0; flex-shrink:0;
    }}
    .content{{flex:1; overflow-y:auto; padding:16px; -webkit-overflow-scrolling:touch;}}
    .content::-webkit-scrollbar{{display:none;}}
    .home-bar{{
      height:22px; display:flex; align-items:center; justify-content:center;
      background:#fff; flex-shrink:0;
    }}
    .home-bar span{{width:128px; height:5px; border-radius:999px; background:#cbd5e1;}}
    .btn{{border-radius:1rem;}}
    .btn:active{{transform:scale(0.95);}}
    .card{{background:#fff;border:1px solid #e2e8f0;border-radius:1.25rem;box-shadow:0 4px 12px rgba(0,0,0,0.05);}}
    .toast{{
      position:absolute; left:50%; bottom:36px; transform:translateX(-50%) translateY(8px);
      background:#0f172a;color:#fff;padding:10px 14px;border-radius:14px;font-size:13px;
      opacity:0;transition:.2s;z-index:50; max-width:86%;
    }}
    .toast.show{{opacity:1;transform:translateX(-50%) translateY(0);}}
    .modal-mask{{
      position:absolute; inset:0; background:rgba(15,23,42,.45);
      display:none; align-items:center; justify-content:center; padding:20px; z-index:40;
    }}
    .modal-mask.show{{display:flex;}}
    .hint{{margin-top:14px; font-size:12px; color:#64748b; text-align:center;}}
  </style>
</head>
<body>
  <div class="stage">
    <div class="phone" aria-label="手机预览外壳">
      <div class="island"></div>
      <div class="phone-screen">
        <div class="status-bar">
          <span>9:41</span>
          <span style="display:flex;gap:6px;align-items:center;">
            <i class="fa-solid fa-signal"></i>
            <i class="fa-solid fa-wifi"></i>
            <i class="fa-solid fa-battery-full"></i>
          </span>
        </div>
        <div class="nav-bar">
          {back}
          <div class="text-sm font-semibold text-slate-900">{title}</div>
          <span class="w-4"></span>
        </div>
        <div class="content">{body}</div>
        <div class="home-bar"><span></span></div>
        <div id="toast" class="toast"></div>
      </div>
    </div>
    <p class="hint">企微 H5 演示外壳（iPhone 16 · 390×844）· 无独立底部业务 Tab</p>
  </div>
  <script>
    function toast(m){{const el=document.getElementById('toast');el.textContent=m;el.classList.add('show');clearTimeout(window.t);window.t=setTimeout(()=>el.classList.remove('show'),2000);}}
    function openModal(id){{document.getElementById(id).classList.add('show');}}
    function closeModal(id){{document.getElementById(id).classList.remove('show');}}
  </script>
</body>
</html>
"""

wecom_pages = {}

wecom_pages["wecom_入口.html"] = wecom_shell(
    "智能设备巡检",
    """
<p class="mb-3 text-xs text-slate-500">企业微信工作台入口 · 复用企微导航 · 无独立底部业务 Tab</p>
<div class="card p-4">
  <div class="text-base font-semibold text-slate-900">点巡检</div>
  <p class="mt-1 text-sm text-slate-500">扫描巡检区域二维码，录入正常/异常结果。</p>
  <div class="mt-4 grid grid-cols-2 gap-3">
    <a href="wecom_扫码.html" class="btn flex items-center justify-center gap-2 bg-teal-700 px-3 py-3 text-sm text-white">扫码巡检</a>
    <a href="wecom_记录列表.html" class="btn flex items-center justify-center border border-slate-200 bg-white px-3 py-3 text-sm text-slate-700">我的记录</a>
  </div>
</div>
<div class="card mt-3 overflow-hidden">
  <img class="h-36 w-full object-cover" src="https://images.unsplash.com/photo-1581092918056-0c4c3acd3789?w=800&q=80" alt="现场设备" />
  <div class="p-4 text-sm text-slate-600">支持正常/异常分支；异常须填写巡检内容并上传现场照片。</div>
</div>
<a class="mt-4 block text-center text-xs text-slate-400" href="../../index.html">返回版本入口</a>
""",
    show_back=False,
)

wecom_pages["wecom_扫码.html"] = wecom_shell(
    "扫码",
    """
<div class="card p-6 text-center">
  <div class="mx-auto flex h-48 w-48 items-center justify-center rounded-2xl border border-dashed border-slate-300 bg-slate-50">
    <i class="fa-solid fa-camera text-4xl text-slate-400"></i>
  </div>
  <p class="mt-4 text-sm text-slate-600">模拟调用企微扫码，识别点巡检区域二维码</p>
  <button class="btn mt-5 w-full bg-teal-700 py-3 text-sm text-white" onclick="location.href='wecom_扫码结果.html'">模拟扫码成功</button>
</div>
""",
)

wecom_pages["wecom_扫码结果.html"] = wecom_shell(
    "区域确认",
    """
<div class="card p-4 text-sm">
  <div class="font-semibold text-slate-900">门吊行走机构</div>
  <div class="mt-2 space-y-1 text-slate-600">
    <div>区域编号：A-10086</div>
    <div>运营设备：1号门吊（OP-2026-001）</div>
  </div>
</div>
<div class="mt-4 grid grid-cols-2 gap-3">
  <a href="wecom_录入正常.html" class="btn bg-emerald-600 py-3 text-center text-sm text-white">录入正常</a>
  <a href="wecom_录入异常.html" class="btn bg-rose-600 py-3 text-center text-sm text-white">录入异常</a>
</div>
""",
)

wecom_pages["wecom_录入正常.html"] = wecom_shell(
    "录入正常",
    """
<div class="card space-y-3 p-4 text-sm">
  <div><label class="mb-1 block text-xs text-slate-500">巡检编号</label><input class="w-full rounded-xl border border-slate-200 px-3 py-2" value="系统自动生成" disabled /></div>
  <div><label class="mb-1 block text-xs text-slate-500">巡检名称</label><input class="w-full rounded-xl border border-slate-200 px-3 py-2" value="1号门吊 / 门吊行走机构" disabled /></div>
  <div><label class="mb-1 block text-xs text-slate-500">巡检项目</label><input class="w-full rounded-xl border border-slate-200 px-3 py-2" placeholder="最多50字" /></div>
  <div><label class="mb-1 block text-xs text-slate-500">巡检内容（非必填）</label><textarea class="w-full rounded-xl border border-slate-200 px-3 py-2" rows="3" placeholder="富文本简化为多行输入"></textarea></div>
  <div><label class="mb-1 block text-xs text-slate-500">现场照片（非必填）</label><input type="file" accept="image/png,image/jpeg" multiple class="w-full text-xs" /></div>
  <div class="rounded-xl bg-slate-50 px-3 py-2 text-xs text-slate-500">设备定位：已开启（提示状态）</div>
</div>
<button class="btn mt-4 w-full bg-teal-700 py-3 text-sm text-white" onclick="location.href='wecom_提交成功.html'">提交巡检结果</button>
""",
)

wecom_pages["wecom_录入异常.html"] = wecom_shell(
    "录入异常",
    """
<div class="mb-3 rounded-xl bg-rose-50 px-3 py-2 text-xs text-rose-700">异常时：巡检内容与现场照片均为必填。</div>
<div class="card space-y-3 p-4 text-sm">
  <div><label class="mb-1 block text-xs text-slate-500">巡检编号</label><input class="w-full rounded-xl border border-slate-200 px-3 py-2" value="系统自动生成" disabled /></div>
  <div><label class="mb-1 block text-xs text-slate-500">巡检名称</label><input class="w-full rounded-xl border border-slate-200 px-3 py-2" value="2号输送线 / 输送驱动端" disabled /></div>
  <div><label class="mb-1 block text-xs text-slate-500">巡检项目</label><input class="w-full rounded-xl border border-slate-200 px-3 py-2" placeholder="最多50字" /></div>
  <div><label class="mb-1 block text-xs text-slate-500">巡检内容（必填）</label><textarea id="content" class="w-full rounded-xl border border-slate-200 px-3 py-2" rows="3" placeholder="请描述异常现象"></textarea></div>
  <div><label class="mb-1 block text-xs text-slate-500">现场照片（必填）</label><input id="photos" type="file" accept="image/png,image/jpeg" multiple class="w-full text-xs" /></div>
  <div class="rounded-xl bg-slate-50 px-3 py-2 text-xs text-slate-500">设备定位：已开启（提示状态）</div>
</div>
<button class="btn mt-4 w-full bg-teal-700 py-3 text-sm text-white" onclick="submitAbnormal()">提交巡检结果</button>
<script>
function submitAbnormal(){
  const c=document.getElementById('content').value.trim();
  const p=document.getElementById('photos').files;
  if(!c){ toast('异常时巡检内容必填'); return; }
  if(!p.length){ toast('异常时必须上传现场照片'); return; }
  location.href='wecom_提交成功.html';
}
</script>
""",
)

wecom_pages["wecom_提交成功.html"] = wecom_shell(
    "提交成功",
    """
<div class="card p-8 text-center">
  <div class="mx-auto flex h-14 w-14 items-center justify-center rounded-full bg-emerald-50 text-emerald-600">
    <i class="fa-solid fa-check text-xl"></i>
  </div>
  <div class="mt-4 text-base font-semibold text-slate-900">巡检结果已提交</div>
  <p class="mt-2 text-sm text-slate-500">如需平台审批，将由平台流程承接（本页不展示审批界面）。</p>
  <a href="wecom_入口.html" class="btn mt-6 inline-block bg-teal-700 px-5 py-2.5 text-sm text-white">返回入口</a>
</div>
""",
)

wecom_pages["wecom_记录列表.html"] = wecom_shell(
    "我的记录",
    """
<div class="space-y-3">
  <a href="wecom_记录详情.html" class="card block p-4">
    <div class="flex items-center justify-between text-sm">
      <span class="font-medium text-slate-900">门吊行走机构</span>
      <span class="rounded-full bg-emerald-50 px-2 py-0.5 text-xs text-emerald-700">正常</span>
    </div>
    <div class="mt-1 text-xs text-slate-500">2026-08-07 07:40 · XJ-20260807-01</div>
  </a>
  <a href="wecom_记录详情.html" class="card block p-4">
    <div class="flex items-center justify-between text-sm">
      <span class="font-medium text-slate-900">输送驱动端</span>
      <span class="rounded-full bg-rose-50 px-2 py-0.5 text-xs text-rose-700">异常</span>
    </div>
    <div class="mt-1 text-xs text-slate-500">2026-08-06 16:20 · XJ-20260806-18</div>
  </a>
</div>
""",
)

wecom_pages["wecom_记录详情.html"] = wecom_shell(
    "记录详情",
    """
<div class="card space-y-3 p-4 text-sm">
  <div class="flex justify-between"><span class="text-slate-500">结果</span><span class="text-rose-600 font-medium">异常</span></div>
  <div class="flex justify-between"><span class="text-slate-500">设备</span><span>2号输送线</span></div>
  <div class="flex justify-between"><span class="text-slate-500">区域</span><span>输送驱动端</span></div>
  <div><div class="text-slate-500 mb-1">巡检内容</div><div class="rounded-xl bg-slate-50 p-3">驱动端异响，建议立即维修</div></div>
  <div>
    <div class="text-slate-500 mb-2">现场照片</div>
    <img class="h-40 w-full rounded-xl object-cover" src="https://images.unsplash.com/photo-1504328345606-18bbc8c9d7d1?w=800&q=80" alt="现场照片" />
  </div>
</div>
""",
)

for fname, content in wecom_pages.items():
    (WECOM / fname).write_text(content, encoding="utf-8")

print(f"WeCom pages: {len(list(WECOM.glob('*.html')))}")

# ---------- version index + global portal ----------
(ROOT / "index.html").write_text(
    """<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
  <title>EMS v1.0.0 原型入口</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css" />
</head>
<body class="bg-slate-50 text-slate-800" style="font-family:-apple-system,BlinkMacSystemFont,'SF Pro Text','Segoe UI',Roboto,'Helvetica Neue',sans-serif;line-height:1.6;">
  <div class="mx-auto max-w-4xl px-4 py-12">
    <p class="text-sm font-medium text-teal-700">当前版本：v1.0.0</p>
    <h1 class="mt-2 text-2xl font-bold text-slate-900">智能设备管理 · 版本原型入口</h1>
    <p class="mt-3 text-sm text-slate-600">已生成：PC 端 Web + 企业微信内嵌 H5。不含消息中心、审批流、角色权限页面。</p>

    <div class="mt-8 grid gap-4 md:grid-cols-2">
      <a id="pc" href="pages/设备运营_运营设备_page.html" class="rounded-2xl border border-slate-200 bg-white p-5 shadow-[0_4px_12px_rgba(0,0,0,0.05)] transition hover:-translate-y-1 hover:shadow-[0_8px_24px_rgba(0,0,0,0.08)]">
        <div class="flex items-center gap-2 text-teal-700"><i class="fa-solid fa-desktop"></i><span class="font-semibold">PC 端 Web 原型</span></div>
        <p class="mt-2 text-sm text-slate-500">侧边栏业务菜单 · 列表/表单/选择器齐全。点击进入运营设备列表。</p>
      </a>
      <a id="wecom" href="pages/wecom/wecom_入口.html" class="rounded-2xl border border-slate-200 bg-white p-5 shadow-[0_4px_12px_rgba(0,0,0,0.05)] transition hover:-translate-y-1 hover:shadow-[0_8px_24px_rgba(0,0,0,0.08)]">
        <div class="flex items-center gap-2 text-teal-700"><i class="fa-brands fa-weixin"></i><span class="font-semibold">企微 H5 原型</span></div>
        <p class="mt-2 text-sm text-slate-500">无手机壳、无底部 Tab · 扫码点巡检主路径。</p>
      </a>
      <div id="app" class="rounded-2xl border border-dashed border-slate-200 bg-white p-5">
        <div class="font-semibold text-slate-400">独立 App 原型</div>
        <p class="mt-2 text-sm text-slate-400">本版本未生成（本次确认：PC+企微H5）</p>
      </div>
      <a href="../../../docs/versions/v1.0.0/prd.html" class="rounded-2xl border border-slate-200 bg-white p-5 shadow-[0_4px_12px_rgba(0,0,0,0.05)]">
        <div class="font-semibold text-slate-900">PRD 阅读页</div>
        <p class="mt-2 text-sm text-slate-500">查看 v1.0.0 完整需求文档</p>
      </a>
    </div>

    <div class="mt-8 rounded-2xl border border-slate-200 bg-white p-5">
      <h2 class="text-sm font-semibold text-slate-900">PC 模块快速入口</h2>
      <div class="mt-3 grid grid-cols-2 gap-2 text-sm md:grid-cols-3">
        <a class="rounded-xl bg-slate-50 px-3 py-2 hover:bg-teal-50" href="pages/基础配置_设备清单_page.html">设备清单</a>
        <a class="rounded-xl bg-slate-50 px-3 py-2 hover:bg-teal-50" href="pages/设备运营_运营设备_page.html">运营设备</a>
        <a class="rounded-xl bg-slate-50 px-3 py-2 hover:bg-teal-50" href="pages/点巡检_点巡检记录_page.html">点巡检记录</a>
        <a class="rounded-xl bg-slate-50 px-3 py-2 hover:bg-teal-50" href="pages/保养管理_保养计划_page.html">保养计划</a>
        <a class="rounded-xl bg-slate-50 px-3 py-2 hover:bg-teal-50" href="pages/设备维修_故障报修_page.html">故障报修</a>
        <a class="rounded-xl bg-slate-50 px-3 py-2 hover:bg-teal-50" href="pages/运行管理_加油记录_page.html">加油记录</a>
      </div>
    </div>

    <a class="mt-6 inline-block text-sm text-teal-700 hover:underline" href="../../index.html">返回全局总入口</a>
  </div>
</body>
</html>
""",
    encoding="utf-8",
)

(ROOT.parent.parent / "index.html").write_text(
    """<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
  <title>智能设备管理 EMS · 原型总入口</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css" />
</head>
<body class="bg-slate-50 text-slate-800" style="font-family:-apple-system,BlinkMacSystemFont,'SF Pro Text','Segoe UI',Roboto,'Helvetica Neue',sans-serif;line-height:1.6;">
  <div class="mx-auto max-w-6xl px-4 py-10">
    <header class="mb-8">
      <p class="text-sm font-medium text-teal-700">智能设备管理（EMS）</p>
      <h1 class="mt-1 text-2xl font-bold text-slate-900">原型与 PRD 全局总入口</h1>
      <p class="mt-2 text-sm text-slate-500">适配 GitHub Pages 静态发布。本地可用任意静态服务器打开本文件。</p>
    </header>
    <div class="overflow-hidden rounded-2xl border border-slate-200 bg-white shadow-[0_4px_12px_rgba(0,0,0,0.05)]">
      <table class="w-full text-left text-sm">
        <thead class="bg-slate-900 text-slate-100">
          <tr>
            <th class="px-4 py-3 font-semibold">版本号</th>
            <th class="px-4 py-3 font-semibold">版本迭代说明</th>
            <th class="px-4 py-3 font-semibold">PC 端原型</th>
            <th class="px-4 py-3 font-semibold">独立 App 原型</th>
            <th class="px-4 py-3 font-semibold">企微 H5 原型</th>
            <th class="px-4 py-3 font-semibold">PRD 文档</th>
          </tr>
        </thead>
        <tbody>
          <tr class="border-t border-slate-100 hover:bg-slate-50">
            <td class="px-4 py-3 font-medium text-slate-900">v1.0.0</td>
            <td class="px-4 py-3 text-slate-600">首版：PC 业务端 + 企微 H5 扫码点巡检</td>
            <td class="px-4 py-3"><a class="text-teal-700 hover:underline" href="./versions/v1.0.0/index.html#pc">进入 PC</a></td>
            <td class="px-4 py-3 text-slate-400">未生成</td>
            <td class="px-4 py-3"><a class="text-teal-700 hover:underline" href="./versions/v1.0.0/pages/wecom/wecom_入口.html">进入企微H5</a></td>
            <td class="px-4 py-3">
              <a class="text-teal-700 hover:underline" href="../docs/versions/v1.0.0/prd.html">阅读页</a>
              <span class="text-slate-300"> · </span>
              <a class="text-teal-700 hover:underline" href="../docs/versions/v1.0.0/prd.md">Markdown</a>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</body>
</html>
""",
    encoding="utf-8",
)

print("OK: portals updated")
