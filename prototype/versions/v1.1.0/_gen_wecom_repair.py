# -*- coding: utf-8 -*-
"""Generate WeCom H5 repair module pages aligned to Axure PC."""
from pathlib import Path

OUT = Path(r"G:\产品\EMS\prototype\versions\v1.1.0\pages\wecom")

SHELL = r'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
  <title>__TITLE__ · 企微H5 · EMS v1.1.0</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css" />
  <style>
    body{font-family:-apple-system,BlinkMacSystemFont,"SF Pro Text","Segoe UI",Roboto,"Helvetica Neue",sans-serif;line-height:1.6;margin:0;min-height:100vh;background:linear-gradient(160deg,#e2e8f0 0%,#f8fafc 45%,#cbd5e1 100%);}
    .stage{min-height:100vh;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:24px 16px;}
    .phone{width:390px;height:844px;border-radius:48px;border:10px solid #e5e7eb;background:#0f172a;box-shadow:0 24px 64px rgba(15,23,42,.22);position:relative;overflow:hidden;flex-shrink:0;}
    .island{position:absolute;top:12px;left:50%;transform:translateX(-50%);width:120px;height:32px;border-radius:20px;background:#0f172a;z-index:30;}
    .phone-screen{position:absolute;inset:0;margin:8px;border-radius:40px;overflow:hidden;background:#f8fafc;display:flex;flex-direction:column;}
    .status-bar{height:48px;padding:14px 20px 0;display:flex;justify-content:space-between;align-items:flex-start;font-size:12px;font-weight:600;color:#0f172a;flex-shrink:0;}
    .nav-bar{height:48px;display:flex;align-items:center;justify-content:space-between;padding:0 16px;background:#fff;border-bottom:1px solid #e2e8f0;flex-shrink:0;}
    .content{flex:1;overflow-y:auto;padding:16px;-webkit-overflow-scrolling:touch;}
    .content::-webkit-scrollbar{display:none;}
    .footer-bar{flex-shrink:0;padding:12px 16px 8px;background:#fff;border-top:1px solid #e2e8f0;}
    .home-bar{height:22px;display:flex;align-items:center;justify-content:center;background:#fff;flex-shrink:0;}
    .home-bar span{width:128px;height:5px;border-radius:999px;background:#cbd5e1;}
    .btn{border-radius:1rem;} .btn:active{transform:scale(0.95);}
    .card{background:#fff;border:1px solid #e2e8f0;border-radius:1.25rem;box-shadow:0 4px 12px rgba(0,0,0,0.05);}
    .input,.select,textarea.input{width:100%;border:1px solid #e2e8f0;border-radius:0.75rem;padding:0.625rem 0.75rem;font-size:0.875rem;background:#fff;outline:none;box-sizing:border-box;}
    .input:focus,.select:focus,textarea.input:focus{border-color:#0f766e;}
    .input[readonly],.input:disabled{background:#f8fafc;color:#334155;}
    .label{display:block;margin-bottom:0.25rem;font-size:0.75rem;color:#64748b;}
    .req::after{content:"*";color:#e11d48;margin-left:2px;}
    .sec-title{display:flex;align-items:center;justify-content:space-between;margin-bottom:12px;padding-left:8px;border-left:3px solid #0f766e;}
    .sec-title h3{font-size:14px;font-weight:600;color:#0f172a;margin:0;}
    .toast{position:absolute;left:50%;bottom:36px;transform:translateX(-50%) translateY(8px);background:#0f172a;color:#fff;padding:10px 14px;border-radius:14px;font-size:13px;opacity:0;transition:.2s;z-index:50;max-width:86%;}
    .toast.show{opacity:1;transform:translateX(-50%) translateY(0);}
    .modal-mask{position:absolute;inset:0;background:rgba(15,23,42,.45);display:none;align-items:center;justify-content:center;padding:16px;z-index:40;}
    .modal-mask.show{display:flex;}
    .modal-box{width:100%;max-height:82%;overflow:auto;background:#fff;border-radius:1.5rem;padding:16px;box-shadow:0 8px 24px rgba(0,0,0,0.08);}
    .hint{margin-top:14px;font-size:12px;color:#64748b;text-align:center;}
    .chip{border-radius:999px;border:1px solid #e2e8f0;background:#fff;color:#475569;padding:6px 12px;font-size:12px;font-weight:500;white-space:nowrap;}
    .chip.active{background:#0f172a;color:#fff;border-color:#0f172a;}
    .cell{border:1px solid #e2e8f0;border-radius:0.75rem;padding:10px;background:#f8fafc;}
    .cell .k{font-size:11px;color:#64748b;} .cell .v{font-size:13px;color:#0f172a;margin-top:2px;word-break:break-all;}
    .row{display:flex;justify-content:space-between;gap:12px;padding:8px 0;border-bottom:1px solid #f1f5f9;font-size:13px;}
    .row:last-child{border-bottom:0;}
    .row .k{color:#64748b;flex-shrink:0;} .row .v{color:#0f172a;text-align:right;}
    .meta{font-size:12px;color:#64748b;line-height:1.5;}
    .upload{border:1px dashed #cbd5e1;border-radius:0.75rem;padding:14px;text-align:center;color:#64748b;font-size:12px;background:#f8fafc;}
    .equip-item.selected{border-color:#0f766e;box-shadow:0 0 0 1px #0f766e;}
    .radio{width:18px;height:18px;border-radius:999px;border:2px solid #cbd5e1;flex-shrink:0;}
    .equip-item.selected .radio{border-color:#0f766e;background:#0f766e;box-shadow:inset 0 0 0 3px #fff;}
  </style>
</head>
<body>
  <div class="stage">
    <div class="phone">
      <div class="island"></div>
      <div class="phone-screen">
        <div class="status-bar"><span>9:41</span><span style="display:flex;gap:6px;"><i class="fa-solid fa-signal"></i><i class="fa-solid fa-wifi"></i><i class="fa-solid fa-battery-full"></i></span></div>
        <div class="nav-bar">
          __NAV__
        </div>
        <div class="content">
__BODY__
        </div>
        __FOOTER__
        <div class="home-bar"><span></span></div>
        <div id="toast" class="toast"></div>
      </div>
    </div>
    <p class="hint">企微 H5 演示外壳（iPhone 16 · 390×844）· 无独立底部业务 Tab</p>
  </div>
  <script>
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
__SCRIPT__
  </script>
</body>
</html>
'''

def write(name, title, nav, body, script="", footer=""):
    html = (SHELL
            .replace("__TITLE__", title)
            .replace("__NAV__", nav)
            .replace("__BODY__", body)
            .replace("__SCRIPT__", script)
            .replace("__FOOTER__", footer))
    path = OUT / name
    path.write_text(html, encoding="utf-8")
    print("wrote", path.name)


# ========== 故障通知 ==========
write(
    "wecom_故障通知_列表.html",
    "故障通知",
    '''<a href="wecom_入口.html" class="text-slate-700"><i class="fa-solid fa-chevron-left"></i></a>
          <div class="text-sm font-semibold text-slate-900">故障通知</div>
          <span class="w-4"></span>''',
    '''
          <p class="mb-2 text-xs text-slate-500">业务汇总（只读）· 操作仅「查看」· 非消息中心</p>
          <div id="statusChips" class="mb-3 flex gap-2 overflow-x-auto pb-1">
            <button type="button" class="chip active">全部</button>
            <button type="button" class="chip">待处理</button>
            <button type="button" class="chip">已处理</button>
          </div>
          <div class="mb-3 flex gap-2">
            <input id="kw" class="input" placeholder="通知编号 / 设备编号 / 名称" />
            <button type="button" class="btn shrink-0 bg-teal-700 px-3 text-sm text-white" onclick="doSearch()">查询</button>
          </div>
          <div id="list" class="space-y-3"></div>
          <p id="empty" class="hidden py-10 text-center text-sm text-slate-400">无匹配通知</p>
''',
    '''
    const DATA=[
      {id:'GN-55456541', time:'2024-12-23 12:00', code:'2530门', name:'2530门机', spec:'4546', loc:'3泊位', owner:'张飞', source:'点巡检', status:'待处理', content:'点巡检发现驱动端异响，建议立即维修。'},
      {id:'GN-55456542', time:'2024-12-23 12:00', code:'4530门', name:'4530门机', spec:'4546', loc:'3泊位', owner:'张飞', source:'点巡检', status:'待处理', content:'限位开关异常，建议安排故障报修。'},
      {id:'GN-55456543', time:'2024-12-23 12:00', code:'4531门', name:'4531门机', spec:'4546', loc:'3泊位', owner:'张飞', source:'点巡检', status:'已处理', content:'钢丝绳磨损超限，已转故障报修。'}
    ];
    let filtered=DATA.slice(), status='全部';
    function render(){
      const box=document.getElementById('list'), empty=document.getElementById('empty');
      if(!filtered.length){box.innerHTML='';empty.classList.remove('hidden');return;}
      empty.classList.add('hidden');
      box.innerHTML=filtered.map(d=>{
        const chip=d.status==='已处理'?'bg-emerald-50 text-emerald-700':'bg-amber-50 text-amber-700';
        return '<a href="wecom_故障通知_详情.html?id='+encodeURIComponent(d.id)+'" class="card block p-4">'
          +'<div class="flex items-start justify-between gap-2"><div class="min-w-0">'
          +'<div class="text-sm font-medium text-slate-900">'+d.id+' · '+d.name+'</div>'
          +'<div class="meta mt-1">'+d.code+' · '+d.spec+' · '+d.loc+'</div>'
          +'<div class="meta mt-0.5">通知时间 '+d.time+' · 来源 '+d.source+' · '+d.owner+'</div>'
          +'</div><div class="shrink-0 text-right"><span class="rounded-full px-2 py-0.5 text-xs '+chip+'">'+d.status+'</span>'
          +'<div class="mt-2 text-xs font-medium text-teal-700">查看</div></div></div></a>';
      }).join('');
    }
    function apply(){
      const q=(document.getElementById('kw').value||'').trim().toLowerCase();
      filtered=DATA.filter(d=>{
        if(status!=='全部' && d.status!==status) return false;
        if(!q) return true;
        return (d.id+d.code+d.name+d.loc+d.owner).toLowerCase().indexOf(q)>=0;
      });
      render();
    }
    function doSearch(){ apply(); toast('已查询，共 '+filtered.length+' 条'); }
    document.getElementById('statusChips').querySelectorAll('.chip').forEach(btn=>{
      btn.addEventListener('click',()=>{
        document.getElementById('statusChips').querySelectorAll('.chip').forEach(c=>c.classList.remove('active'));
        btn.classList.add('active'); status=btn.textContent.trim(); apply();
      });
    });
    document.getElementById('kw').addEventListener('keydown',e=>{if(e.key==='Enter')doSearch();});
    render();
'''
)

write(
    "wecom_故障通知_详情.html",
    "故障通知详情",
    '''<a href="wecom_故障通知_列表.html" class="text-slate-700"><i class="fa-solid fa-chevron-left"></i></a>
          <div class="text-sm font-semibold text-slate-900">故障通知详情</div>
          <span class="w-4"></span>''',
    '''
          <div class="card mb-3 p-4">
            <div class="sec-title"><h3>运营设备</h3></div>
            <div class="grid grid-cols-2 gap-2">
              <div class="cell"><div class="k">运营设备编号</div><div class="v" id="eqCode">-</div></div>
              <div class="cell"><div class="k">运营设备名称</div><div class="v" id="eqName">-</div></div>
              <div class="cell"><div class="k">规格型号</div><div class="v" id="eqSpec">-</div></div>
              <div class="cell"><div class="k">使用位置</div><div class="v" id="eqLoc">-</div></div>
            </div>
          </div>
          <div class="card mb-3 p-4">
            <div class="sec-title"><h3>通知信息</h3></div>
            <div class="row"><span class="k">通知编号</span><span class="v" id="nid">-</span></div>
            <div class="row"><span class="k">通知时间</span><span class="v" id="ntime">-</span></div>
            <div class="row"><span class="k">通知维保负责人</span><span class="v" id="owner">-</span></div>
            <div class="row"><span class="k">通知来源</span><span class="v" id="source">-</span></div>
            <div class="row"><span class="k">处理状态</span><span class="v" id="status">-</span></div>
            <div class="pt-2"><div class="text-xs text-slate-500 mb-1">通知内容</div>
              <div id="content" class="rounded-xl bg-slate-50 px-3 py-3 text-sm text-slate-700">-</div></div>
          </div>
          <p class="mb-3 text-center text-xs text-slate-400">只读查看 · 对应 PC「查看」</p>
          <a id="goRepair" href="wecom_故障报修_新增.html" class="btn flex items-center justify-center bg-teal-700 py-3 text-sm text-white">去建故障报修</a>
''',
    '''
    const MAP={
      'GN-55456541':{id:'GN-55456541',time:'2024-12-23 12:00',code:'2530门',name:'2530门机',spec:'4546',loc:'3泊位',owner:'张飞',source:'点巡检',status:'待处理',content:'点巡检发现驱动端异响，建议立即维修。'},
      'GN-55456542':{id:'GN-55456542',time:'2024-12-23 12:00',code:'4530门',name:'4530门机',spec:'4546',loc:'3泊位',owner:'张飞',source:'点巡检',status:'待处理',content:'限位开关异常，建议安排故障报修。'},
      'GN-55456543':{id:'GN-55456543',time:'2024-12-23 12:00',code:'4531门',name:'4531门机',spec:'4546',loc:'3泊位',owner:'张飞',source:'点巡检',status:'已处理',content:'钢丝绳磨损超限，已转故障报修。'}
    };
    const d=MAP[new URLSearchParams(location.search).get('id')]||MAP['GN-55456541'];
    eqCode.textContent=d.code; eqName.textContent=d.name; eqSpec.textContent=d.spec; eqLoc.textContent=d.loc;
    nid.textContent=d.id; ntime.textContent=d.time; owner.textContent=d.owner; source.textContent=d.source; status.textContent=d.status; content.textContent=d.content;
    sessionStorage.setItem('ems_wecom_selected_equip', JSON.stringify({code:d.code,name:d.name,spec:d.spec,loc:d.loc,status:'故障',type:'起重设备'}));
'''
)

# ========== 故障报修 ==========
write(
    "wecom_故障报修_列表.html",
    "故障报修",
    '''<a href="wecom_入口.html" class="text-slate-700"><i class="fa-solid fa-chevron-left"></i></a>
          <div class="text-sm font-semibold text-slate-900">故障报修</div>
          <a href="wecom_故障报修_新增.html" class="text-sm text-teal-700">新增</a>''',
    '''
          <div id="chips" class="mb-3 flex gap-2 overflow-x-auto pb-1">
            <button type="button" class="chip active">全部</button>
            <button type="button" class="chip">待计划</button>
            <button type="button" class="chip">维修中</button>
            <button type="button" class="chip">已完工</button>
          </div>
          <div class="mb-3 flex gap-2">
            <input id="kw" class="input" placeholder="报修单号 / 设备编号 / 名称" />
            <button type="button" class="btn shrink-0 bg-teal-700 px-3 text-sm text-white" onclick="doSearch()">查询</button>
          </div>
          <div id="list" class="space-y-3"></div>
''',
    '''
    const DATA=[
      {no:'55456541', code:'46546', name:'门机', spec:'46546', loc:'3号泊位', status:'待计划', type:'运行故障', level:'严重', happen:'2025-05-09 12:00', creator:'张飞', created:'2025-05-09 12:00'},
      {no:'55456542', code:'46546', name:'门机', spec:'46546', loc:'3号泊位', status:'待计划', type:'运行故障', level:'严重', happen:'2025-05-09 12:00', creator:'张飞', created:'2025-05-09 12:00'},
      {no:'55456543', code:'46546', name:'门机', spec:'46546', loc:'3号泊位', status:'维修中', type:'运行故障', level:'严重', happen:'2025-05-09 12:00', creator:'张飞', created:'2025-05-09 12:00'}
    ];
    let filtered=DATA.slice(), st='全部';
    function statusChip(s){
      if(s==='待计划') return 'bg-amber-50 text-amber-700';
      if(s==='维修中') return 'bg-sky-50 text-sky-700';
      return 'bg-emerald-50 text-emerald-700';
    }
    function render(){
      list.innerHTML=filtered.map(d=>'<div class="card p-4">'
        +'<a href="wecom_故障报修_详情.html?no='+d.no+'" class="block">'
        +'<div class="flex items-start justify-between gap-2"><div class="min-w-0">'
        +'<div class="text-sm font-medium text-slate-900">'+d.no+' · '+d.name+'</div>'
        +'<div class="meta mt-1">'+d.code+' · '+d.spec+' · '+d.loc+'</div>'
        +'<div class="meta mt-0.5">'+d.type+' · '+d.level+' · 发生 '+d.happen+'</div>'
        +'</div><span class="shrink-0 rounded-full px-2 py-0.5 text-xs '+statusChip(d.status)+'">'+d.status+'</span></div></a>'
        +(d.status==='待计划'?'<div class="mt-3 flex flex-wrap gap-3 text-xs text-teal-700"><a href="wecom_故障报修_详情.html?no='+d.no+'">查看</a><button type="button" onclick="toast(\\'已删除（原型）\\')">删除</button><a href="wecom_维修计划_新增.html?fault='+d.no+'">去建计划</a></div>':'<div class="mt-3 text-xs text-teal-700"><a href="wecom_故障报修_详情.html?no='+d.no+'">查看</a></div>')
        +'</div>').join('')||'<p class="py-10 text-center text-sm text-slate-400">无数据</p>';
    }
    function apply(){
      const q=(kw.value||'').trim().toLowerCase();
      filtered=DATA.filter(d=>{
        if(st!=='全部'&&d.status!==st) return false;
        if(!q) return true;
        return (d.no+d.code+d.name+d.loc).toLowerCase().indexOf(q)>=0;
      }); render();
    }
    function doSearch(){apply();toast('已查询，共 '+filtered.length+' 条');}
    chips.querySelectorAll('.chip').forEach(btn=>btn.addEventListener('click',()=>{
      chips.querySelectorAll('.chip').forEach(c=>c.classList.remove('active')); btn.classList.add('active'); st=btn.textContent.trim(); apply();
    }));
    kw.addEventListener('keydown',e=>{if(e.key==='Enter')doSearch();});
    render();
'''
)

write(
    "wecom_故障报修_新增.html",
    "故障报修",
    '''<a href="wecom_故障报修_列表.html" class="text-slate-700" onclick="sessionStorage.removeItem('ems_wecom_selected_equip')"><i class="fa-solid fa-chevron-left"></i></a>
          <div class="text-sm font-semibold text-slate-900">故障报修</div>
          <span class="w-4"></span>''',
    '''
          <div class="card mb-3 p-4">
            <div class="sec-title">
              <h3>运营设备</h3>
              <a href="wecom_选择运营设备.html?from=repair" class="text-xs font-medium text-teal-700">选择运营设备</a>
            </div>
            <div id="equipEmpty" class="rounded-xl border border-dashed border-slate-200 bg-slate-50 px-3 py-4 text-center text-xs text-slate-400">请选择运营设备</div>
            <div id="equipInfo" class="hidden grid grid-cols-2 gap-2">
              <div class="cell"><div class="k">运营设备编号</div><div class="v" id="eqCode">-</div></div>
              <div class="cell"><div class="k">运营设备名称</div><div class="v" id="eqName">-</div></div>
              <div class="cell"><div class="k">规格型号</div><div class="v" id="eqSpec">-</div></div>
              <div class="cell"><div class="k">使用位置</div><div class="v" id="eqLoc">-</div></div>
            </div>
          </div>
          <div class="card mb-3 p-4">
            <div class="sec-title"><h3>故障信息</h3></div>
            <div class="mb-3"><label class="label">故障报修单号</label><input class="input" disabled value="系统生成" /></div>
            <div class="mb-3"><label class="label req">故障类型</label>
              <select id="ftype" class="select"><option value="">请选择</option><option>运行故障</option><option>机械故障</option><option>电气故障</option><option>其他</option></select></div>
            <div class="mb-3"><label class="label req">严重等级</label>
              <select id="level" class="select"><option value="">请选择</option><option>一般</option><option selected>严重</option><option>紧急</option></select></div>
            <div class="mb-3"><label class="label req">故障发生时间</label>
              <input id="happen" class="input" type="datetime-local" value="2025-05-09T12:00" /></div>
            <div class="mb-3"><label class="label">故障描述</label>
              <textarea id="desc" class="input" rows="3" placeholder="请输入"></textarea></div>
            <div><label class="label">现场照片</label>
              <button type="button" class="upload w-full" onclick="toast('已上传现场照片（原型）')"><i class="fa-solid fa-camera mb-1"></i><br/>上传图片</button></div>
          </div>
          <div class="grid grid-cols-2 gap-3 pb-2">
            <a href="wecom_故障报修_列表.html" class="btn flex items-center justify-center border border-slate-200 bg-white py-3 text-sm text-slate-700" onclick="sessionStorage.removeItem('ems_wecom_selected_equip')">取消</a>
            <button type="button" class="btn bg-teal-700 py-3 text-sm text-white" onclick="submitForm()">确定</button>
          </div>
''',
    '''
    function fill(eq){
      if(!eq){equipEmpty.classList.remove('hidden');equipInfo.classList.add('hidden');return;}
      equipEmpty.classList.add('hidden');equipInfo.classList.remove('hidden');
      eqCode.textContent=eq.code||'-'; eqName.textContent=eq.name||'-'; eqSpec.textContent=eq.spec||'-'; eqLoc.textContent=eq.loc||'-';
    }
    function submitForm(){
      if(!eqCode.textContent||eqCode.textContent==='-'){toast('请先选择运营设备');return;}
      if(!ftype.value){toast('请选择故障类型');return;}
      if(!level.value){toast('请选择严重等级');return;}
      if(!happen.value){toast('请选择故障发生时间');return;}
      toast('已确定'); sessionStorage.removeItem('ems_wecom_selected_equip');
      setTimeout(()=>location.href='wecom_故障报修_列表.html',600);
    }
    try{fill(JSON.parse(sessionStorage.getItem('ems_wecom_selected_equip')||'null'));}catch(e){fill(null);}
'''
)

write(
    "wecom_故障报修_详情.html",
    "故障报修详情",
    '''<a href="wecom_故障报修_列表.html" class="text-slate-700"><i class="fa-solid fa-chevron-left"></i></a>
          <div class="text-sm font-semibold text-slate-900">故障报修详情</div>
          <span class="w-4"></span>''',
    '''
          <div class="card mb-3 p-4">
            <div class="sec-title"><h3>运营设备</h3></div>
            <div class="grid grid-cols-2 gap-2">
              <div class="cell"><div class="k">运营设备编号</div><div class="v">46546</div></div>
              <div class="cell"><div class="k">运营设备名称</div><div class="v">门机</div></div>
              <div class="cell"><div class="k">规格型号</div><div class="v">46546</div></div>
              <div class="cell"><div class="k">使用位置</div><div class="v">3号泊位</div></div>
            </div>
          </div>
          <div class="card mb-3 p-4">
            <div class="sec-title"><h3>报修信息</h3></div>
            <div class="row"><span class="k">故障报修单号</span><span class="v" id="no">55456541</span></div>
            <div class="row"><span class="k">故障状态</span><span class="v"><span class="rounded-full bg-amber-50 px-2 py-0.5 text-xs text-amber-700">待计划</span></span></div>
            <div class="row"><span class="k">故障类型</span><span class="v">运行故障</span></div>
            <div class="row"><span class="k">严重等级</span><span class="v">严重</span></div>
            <div class="row"><span class="k">故障发生时间</span><span class="v">2025-05-09 12:00</span></div>
            <div class="row"><span class="k">创建人</span><span class="v">张飞</span></div>
            <div class="row"><span class="k">创建时间</span><span class="v">2025-05-09 12:00</span></div>
          </div>
          <a href="wecom_维修计划_新增.html" class="btn flex items-center justify-center bg-teal-700 py-3 text-sm text-white" id="goPlan">去建维修计划</a>
''',
    '''
    const no=new URLSearchParams(location.search).get('no')||'55456541';
    document.getElementById('no').textContent=no;
    document.getElementById('goPlan').href='wecom_维修计划_新增.html?fault='+encodeURIComponent(no);
    sessionStorage.setItem('ems_wecom_selected_fault', JSON.stringify({
      no:no, code:'46546', name:'门机', spec:'46546', loc:'3号泊位', type:'运行故障', level:'严重', happen:'2025-05-09 12:00'
    }));
'''
)

# ========== 选取故障设备 ==========
write(
    "wecom_选取故障设备.html",
    "选取故障设备",
    '''<a id="backLink" href="wecom_维修计划_新增.html" class="text-slate-700"><i class="fa-solid fa-chevron-left"></i></a>
          <div class="text-sm font-semibold text-slate-900">故障设备</div>
          <span class="w-4"></span>''',
    '''
          <p class="mb-2 text-xs text-slate-500">数据为已上报故障设备，且尚未发起完工验收的数据</p>
          <div class="mb-3 flex gap-2">
            <input id="kw" class="input" placeholder="运营设备编号、名称 / 报修单号" />
            <button type="button" class="btn shrink-0 bg-teal-700 px-3 text-sm text-white" onclick="doSearch()">搜索</button>
          </div>
          <div id="list" class="space-y-2 pb-20"></div>
''',
    '''
    const from=new URLSearchParams(location.search).get('from')||'plan';
    const back=from==='finish'?'wecom_维修完工_新增.html':'wecom_维修计划_新增.html';
    backLink.href=back;
    const DATA=[
      {no:'55456541', code:'46546', name:'门机', spec:'46546', loc:'3号泊位', type:'运行故障', level:'严重', happen:'2025-05-09 12:00'},
      {no:'55456542', code:'46546', name:'门机', spec:'46546', loc:'3号泊位', type:'运行故障', level:'严重', happen:'2025-05-09 12:00'},
      {no:'55456543', code:'46547', name:'门机', spec:'46547', loc:'3号泊位', type:'电气故障', level:'一般', happen:'2025-05-09 12:00'}
    ];
    let selected=null, filtered=DATA.slice();
    function render(){
      list.innerHTML=filtered.map((d,i)=>{
        const on=selected&&selected.no===d.no;
        return '<div class="card equip-item p-3 '+(on?'selected':'')+'" onclick="pick('+i+')">'
          +'<div class="flex gap-3"><div class="radio mt-1"></div><div class="min-w-0 flex-1">'
          +'<div class="text-sm font-medium">'+d.no+' · '+d.name+'</div>'
          +'<div class="meta mt-1">'+d.code+' · '+d.spec+' · '+d.loc+'</div>'
          +'<div class="meta">'+d.type+' · '+d.level+' · '+d.happen+'</div>'
          +'</div></div></div>';
      }).join('')||'<p class="py-10 text-center text-sm text-slate-400">无匹配数据</p>';
    }
    function pick(i){selected=filtered[i];render();}
    function doSearch(){
      const q=(kw.value||'').trim().toLowerCase();
      filtered=DATA.filter(d=>!q||(d.no+d.code+d.name).toLowerCase().indexOf(q)>=0);
      if(selected&&!filtered.some(x=>x.no===selected.no)) selected=null;
      render();
    }
    function confirmPick(){
      if(!selected){toast('请先选择故障设备');return;}
      sessionStorage.setItem('ems_wecom_selected_fault', JSON.stringify(selected));
      toast('已选择：'+selected.no);
      setTimeout(()=>location.href=back,400);
    }
    kw.addEventListener('keydown',e=>{if(e.key==='Enter')doSearch();});
    render();
''',
    footer='''<div class="footer-bar">
          <div class="grid grid-cols-2 gap-3">
            <a id="cancelLink" href="wecom_维修计划_新增.html" class="btn flex items-center justify-center border border-slate-200 bg-white py-3 text-sm text-slate-700">取消</a>
            <button type="button" class="btn bg-teal-700 py-3 text-sm text-white" onclick="confirmPick()">确定</button>
          </div>
        </div>
        <script>document.getElementById('cancelLink').href=document.getElementById('backLink').href;</script>'''
)

# Fix footer for 选取故障设备 - the inline script in footer is messy. Let me fix in a cleaner way after.
# Actually I'll patch the cancel link in the main script instead.

# ========== 维修计划 ==========
write(
    "wecom_维修计划_列表.html",
    "维修计划",
    '''<a href="wecom_入口.html" class="text-slate-700"><i class="fa-solid fa-chevron-left"></i></a>
          <div class="text-sm font-semibold text-slate-900">维修计划</div>
          <a href="wecom_维修计划_新增.html" class="text-sm text-teal-700">新增</a>''',
    '''
          <div id="chips" class="mb-3 flex gap-2 overflow-x-auto pb-1">
            <button type="button" class="chip active">全部</button>
            <button type="button" class="chip">草稿</button>
            <button type="button" class="chip">审核中</button>
            <button type="button" class="chip">已通过</button>
          </div>
          <div class="space-y-3" id="list"></div>
''',
    '''
    const DATA=[
      {no:'WJ-55456541', code:'465465', name:'门机', spec:'465465', loc:'3号泊位', time:'2025-08-09 12:00 至 2025-08-09 12:00', persons:'张飞、张倩', fault:'465465', type:'运行故障', level:'严重', happen:'2025-05-09 12:00', biz:'已通过'},
      {no:'WJ-55456542', code:'465465', name:'门机', spec:'465465', loc:'3号泊位', time:'2025-08-09 12:00 至 2025-08-09 12:00', persons:'张飞、张倩', fault:'465465', type:'运行故障', level:'严重', happen:'2025-05-09 12:00', biz:'草稿'},
      {no:'WJ-55456543', code:'465465', name:'门机', spec:'465465', loc:'3号泊位', time:'2025-08-10 09:00 至 2025-08-10 17:00', persons:'张飞、张倩', fault:'465465', type:'运行故障', level:'严重', happen:'2025-05-09 12:00', biz:'审核中'}
    ];
    function chip(s){return s==='已通过'?'bg-emerald-50 text-emerald-700':s==='审核中'?'bg-amber-50 text-amber-700':'bg-slate-100 text-slate-600';}
    function render(rows){
      list.innerHTML=rows.map(d=>'<div class="card p-4">'
        +'<a href="wecom_维修计划_详情.html?no='+encodeURIComponent(d.no)+'" class="block">'
        +'<div class="flex items-start justify-between gap-2"><div class="min-w-0">'
        +'<div class="text-sm font-medium text-slate-900">'+d.no+' · '+d.name+'</div>'
        +'<div class="meta mt-1">'+d.code+' · '+d.loc+' · '+d.type+'/'+d.level+'</div>'
        +'<div class="meta mt-0.5">计划时间 '+d.time+'</div>'
        +'<div class="meta">计划维修人员 '+d.persons+' · 故障单 '+d.fault+'</div>'
        +'</div><span class="shrink-0 rounded-full px-2 py-0.5 text-xs '+chip(d.biz)+'">'+d.biz+'</span></div></a>'
        +(d.biz==='草稿'?'<div class="mt-3 flex flex-wrap gap-3 text-xs text-teal-700"><a href="wecom_维修计划_新增.html">编辑</a><button type="button" onclick="toast(\\'已提交，进入平台审批\\')">提交</button><button type="button" onclick="toast(\\'已删除（原型）\\')">删除</button></div>':'')
        +'</div>').join('');
    }
    let st='全部';
    function apply(){render(DATA.filter(d=>st==='全部'||d.biz===st));}
    chips.querySelectorAll('.chip').forEach(btn=>btn.addEventListener('click',()=>{
      chips.querySelectorAll('.chip').forEach(c=>c.classList.remove('active'));btn.classList.add('active');st=btn.textContent.trim();apply();
    }));
    apply();
'''
)

write(
    "wecom_维修计划_新增.html",
    "维修计划",
    '''<a href="wecom_维修计划_列表.html" class="text-slate-700"><i class="fa-solid fa-chevron-left"></i></a>
          <div class="text-sm font-semibold text-slate-900">维修计划</div>
          <span class="w-4"></span>''',
    '''
          <div class="card mb-3 p-4">
            <div class="sec-title">
              <h3>故障设备</h3>
              <a href="wecom_选取故障设备.html?from=plan" class="text-xs font-medium text-teal-700">选取故障设备</a>
            </div>
            <div id="faultEmpty" class="rounded-xl border border-dashed border-slate-200 bg-slate-50 px-3 py-4 text-center text-xs text-slate-400">请选取已上报且未完工验收的故障设备</div>
            <div id="faultInfo" class="hidden">
              <div class="row"><span class="k">故障报修单号</span><span class="v" id="fNo">-</span></div>
              <div class="grid grid-cols-2 gap-2 mt-2">
                <div class="cell"><div class="k">运营设备编号</div><div class="v" id="eqCode">-</div></div>
                <div class="cell"><div class="k">运营设备名称</div><div class="v" id="eqName">-</div></div>
                <div class="cell"><div class="k">规格型号</div><div class="v" id="eqSpec">-</div></div>
                <div class="cell"><div class="k">使用位置</div><div class="v" id="eqLoc">-</div></div>
              </div>
              <div class="row mt-2"><span class="k">故障类型</span><span class="v" id="fType">-</span></div>
              <div class="row"><span class="k">严重等级</span><span class="v" id="fLevel">-</span></div>
              <div class="row"><span class="k">故障发生时间</span><span class="v" id="fHappen">-</span></div>
            </div>
          </div>
          <div class="card mb-3 p-4">
            <div class="sec-title"><h3>维修计划</h3></div>
            <div class="mb-3"><label class="label">维修计划单号</label><input class="input" disabled value="系统生成" /></div>
            <div class="mb-3"><label class="label req">维修计划时间</label>
              <div class="space-y-2">
                <input id="tStart" class="input" type="datetime-local" value="2025-08-09T12:00" />
                <input id="tEnd" class="input" type="datetime-local" value="2025-08-09T17:00" />
              </div>
              <p class="mt-1 text-xs text-slate-400">请选择时间范围（起止均含日期）</p>
            </div>
            <div class="mb-3"><label class="label req">计划维修人员</label>
              <select id="persons" class="select"><option value="">请选择</option><option>张飞、张倩</option><option>王工</option><option>李工、陈工</option></select></div>
            <div><label class="label">相关说明</label><textarea id="remark" class="input" rows="3" placeholder="请输入"></textarea></div>
          </div>
          <div class="grid grid-cols-2 gap-3 pb-2">
            <a href="wecom_维修计划_列表.html" class="btn flex items-center justify-center border border-slate-200 bg-white py-3 text-sm text-slate-700">取消</a>
            <button type="button" class="btn bg-teal-700 py-3 text-sm text-white" onclick="submitForm()">确定</button>
          </div>
''',
    '''
    function fill(f){
      if(!f){faultEmpty.classList.remove('hidden');faultInfo.classList.add('hidden');return;}
      faultEmpty.classList.add('hidden');faultInfo.classList.remove('hidden');
      fNo.textContent=f.no||'-'; eqCode.textContent=f.code||'-'; eqName.textContent=f.name||'-';
      eqSpec.textContent=f.spec||'-'; eqLoc.textContent=f.loc||'-';
      fType.textContent=f.type||'-'; fLevel.textContent=f.level||'-'; fHappen.textContent=f.happen||'-';
    }
    function submitForm(){
      if(!fNo.textContent||fNo.textContent==='-'){toast('请选取故障设备');return;}
      if(!tStart.value||!tEnd.value){toast('请选择维修计划时间');return;}
      if(tStart.value>=tEnd.value){toast('结束时间须晚于开始时间');return;}
      if(!persons.value){toast('请选择计划维修人员');return;}
      toast('已确定（进入平台审批）');
      sessionStorage.removeItem('ems_wecom_selected_fault');
      setTimeout(()=>location.href='wecom_维修计划_列表.html',600);
    }
    // 支持从报修详情带入
    const faultQ=new URLSearchParams(location.search).get('fault');
    try{
      let f=JSON.parse(sessionStorage.getItem('ems_wecom_selected_fault')||'null');
      if(!f && faultQ){ f={no:faultQ,code:'46546',name:'门机',spec:'46546',loc:'3号泊位',type:'运行故障',level:'严重',happen:'2025-05-09 12:00'}; sessionStorage.setItem('ems_wecom_selected_fault',JSON.stringify(f)); }
      fill(f);
    }catch(e){fill(null);}
'''
)

write(
    "wecom_维修计划_详情.html",
    "维修计划详情",
    '''<a href="wecom_维修计划_列表.html" class="text-slate-700"><i class="fa-solid fa-chevron-left"></i></a>
          <div class="text-sm font-semibold text-slate-900">维修计划详情</div>
          <span class="w-4"></span>''',
    '''
          <div class="card mb-3 p-4">
            <div class="sec-title"><h3>运营设备</h3></div>
            <div class="grid grid-cols-2 gap-2">
              <div class="cell"><div class="k">运营设备编号</div><div class="v">465465</div></div>
              <div class="cell"><div class="k">运营设备名称</div><div class="v">门机</div></div>
              <div class="cell"><div class="k">规格型号</div><div class="v">465465</div></div>
              <div class="cell"><div class="k">使用位置</div><div class="v">3号泊位</div></div>
            </div>
          </div>
          <div class="card mb-3 p-4">
            <div class="sec-title"><h3>故障信息</h3></div>
            <div class="row"><span class="k">故障报修单号</span><span class="v">465465</span></div>
            <div class="row"><span class="k">故障类型</span><span class="v">运行故障</span></div>
            <div class="row"><span class="k">严重等级</span><span class="v">严重</span></div>
            <div class="row"><span class="k">故障发生时间</span><span class="v">2025-05-09 12:00</span></div>
          </div>
          <div class="card mb-3 p-4">
            <div class="sec-title"><h3>维修计划</h3></div>
            <div class="row"><span class="k">维修计划单号</span><span class="v" id="pNo">WJ-55456541</span></div>
            <div class="row"><span class="k">维修计划时间</span><span class="v text-xs">2025-08-09 12:00 至 2025-08-09 12:00</span></div>
            <div class="row"><span class="k">计划维修人员</span><span class="v">张飞、张倩</span></div>
            <div class="row"><span class="k">业务状态</span><span class="v"><span class="rounded-full bg-emerald-50 px-2 py-0.5 text-xs text-emerald-700">已通过</span></span></div>
          </div>
          <a href="wecom_维修派工_新增.html" class="btn flex items-center justify-center bg-teal-700 py-3 text-sm text-white">去建维修派工</a>
''',
    '''
    const no=new URLSearchParams(location.search).get('no')||'WJ-55456541';
    pNo.textContent=no;
    sessionStorage.setItem('ems_wecom_selected_repair_plan', JSON.stringify({
      no:no, name:'门机维修计划', code:'465465', equip:'门机', spec:'465465', loc:'3号泊位',
      time:'2025-08-09 12:00 至 2025-08-09 12:00', persons:'张飞、张倩',
      fault:'465465', type:'运行故障', level:'严重', happen:'2025-05-09 12:00'
    }));
'''
)

# ========== 选取维修计划 ==========
write(
    "wecom_选取维修计划.html",
    "选取维修计划",
    '''<a href="wecom_维修派工_新增.html" class="text-slate-700"><i class="fa-solid fa-chevron-left"></i></a>
          <div class="text-sm font-semibold text-slate-900">维修计划</div>
          <span class="w-4"></span>''',
    '''
          <div class="mb-3 flex gap-2">
            <input id="kw" class="input" placeholder="计划单号 / 设备编号 / 名称" />
            <button type="button" class="btn shrink-0 bg-teal-700 px-3 text-sm text-white" onclick="doSearch()">搜索</button>
          </div>
          <div id="list" class="space-y-2 pb-20"></div>
''',
    '''
    const DATA=[
      {no:'WJ-55456541', name:'门机维修计划', code:'465465', equip:'门机', spec:'465465', loc:'3号泊位', time:'2025-08-09 12:00 至 2025-08-09 12:00', persons:'张飞、张倩', fault:'465465', type:'运行故障', level:'严重', happen:'2025-05-09 12:00'},
      {no:'WJ-55456542', name:'门机维修计划', code:'465465', equip:'门机', spec:'465465', loc:'3号泊位', time:'2025-08-10 09:00 至 2025-08-10 17:00', persons:'张飞、张倩', fault:'465465', type:'运行故障', level:'严重', happen:'2025-05-09 12:00'}
    ];
    let selected=null, filtered=DATA.slice();
    function render(){
      list.innerHTML=filtered.map((d,i)=>{
        const on=selected&&selected.no===d.no;
        return '<div class="card equip-item p-3 '+(on?'selected':'')+'" onclick="pick('+i+')">'
          +'<div class="flex gap-3"><div class="radio mt-1"></div><div class="min-w-0 flex-1">'
          +'<div class="text-sm font-medium">'+d.no+' · '+d.equip+'</div>'
          +'<div class="meta mt-1">计划时间 '+d.time+'</div>'
          +'<div class="meta">计划人员 '+d.persons+' · 故障单 '+d.fault+'</div>'
          +'</div></div></div>';
      }).join('');
    }
    function pick(i){selected=filtered[i];render();}
    function doSearch(){
      const q=(kw.value||'').trim().toLowerCase();
      filtered=DATA.filter(d=>!q||(d.no+d.code+d.equip).toLowerCase().indexOf(q)>=0);
      render();
    }
    function confirmPick(){
      if(!selected){toast('请先选择维修计划');return;}
      sessionStorage.setItem('ems_wecom_selected_repair_plan', JSON.stringify(selected));
      toast('已选择：'+selected.no);
      setTimeout(()=>location.href='wecom_维修派工_新增.html',400);
    }
    render();
''',
    footer='''<div class="footer-bar">
          <div class="grid grid-cols-2 gap-3">
            <a href="wecom_维修派工_新增.html" class="btn flex items-center justify-center border border-slate-200 bg-white py-3 text-sm text-slate-700">取消</a>
            <button type="button" class="btn bg-teal-700 py-3 text-sm text-white" onclick="confirmPick()">确定</button>
          </div>
        </div>'''
)

# ========== 维修派工 ==========
write(
    "wecom_维修派工_列表.html",
    "维修派工",
    '''<a href="wecom_入口.html" class="text-slate-700"><i class="fa-solid fa-chevron-left"></i></a>
          <div class="text-sm font-semibold text-slate-900">维修派工</div>
          <a href="wecom_维修派工_新增.html" class="text-sm text-teal-700">新增</a>''',
    '''
          <div class="mb-3 flex gap-2">
            <input id="kw" class="input" placeholder="派工单号 / 计划单号 / 设备" />
            <button type="button" class="btn shrink-0 bg-teal-700 px-3 text-sm text-white" onclick="doSearch()">查询</button>
          </div>
          <div id="list" class="space-y-3"></div>
''',
    '''
    const DATA=[
      {no:'WP-55456541', time:'2025-08-09 12:00 至 2025-08-09 12:00', person:'张飞', plan:'55456541', code:'465465', name:'门机', spec:'465465', loc:'3号泊位', ptime:'2025-08-09 12:00 至 2025-08-09 12:00', ppersons:'张飞、张倩', fault:'465465', type:'运行故障', level:'严重', happen:'2025-05-09 12:00'},
      {no:'WP-55456542', time:'2025-08-09 12:00 至 2025-08-09 12:00', person:'张飞', plan:'55456542', code:'465465', name:'门机', spec:'465465', loc:'3号泊位', ptime:'2025-08-09 12:00 至 2025-08-09 12:00', ppersons:'张飞、张倩', fault:'465465', type:'运行故障', level:'严重', happen:'2025-05-09 12:00'}
    ];
    let filtered=DATA.slice();
    function render(){
      list.innerHTML=filtered.map(d=>'<div class="card p-4">'
        +'<div class="text-sm font-medium text-slate-900">'+d.no+' · '+d.name+'</div>'
        +'<div class="meta mt-1">维修时间 '+d.time+'</div>'
        +'<div class="meta">维修人员 '+d.person+' · 计划单 '+d.plan+'</div>'
        +'<div class="meta">'+d.code+' · '+d.loc+' · '+d.type+'/'+d.level+'</div>'
        +'<div class="mt-3 flex flex-wrap gap-3 text-xs text-teal-700"><button type="button" onclick="toast(\\'详情（原型）\\')">查看</button><button type="button" onclick="toast(\\'已删除（原型）\\')">删除</button></div>'
        +'</div>').join('')||'<p class="py-10 text-center text-sm text-slate-400">无数据</p>';
    }
    function doSearch(){
      const q=(kw.value||'').trim().toLowerCase();
      filtered=DATA.filter(d=>!q||(d.no+d.plan+d.name+d.code).toLowerCase().indexOf(q)>=0);
      render(); toast('已查询，共 '+filtered.length+' 条');
    }
    render();
'''
)

write(
    "wecom_维修派工_新增.html",
    "维修派工",
    '''<a href="wecom_维修派工_列表.html" class="text-slate-700"><i class="fa-solid fa-chevron-left"></i></a>
          <div class="text-sm font-semibold text-slate-900">维修派工</div>
          <span class="w-4"></span>''',
    '''
          <div class="card mb-3 p-4">
            <div class="sec-title">
              <h3>维修计划</h3>
              <a href="wecom_选取维修计划.html" class="text-xs font-medium text-teal-700">选取维修计划</a>
            </div>
            <div id="planEmpty" class="rounded-xl border border-dashed border-slate-200 bg-slate-50 px-3 py-4 text-center text-xs text-slate-400">请选取维修计划</div>
            <div id="planInfo" class="hidden">
              <div class="row"><span class="k">维修计划单号</span><span class="v" id="pNo">-</span></div>
              <div class="row"><span class="k">维修计划时间</span><span class="v text-xs" id="pTime">-</span></div>
              <div class="row"><span class="k">计划维修人员</span><span class="v" id="pPersons">-</span></div>
              <div class="grid grid-cols-2 gap-2 mt-2">
                <div class="cell"><div class="k">运营设备编号</div><div class="v" id="eqCode">-</div></div>
                <div class="cell"><div class="k">运营设备名称</div><div class="v" id="eqName">-</div></div>
                <div class="cell"><div class="k">规格型号</div><div class="v" id="eqSpec">-</div></div>
                <div class="cell"><div class="k">使用位置</div><div class="v" id="eqLoc">-</div></div>
              </div>
              <div class="row mt-2"><span class="k">故障单号</span><span class="v" id="fNo">-</span></div>
              <div class="row"><span class="k">故障类型 / 等级</span><span class="v" id="fTL">-</span></div>
              <div class="row"><span class="k">故障发生时间</span><span class="v" id="fHappen">-</span></div>
            </div>
          </div>
          <div class="card mb-3 p-4">
            <div class="sec-title"><h3>派工信息</h3></div>
            <div class="mb-3"><label class="label">维修派工单号</label><input class="input" disabled value="系统生成" /></div>
            <div class="mb-3"><label class="label req">维修时间</label>
              <div class="space-y-2">
                <input id="tStart" class="input" type="datetime-local" value="2025-08-09T12:00" />
                <input id="tEnd" class="input" type="datetime-local" value="2025-08-09T17:00" />
              </div>
              <p class="mt-1 text-xs text-slate-400">请选择时间范围（起止均含日期）</p>
            </div>
            <div class="mb-3"><label class="label req">维修人员</label>
              <select id="person" class="select"><option value="">请选择</option><option>张飞</option><option>张倩</option><option>王工</option><option>李工</option></select></div>
            <div><label class="label">作业说明</label><textarea class="input" rows="3" placeholder="请输入"></textarea></div>
          </div>
          <div class="grid grid-cols-2 gap-3 pb-2">
            <a href="wecom_维修派工_列表.html" class="btn flex items-center justify-center border border-slate-200 bg-white py-3 text-sm text-slate-700">取消</a>
            <button type="button" class="btn bg-teal-700 py-3 text-sm text-white" onclick="submitForm()">确定</button>
          </div>
''',
    '''
    function fill(p){
      if(!p){planEmpty.classList.remove('hidden');planInfo.classList.add('hidden');return;}
      planEmpty.classList.add('hidden');planInfo.classList.remove('hidden');
      pNo.textContent=p.no||'-'; pTime.textContent=p.time||'-'; pPersons.textContent=p.persons||'-';
      eqCode.textContent=p.code||'-'; eqName.textContent=p.equip||p.name||'-';
      eqSpec.textContent=p.spec||'-'; eqLoc.textContent=p.loc||'-';
      fNo.textContent=p.fault||'-'; fTL.textContent=(p.type||'-')+' / '+(p.level||'-'); fHappen.textContent=p.happen||'-';
    }
    function submitForm(){
      if(!pNo.textContent||pNo.textContent==='-'){toast('请选取维修计划');return;}
      if(!tStart.value||!tEnd.value){toast('请选择维修时间');return;}
      if(tStart.value>=tEnd.value){toast('结束时间须晚于开始时间');return;}
      if(!person.value){toast('请选择维修人员');return;}
      toast('已确定'); sessionStorage.removeItem('ems_wecom_selected_repair_plan');
      setTimeout(()=>location.href='wecom_维修派工_列表.html',600);
    }
    try{fill(JSON.parse(sessionStorage.getItem('ems_wecom_selected_repair_plan')||'null'));}catch(e){fill(null);}
'''
)

# ========== 维修完工 ==========
write(
    "wecom_维修完工_列表.html",
    "维修完工",
    '''<a href="wecom_入口.html" class="text-slate-700"><i class="fa-solid fa-chevron-left"></i></a>
          <div class="text-sm font-semibold text-slate-900">维修完工</div>
          <a href="wecom_维修完工_新增.html" class="text-sm text-teal-700">新增</a>''',
    '''
          <div id="chips" class="mb-3 flex gap-2 overflow-x-auto pb-1">
            <button type="button" class="chip active">全部</button>
            <button type="button" class="chip">草稿</button>
            <button type="button" class="chip">审核中</button>
            <button type="button" class="chip">已通过</button>
          </div>
          <div id="list" class="space-y-3"></div>
''',
    '''
    const DATA=[
      {no:'WG-55456541', accept:'2025-08-09 12:00', code:'465465', name:'门机', fault:'465465', type:'运行故障', level:'严重', happen:'2025-05-09 12:00', spec:'46556', biz:'已通过', creator:'张飞'},
      {no:'WG-55456542', accept:'2025-08-09 12:00', code:'465465', name:'门机', fault:'465465', type:'运行故障', level:'严重', happen:'2025-05-09 12:00', spec:'46556', biz:'草稿', creator:'张飞'},
      {no:'WG-55456543', accept:'2025-08-09 12:00', code:'465465', name:'门机', fault:'465465', type:'运行故障', level:'严重', happen:'2025-05-09 12:00', spec:'46556', biz:'审核中', creator:'张飞'}
    ];
    function chip(s){return s==='已通过'?'bg-emerald-50 text-emerald-700':s==='审核中'?'bg-amber-50 text-amber-700':'bg-slate-100 text-slate-600';}
    function render(rows){
      list.innerHTML=rows.map(d=>'<div class="card p-4">'
        +'<a href="wecom_维修完工_详情.html?no='+encodeURIComponent(d.no)+'" class="block">'
        +'<div class="flex items-start justify-between gap-2"><div class="min-w-0">'
        +'<div class="text-sm font-medium text-slate-900">'+d.no+' · '+d.name+'</div>'
        +'<div class="meta mt-1">完工验收日期 '+d.accept+'</div>'
        +'<div class="meta">设备 '+d.code+' · 故障单 '+d.fault+' · '+d.type+'/'+d.level+'</div>'
        +'<div class="meta">故障发生 '+d.happen+' · 规格 '+d.spec+'</div>'
        +'</div><span class="shrink-0 rounded-full px-2 py-0.5 text-xs '+chip(d.biz)+'">'+d.biz+'</span></div></a>'
        +(d.biz==='草稿'?'<div class="mt-3 flex flex-wrap gap-3 text-xs text-teal-700"><a href="wecom_维修完工_新增.html">编辑</a><button type="button" onclick="toast(\\'已提交，进入平台审批\\')">提交</button><button type="button" onclick="toast(\\'已删除（原型）\\')">删除</button></div>':'')
        +'</div>').join('');
    }
    let st='全部';
    function apply(){render(DATA.filter(d=>st==='全部'||d.biz===st));}
    chips.querySelectorAll('.chip').forEach(btn=>btn.addEventListener('click',()=>{
      chips.querySelectorAll('.chip').forEach(c=>c.classList.remove('active'));btn.classList.add('active');st=btn.textContent.trim();apply();
    }));
    apply();
'''
)

write(
    "wecom_维修完工_新增.html",
    "维修完工",
    '''<a href="wecom_维修完工_列表.html" class="text-slate-700"><i class="fa-solid fa-chevron-left"></i></a>
          <div class="text-sm font-semibold text-slate-900">维修完工</div>
          <span class="w-4"></span>''',
    '''
          <div class="card mb-3 p-4">
            <div class="sec-title">
              <h3>故障设备</h3>
              <a href="wecom_选取故障设备.html?from=finish" class="text-xs font-medium text-teal-700">选取故障设备</a>
            </div>
            <div id="faultEmpty" class="rounded-xl border border-dashed border-slate-200 bg-slate-50 px-3 py-4 text-center text-xs text-slate-400">请选取尚未发起完工验收的故障设备</div>
            <div id="faultInfo" class="hidden">
              <div class="row"><span class="k">故障单号</span><span class="v" id="fNo">-</span></div>
              <div class="grid grid-cols-2 gap-2 mt-2">
                <div class="cell"><div class="k">设备编号</div><div class="v" id="eqCode">-</div></div>
                <div class="cell"><div class="k">设备名称</div><div class="v" id="eqName">-</div></div>
                <div class="cell"><div class="k">设备规格</div><div class="v" id="eqSpec">-</div></div>
                <div class="cell"><div class="k">使用位置</div><div class="v" id="eqLoc">-</div></div>
              </div>
              <div class="row mt-2"><span class="k">故障类型</span><span class="v" id="fType">-</span></div>
              <div class="row"><span class="k">严重等级</span><span class="v" id="fLevel">-</span></div>
              <div class="row"><span class="k">故障发生时间</span><span class="v" id="fHappen">-</span></div>
            </div>
          </div>
          <div class="card mb-3 p-4">
            <div class="sec-title"><h3>关联计划 / 派工（回显）</h3></div>
            <div class="row"><span class="k">维修计划</span><span class="v text-xs">WJ-55456541 · 2025-08-09 12:00 至 2025-08-09 12:00</span></div>
            <div class="row"><span class="k">维修派工</span><span class="v text-xs">WP-55456541 · 张飞</span></div>
          </div>
          <div class="card mb-3 p-4">
            <div class="sec-title"><h3>完工验收</h3></div>
            <div class="mb-3"><label class="label">维修完工单号</label><input class="input" disabled value="系统生成" /></div>
            <div class="mb-3"><label class="label req">完工验收日期</label>
              <input id="accept" class="input" type="datetime-local" value="2025-08-09T12:00" /></div>
            <div class="mb-3"><label class="label req">验收结论</label>
              <select id="result" class="select"><option value="">请选择</option><option>合格</option><option>带病运行观察</option><option>不合格</option></select></div>
            <div class="mb-3"><label class="label req">验收人员</label>
              <select id="acceptor" class="select"><option value="">请选择</option><option>张飞</option><option>王工</option><option>赵工</option></select></div>
            <div class="mb-3"><label class="label">验收概述</label>
              <textarea id="summary" class="input" rows="3" placeholder="请输入"></textarea></div>
            <div class="mb-3"><label class="label">记录表</label>
              <button type="button" class="upload w-full" onclick="toast('已上传（原型）')"><i class="fa-solid fa-cloud-arrow-up mb-1"></i><br/>上传文件</button></div>
            <div><label class="label">现场照片</label>
              <button type="button" class="upload w-full" onclick="toast('已上传（原型）')"><i class="fa-solid fa-camera mb-1"></i><br/>上传图片</button></div>
          </div>
          <div class="grid grid-cols-2 gap-3 pb-2">
            <a href="wecom_维修完工_列表.html" class="btn flex items-center justify-center border border-slate-200 bg-white py-3 text-sm text-slate-700">取消</a>
            <button type="button" class="btn bg-teal-700 py-3 text-sm text-white" onclick="submitForm()">确定</button>
          </div>
''',
    '''
    function fill(f){
      if(!f){faultEmpty.classList.remove('hidden');faultInfo.classList.add('hidden');return;}
      faultEmpty.classList.add('hidden');faultInfo.classList.remove('hidden');
      fNo.textContent=f.no||'-'; eqCode.textContent=f.code||'-'; eqName.textContent=f.name||'-';
      eqSpec.textContent=f.spec||'-'; eqLoc.textContent=f.loc||'-';
      fType.textContent=f.type||'-'; fLevel.textContent=f.level||'-'; fHappen.textContent=f.happen||'-';
    }
    function submitForm(){
      if(!fNo.textContent||fNo.textContent==='-'){toast('请选取故障设备');return;}
      if(!accept.value){toast('请选择完工验收日期');return;}
      if(!result.value){toast('请选择验收结论');return;}
      if(!acceptor.value){toast('请选择验收人员');return;}
      toast('已确定（进入平台审批）');
      sessionStorage.removeItem('ems_wecom_selected_fault');
      setTimeout(()=>location.href='wecom_维修完工_列表.html',600);
    }
    try{fill(JSON.parse(sessionStorage.getItem('ems_wecom_selected_fault')||'null'));}catch(e){fill(null);}
'''
)

write(
    "wecom_维修完工_详情.html",
    "维修完工详情",
    '''<a href="wecom_维修完工_列表.html" class="text-slate-700"><i class="fa-solid fa-chevron-left"></i></a>
          <div class="text-sm font-semibold text-slate-900">维修完工详情</div>
          <span class="w-4"></span>''',
    '''
          <div class="card mb-3 p-4">
            <div class="sec-title"><h3>设备 / 故障</h3></div>
            <div class="row"><span class="k">设备编号</span><span class="v">465465</span></div>
            <div class="row"><span class="k">设备名称</span><span class="v">门机</span></div>
            <div class="row"><span class="k">设备规格</span><span class="v">46556</span></div>
            <div class="row"><span class="k">故障单号</span><span class="v">465465</span></div>
            <div class="row"><span class="k">故障类型</span><span class="v">运行故障</span></div>
            <div class="row"><span class="k">严重等级</span><span class="v">严重</span></div>
            <div class="row"><span class="k">故障发生时间</span><span class="v">2025-05-09 12:00</span></div>
          </div>
          <div class="card mb-3 p-4">
            <div class="sec-title"><h3>完工验收</h3></div>
            <div class="row"><span class="k">维修完工单号</span><span class="v" id="no">WG-55456541</span></div>
            <div class="row"><span class="k">完工验收日期</span><span class="v">2025-08-09 12:00</span></div>
            <div class="row"><span class="k">验收结论</span><span class="v">合格</span></div>
            <div class="row"><span class="k">验收人员</span><span class="v">张飞</span></div>
            <div class="row"><span class="k">业务状态</span><span class="v"><span class="rounded-full bg-emerald-50 px-2 py-0.5 text-xs text-emerald-700">已通过</span></span></div>
          </div>
''',
    '''
    no.textContent=new URLSearchParams(location.search).get('no')||'WG-55456541';
'''
)

print("done")
