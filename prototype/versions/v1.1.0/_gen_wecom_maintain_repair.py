# -*- coding: utf-8 -*-
"""Generate v1.1.0 WeCom H5 pages for 保养管理 + 设备维修."""
from pathlib import Path

OUT = Path(__file__).resolve().parent / "pages" / "wecom"
OUT.mkdir(parents=True, exist_ok=True)

CSS = """
    body{
      font-family:-apple-system,BlinkMacSystemFont,"SF Pro Text","Segoe UI",Roboto,"Helvetica Neue",sans-serif;
      line-height:1.6; margin:0; min-height:100vh;
      background:linear-gradient(160deg,#e2e8f0 0%,#f8fafc 45%,#cbd5e1 100%);
    }
    .stage{min-height:100vh;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:24px 16px;}
    .phone{
      width:390px; height:844px; border-radius:48px; border:10px solid #e5e7eb;
      background:#0f172a; box-shadow:0 24px 64px rgba(15,23,42,.22);
      position:relative; overflow:hidden; flex-shrink:0;
    }
    .island{
      position:absolute; top:12px; left:50%; transform:translateX(-50%);
      width:120px; height:32px; border-radius:20px; background:#0f172a; z-index:30;
    }
    .phone-screen{
      position:absolute; inset:0; margin:8px; border-radius:40px; overflow:hidden;
      background:#f8fafc; display:flex; flex-direction:column;
    }
    .status-bar{
      height:48px; padding:14px 20px 0; display:flex; justify-content:space-between;
      align-items:flex-start; font-size:12px; font-weight:600; color:#0f172a; flex-shrink:0;
    }
    .nav-bar{
      height:48px; display:flex; align-items:center; justify-content:space-between;
      padding:0 16px; background:#fff; border-bottom:1px solid #e2e8f0; flex-shrink:0;
    }
    .content{flex:1; overflow-y:auto; padding:16px; -webkit-overflow-scrolling:touch;}
    .content::-webkit-scrollbar{display:none;}
    .home-bar{
      height:22px; display:flex; align-items:center; justify-content:center;
      background:#fff; flex-shrink:0;
    }
    .home-bar span{width:128px; height:5px; border-radius:999px; background:#cbd5e1;}
    .btn{border-radius:1rem;}
    .btn:active{transform:scale(0.95);}
    .card{background:#fff;border:1px solid #e2e8f0;border-radius:1.25rem;box-shadow:0 4px 12px rgba(0,0,0,0.05);}
    .input,.select,textarea.input{
      width:100%; border:1px solid #e2e8f0; border-radius:0.75rem; padding:0.625rem 0.75rem;
      font-size:0.875rem; background:#fff; color:#0f172a; outline:none; box-sizing:border-box;
    }
    .input:focus,.select:focus{border-color:#0f766e;}
    .label{display:block; margin-bottom:0.25rem; font-size:0.75rem; color:#64748b;}
    .toast{
      position:absolute; left:50%; bottom:36px; transform:translateX(-50%) translateY(8px);
      background:#0f172a;color:#fff;padding:10px 14px;border-radius:14px;font-size:13px;
      opacity:0;transition:.2s;z-index:50; max-width:86%;
    }
    .toast.show{opacity:1;transform:translateX(-50%) translateY(0);}
    .modal-mask{
      position:absolute; inset:0; background:rgba(15,23,42,.45);
      display:none; align-items:center; justify-content:center; padding:20px; z-index:40;
    }
    .modal-mask.show{display:flex;}
    .modal-box{
      width:100%; max-height:78%; overflow:auto; background:#fff; border-radius:1.5rem;
      padding:16px; box-shadow:0 8px 24px rgba(0,0,0,0.08);
    }
    .hint{margin-top:14px; font-size:12px; color:#64748b; text-align:center;}
    .chip{border-radius:999px;border:1px solid #e2e8f0;background:#fff;color:#475569;padding:6px 12px;font-size:12px;font-weight:500;white-space:nowrap;}
    .chip.active{background:#0f172a;color:#fff;border-color:#0f172a;}
"""

JS = """
    function toast(m){const el=document.getElementById('toast');el.textContent=m;el.classList.add('show');clearTimeout(window.t);window.t=setTimeout(()=>el.classList.remove('show'),2000);}
    function openModal(id){document.getElementById(id).classList.add('show');}
    function closeModal(id){document.getElementById(id).classList.remove('show');}
    function bindChips(rootId){
      const root=document.getElementById(rootId); if(!root) return;
      root.querySelectorAll('.chip').forEach(btn=>{
        btn.addEventListener('click',()=>{
          root.querySelectorAll('.chip').forEach(c=>c.classList.remove('active'));
          btn.classList.add('active');
          toast('已筛选：'+btn.textContent.trim());
        });
      });
    }
"""


def shell(title, body, back="wecom_入口.html", right="", extra_js=""):
    if back:
        back_html = '<a href="%s" class="text-slate-700"><i class="fa-solid fa-chevron-left"></i></a>' % back
    else:
        back_html = '<span class="w-4"></span>'
    right_html = right or '<span class="w-4"></span>'
    return """<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
  <title>%(title)s · 企微H5 · EMS v1.1.0</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css" />
  <style>%(css)s</style>
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
          %(back)s
          <div class="text-sm font-semibold text-slate-900">%(title)s</div>
          %(right)s
        </div>
        <div class="content">
%(body)s
        </div>
        <div class="home-bar"><span></span></div>
        <div id="toast" class="toast"></div>
      </div>
    </div>
    <p class="hint">企微 H5 演示外壳（iPhone 16 · 390×844）· 无独立底部业务 Tab</p>
  </div>
  <script>
%(js)s
%(extra)s
  </script>
</body>
</html>
""" % {
        "title": title,
        "css": CSS,
        "back": back_html,
        "right": right_html,
        "body": body,
        "js": JS,
        "extra": extra_js,
    }


def badge(text, kind="muted"):
    colors = {
        "ok": "bg-emerald-50 text-emerald-700",
        "danger": "bg-rose-50 text-rose-700",
        "warn": "bg-amber-50 text-amber-700",
        "muted": "bg-slate-100 text-slate-600",
    }
    return '<span class="rounded-full px-2 py-0.5 text-xs %s">%s</span>' % (colors.get(kind, colors["muted"]), text)


def card_link(href, title, meta, right=""):
    return """
  <a href="%s" class="card block p-4">
    <div class="flex items-start justify-between gap-2">
      <div class="min-w-0">
        <div class="text-sm font-medium text-slate-900">%s</div>
        <div class="mt-1 text-xs text-slate-500">%s</div>
      </div>
      <div class="shrink-0 flex flex-wrap gap-1 justify-end">%s</div>
    </div>
  </a>""" % (href, title, meta, right)


def card_block(title, meta, right="", actions=""):
    act = ('<div class="mt-3 flex flex-wrap gap-3 text-xs text-teal-700">%s</div>' % actions) if actions else ""
    return """
  <div class="card p-4">
    <div class="flex items-start justify-between gap-2">
      <div class="min-w-0">
        <div class="text-sm font-medium text-slate-900">%s</div>
        <div class="mt-1 text-xs text-slate-500">%s</div>
      </div>
      <div class="shrink-0">%s</div>
    </div>
    %s
  </div>""" % (title, meta, right, act)


def field(label, control):
    return '<div class="mb-3"><label class="label">%s</label>%s</div>' % (label, control)


def toast_btn(label, msg, extra_class="input text-left text-slate-500"):
    return '<button type="button" class="%s" onclick="toast(%s)">%s</button>' % (
        extra_class,
        repr(msg),
        label,
    )


def form_actions(back):
    return """
<div class="mt-4 grid grid-cols-2 gap-3">
  <a href="%s" class="btn flex items-center justify-center border border-slate-200 bg-white py-3 text-sm text-slate-700">取消</a>
  <button type="button" class="btn bg-teal-700 py-3 text-sm text-white" onclick="toast('已保存 / 已提交（进入平台审批）');setTimeout(function(){location.href='%s'},600)">保存 / 提交</button>
</div>""" % (back, back)


def chips(cid, items):
    bits = ['<div id="%s" class="mb-3 flex gap-2 overflow-x-auto pb-1">' % cid]
    for i, name in enumerate(items):
        cls = "chip active" if i == 0 else "chip"
        bits.append('<button type="button" class="%s">%s</button>' % (cls, name))
    bits.append("</div>")
    return "".join(bits)


pages = {}

pages["wecom_入口.html"] = shell(
    "智能设备管理",
    """
<p class="mb-3 text-xs text-slate-500">企业微信工作台入口 · 无独立底部 Tab · 复用企微导航</p>

<div class="card p-4">
  <div class="text-base font-semibold text-slate-900">点巡检</div>
  <p class="mt-1 text-sm text-slate-500">扫描巡检区域二维码，录入正常/异常结果。</p>
  <div class="mt-4 grid grid-cols-2 gap-3">
    <a href="wecom_扫码.html" class="btn flex items-center justify-center gap-2 bg-teal-700 px-3 py-3 text-sm text-white">扫码巡检</a>
    <a href="wecom_记录列表.html" class="btn flex items-center justify-center border border-slate-200 bg-white px-3 py-3 text-sm text-slate-700">我的记录</a>
  </div>
</div>

<div class="card mt-3 p-4">
  <div class="text-base font-semibold text-slate-900">保养管理</div>
  <p class="mt-1 text-sm text-slate-500">通知汇总、计划编制、派工完工。</p>
  <div class="mt-4 grid grid-cols-1 gap-2">
    <a href="wecom_保养通知_列表.html" class="btn flex items-center justify-between border border-slate-200 bg-white px-3 py-3 text-sm text-slate-700"><span><i class="fa-solid fa-bell mr-2 text-slate-400"></i>保养通知</span><i class="fa-solid fa-chevron-right text-slate-300"></i></a>
    <a href="wecom_保养计划_列表.html" class="btn flex items-center justify-between border border-slate-200 bg-white px-3 py-3 text-sm text-slate-700"><span><i class="fa-solid fa-calendar-check mr-2 text-slate-400"></i>保养计划</span><i class="fa-solid fa-chevron-right text-slate-300"></i></a>
    <a href="wecom_保养完工_列表.html" class="btn flex items-center justify-between border border-slate-200 bg-white px-3 py-3 text-sm text-slate-700"><span><i class="fa-solid fa-clipboard-check mr-2 text-slate-400"></i>保养完工</span><i class="fa-solid fa-chevron-right text-slate-300"></i></a>
  </div>
</div>

<div class="card mt-3 p-4">
  <div class="text-base font-semibold text-slate-900">设备维修</div>
  <p class="mt-1 text-sm text-slate-500">故障通知至报修、计划、派工、验收全链路。</p>
  <div class="mt-4 grid grid-cols-1 gap-2">
    <a href="wecom_故障通知_列表.html" class="btn flex items-center justify-between border border-slate-200 bg-white px-3 py-3 text-sm text-slate-700"><span><i class="fa-solid fa-triangle-exclamation mr-2 text-slate-400"></i>故障通知</span><i class="fa-solid fa-chevron-right text-slate-300"></i></a>
    <a href="wecom_故障报修_列表.html" class="btn flex items-center justify-between border border-slate-200 bg-white px-3 py-3 text-sm text-slate-700"><span><i class="fa-solid fa-screwdriver-wrench mr-2 text-slate-400"></i>故障报修</span><i class="fa-solid fa-chevron-right text-slate-300"></i></a>
    <a href="wecom_维修计划_列表.html" class="btn flex items-center justify-between border border-slate-200 bg-white px-3 py-3 text-sm text-slate-700"><span><i class="fa-solid fa-list-check mr-2 text-slate-400"></i>维修计划</span><i class="fa-solid fa-chevron-right text-slate-300"></i></a>
    <a href="wecom_维修派工_列表.html" class="btn flex items-center justify-between border border-slate-200 bg-white px-3 py-3 text-sm text-slate-700"><span><i class="fa-solid fa-user-gear mr-2 text-slate-400"></i>维修派工</span><i class="fa-solid fa-chevron-right text-slate-300"></i></a>
    <a href="wecom_维修完工_列表.html" class="btn flex items-center justify-between border border-slate-200 bg-white px-3 py-3 text-sm text-slate-700"><span><i class="fa-solid fa-flag-checkered mr-2 text-slate-400"></i>维修完工</span><i class="fa-solid fa-chevron-right text-slate-300"></i></a>
  </div>
</div>

<a class="mt-4 block text-center text-xs text-slate-400" href="../../index.html">返回版本入口</a>
""",
    back=None,
)

pages["wecom_保养通知_列表.html"] = shell(
    "保养通知",
    """
<p class="mb-3 text-xs text-slate-500">业务汇总（只读），非消息中心。</p>
<div class="mb-3"><input class="input" placeholder="搜索设备编号 / 名称" /></div>
<div class="space-y-3">
%s
%s
</div>
"""
    % (
        card_link("wecom_保养通知_详情.html", "BN-20260805-01 · 1号门吊", "下次保养 2026-08-10 · 通知 2026-08-05 · 王工", badge("待保养", "warn")),
        card_link("wecom_保养通知_详情.html", "BN-20260806-03 · 2号输送线", "下次保养 2026-08-12 · 通知 2026-08-06 · 赵工", badge("待保养", "warn")),
    ),
)

pages["wecom_保养通知_详情.html"] = shell(
    "通知详情",
    """
<div class="card p-4 space-y-3 text-sm">
  <div class="flex justify-between"><span class="text-slate-500">通知编号</span><span class="font-medium text-slate-900">BN-20260805-01</span></div>
  <div class="flex justify-between"><span class="text-slate-500">运营设备</span><span class="text-slate-900">OP-2026-001 / 1号门吊</span></div>
  <div class="flex justify-between"><span class="text-slate-500">下次保养日期</span><span class="text-slate-900">2026-08-10</span></div>
  <div class="flex justify-between"><span class="text-slate-500">通知日期</span><span class="text-slate-900">2026-08-05</span></div>
  <div class="flex justify-between"><span class="text-slate-500">维保负责人</span><span class="text-slate-900">王工</span></div>
  <div class="pt-2 border-t border-slate-100 text-xs text-slate-500">来源：周期保养规则自动汇总，仅查看。</div>
</div>
<a href="wecom_保养计划_新增.html" class="btn mt-4 flex items-center justify-center bg-teal-700 py-3 text-sm text-white">去建保养计划</a>
""",
    back="wecom_保养通知_列表.html",
)

pages["wecom_保养计划_列表.html"] = shell(
    "保养计划",
    chips("planChips", ["全部", "草稿", "审核中", "已通过"])
    + '<div class="space-y-3">'
    + card_link("wecom_保养计划_详情.html", "BJ-2026-021 · 1号门吊", "周期保养 · 2026-08-10 09:00-12:00", badge("已通过", "ok"))
    + card_block(
        "BJ-2026-028 · 2号输送线",
        "专项保养 · 2026-08-15 14:00-17:00",
        badge("草稿", "muted"),
        '<a href="wecom_保养计划_新增.html">编辑</a><button type="button" onclick="toast(' + repr("已提交，进入平台审批") + ')">提交</button><button type="button" onclick="toast(' + repr("已删除（原型）") + ')">删除</button>',
    )
    + "</div>",
    right='<a href="wecom_保养计划_新增.html" class="text-sm text-teal-700">新增</a>',
    extra_js="bindChips('planChips');",
)

pages["wecom_保养计划_新增.html"] = shell(
    "新增保养计划",
    field("保养类型", '<select class="select"><option>周期保养</option><option>专项保养</option></select>')
    + field("运营设备", toast_btn("选择运营设备", "选择运营设备（原型）"))
    + field("保养标准", toast_btn("选择保养标准", "选择保养标准（原型）"))
    + field("计划开始", '<input class="input" type="datetime-local" value="2026-08-15T14:00" />')
    + field("计划结束", '<input class="input" type="datetime-local" value="2026-08-15T17:00" />')
    + field("维保负责人", '<input class="input" value="赵工" />')
    + field("备注", '<textarea class="input" rows="3" placeholder="选填"></textarea>')
    + form_actions("wecom_保养计划_列表.html"),
    back="wecom_保养计划_列表.html",
)

pages["wecom_保养计划_详情.html"] = shell(
    "计划详情",
    """
<div class="card p-4 space-y-3 text-sm">
  <div class="flex justify-between"><span class="text-slate-500">计划单号</span><span class="font-medium">BJ-2026-021</span></div>
  <div class="flex justify-between"><span class="text-slate-500">运营设备</span><span>1号门吊</span></div>
  <div class="flex justify-between"><span class="text-slate-500">类型</span><span>周期保养</span></div>
  <div class="flex justify-between"><span class="text-slate-500">计划时间</span><span>2026-08-10 09:00-12:00</span></div>
  <div class="flex justify-between items-center"><span class="text-slate-500">业务状态</span>%s</div>
</div>
"""
    % badge("已通过", "ok"),
    back="wecom_保养计划_列表.html",
)

pages["wecom_保养完工_列表.html"] = shell(
    "保养完工",
    chips("bwChips", ["全部", "草稿", "已通过"])
    + '<div class="space-y-3">'
    + card_link("wecom_保养完工_详情.html", "BW-2026-015 · 1号门吊", "计划 BJ-2026-021 · 验收 2026-08-10 · 下次 2026-09-10", badge("已通过", "ok"))
    + card_block(
        "BW-2026-019 · 2号输送线",
        "计划 BJ-2026-028 · 验收 2026-08-07",
        badge("草稿", "muted"),
        '<a href="wecom_保养完工_新增.html">编辑</a><button type="button" onclick="toast(' + repr("已提交，进入平台审批") + ')">提交</button>',
    )
    + "</div>",
    right='<a href="wecom_保养完工_新增.html" class="text-sm text-teal-700">新增</a>',
    extra_js="bindChips('bwChips');",
)

pages["wecom_保养完工_新增.html"] = shell(
    "新增保养完工",
    field("保养计划", toast_btn("选择保养计划", "选择已生效保养计划（原型）"))
    + field("验收日期", '<input class="input" type="date" value="2026-08-10" />')
    + field("下次保养日期", '<input class="input" type="date" value="2026-09-10" />')
    + field(
        "派工记录",
        """<button type="button" class="btn w-full border border-dashed border-slate-300 py-3 text-sm text-slate-600" onclick="openModal('mDispatch')">添加派工记录</button>
<div class="mt-2 rounded-xl bg-slate-50 px-3 py-2 text-xs text-slate-600">王工 · 2026-08-10 09:00-11:30</div>""",
    )
    + field("完工说明", '<textarea class="input" rows="3" placeholder="填写验收结论"></textarea>')
    + form_actions("wecom_保养完工_列表.html")
    + """
<div id="mDispatch" class="modal-mask" onclick="if(event.target===this)closeModal('mDispatch')">
  <div class="modal-box">
    <div class="mb-3 flex items-center justify-between">
      <div class="text-sm font-semibold">添加派工</div>
      <button type="button" onclick="closeModal('mDispatch')"><i class="fa-solid fa-xmark text-slate-400"></i></button>
    </div>
    <div class="mb-3"><label class="label">作业人</label><input class="input" value="王工" /></div>
    <div class="mb-3"><label class="label">开始时间</label><input class="input" type="datetime-local" value="2026-08-10T09:00" /></div>
    <div class="mb-3"><label class="label">结束时间</label><input class="input" type="datetime-local" value="2026-08-10T11:30" /></div>
    <button type="button" class="btn mt-2 w-full bg-teal-700 py-3 text-sm text-white" onclick="closeModal('mDispatch');toast('已添加派工记录')">确定</button>
  </div>
</div>
""",
    back="wecom_保养完工_列表.html",
)

pages["wecom_保养完工_详情.html"] = shell(
    "完工详情",
    """
<div class="card p-4 space-y-3 text-sm">
  <div class="flex justify-between"><span class="text-slate-500">完工单号</span><span class="font-medium">BW-2026-015</span></div>
  <div class="flex justify-between"><span class="text-slate-500">计划单号</span><span>BJ-2026-021</span></div>
  <div class="flex justify-between"><span class="text-slate-500">运营设备</span><span>1号门吊</span></div>
  <div class="flex justify-between"><span class="text-slate-500">验收日期</span><span>2026-08-10</span></div>
  <div class="flex justify-between"><span class="text-slate-500">下次保养</span><span>2026-09-10</span></div>
  <div class="flex justify-between items-center"><span class="text-slate-500">业务状态</span>%s</div>
</div>
"""
    % badge("已通过", "ok"),
    back="wecom_保养完工_列表.html",
)

pages["wecom_故障通知_列表.html"] = shell(
    "故障通知",
    """
<p class="mb-3 text-xs text-slate-500">本期来源：点巡检「立即维修」建议（只读）。</p>
<div class="space-y-3">
%s
</div>
"""
    % card_link("wecom_故障通知_详情.html", "GN-20260806-02 · 2号输送线", "点巡检-立即维修 · 2026-08-06 16:35", badge("待处理", "warn")),
)

pages["wecom_故障通知_详情.html"] = shell(
    "通知详情",
    """
<div class="card p-4 space-y-3 text-sm">
  <div class="flex justify-between"><span class="text-slate-500">通知编号</span><span class="font-medium">GN-20260806-02</span></div>
  <div class="flex justify-between"><span class="text-slate-500">来源</span><span>点巡检-立即维修</span></div>
  <div class="flex justify-between"><span class="text-slate-500">运营设备</span><span>2号输送线</span></div>
  <div class="flex justify-between"><span class="text-slate-500">通知时间</span><span>2026-08-06 16:35</span></div>
  <div><div class="text-slate-500 mb-1">摘要</div><div class="rounded-xl bg-slate-50 px-3 py-2 text-slate-800">驱动端异响，建议立即维修</div></div>
</div>
<a href="wecom_故障报修_新增.html" class="btn mt-4 flex items-center justify-center bg-teal-700 py-3 text-sm text-white">去故障报修</a>
""",
    back="wecom_故障通知_列表.html",
)

pages["wecom_故障报修_列表.html"] = shell(
    "故障报修",
    chips("gzChips", ["全部", "待计划", "待派工", "待验收", "已完工"])
    + '<div class="space-y-3">'
    + card_link("wecom_故障报修_详情.html", "GZ-2026-044 · 2号输送线", "机械故障 · 2026-08-06 16:10", badge("待派工", "warn") + " " + badge("紧急", "danger"))
    + card_link("wecom_故障报修_详情.html", "GZ-2026-039 · 1号门吊", "电气故障 · 2026-07-28 10:20", badge("已完工", "ok") + " " + badge("一般", "muted"))
    + "</div>",
    right='<a href="wecom_故障报修_新增.html" class="text-sm text-teal-700">新增</a>',
    extra_js="bindChips('gzChips');",
)

pages["wecom_故障报修_新增.html"] = shell(
    "新增故障报修",
    field("运营设备", toast_btn("选取故障设备", "选取故障设备（原型）"))
    + field("故障类型", '<select class="select"><option>机械故障</option><option>电气故障</option><option>其他</option></select>')
    + field("严重程度", '<select class="select"><option>一般</option><option>严重</option><option selected>紧急</option></select>')
    + field("发生时间", '<input class="input" type="datetime-local" value="2026-08-06T16:10" />')
    + field("故障描述", '<textarea class="input" rows="3" placeholder="描述现象与影响范围">驱动端异响</textarea>')
    + field(
        "现场照片",
        '<button type="button" class="btn w-full border border-dashed border-slate-300 py-6 text-sm text-slate-500" onclick="toast(' + repr("上传照片（原型）") + ')"><i class="fa-solid fa-camera mr-2"></i>上传现场照片</button>',
    )
    + form_actions("wecom_故障报修_列表.html"),
    back="wecom_故障报修_列表.html",
)

pages["wecom_故障报修_详情.html"] = shell(
    "报修详情",
    """
<div class="card p-4 space-y-3 text-sm">
  <div class="flex justify-between"><span class="text-slate-500">报修单号</span><span class="font-medium">GZ-2026-044</span></div>
  <div class="flex justify-between"><span class="text-slate-500">运营设备</span><span>2号输送线</span></div>
  <div class="flex justify-between"><span class="text-slate-500">故障类型</span><span>机械故障</span></div>
  <div class="flex justify-between items-center"><span class="text-slate-500">严重程度</span>%s</div>
  <div class="flex justify-between"><span class="text-slate-500">发生时间</span><span>2026-08-06 16:10</span></div>
  <div class="flex justify-between items-center"><span class="text-slate-500">故障状态</span>%s</div>
  <div><div class="text-slate-500 mb-1">描述</div><div class="rounded-xl bg-slate-50 px-3 py-2">驱动端异响</div></div>
</div>
"""
    % (badge("紧急", "danger"), badge("待派工", "warn")),
    back="wecom_故障报修_列表.html",
)

pages["wecom_维修计划_列表.html"] = shell(
    "维修计划",
    chips("wjChips", ["全部", "草稿", "已通过", "已作废"])
    + '<div class="space-y-3">'
    + card_link("wecom_维修计划_详情.html", "WJ-2026-031 · 2号输送线", "故障 GZ-2026-044 · 计划 2026-08-07 09:00", badge("已通过", "ok"))
    + card_block(
        "WJ-2026-033 · 2号输送线",
        "故障 GZ-2026-044 · 计划 2026-08-08 14:00",
        badge("草稿", "muted"),
        '<a href="wecom_维修计划_新增.html">编辑</a><button type="button" onclick="toast(' + repr("已提交，进入平台审批") + ')">提交</button><button type="button" onclick="toast(' + repr("已删除（原型）") + ')">删除</button>',
    )
    + "</div>",
    right='<a href="wecom_维修计划_新增.html" class="text-sm text-teal-700">新增</a>',
    extra_js="bindChips('wjChips');",
)

pages["wecom_维修计划_新增.html"] = shell(
    "新增维修计划",
    field("故障单", toast_btn("选取故障单", "选取故障设备 / 故障单（原型）"))
    + field("计划维修时间", '<input class="input" type="datetime-local" value="2026-08-08T14:00" />')
    + field("维修内容", '<textarea class="input" rows="3" placeholder="计划维修项目">更换驱动轴承并复核对中</textarea>')
    + field("预计工时（小时）", '<input class="input" type="number" value="3" />')
    + form_actions("wecom_维修计划_列表.html"),
    back="wecom_维修计划_列表.html",
)

pages["wecom_维修计划_详情.html"] = shell(
    "计划详情",
    """
<div class="card p-4 space-y-3 text-sm">
  <div class="flex justify-between"><span class="text-slate-500">计划单号</span><span class="font-medium">WJ-2026-031</span></div>
  <div class="flex justify-between"><span class="text-slate-500">故障单号</span><span>GZ-2026-044</span></div>
  <div class="flex justify-between"><span class="text-slate-500">运营设备</span><span>2号输送线</span></div>
  <div class="flex justify-between"><span class="text-slate-500">计划维修时间</span><span>2026-08-07 09:00</span></div>
  <div class="flex justify-between items-center"><span class="text-slate-500">状态</span>%s</div>
</div>
<p class="mt-3 text-xs text-slate-500">已存在派工记录时不可作废。</p>
"""
    % badge("已通过", "ok"),
    back="wecom_维修计划_列表.html",
)

pages["wecom_维修派工_列表.html"] = shell(
    "维修派工",
    """
<p class="mb-3 text-xs text-slate-500">一计划一次派工。</p>
<div class="space-y-3">
%s
</div>
"""
    % card_block(
        "WP-2026-022 · 2号输送线",
        "计划 WJ-2026-031 · 2026-08-07 09:00-11:30",
        badge("已登记", "ok"),
        '<button type="button" onclick="toast(' + repr("查看派工") + ')">查看</button><a href="wecom_维修派工_新增.html">编辑</a><button type="button" onclick="toast(' + repr("已删除（原型）") + ')">删除</button>',
    ),
    right='<a href="wecom_维修派工_新增.html" class="text-sm text-teal-700">新增</a>',
)

pages["wecom_维修派工_新增.html"] = shell(
    "新增维修派工",
    field("维修计划", toast_btn("选取维修计划", "选取维修计划（原型）"))
    + field("维修开始", '<input class="input" type="datetime-local" value="2026-08-07T09:00" />')
    + field("维修结束", '<input class="input" type="datetime-local" value="2026-08-07T11:30" />')
    + field("维修人员", '<input class="input" value="李工、陈工" />')
    + field("作业说明", '<textarea class="input" rows="3" placeholder="选填"></textarea>')
    + form_actions("wecom_维修派工_列表.html"),
    back="wecom_维修派工_列表.html",
)

pages["wecom_维修完工_列表.html"] = shell(
    "维修完工",
    chips("wwChips", ["全部", "草稿", "已通过"])
    + '<div class="space-y-3">'
    + card_link("wecom_维修完工_详情.html", "WW-2026-017 · 1号门吊", "故障 GZ-2026-039 · 验收 2026-07-29", badge("已通过", "ok"))
    + card_block(
        "WW-2026-021 · 2号输送线",
        "故障 GZ-2026-044 · 验收 2026-08-07",
        badge("草稿", "muted"),
        '<a href="wecom_维修完工_新增.html">编辑</a><button type="button" onclick="toast(' + repr("已提交，进入平台审批") + ')">提交</button>',
    )
    + "</div>",
    right='<a href="wecom_维修完工_新增.html" class="text-sm text-teal-700">新增</a>',
    extra_js="bindChips('wwChips');",
)

pages["wecom_维修完工_新增.html"] = shell(
    "新增维修完工",
    field("故障单", toast_btn("选取故障单", "选取未完工故障单（原型）"))
    + """
<div class="card mb-3 p-3 text-xs text-slate-600">
  <div class="font-medium text-slate-800 mb-2">关联计划 / 派工（回显）</div>
  <div>计划 WJ-2026-031 · 派工 WP-2026-022 · 09:00-11:30</div>
</div>
"""
    + field("验收日期", '<input class="input" type="date" value="2026-08-07" />')
    + field("验收结论", '<select class="select"><option>合格</option><option>带病运行观察</option><option>不合格</option></select>')
    + field("完工说明", '<textarea class="input" rows="3" placeholder="填写验收说明"></textarea>')
    + form_actions("wecom_维修完工_列表.html"),
    back="wecom_维修完工_列表.html",
)

pages["wecom_维修完工_详情.html"] = shell(
    "完工详情",
    """
<div class="card p-4 space-y-3 text-sm">
  <div class="flex justify-between"><span class="text-slate-500">完工单号</span><span class="font-medium">WW-2026-017</span></div>
  <div class="flex justify-between"><span class="text-slate-500">故障单号</span><span>GZ-2026-039</span></div>
  <div class="flex justify-between"><span class="text-slate-500">运营设备</span><span>1号门吊</span></div>
  <div class="flex justify-between"><span class="text-slate-500">验收日期</span><span>2026-07-29</span></div>
  <div class="flex justify-between items-center"><span class="text-slate-500">业务状态</span>%s</div>
</div>
"""
    % badge("已通过", "ok"),
    back="wecom_维修完工_列表.html",
)

for name, html in pages.items():
    (OUT / name).write_text(html, encoding="utf-8")
    print("wrote", name)

print("done", len(pages))
