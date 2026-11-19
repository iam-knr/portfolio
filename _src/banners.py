"""Generate banner.svg and banner.png for article slugs. Usage: python3 _src/banners.py slug [slug...]"""
import sys,os
sys.path.insert(0,'_src')
import hero
from playwright.sync_api import sync_playwright
slugs=sys.argv[1:] or list(hero.CFG)
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':1200,'height':630})
    for s in slugs:
        svg,_=hero.svg(s)
        os.makedirs(f'blog/{s}',exist_ok=True)
        open(f'blog/{s}/banner.svg','w',encoding='utf8').write(svg)
        pg.set_content(f'<body style="margin:0">{svg}</body>')
        pg.screenshot(path=f'blog/{s}/banner.png',clip={'x':0,'y':0,'width':1200,'height':630})
        print(s)
    b.close()
