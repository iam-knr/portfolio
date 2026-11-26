"""Builds the lead magnet PDFs in /downloads from the data below.
Run: python3 _src/pdfs.py   (needs playwright with chromium)"""
import html,os,sys
from playwright.sync_api import sync_playwright

RED="#d81e16";INK="#151210"
CSS=f"""
@page{{size:A4;margin:16mm 15mm}}
*{{box-sizing:border-box}}
body{{font-family:Arial,Helvetica,'Liberation Sans',sans-serif;color:{INK};font-size:11.5px;line-height:1.5;margin:0}}
.top{{display:flex;justify-content:space-between;align-items:center;border-bottom:3px solid {INK};padding-bottom:8px;margin-bottom:14px}}
.logo{{font-weight:900;font-size:18px;letter-spacing:1px}}.logo b{{background:{RED};color:#fff;padding:0 3px}}
.tag{{font-size:9.5px;letter-spacing:2px;text-transform:uppercase;color:#6b645a}}
h1{{font-size:26px;line-height:1.1;margin:6px 0 6px;font-weight:900}}
.lede{{font-size:12.5px;margin:0 0 12px;color:#3a352f}}
h2{{font-size:13.5px;margin:14px 0 5px;padding:3px 8px;background:{INK};color:#fff;font-weight:800;break-after:avoid}}
.item{{display:flex;gap:8px;padding:4px 0;border-bottom:1px dotted #bdb6aa;break-inside:avoid}}
.box{{flex:0 0 12px;height:12px;border:1.6px solid {INK};margin-top:2px}}
.item b{{display:block}}.item span{{color:#4a443d}}
.line{{border-bottom:1px solid #9b9488;height:20px}}
.note{{font-size:10px;color:#5a544c;border-top:2px solid {RED};margin-top:16px;padding-top:6px}}
.foot{{margin-top:12px;font-size:10.5px}}.foot a{{color:{RED};font-weight:700}}
"""
def build(title,lede,groups,foot,note,blank=0):
    h=f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>'
    h+='<div class="top"><div class="logo">K<b>N</b>R</div><div class="tag">Free download · iamknr.in</div></div>'
    h+=f'<h1>{html.escape(title)}</h1><p class="lede">{html.escape(lede)}</p>'
    for g,items in groups:
        h+=f'<h2>{html.escape(g)}</h2>'
        for it in items:
            if it==LINES:
                h+='<div class="line"></div>'*8;continue
            if isinstance(it,tuple):
                h+=f'<div class="item"><div class="box"></div><div><b>{html.escape(it[0])}</b><span>{html.escape(it[1])}</span></div></div>'
            else:
                h+=f'<div class="item"><div class="box"></div><div><b>{html.escape(it)}</b></div></div>'
    for _ in range(blank):h+='<div class="line"></div>'
    h+=f'<div class="foot">{foot}</div><div class="note">{html.escape(note)}</div></body></html>'
    return h

DOCS={}
LINES=('__lines__','')

DOCS['meta-ad-pre-publish-checklist-india.pdf']=build(
"Meta Ad Pre-Publish Checklist for Indian Advertisers",
"Read your ad against these checks before you press publish. Each one is a pattern that tends to get ads rejected or questioned. Tick it, or rewrite the line.",
[("1. Talking about the person",[
 ("No guess about the reader's situation","\"Are you struggling with debt?\" reads as if Meta knows the person's finances. Talk about the topic instead: \"Debt help for people who want a plan.\""),
 ("\"You\" is not next to health, money, age, religion or identity","Check the headline and the first line of primary text, where this slips in most."),
]),
("2. Health and wellness",[
 ("No promise of a result in a set time","\"Lose 5 kg in 7 days\" is a timeframe promise."),
 ("No cure claims","Say what the product or service is, not that it cures a condition."),
 ("No body-shaming and no before and after images","Both are common reasons for rejection."),
]),
("3. Money and income",[
 ("No specific earnings figure unless you can prove it for a normal customer","\"Earn 1 lakh a month\" needs proof and context, and is safer left out."),
 ("No \"passive income\" or \"financial freedom\" promise","Describe the skill or product and the effort needed."),
 ("No guaranteed returns, clients, jobs or results","The word \"guaranteed\" next to an outcome is a flag."),
 ("Loans, crypto and \"no credit check\" lines have been read against Meta's financial products rules","These categories can need extra approval or a licence."),
]),
("4. Education and coaching (India)",[
 ("No placement or salary figure you cannot show with proof","\"100% placement\" and \"pay after placement\" are the classic ones."),
 ("Say what support you give, not what outcome you promise","Example: interview prep sessions, job application support and guidance."),
 ("Fee and refund wording matches your own terms page","The ad, the landing page and the terms should say the same thing."),
]),
("5. Claims and proof",[
 ("No government approval or certification claim without the paper to show it","Keep the certificate ready in case you are asked."),
 ("\"No. 1\", \"best\" and \"top\" claims have a source on the landing page","If you cannot point to a source, remove the claim."),
 ("No clickbait, no ALL CAPS shouting, no fake urgency","Fake countdowns and \"only 2 left\" lines you cannot back up."),
]),
("6. Creatives",[
 ("Read the text inside every image and video frame","The rules apply to the words in the creative as well as the caption."),
 ("Image shows the product or service, not the viewer's body or problem","Close-ups of skin, weight or debt papers are risky."),
 ("Aspect ratio and resolution suit each placement","Feed, Stories and Reels need different crops."),
]),
("7. Landing page and account",[
 ("The landing page says what the ad says","A claim in the ad that is missing on the page is a mismatch."),
 ("Privacy policy and contact details are on the page",""),
 ("The ad account and payment method belong to your business","Ask who owns the account before you spend. It matters if anything goes wrong."),
 ("Someone other than the writer has read the ad once","Fresh eyes catch the line you stopped seeing."),
])],
'Want this check done for you inside Ads Manager? AdCheck is a free Chrome extension that marks risky phrases and explains why. <a href="https://adcheck.iamknr.in/">adcheck.iamknr.in</a> · Guide: <a href="https://iamknr.in/blog/adcheck-meta-ad-rejection-checker-chrome-extension/">iamknr.in/blog</a>',
"This checklist is based on Meta's published Advertising Standards and public guidance, including ASCI and CCPA summaries. It is a working aid, not legal advice, and following it does not guarantee approval. Meta also reviews images, landing pages and account history.")

DOCS['programmatic-seo-launch-checklist.pdf']=build(
"Programmatic SEO Launch Checklist for WordPress",
"Use this before you publish a batch of pages made from a data file and a template. It is the list I use for generated pages, including the city pages on AI in Marketing.",
[("1. Pick the pages worth making",[
 ("Each page answers a different search, not the same one with a new word","If two pages would give the same answer, make one page."),
 ("You checked real search volume for the pattern","Look at the keyword in a tool such as Semrush before you build 100 pages."),
 ("A person would find the page useful without the search engine","Ask: would I send this link to a friend?"),
]),
("2. Data",[
 ("Every row has real facts that differ from the other rows","Prices, places, steps, examples, rules that are true for that page."),
 ("No invented numbers, quotes or reviews","If you do not have a source, leave it out."),
 ("Each fact that could change has a date or a source","Add a line such as \"checked October 2026\"."),
]),
("3. Template",[
 ("At least 40% of the text on each page is unique to that page","This is my own rule for generated pages. Boilerplate is fine, but it cannot be most of the page."),
 ("One H1, a clear opening answer and a short FAQ with real questions",""),
 ("Titles are under about 60 characters and descriptions under about 160","Each one is different from every other page."),
 ("Each page has one canonical URL","Check that the template does not output two."),
 ("Schema matches what is on the page","FAQ schema only if the FAQ is visible."),
]),
("4. Site structure",[
 ("A pillar page links to every child page","And each child links back to the pillar."),
 ("Pages link to a few related pages, not to all of them","Nearby cities, related services, the next step."),
 ("All pages are in the sitemap","Update the last modified date when you change a page."),
 ("The new pages have a clear path to a lead magnet or form","A page with no next step wastes the visit."),
]),
("5. Launch in small steps",[
 ("Read at least 10 pages by hand, start to end","Look for repeated sentences, wrong names and empty sections."),
 ("Check on a phone","Tables, long titles and images break on small screens first."),
 ("Publish 10 to 20 pages first, not 500","Watch indexing for two weeks."),
 ("Keep thin pages out of the index until they are fixed","Use noindex while you improve them."),
 ("Ask for indexing on the pillar and a few children in Search Console",""),
]),
("6. After launch",[
 ("Track impressions and clicks by page group","Compare the group, not single pages."),
 ("Merge or remove pages that get no impressions after two months",""),
 ("Refresh facts every quarter","Change the date only when the content really changed."),
])],
'The Big SEO Programmatic plugin is free on WordPress.org. Read the full guide at <a href="https://iamknr.in/blog/programmatic-seo-wordpress-plugin-big-seo-programmatic/">iamknr.in/blog</a>.',
"A working checklist from the author's own practice. Search engines change their rules, so check current guidance for anything that matters to your site.")

DOCS['wordpress-plugin-update-safety-checklist.pdf']=build(
"WordPress Plugin Update Safety Checklist",
"A short routine for updating plugins without losing a night to a broken site. Use it for manual updates, and as the rules you set for automatic ones.",
[("1. Before you update",[
 ("Take a full backup of files and database","A plugin snapshot is not a backup. Keep both."),
 ("Read the changelog for the update","Look for words like breaking change, removed, requires, or new minimum PHP."),
 ("Check PHP and WordPress versions against the plugin's requirements",""),
 ("List the pages that must never break","Home, login, contact, checkout, your main landing pages."),
 ("Avoid updates during a sale or a live ad push","A broken page while ads run spends budget on visitors who see an error."),
]),
("2. Update",[
 ("Update one plugin at a time","If something breaks, you know which one."),
 ("Update plugins that other plugins depend on first, then the dependants",""),
 ("Keep the previous version's zip file","You need it for a manual rollback."),
]),
("3. Check straight after",[
 ("Open the home page and the login page in a private window",""),
 ("Open every page on your must-not-break list",""),
 ("Submit one test form and one test enquiry","Pages can load while forms fail."),
 ("Place a test order if you sell online",""),
 ("Check the browser console and the PHP error log","Server errors and fatal errors are the clearest signs."),
 ("Check that your tracking still fires","Open Tag Manager preview or your analytics real-time view."),
]),
("4. If something broke",[
 ("Restore the previous version of that plugin first","Do not change three things at once."),
 ("Write down the plugin, the two versions and the error",""),
 ("Tell the plugin author with those details",""),
 ("Hold that version until a fix ships","Do not let auto-updates install it again."),
]),
("5. Set it up so you hear about it",[
 ("Send error alerts to an email you read",""),
 ("Test the alert once",""),
 ("Review the update history once a month",""),
])],
'Backstep Updates saves a copy before every plugin update, checks your site after, and restores the old version if it breaks. Free. <a href="https://backstep.iamknr.in/">backstep.iamknr.in</a> · Guide: <a href="https://iamknr.in/blog/backstep-updates-wordpress-plugin-rollback/">iamknr.in/blog</a>',
"A working checklist, not a guarantee. A site can break in ways a quick check will not see. Keep real backups.")

DOCS['desktop-buddy-weekly-setup-sheet.pdf']=build(
"Desktop Buddy Weekly Setup Sheet",
"Fill this in once. It turns a desktop buddy such as Shika AI into a small system that keeps you on your tasks, and shows which jobs you could hand to an AI agent later.",
[("1. Your repeat jobs (write them in the lines below)",[
 ("List ten things you do every week","Reports, replies, checks, notes, follow-ups, invoices."),
 ("Mark each as: talk, remind, or hand off","Talk = you could say it out loud. Remind = you only forget it. Hand off = a tool could do the steps."),
 LINES,
]),
("2. Talk jobs (voice typing)",[
 ("Pick three writing jobs you can say out loud","Emails, client notes, first drafts of reports."),
 ("Say the draft, then edit it once","Speaking is fast. Editing is where the quality comes from."),
 ("Keep private material on a tool that runs on your own machine","Shika runs speech to text and cleanup with local models."),
]),
("3. Remind jobs",[
 ("Set three daily reminders","For example: check ad accounts, answer leads, plan tomorrow."),
 ("Set one weekly reminder for the job you keep skipping",""),
 ("Put one sticky note on the screen for the single most important task today",""),
]),
("4. Focus",[
 ("Run one focus timer block before noon","Start with 25 minutes. Make it longer only if it works."),
 ("Close chat and mail during the block",""),
 ("Write down what you finished when the timer ends",""),
]),
("5. Weekly review (Friday, 15 minutes)",[
 ("Which reminders did I ignore, and why?","Remove or move them."),
 ("Which job took the longest?","That is the first one to look at for automation."),
 ("Which job had clear steps and no judgement?","That is a good first job for an AI agent. Start in draft mode and approve each result."),
])],
'Shika AI is a free, open source desktop buddy with voice typing, reminders, tasks, sticky notes and a focus timer for Linux, macOS and Windows. <a href="https://iam-knr.github.io/desktop-buddy/">Get Shika AI</a> · Guide: <a href="https://iamknr.in/blog/shika-ai-desktop-buddy-hobby-project/">iamknr.in/blog</a>',
"A simple weekly routine. Use any tool you like with it.")

if __name__=='__main__':
    os.makedirs('downloads',exist_ok=True)
    with sync_playwright() as p:
        b=p.chromium.launch();pg=b.new_page()
        for name,doc in DOCS.items():
            pg.set_content(doc);pg.pdf(path='downloads/'+name,format='A4',print_background=True)
            print(name)
        b.close()
