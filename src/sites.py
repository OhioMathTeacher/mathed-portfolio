import html
E=html.escape
import os
HOME=os.environ.get("PORTFOLIO_HOME","../index.html")
OUT_DIR=os.environ.get("PORTFOLIO_OUT",os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","docs","samples"))

CSS="""
  :root{--bg:%(bg)s; --bg2:%(bg2)s; --ink:%(ink)s; --ink2:#5F6368; --ink3:#80868B; --line:%(line)s; --accent:%(accent)s; --accent-ink:#FFFFFF; --accent-soft:%(accent_soft)s; --embed:%(bg2)s; --link:%(link)s; --yellow:#FEF7E0; --r:%(radius)s; --head:%(head_font)s; --body:%(body_font)s}
  @media (prefers-color-scheme: dark){ :root:not([data-theme="light"]){--bg:#1C1D20; --bg2:#26282C; --ink:#E8EAED; --ink2:#BDC1C6; --ink3:#9AA0A6; --line:#3C4043; --accent:%(accent_dark)s; --accent-ink:#1C1D20; --accent-soft:%(accent_soft_dark)s; --embed:#2E3034; --link:#8AB4F8; --yellow:#3A3320} }
  :root[data-theme="dark"]{--bg:#1C1D20; --bg2:#26282C; --ink:#E8EAED; --ink2:#BDC1C6; --ink3:#9AA0A6; --line:#3C4043; --accent:%(accent_dark)s; --accent-ink:#1C1D20; --accent-soft:%(accent_soft_dark)s; --embed:#2E3034; --link:#8AB4F8; --yellow:#3A3320}
  *{box-sizing:border-box}
  body{margin:0; background:var(--bg); color:var(--ink); font-family:var(--body); font-size:16px; line-height:1.6}
  h1,h2,h3,.gbar .site,.banner h1{font-family:var(--head)}
  a{color:var(--link)} p{margin:0 0 12px} ul{margin:0 0 12px; padding-left:22px} li{margin-bottom:4px}
  h1,h2,h3,h4{font-weight:500; margin:0; line-height:1.25} h2{font-size:28px; margin-bottom:6px} h3{font-size:20px; margin:26px 0 8px} h4{font-size:15px; color:var(--ink2); text-transform:uppercase; letter-spacing:.06em; margin:18px 0 6px}
  .sample{background:var(--yellow); color:var(--ink); font-size:13px; padding:8px 20px; text-align:center; border-bottom:1px solid var(--line)}
  .sample a{color:inherit}
  .gbar{display:flex; align-items:center; justify-content:space-between; gap:16px; padding:12px 24px; border-bottom:1px solid var(--line); background:var(--bg); position:sticky; top:0; z-index:5; flex-wrap:wrap}
  .gbar .site{font-size:20px; font-weight:500}
  .gbar nav{display:flex; gap:4px; flex-wrap:wrap}
  .gbar nav a{color:var(--ink2); text-decoration:none; padding:8px 12px; border-radius:calc(var(--r)/2); font-size:14px; font-weight:500}
  .gbar nav a:hover{background:var(--bg2)} .gbar nav a.on{color:var(--accent); box-shadow:inset 0 -2px 0 var(--accent); border-radius:0}
  %(nav_css)s
  .banner{background:var(--accent); color:#fff; padding:56px 24px; text-align:center; %(banner_css)s}
  .banner h1{font-size:40px; font-weight:400} .banner p{font-size:17px; opacity:.9; margin:8px 0 0}
  %(extra_css)s
  main{max-width:860px; margin:0 auto; padding:36px 24px 80px}
  .page{display:none} .page.on{display:block}
  .sub{display:flex; gap:8px; flex-wrap:wrap; margin:4px 0 24px; padding-bottom:16px; border-bottom:1px solid var(--line)}
  .sub a{font-size:13px; padding:5px 12px; border:1px solid var(--line); border-radius:16px; text-decoration:none; color:var(--ink2)} .sub a.on{background:var(--accent-soft); color:var(--accent); border-color:transparent; font-weight:600}
  .lead{color:var(--ink2); font-size:17px; margin-bottom:20px}
  .embed{background:var(--embed); border:1px solid var(--line); border-radius:var(--r); padding:16px 18px; display:flex; gap:14px; align-items:center; margin:12px 0 18px}
  .embed .ico{width:40px; height:48px; border-radius:calc(var(--r)/2); background:var(--bg); border:1px solid var(--line); display:grid; place-items:center; font-size:11px; font-weight:700; color:var(--accent); flex:none}
  .embed .nm{font-weight:500} .embed .meta{font-size:13px; color:var(--ink3)}
  .video{background:#111; color:#ddd; border-radius:var(--r); aspect-ratio:16/9; display:grid; place-items:center; margin:12px 0 18px; font-size:14px; position:relative}
  .video::before{content:"▶"; font-size:44px; color:#fff; opacity:.85; position:absolute}
  .video span{position:absolute; bottom:12px; left:14px; font-size:12px; opacity:.8}
  .card{border:1px solid var(--line); border-radius:var(--r); padding:18px 20px; margin:12px 0}
  .two{display:grid; grid-template-columns:1fr 1fr; gap:16px} @media(max-width:700px){.two{grid-template-columns:1fr}}
  .v{border:1px solid var(--line); border-radius:var(--r); padding:16px 18px; background:var(--bg2)} .v h4{margin-top:0}
  .cm{display:grid; grid-template-columns:36px 1fr; gap:12px; padding:12px 0; border-top:1px solid var(--line)}
  .cm .av{width:36px; height:36px; border-radius:50%; display:grid; place-items:center; font-size:13px; font-weight:600; color:#fff; background:var(--ink3)}
  .cm.me .av{background:var(--accent); color:var(--accent-ink)} .cm .who{font-size:13px; color:var(--ink2); margin-bottom:2px} .cm .who b{color:var(--ink); font-weight:500} .cm p{margin:0}
  .cm.me{padding-left:24px}
  .tag{display:inline-block; font-size:11px; font-weight:600; letter-spacing:.05em; text-transform:uppercase; padding:2px 8px; border-radius:10px; background:var(--accent-soft); color:var(--accent); margin-left:8px; vertical-align:middle}
  .mile{background:var(--bg2); border-left:4px solid var(--accent); padding:12px 16px; border-radius:0 6px 6px 0; margin:12px 0 18px; font-size:15px}
  table{border-collapse:collapse; width:100%; font-size:14.5px; margin:8px 0 16px} th,td{text-align:left; padding:8px 10px; border-bottom:1px solid var(--line); vertical-align:top} th{color:var(--ink2); font-weight:500}
  .work{background:var(--bg2); border:1px dashed var(--line); border-radius:var(--r); padding:12px 14px; font-family:"Comic Sans MS","Chalkboard SE",cursive; font-size:14.5px; color:var(--ink); margin:8px 0}
  .math{font-family:"STIX Two Text","Times New Roman",serif; font-size:17px}
  .ref{color:var(--link); text-decoration:underline dotted; cursor:pointer}
  .goal{display:grid; grid-template-columns:24px 1fr; gap:10px; margin:6px 0} .goal .b{width:20px; height:20px; border:2px solid var(--ink3); border-radius:3px; display:grid; place-items:center; font-size:13px; color:var(--accent)}
  .ts{font-family:ui-monospace,Menlo,monospace; font-size:13px; color:var(--accent); margin-right:8px}
  .empty{border:2px dashed var(--line); border-radius:var(--r); padding:28px; text-align:center; color:var(--ink3); margin:16px 0}
  footer{border-top:1px solid var(--line); padding:20px 24px; font-size:13px; color:var(--ink3); text-align:center}
"""
JS="""
<script>
(function(){
  const links=[...document.querySelectorAll('.gbar nav a, .sub a, a[data-go]')];
  function show(id){
    const target=document.getElementById(id)?id:document.querySelector('.page').id;
    document.querySelectorAll('.page').forEach(p=>p.classList.toggle('on',p.id===target));
    const grp=document.getElementById(target).dataset.group||target;
    document.querySelectorAll('.gbar nav a').forEach(a=>a.classList.toggle('on',a.dataset.group===grp));
    document.querySelectorAll('.sub a').forEach(a=>a.classList.toggle('on',a.getAttribute('href')==='#'+target));
    window.scrollTo({top:0});
  }
  links.forEach(a=>a.addEventListener('click',e=>{const h=a.getAttribute('href'); if(h&&h.startsWith('#')){e.preventDefault(); history.replaceState(null,'','#'+h.slice(1)); show(h.slice(1));}}));
  show((location.hash||'#home').slice(1));
})();
</script>
"""
THEMES={
 "editorial":dict(fonts_url="https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,500;1,400&family=Nunito+Sans:wght@400;600;700&display=swap",
   head_font='"Lora",Georgia,serif', body_font='"Nunito Sans","Helvetica Neue",Arial,sans-serif',
   bg="#FDFCFA", bg2="#F4F1EC", ink="#1F2A2E", line="#E3DED6", accent="#0B6E6E", accent_dark="#5FC6C0", accent_soft="#DDF0EE", accent_soft_dark="#173A3A", link="#0B6E6E", radius="4px",
   banner_css="background:linear-gradient(180deg,#0B6E6E 0%,#0A5C5C 100%); padding:72px 24px 64px; border-bottom:6px solid #E9B44C",
   extra_css=".banner h1{font-size:46px; font-style:italic; letter-spacing:.01em} .banner p{font-family:var(--body); letter-spacing:.12em; text-transform:uppercase; font-size:12px; margin-top:14px} h2{font-style:italic; font-weight:500} h3{font-weight:500} .tag{background:#E9B44C; color:#1F2A2E} .mile{border-left-color:#E9B44C} .embed .ico{color:#0B6E6E}",
   nav_css=".gbar nav a{letter-spacing:.04em; text-transform:uppercase; font-size:12.5px}"),
 "bold":dict(fonts_url="https://fonts.googleapis.com/css2?family=Oswald:wght@400;500;600&family=Source+Sans+3:wght@400;600&display=swap",
   head_font='"Oswald","Arial Narrow",Impact,sans-serif', body_font='"Source Sans 3","Helvetica Neue",Arial,sans-serif',
   bg="#FFFFFF", bg2="#F2F2F0", ink="#1F2328", line="#D9DAD7", accent="#D95D1E", accent_dark="#F5915B", accent_soft="#FBE6DA", accent_soft_dark="#4A2A18", link="#B4470F", radius="2px",
   banner_css="background:#1F2328; color:#fff; text-align:left; padding:48px 24px 40px; background-image:repeating-linear-gradient(135deg,transparent 0 22px,rgba(255,255,255,.04) 22px 24px)",
   extra_css=".banner h1{font-size:56px; text-transform:uppercase; letter-spacing:.03em; color:#F5915B; max-width:860px; margin:0 auto} .banner p{max-width:860px; margin:6px auto 0; font-weight:600; text-transform:uppercase; letter-spacing:.08em; font-size:13px} h2{text-transform:uppercase; letter-spacing:.02em; font-size:30px} h3{text-transform:uppercase; letter-spacing:.02em; font-size:19px} .gbar .site{text-transform:uppercase; letter-spacing:.04em} .card,.v{border-left:4px solid var(--accent)} .work{font-family:var(--body); font-weight:600}",
   nav_css=".gbar nav a{font-family:var(--head); text-transform:uppercase; letter-spacing:.05em; font-size:14px} .gbar nav a.on{background:var(--accent); color:var(--accent-ink); box-shadow:none; border-radius:2px}"),
 "playful":dict(fonts_url="https://fonts.googleapis.com/css2?family=Quicksand:wght@500;600;700&family=Nunito:wght@400;600;700&display=swap",
   head_font='"Quicksand","Trebuchet MS",sans-serif', body_font='"Nunito","Helvetica Neue",Arial,sans-serif',
   bg="#FFFFFF", bg2="#F5F3FB", ink="#2A2540", line="#E2DDF0", accent="#6B4FBB", accent_dark="#B39DF0", accent_soft="#ECE6FA", accent_soft_dark="#33285A", link="#5A3FA8", radius="14px",
   banner_css="background:#6B4FBB; background-image:linear-gradient(rgba(255,255,255,.14) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.14) 1px,transparent 1px); background-size:24px 24px; padding:64px 24px",
   extra_css=".banner h1{font-weight:700; font-size:44px} .banner p{background:#7EE0B8; color:#2A2540; display:inline-block; padding:4px 14px; border-radius:20px; font-weight:700; font-size:14px; margin-top:14px; opacity:1} h2{font-weight:700} h3{font-weight:700} .card,.v,.empty{border-width:2px} .empty{border-color:#7EE0B8; background:#F1FBF6; color:#2A2540} .tag{background:#7EE0B8; color:#2A2540} .goal .b{border-radius:50%} .sample{background:#F1FBF6}",
   nav_css=".gbar nav a{font-family:var(--head); font-weight:700; border-radius:20px} .gbar nav a.on{background:var(--accent-soft); box-shadow:none; border-radius:20px}"),
}
def comment(who,role,date,text,me=False):
    ini=''.join(w[0] for w in who.split()[:2])
    return f'<div class="cm{" me" if me else ""}"><div class="av">{E(ini)}</div><div><div class="who"><b>{E(who)}</b> · {E(role)} · {E(date)}</div><p>{text}</p></div></div>'
def embed(name,meta,kind="PDF"):
    return f'<div class="embed"><div class="ico">{E(kind)}</div><div><div class="nm">{E(name)}</div><div class="meta">{E(meta)}</div></div></div>'
def artifact_page(title,tag,artifact,context,reflection,feedback,connections,nxt):
    return f'''<h3>{E(title)}<span class="tag">{E(tag)}</span></h3>
<h4>Artifact</h4>{artifact}
<h4>Context</h4><p>{context}</p>
<h4>Reflection</h4>{reflection}
<h4>Feedback &amp; reply</h4>{feedback}
<h4>Connections</h4><p>{connections}</p>
<h4>Next step</h4><p>{nxt}</p>'''

def site(title,name,subtitle,pages,nav,footer_note,desc,theme="editorial"):
    """pages: list of (id, group, heading, body_html). nav: list of (group_label, group_id, [(sub_label, page_id)...])"""
    navhtml=''.join(f'<a href="#{g[2][0][1]}" data-group="{g[1]}">{E(g[0])}</a>' for g in nav)
    body=[]
    for pid,group,heading,content in pages:
        subs=[g for g in nav if g[1]==group][0][2]
        subhtml='<div class="sub">'+''.join(f'<a href="#{sp}">{E(sl)}</a>' for sl,sp in subs)+'</div>' if len(subs)>1 else ''
        body.append(f'<div class="page" id="{pid}" data-group="{group}"><h2>{E(heading)}</h2>{subhtml}{content}</div>')
    T=THEMES[theme]; css=CSS
    for k,v in T.items(): css=css.replace('%('+k+')s',v)
    return f'''<title>{E(title)}</title>
<link rel="stylesheet" href="{T['fonts_url']}">
<style>{css}</style>
<div class="sample">Sample portfolio · {E(name)} is a fictional student · Miami University Mathematics Education · <a href="{HOME}">← Back to the program site</a></div>
<div class="gbar"><div class="site">{E(name)}</div><nav>{navhtml}</nav></div>
<div class="banner"><h1>{E(name)}</h1><p>{E(subtitle)}</p></div>
<main>{''.join(body)}</main>
<footer>{E(footer_note)} · Built with Google Sites (sample rendering)</footer>
{JS}'''
