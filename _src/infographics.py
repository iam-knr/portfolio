# Builds the five infographics for the "Build notes" cards on the home page.
import re,io
P='/home/claude/portfolio/index.html'
CR='#f6f1e8'

def T(x,y,s,cls='s',anchor='start',extra=''):
    return f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}" {extra}>{s}</text>'
def R(x,y,w,h,cls,rx=8,extra=''):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{cls}" {extra}/>'
def L(d,cls='st',mk=None):
    m=f' marker-end="url(#{mk})"' if mk else ''
    return f'<path d="{d}" class="{cls}"{m}/>'
def defs(i,ink=False):
    c='#151210' if ink else CR
    return f'<defs><marker id="ar{i}" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L8,4 L0,8z" fill="{c}"/></marker></defs>'
def svg(label,body,i,vb='0 0 520 210'):
    return f'<svg class="ig" viewBox="{vb}" role="img" aria-label="{label}" xmlns="http://www.w3.org/2000/svg">{defs(i)}{body}</svg>'

# 1 Shika
b=[]
for r in range(3):
    for c in range(5):
        b.append(f'<circle cx="{34+c*17}" cy="{34+r*17}" r="6" class="cr" opacity="{1 if (r*5+c)%4 else .55}"/>')
b.append(T(24,138,'15','n','start','font-size="66"'))
b.append(T(24,160,'PET COMPANIONS','s'))
b.append(T(24,176,'ON YOUR SCREEN','s','start','opacity=".75"'))
b.append(R(150,16,356,118,'st',14,'stroke-dasharray="4 4"'))
b.append(T(166,36,'RUNS ON MY OWN MACHINE','s'))
xs=[164,276,388]; labs=[('HOLD A KEY','AND TALK'),('SHIKA TIDIES','THE TEXT'),('TEXT LANDS','AT CURSOR')]
for k,(x,(a,c2)) in enumerate(zip(xs,labs)):
    b.append(R(x,52,104,60,'ac' if k==1 else 'cr',8))
    col='' if k==1 else 'ink'
    b.append(T(x+52,78,a,'m '+col,'middle'))
    b.append(T(x+52,94,c2,'m '+col,'middle'))
    if k<2: b.append(L(f'M{x+106},82 L{x+120},82','st','ar1'))
b.append(T(150,160,'ALSO KEEPS ME ON TRACK','s'))
px=150
for lab,w in [('REMINDERS',84),('TASKS',56),('STICKY NOTES',92),('FOCUS TIMER',88)]:
    b.append(R(px,168,w,26,'st',13)); b.append(T(px+w/2,185,lab,'s','middle')); px+=w+6
S1=svg('Shika AI: hold a key and talk, Shika tidies the text, the words land at your cursor, all on your own machine. It also keeps reminders, tasks, sticky notes and a focus timer, with 15 pet companions.',''.join(b),1)

# 2 AdCheck
b=[]
b.append(R(24,18,150,130,'cr',10))
b.append(R(24,18,150,18,'ink',10)); b.append(R(24,28,150,8,'ink',0))
b.append(R(34,44,130,34,'cr',3,'opacity=".0"'))
b.append(R(32,46,134,20,'ac',3)); b.append(T(40,60,'Guaranteed leads','s ','start','fill="#f6f1e8"'))
b.append(T(40,88,'Learn Meta Ads','s ink'))
b.append(R(32,96,134,20,'ac',3)); b.append(T(40,110,'Earn 50k a month','s','start'))
b.append(R(34,124,60,10,'ink',3,'opacity=".18"'))
b.append(T(24,168,'AD DRAFT IN ADS MANAGER','s'))
b.append(L('M178,84 L198,84','st','ar2'))
b.append(R(200,64,80,40,'ac',8)); b.append(T(240,89,'ADCHECK','m','middle'))
b.append(L('M284,84 L326,84','st','ar2'))
rows=[('FLAG','GUARANTEES',True),('FLAG','INCOME CLAIMS',True),('PASS','EVERYTHING ELSE',False)]
for k,(tag,lab,flag) in enumerate(rows):
    y=18+k*40
    b.append(R(330,y,176,32,'cr',7))
    b.append(R(330,y,44,32,'ac' if flag else 'ink',7)); b.append(R(360,y,14,32,'ac' if flag else 'ink',0))
    b.append(T(352,y+20,tag,'s','middle'))
    b.append(T(382,y+20,lab,'s ink'))
b.append(T(330,152,'EACH FLAG GIVES THE REASON','s')); b.append(T(330,166,'AND A SAFER FIX','s'))
b.append(T(24,200,'25+','n','start','font-size="38"'))
b.append(T(98,186,'RULES IN','s')); b.append(T(98,200,'8 GROUPS','s'))
for k in range(8):
    b.append(R(200+k*38,184,34,14,'ac' if k in (2,3) else 'st',3))
S2=svg('AdCheck: an ad draft goes into AdCheck, which reads it and returns flags with the reason and a safer fix, such as guarantees and income claims. It checks 25 plus rules in 8 groups.',''.join(b),2)

# 3 Programmatic SEO
b=[]
b.append(T(24,20,'REAL DATA ROWS','s'))
b.append(R(24,28,98,108,'cr',8)); b.append(R(24,28,98,20,'ink',8,'')); b.append(R(24,40,98,8,'ink',0))
for k in range(5):
    b.append(R(32,56+k*16,34,6,'ink',3,'opacity=".25"')); b.append(R(74,56+k*16,40,6,'ink',3,'opacity=".25"'))
b.append(L('M126,82 L146,82','st','ar3'))
b.append(R(148,52,96,56,'ac',8)); b.append(T(196,76,'ONE','m','middle')); b.append(T(196,92,'TEMPLATE','m','middle'))
b.append(T(148,126,'40%+ UNIQUE','s')); b.append(T(148,140,'TEXT PER PAGE','s'))
b.append(L('M248,82 L268,82','st','ar3'))
b.append(R(270,52,92,56,'st',8,'stroke-dasharray="4 4"')); b.append(T(316,76,'READ 10','m','middle')); b.append(T(316,92,'BY HAND','m','middle'))
b.append(T(270,126,'PUBLISH 10 TO','s')); b.append(T(270,140,'20 AT A TIME','s'))
b.append(L('M366,82 L386,82','st','ar3'))
held={(0,3),(1,1),(2,2),(3,0)}
for r in range(4):
    for c in range(4):
        x=390+c*28; y=24+r*28
        if (r,c) in held: b.append(R(x,y,22,24,'st',3,'stroke-dasharray="3 3" opacity=".8"'))
        else: b.append(R(x,y,22,24,'cr',3))
b.append(R(390,142,12,12,'cr',2)); b.append(T(408,152,'LIVE','s'))
b.append(R(450,142,12,12,'st',2,'stroke-dasharray="3 3"')); b.append(T(468,152,'HELD','s'))
b.append(T(24,196,'100+','n','start','font-size="42"'))
b.append(T(140,182,'ACTIVE','s')); b.append(T(140,196,'INSTALLS','s'))
S3=svg('Programmatic SEO: real data rows go into one template with at least 40 percent unique text per page, you read 10 pages by hand, then publish 10 to 20 at a time while weak pages are held back. The plugin has 100 plus active installs.',''.join(b),3)

# 4 SafeStep
b=[]
nodes=[(24,'1','SNAPSHOT',('COPY OF THE','OLD FILES')),(148,'2','INSTALL',('WORDPRESS','AS USUAL')),(272,'3','CHECK',('HOME + LOGIN','+ YOUR PAGES'))]
for k,(x,n,t,(a,c2)) in enumerate(nodes):
    chk=(k==2)
    b.append(R(x,34,100,72,'ac' if chk else 'cr',8))
    col='' if chk else 'ink'
    b.append(T(x+12,54,n,'s '+col,'start','opacity=".7"'))
    b.append(T(x+50,66,t,'m '+col,'middle'))
    b.append(T(x+50,84,a,'s '+col,'middle')); b.append(T(x+50,97,c2,'s '+col,'middle'))
    if k<2: b.append(L(f'M{x+104},70 L{x+120},70','st','ar4'))
b.append(L('M376,62 L394,44','st','ar4')); b.append(L('M376,78 L394,96','st','ar4'))
b.append(R(396,20,100,44,'cr',8)); b.append(T(446,39,'KEEP IT','m ink','middle')); b.append(T(446,54,'SITE HEALTHY','s ink','middle'))
b.append(R(396,76,100,44,'ac',8)); b.append(T(446,95,'ROLL BACK','m','middle')); b.append(T(446,110,'SITE BROKEN','s','middle'))
b.append(L('M446,122 L446,148 L74,148 L74,110','st','ar4'))
b.append(T(260,168,'OLD VERSION RETURNS, YOU GET AN EMAIL','s','middle'))
b.append(T(24,200,'GPL','n','start','font-size="38"'))
b.append(T(118,200,'FREE PLUGIN','s'))
S4=svg('SafeStep Updates: snapshot the old files, WordPress installs the update as usual, SafeStep checks the home page, login page and your pages. If the site is healthy it keeps the update. If it is broken it rolls back, the old version returns and you get an email. A free GPL plugin.',''.join(b),4)

# 5 Book
b=[]
b.append(T(24,20,'5 PLATFORMS','s'))
px=24
for lab,w in [('META',60),('LINKEDIN',84),('TIKTOK',70),('SNAPCHAT',90),('X',38)]:
    b.append(R(px,28,w,28,'cr',14)); b.append(T(px+w/2,46,lab,'s ink','middle')); px+=w+8
b.append(T(24,82,'160+ SCREENSHOTS','s'))
for k in range(16):
    x=24+k*30
    b.append(R(x,90,24,34,'st',4)); b.append(R(x,90,24,8,'cr',4)); b.append(R(x+4,104,16,3,'cr',1.5,'opacity=".6"')); b.append(R(x+4,111,10,3,'cr',1.5,'opacity=".6"'))
b.append(T(24,146,'75 STEP BY STEP SOPS','s'))
for r in range(4):
    for c in range(15):
        b.append(R(24+c*14,154+r*14,10,10,'ac',2))
b.append(T(250,206,'75','n','start','font-size="74"'))
b.append(T(366,170,'SOPS','m')); b.append(T(366,186,'INSIDE','m')); b.append(T(366,202,'THE BOOK','s','start','opacity=".75"'))
S5=svg('The Ad Account Nobody Shows You: a book on social ads that covers 5 platforms, Meta, LinkedIn, TikTok, Snapchat and X, with 160 plus screenshots and 75 step by step SOPs.',''.join(b),5)

s=open(P).read()
S=[S1,S2,S3,S4,S5]
# replace each tile in order inside build-notes
i0=s.find('id="build-notes"'); i1=s.find('id="hire"')
seg=s[i0:i1]
pat=re.compile(r'<span class="tile ([rk])"(?: aria-hidden="true">.*?</small>|>.*?</svg>)</span>',re.S)
tiles=pat.findall(seg); assert len(tiles)==5,len(tiles)
it=iter(S)
seg=pat.sub(lambda m:f'<span class="tile {m.group(1)}">{next(it)}</span>',seg)
seg=seg.replace('<a class="cell" style="grid-column:1/-1" data-cur="Open"','<a class="cell wide" style="grid-column:1/-1" data-cur="Open"')
s=s[:i0]+seg+s[i1:]
open(P,'w').write(s)
print('ok')
