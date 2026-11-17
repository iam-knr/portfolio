import re,json,glob,os,html,sys
sys.path.insert(0,'_src')
from ig import IGS
BASE="https://iamknr.in"
DATE="2026-11-17"
FONTS='<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,400..900&family=Instrument+Serif:ital@0;1&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">'
PERSON={"@type":"Person","@id":BASE+"/#kailas","name":"Kailas (KNR) Nath R","alternateName":"KNR","url":BASE+"/","image":BASE+"/blog/knr.png","jobTitle":"Agentic AI Consultant and Digital Marketing Consultant","sameAs":["https://linkedin.com/in/iamknr/","https://github.com/iam-knr/","https://profiles.wordpress.org/kailasnathr/","https://aiinmarketing.in/author/kailasnathr","https://adsmentor.in"]}
def slugify(t):
    t=re.sub(r'<[^>]+>','',t);t=html.unescape(t).lower();return re.sub(r'[^a-z0-9]+','-',t).strip('-')[:60]
def parse(path):
    raw=open(path,encoding='utf8').read()
    head,body=raw.split('\n---\n',1)
    m={}
    for line in head.strip().strip('-').strip().split('\n'):
        k,v=line.split(':',1);m[k.strip()]=v.strip()
    m['body']=body.strip();return m
arts=[parse(p) for p in sorted(glob.glob('_src/*.html'))]
arts.sort(key=lambda a:int(a['order']))
HEADER=f'''<header class="top"><div class="wide"><a class="logo" href="/">K<b>N</b>R</a><nav aria-label="Main"><a href="/">Home</a><a href="/blog/">Articles</a><a href="/#hire">Hire</a><a href="https://linkedin.com/in/iamknr/" rel="noopener">LinkedIn</a></nav></div></header>'''
AUTHOR='''<section class="author" aria-label="About the author"><img src="/blog/knr.png" width="150" height="150" alt="Kailas (KNR) Nath R working on his laptop" loading="lazy"><div><div class="lab">About the author</div><h2>Kailas (KNR) Nath R</h2><p class="role">Agentic AI Consultant and Digital Marketing Consultant, India</p><p>Kailas runs paid ads for enterprise and retail brands, builds AI agents and writes the code himself. He is co-founder of Ads Mentor, founder of Dealfox AI CRM, and has trained more than 4,000 marketers in live classes. He is the author of a book on social media ads. He writes here about what he actually builds and runs, and says plainly when something did not work.</p><ul class="facts"><li>7+ years in digital marketing</li><li>4,000+ marketers trained</li><li>Ads Mentor co-founder</li><li>Dealfox AI CRM founder</li><li>Based in India</li></ul><div class="links"><a href="https://linkedin.com/in/iamknr/" rel="me noopener">LinkedIn</a><a href="https://github.com/iam-knr/" rel="me noopener">GitHub</a><a href="https://aiinmarketing.in/author/kailasnathr" rel="me noopener">AI in Marketing</a><a href="https://adsmentor.in" rel="noopener">Ads Mentor</a><a href="https://amazon.in/dp/B0HPKN3W3D" rel="noopener">The book</a><a href="/#hire">Work with Kailas</a></div></div></section>'''
FOOT='''<footer><div class="wide"><div class="row"><a href="/">Home</a><a href="/blog/">All articles</a><a href="/sitemap.xml">Sitemap</a><a href="/llms.txt">llms.txt</a><a href="https://github.com/iam-knr/">GitHub</a></div>&copy; 2026 Kailas (KNR) Nath R. Based in India.</div></footer>'''
def page(title,desc,path,body,schema,kw="",ptype="article"):
    url=BASE+path
    return f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<meta name="author" content="Kailas (KNR) Nath R">
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
<meta name="theme-color" content="#ebe7df">
<link rel="canonical" href="{url}">
<meta property="og:site_name" content="Kailas (KNR) Nath R">
<meta property="og:type" content="{ptype}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}/blog/knr.png">
<meta name="twitter:card" content="summary">
<script type="application/ld+json">{json.dumps(schema,ensure_ascii=False)}</script>
{FONTS}
<link rel="stylesheet" href="/blog/blog.css">
</head><body>
{HEADER}
{body}
{FOOT}
</body></html>'''

BOOK='''<section class="book" aria-label="The book"><img src="https://aiinmarketing.in/wp-content/uploads/2026/11/the-ad-account-nobody-shows-you-book-banner.png" width="1200" height="630" alt="Cover of the book The Ad Account Nobody Shows You, Social Ads Zero to Pro, with 160+ screenshots and 75 step by step SOPs" loading="lazy"><div class="tx"><div class="lab">The book by Kailas</div><h2>The Ad Account Nobody Shows You</h2><p>Social Ads Zero to Pro, 2026 edition. A hands-on guide to paid social on Meta, LinkedIn, TikTok, Snapchat and X, with 160+ real screenshots, 75 step by step chapters and the rules Indian agencies follow.</p><div class="btns"><a class="p" href="https://amazon.in/dp/B0HPKN3W3D" rel="noopener">Get the book</a><a href="https://aiinmarketing.in/blogs/the-ad-account-nobody-shows-you-book" rel="noopener">Read about it</a></div></div></section>'''
AIMALL=[("The 2.4 lakh mistake: who really owns your ad account?","who-owns-your-ad-account-case-study","Case study"),("Agentic AI: what to hand to AI agents","agentic-ai-marketing-work-competitors-hand-to-agents","Agentic AI"),("Six AI advertising mistakes that cost clients","ai-advertising-problems-nobody-posts-about","Ads"),("What is vibe marketing? A beginner guide","what-is-vibe-marketing","Definition"),("Zero-click AI search: stay visible and get leads","zero-click-ai-search-and-ads","SEO"),("Automated ad accounts: how marketers stay valuable","ad-accounts-run-themselves","Ads"),("Seven questions to ask before paying for an AI marketing course","ai-in-marketing-course-what-to-look-for","Training"),("Best digital marketing course in India, compared on fees and AI","best-digital-marketing-courses-india-2026-how-to-choose","Training")]
def aim(idx):
    pick=[AIMALL[(idx+k)%8] for k in (0,1,2,3)]
    li=''.join(f'<li><a href="https://aiinmarketing.in/blogs/{u}" rel="noopener">{html.escape(t)}<span>{k} &rarr;</span></a></li>' for t,u,k in pick)
    return f'<section class="aim" aria-label="Articles on AI in Marketing"><h2>More on AI in Marketing</h2><p class="sub">Articles from AIM, the live AI marketing program I teach.</p><ul>{li}</ul><a class="all" href="https://aiinmarketing.in/blogs" rel="noopener">View all articles on aiinmarketing.in &rarr;</a></section>'
AIMCARD='<section class="aimcard" aria-label="AI in Marketing"><div class="lab">AI in Marketing by Ads Mentor</div><h2>Want more? Read the AIM articles</h2><p>Case studies, course guides and ad account lessons from the live AI marketing program I teach, all on aiinmarketing.in.</p><a class="btn" href="https://aiinmarketing.in/blogs" rel="noopener">Go to aiinmarketing.in &rarr;</a></section>'
def faqs(body):
    out=[]
    for m in re.finditer(r'<details><summary>(.*?)</summary>\s*<p>(.*?)</p>\s*</details>',body,re.S):
        out.append({"@type":"Question","name":html.unescape(re.sub(r'<[^>]+>','',m.group(1))),"acceptedAnswer":{"@type":"Answer","text":html.unescape(re.sub(r'<[^>]+>','',m.group(2)))}})
    return out
for a in arts:
    body=a['body']
    heads=[]
    def addid(m):
        t=m.group(1);i=slugify(t);heads.append((i,re.sub(r'<[^>]+>','',t)));return f'<h2 id="{i}">{t}</h2>'
    body=re.sub(r'<h2>(.*?)</h2>',addid,body)
    if a['slug'] in IGS:
        cap,svg=IGS[a['slug']]
        fig=f'<figure class="ig">{svg}<figcaption>{html.escape(cap)}</figcaption></figure>'
        parts=body.split('<h2 id=',2)
        body=parts[0]+'<h2 id='+parts[1]+fig+'<h2 id='+parts[2] if len(parts)==3 else body
    toc='<nav class="toc" aria-label="Table of contents"><b>In this article</b><ol>'+''.join(f'<li><a href="#{i}">{html.escape(t)}</a></li>' for i,t in heads)+'</ol></nav>'
    words=len(re.sub(r'<[^>]+>',' ',body).split())
    mins=max(1,round(words/220))
    a['words']=words
    rel=[x for x in arts if x['slug']!=a['slug']]
    relh='<h2 style="margin-top:40px">Keep reading</h2><div class="rel">'+''.join(f'<a href="/blog/{x["slug"]}/"><span>{x["type"]}</span>{html.escape(x["h1"])}</a>' for x in rel[:6])+'</div>'
    cta='<div class="cta"><h2>Want this built for your business?</h2><p>I work with brands in India that want agents, automation and ads that are tied to revenue. Tell me the goal and I will tell you honestly if I can help.</p><a class="btn" href="https://linkedin.com/in/iamknr/" rel="noopener">Message Kailas on LinkedIn</a></div>'
    main=f'''<main><div class="wrap"><div class="crumbs"><a href="/">Home</a> / <a href="/blog/">Articles</a> / {html.escape(a['crumb'])}</div>
<article><h1>{a['h1']}</h1><p class="dek">{a['dek']}</p>
<div class="by"><img src="/blog/knr.png" width="44" height="44" alt="" loading="lazy"><span>By <strong><a href="/#about" style="color:inherit">Kailas (KNR) Nath R</a></strong></span><span>Published <time datetime="{DATE}">17 Nov 2026</time></span><span>{mins} min read</span></div>
<div class="answer"><b>Short answer</b><p>{a['answer']}</p></div>
{toc}
{body}
{cta}
{BOOK}
{aim(int(a['order'])-1)}
</article>
{AUTHOR}
{relh}</div></main>'''
    fq=faqs(body)
    graph=[{"@type":"Article","@id":BASE+f"/blog/{a['slug']}/#article","headline":a['h1'],"description":a['desc'],"datePublished":DATE,"dateModified":DATE,"author":{"@id":BASE+"/#kailas"},"publisher":{"@id":BASE+"/#kailas"},"mainEntityOfPage":BASE+f"/blog/{a['slug']}/","image":BASE+"/blog/knr.png","inLanguage":"en-IN","keywords":a['kw'],"wordCount":words},
           {"@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":BASE+"/"},{"@type":"ListItem","position":2,"name":"Articles","item":BASE+"/blog/"},{"@type":"ListItem","position":3,"name":a['crumb']}]},PERSON]
    if fq:graph.append({"@type":"FAQPage","mainEntity":fq})
    os.makedirs(f'blog/{a["slug"]}',exist_ok=True)
    open(f'blog/{a["slug"]}/index.html','w',encoding='utf8').write(page(a['title'],a['desc'],f'/blog/{a["slug"]}/',main,{"@context":"https://schema.org","@graph":graph},a['kw']))
# index
cards=''.join(f'<div class="card"><div class="k">{a["type"]}</div><h2><a href="/blog/{a["slug"]}/">{html.escape(a["h1"])}</a></h2><p>{a["desc"]}</p><div class="m">{max(1,round(a["words"]/220))} min read &middot; {a["words"]:,} words</div></div>' for a in arts)
idx=f'''<main><div class="wrap"><div class="crumbs"><a href="/">Home</a> / Articles</div><h1>Agentic AI, MCP and AI marketing, explained plainly</h1><p class="dek">Long guides from a working practitioner in India. Each one starts with a definition, shows how the thing works in real campaigns, and lists where it fails.</p>
<div class="cards">{cards}</div>
{BOOK}
{AIMCARD}
{AUTHOR}</div></main>'''
g=[{"@type":"CollectionPage","name":"Articles on agentic AI, MCP and AI in marketing","url":BASE+"/blog/","author":{"@id":BASE+"/#kailas"},"hasPart":[{"@type":"Article","headline":a['h1'],"url":BASE+f"/blog/{a['slug']}/"} for a in arts]},PERSON]
open('blog/index.html','w',encoding='utf8').write(page("Articles on Agentic AI, MCP and AI in Marketing | Kailas (KNR) Nath R","Definition-led guides on agentic AI, Model Context Protocol, AI in marketing, AI in advertising and AI landing pages, by Kailas (KNR) Nath R, an agentic AI consultant in India.","/blog/",idx,{"@context":"https://schema.org","@graph":g},ptype="website"))
# sitemap, robots, llms
urls=[("/",1.0),("/blog/",0.9)]+[(f"/blog/{a['slug']}/",0.8) for a in arts]
open('sitemap.xml','w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join(f'  <url><loc>{BASE}{u}</loc><lastmod>{DATE}</lastmod><priority>{p}</priority></url>\n' for u,p in urls)+'</urlset>\n')
open('robots.txt','w').write(f'User-agent: *\nAllow: /\n\nSitemap: {BASE}/sitemap.xml\n')
llms=f'''# Kailas (KNR) Nath R

> Kailas (KNR) Nath R is an agentic AI consultant and digital marketing consultant based in India. He runs paid ads, builds AI agents and writes code. Co-founder of Ads Mentor, founder of Dealfox AI CRM, author of a book on social media ads, and has trained more than 4,000 marketers.

Home page: {BASE}/
Contact: https://linkedin.com/in/iamknr/

## Articles
'''+''.join(f"- [{a['h1']}]({BASE}/blog/{a['slug']}/): {a['desc']}\n" for a in arts)+f'''
## Profiles
- [LinkedIn](https://linkedin.com/in/iamknr/)
- [GitHub](https://github.com/iam-knr/)
- [Ads Mentor](https://adsmentor.in)
- [AI in Marketing author page](https://aiinmarketing.in/author/kailasnathr)
- [Shika AI desktop pet](https://shika.iamknr.in/)
'''
open('llms.txt','w').write(llms)
print(len(arts),'articles',[ (a['slug'],a['words']) for a in arts])
