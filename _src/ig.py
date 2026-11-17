import html
W=560
INK="#151210";RED="#d81e16";CARD="#f5f2ec";MUTE="#5f584e"
def esc(s):return html.escape(s)
def wrap(h,title,desc,body):
    return f'<svg viewBox="0 0 {W} {h}" role="img" aria-labelledby="igt igd" xmlns="http://www.w3.org/2000/svg" font-family="Archivo,Arial,sans-serif"><title id="igt">{esc(title)}</title><desc id="igd">{esc(desc)}</desc><rect width="{W}" height="{h}" fill="{CARD}"/><rect x="1" y="1" width="{W-2}" height="{h-2}" fill="none" stroke="{INK}" stroke-width="2"/>{body}</svg>'
def head(t,sub=""):
    s=f'<text x="28" y="44" font-size="25" font-weight="800" fill="{INK}">{esc(t)}</text>'
    if sub:s+=f'<text x="28" y="68" font-size="15" fill="{MUTE}">{esc(sub)}</text>'
    return s+f'<rect x="28" y="80" width="56" height="5" fill="{RED}"/>'
def foot(h):
    return f'<text x="{W-24}" y="{h-14}" font-size="13" text-anchor="end" fill="{MUTE}">iamknr.in</text>'
def tx(x,y,s,size=17,w=400,fill=INK,anchor="start"):
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{w}" fill="{fill}" text-anchor="{anchor}">{esc(s)}</text>'
def arrow(x,y1,y2):
    return f'<path d="M{x} {y1} V{y2-7}" stroke="{INK}" stroke-width="2.5" fill="none"/><path d="M{x-7} {y2-9} L{x} {y2} L{x+7} {y2-9}" fill="{INK}"/>'
def steps(title,sub,rows,hl_last=False,numbered=True,cap_arrow=True,gap=14,rowh=66):
    y=104;out=head(title,sub)
    for i,(a,b) in enumerate(rows):
        last=(i==len(rows)-1 and hl_last)
        fill=INK if last else "#fff";tc="#fff" if last else INK;sc="#ffb4ae" if last else MUTE
        out+=f'<rect x="28" y="{y}" width="{W-56}" height="{rowh}" fill="{fill}" stroke="{INK}" stroke-width="2"/>'
        if numbered:
            out+=f'<rect x="28" y="{y}" width="52" height="{rowh}" fill="{RED}"/>'+tx(54,y+rowh/2+9,str(i+1),26,800,"#fff","middle")
            x0=96
        else:x0=44
        out+=tx(x0,y+27,a,19,800,tc)+tx(x0,y+50,b,15,400,sc)
        y+=rowh
        if i<len(rows)-1:
            out+=arrow(W/2,y,y+gap) if cap_arrow else ''
            y+=gap
    h=y+44
    return wrap(h,title,sub+". "+"; ".join(a for a,_ in rows)+".",out+foot(h))
IGS={}
# 1 loop
def loop():
    rows=[("Goal","You set the outcome, not the steps"),("Plan","The model picks the next step"),("Act","It calls a tool: ads, CRM, search, email"),("Observe","It reads the result and stores what matters"),("Report or ask","Goal met, or a human is needed")]
    y=104;o=head("The agentic AI loop","What happens after you give a goal")
    ys=[]
    for i,(a,b) in enumerate(rows):
        last=i==4
        o+=f'<rect x="28" y="{y}" width="430" height="62" fill="{INK if last else "#fff"}" stroke="{INK}" stroke-width="2"/><rect x="28" y="{y}" width="48" height="62" fill="{RED}"/>'+tx(52,y+40,str(i+1),24,800,"#fff","middle")+tx(90,y+26,a,19,800,"#fff" if last else INK)+tx(90,y+48,b,14.5,400,"#ffb4ae" if last else MUTE)
        ys.append(y)
        y+=62
        if i<4:o+=arrow(243,y,y+14);y+=14
    # return path from Observe (4th) to Plan (2nd)
    y4=ys[3]+31;y2=ys[1]+31
    o+=f'<path d="M458 {y4} H520 V{y2} H466" stroke="{RED}" stroke-width="3" fill="none"/><path d="M468 {y2-7} L458 {y2} L468 {y2+7}" fill="{RED}"/>'
    o+=f'<text transform="translate(540,{(y4+y2)/2}) rotate(90)" font-size="14" font-weight="700" fill="{RED}" text-anchor="middle">repeat until done</text>'
    h=y+44
    return wrap(h,"The agentic AI loop","Five steps: goal, plan, act, observe, report or ask. Steps two to four repeat until the goal is met.",o+foot(h))
IGS['what-is-agentic-ai']=("Infographic: the agentic AI loop. The model repeats plan, act and observe until the goal is met.",loop())
# 2 ladder
def ladder():
    rows=[("Generative AI","You decide every step",1),("AI assistant","You decide every step",1),("AI agent","Model decides, inside one task",2),("Agentic system","System plans; you set limits and approvals",3)]
    o=head("Who decides the next step?","Autonomy rises as you go down");y=104
    for a,b,n in rows:
        o+=tx(28,y+20,a,18,800)+tx(28,y+42,b,14.5,400,MUTE)
        o+=f'<rect x="28" y="{y+52}" width="{W-56}" height="14" fill="#e3ddd2"/><rect x="28" y="{y+52}" width="{(W-56)*n/3}" height="14" fill="{RED if n==3 else INK}"/>'
        y+=96
    o+=tx(28,y-8,"Bar = how much the software decides on its own",14,400,MUTE)
    h=y+40
    return wrap(h,"Who decides the next step","Generative AI and assistants: you decide. AI agent: the model decides inside a task. Agentic system: the system plans within your limits.",o+foot(h))
IGS['agentic-ai-in-marketing']=("Infographic: how much of the work the software decides, from generative AI to agentic systems.",ladder())
# 3 MCP
def mcp():
    o=head("How MCP connects AI to your tools","One standard, many tools")
    def b(y,t,s,dark=False,h=60):
        return f'<rect x="150" y="{y}" width="260" height="{h}" fill="{INK if dark else "#fff"}" stroke="{INK}" stroke-width="2"/>'+tx(280,y+26,t,19,800,"#fff" if dark else INK,"middle")+tx(280,y+47,s,14,400,"#ffb4ae" if dark else MUTE,"middle")
    o+=b(104,"Host","The AI app you work in")+arrow(280,164,190)+b(190,"MCP client","Inside the host, keeps the link")+arrow(280,250,276)+b(276,"MCP server","Lists what it can do",True)
    o+=arrow(280,336,364)
    for i,t in enumerate(["Ads","CRM","Analytics","Files"]):
        x=28+i*130
        o+=f'<rect x="{x}" y="364" width="116" height="44" fill="#fff" stroke="{INK}" stroke-width="2"/>'+tx(x+58,392,t,16,700,INK,"middle")
    o+=tx(28,444,"A server offers three things:",15,700)+tx(28,468,"Tools (actions)   Resources (data)   Prompts (templates)",15,400,MUTE)
    h=500
    return wrap(h,"How MCP connects AI to your tools","The AI app host uses a client to talk to an MCP server, which connects to tools such as ads, CRM, analytics and files. Servers offer tools, resources and prompts.",o+foot(h))
IGS['what-is-mcp-model-context-protocol']=("Infographic: host, client and server in the Model Context Protocol.",mcp())
# 4 n8n
def n8n():
    o=head("A lead response agent in n8n","Five nodes, one agent");y=104
    nodes=[("Trigger","New lead from form or Meta"),("CRM check","Duplicate? Existing customer?"),("AI Agent","Classifies intent, picks a reply"),("WhatsApp template","First reply within a minute"),("Notify sales","Owner gets the summary")]
    for i,(a,b) in enumerate(nodes):
        ag=i==2
        o+=f'<rect x="28" y="{y}" width="300" height="{80 if ag else 58}" rx="0" fill="{INK if ag else "#fff"}" stroke="{INK}" stroke-width="2"/>'+tx(44,y+26,a,18,800,"#fff" if ag else INK)+tx(44,y+47,b,14,400,"#ffb4ae" if ag else MUTE)
        if ag:
            for j,t in enumerate(["Chat model","Memory","Tool: CRM lookup"]):
                yy=y+j*30
                o+=f'<rect x="356" y="{yy}" width="176" height="24" fill="#fff" stroke="{RED}" stroke-width="2"/>'+tx(444,yy+17,t,13.5,700,INK,"middle")
            o+=f'<path d="M328 {y+40} H356" stroke="{RED}" stroke-width="2.5"/>'
            y+=80
        else:y+=58
        if i<4:o+=arrow(178,y,y+16);y+=16
    o+=tx(28,y+34,"Limit: max 8 steps. Draft mode first, approval before sending.",14,600,RED)
    h=y+64
    return wrap(h,"A lead response agent in n8n","Trigger, CRM check, AI agent with chat model, memory and CRM lookup tool, WhatsApp template, notify sales. Step limit of 8 and approval before sending.",o+foot(h))
IGS['n8n-ai-agents-marketing-automation']=("Infographic: a lead response agent built from five n8n nodes.",n8n())
# 5 three kinds
def kinds():
    o=head("Three kinds of AI in marketing","Predict, create, act");y=104
    for a,b,c in [("Predicts","Estimates what will happen","Bidding, lead scores, churn"),("Creates","Makes content from a prompt","Ad copy, images, email text"),("Acts","Plans and runs multi-step tasks","Audits, lead follow up, reports")]:
        last=a=="Acts"
        o+=f'<rect x="28" y="{y}" width="{W-56}" height="86" fill="{INK if last else "#fff"}" stroke="{INK}" stroke-width="2"/><rect x="28" y="{y}" width="8" height="86" fill="{RED}"/>'+tx(52,y+30,a,22,800,"#fff" if last else INK)+tx(52,y+54,b,15.5,400,"#fff" if last else INK)+tx(52,y+75,"e.g. "+c,14,400,"#ffb4ae" if last else MUTE)
        y+=86+16
    h=y+34
    return wrap(h,"Three kinds of AI in marketing","Predictive AI estimates outcomes, generative AI creates content, agentic AI plans and runs multi-step tasks.",o+foot(h))
IGS['ai-in-marketing']=("Infographic: predictive, generative and agentic AI in marketing.",kinds())
# 6 week
IGS['ai-in-advertising-meta-google-ads']=("Infographic: a weekly AI-assisted ads routine.",steps("A weekly AI-assisted ads routine","Agents draft, people decide",[("Mon: Audit","Agent posts a ranked list of issues"),("Mon: Clean up","You approve negatives, pause waste"),("Tue: Creative","Agent drafts angles; you pick and launch"),("Wed: Landing pages","Check speed, forms, message match"),("Fri: Report","Plain note; you add the decisions")],numbered=False,rowh=62))
# 7 seven steps
IGS['ai-landing-page-development']=("Infographic: seven steps to build and test a landing page with AI.",steps("Landing page in 7 steps","From promise to proven page",[("Define","Visitor, promise, one sentence"),("Gather","Reviews, questions, objections"),("Outline","Headline, proof, how it works, FAQ"),("Write","Three angles, edit into one voice"),("Build","Clean single file page, reviewed"),("Test","Real phone, form, tracking"),("Learn","One change at a time, log it")],rowh=56,gap=10))
# 8 consultant
IGS['best-agentic-ai-consultant-in-india']=("Infographic: six checks before hiring an agentic AI consultant.",steps("Six checks before you hire","Any miss means keep looking",[("Live agent shown","A running system, not slides"),("A failure story","What broke and how it was fixed"),("Limits and approvals","Step caps, spend caps, human sign off"),("Data handling written","Where data goes, DPDP Act aware"),("Paid pilot, 2 to 4 weeks","One task, one success number"),("You own the build","Workflows, prompts, documents")],hl_last=False,rowh=58,gap=10))
# 9 timeline
IGS['best-digital-marketing-consultant-in-india']=("Infographic: what a good first 90 days with a consultant looks like.",steps("A good first 90 days","What you should see and when",[("Days 1 to 14","Audit, tracking fixed, goal and budget agreed"),("Days 15 to 45","Campaigns and pages live, first learning report"),("Days 46 to 90","Cost per qualified lead falling, reasons written")],hl_last=True,numbered=False,rowh=70,gap=16))

# ---- extra diagram helpers (v2) ----
FIGS={}
def compare(title,sub,lt,rt,rows,rowh=58):
    h0=104;out=head(title,sub)
    cw=(W-56-12)/2
    out+=f'<rect x="28" y="{h0}" width="{cw}" height="40" fill="{INK}"/>'+tx(28+cw/2,h0+27,lt,17,800,"#fff","middle")
    out+=f'<rect x="{28+cw+12}" y="{h0}" width="{cw}" height="40" fill="{RED}"/>'+tx(28+cw+12+cw/2,h0+27,rt,17,800,"#fff","middle")
    y=h0+40
    for a,b in rows:
        out+=f'<rect x="28" y="{y}" width="{cw}" height="{rowh}" fill="#fff" stroke="{INK}" stroke-width="2"/><rect x="{28+cw+12}" y="{y}" width="{cw}" height="{rowh}" fill="#fff" stroke="{INK}" stroke-width="2"/>'
        out+=wraptext(28+12,y+24,a,cw-24,15)+wraptext(28+cw+12+12,y+24,b,cw-24,15)
        y+=rowh
    h=y+44
    return wrap(h,title,sub+". "+lt+" versus "+rt+".",out+foot(h))
def wraptext(x,y,s,width,size=15,lh=20):
    words=s.split();lines=[];cur=""
    mx=int(width/(size*0.52))
    for w in words:
        if len(cur)+len(w)+1<=mx:cur=(cur+" "+w).strip()
        else:lines.append(cur);cur=w
    lines.append(cur)
    return ''.join(tx(x,y+i*lh,l,size,400,INK) for i,l in enumerate(lines))
def checklist(title,sub,items,rowh=44):
    y=104;out=head(title,sub)
    for it in items:
        out+=f'<rect x="28" y="{y}" width="{W-56}" height="{rowh}" fill="#fff" stroke="{INK}" stroke-width="2"/><rect x="42" y="{y+rowh/2-11}" width="22" height="22" fill="none" stroke="{RED}" stroke-width="3"/><path d="M47 {y+rowh/2} l5 6 l9 -12" stroke="{RED}" stroke-width="3" fill="none"/>'
        out+=wraptext(78,y+rowh/2+5,it,W-56-64,15) if len(it)<=52 else wraptext(78,y+17,it,W-56-64,15,18)
        y+=rowh
    h=y+44
    return wrap(h,title,sub+". "+"; ".join(items)+".",out+foot(h))
def stages(title,sub,cols,rows,rowh=50):
    # header columns with rows of label/value: a simple timeline table
    y=104;out=head(title,sub);n=len(cols);cw=(W-56)/n
    for i,c in enumerate(cols):
        out+=f'<rect x="{28+i*cw}" y="{y}" width="{cw}" height="40" fill="{INK if i%2==0 else RED}"/>'+tx(28+i*cw+cw/2,y+26,c,16,800,"#fff","middle")
    y+=40
    for r in rows:
        for i,c in enumerate(r):
            out+=f'<rect x="{28+i*cw}" y="{y}" width="{cw}" height="{rowh}" fill="#fff" stroke="{INK}" stroke-width="2"/>'+wraptext(28+i*cw+10,y+22,c,cw-20,14,18)
        y+=rowh
    h=y+44
    return wrap(h,title,sub+". "+", ".join(cols)+".",out+foot(h))

FIGS['agentic-run']=("Diagram: one agent run, from goal to report, with every tool call logged.",steps("One agent run","Goal in, report out, nothing changed",[("Goal","Which campaigns overspent yesterday, and why?"),("Plan","Need costs and budgets, then a reason"),("Tool call 1","get_campaign_costs: C is at 142 percent"),("Tool calls 2 and 3","Budget unchanged; one broad keyword found"),("Report","Cause named with evidence; no changes made")],hl_last=True,numbered=False,rowh=60,gap=12))
FIGS['agentic-checklist']=("Checklist: eight questions to answer before an agent runs on real work.",checklist("Before you trust an agent","Answer yes to all eight",["The goal has a number and a time","Every tool is read-only unless writing is the point","There is a maximum step count","Spending and customer messages need approval","Every run writes to a log you can read","I checked 10 outputs against the source","An alert fires when a run fails","One person owns it and knows how to switch it off"]))

FIGS['agentic-mkt-score']=("Diagram: score each use case on four questions, then start with the highest total.",stages("Pick the first use case","Score 1 to 5 on each question",["Use case","Repeat","Clear","Safe","Data"],[["Reporting","5","5","5","4"],["Search terms","4","4","5","4"],["Lead follow up","5","3","2","4"],["Budget changes","3","3","1","3"]],rowh=46))
FIGS['agentic-lead-sop']=("Diagram: the lead response agent, from form submit to approved first reply.",steps("Lead response agent","Draft first, auto-send later",[("Lead arrives","Form or Meta lead form"),("Duplicate check","Match by phone and email"),("Classify intent","Label plus the supporting quote"),("Draft from template","Name and product filled in"),("Human approves","Auto-send only after 2 clean weeks")],hl_last=True,numbered=False,rowh=60,gap=12))
FIGS['mcp-sequence']=("Diagram: the order of messages when an assistant uses an MCP server.",steps("One MCP request","Who talks to whom, in order",[("1. Client asks the server","tools/list: what can you do?"),("2. Server replies","Tool names, descriptions, inputs"),("3. Model picks a tool","Writes arguments such as date = yesterday"),("4. Server runs it","Calls the real system with its own key"),("5. Model answers","Reads the result and replies in plain words")],numbered=False,rowh=60,gap=12))
FIGS['mcp-sop']=("Diagram: connect a first MCP server safely, from choosing the data to the 30 day review.",steps("First MCP connection","Read-only, limited, logged",[("Choose one read-only source","Reports folder or analytics"),("Check the server","Maker, code, last update, access asked"),("Limited key","Never an admin key"),("Test five real questions","Check each against the source"),("Approvals on, log it","Review in 30 days")],rowh=60,gap=12))
FIGS['mcp-checklist']=("Checklist: eight checks before you connect an MCP server to real data.",checklist("Server review","Eight checks before connecting",["I know who made it and can read the code","It asks only for the access the job needs","I made a limited, read-only key for it","Its tool list matches its documentation","Tool approvals are switched on","Results cannot trigger spending or deletion alone","I tested five questions I already know the answer to","It is written in my access log with a review date"]))
FIGS['n8n-lead-flow']=("Diagram: the lead response flow in n8n with an approval step and an error flow.",steps("Lead response in n8n","Eleven steps, one human click",[("Trigger and clean","Webhook; fix phone, email, case"),("Duplicate check","Search CRM; stop if found"),("AI Agent labels intent","Ready, researching or not a fit"),("CRM record and draft","Template, no invented offers"),("Approval in team chat","Approve or edit; then send")],hl_last=True,rowh=60,gap=12))
FIGS['n8n-selfhost']=("Checklist: eight tasks that keep a self-hosted n8n safe and running.",checklist("Self-hosting n8n","Eight jobs, done once, reviewed monthly",["Small server set up from the official docs","Domain with HTTPS for webhooks","Owner login locked down, no public sign up","Daily database and key backup","One restore test completed","Monthly update after reading release notes","Uptime alert to my phone","One page runbook written"]))

FIGS['aim-funnel']=("Diagram: where AI helps at each funnel stage, and what stays human.",stages("AI across the funnel","Help at each stage, judgment stays human",["Stage","AI helps with","You decide"],[["Awareness","Creative variants, briefs","Message, channel"],["Interest","Page checks, headline tests","Offer, proof"],["Decision","Lead scoring, reply drafts","Price, objections"],["Purchase","Reminders, call notes","Closing"],["Retention","Churn flags, review watch","Root cause"]],rowh=52))
FIGS['aim-pilot']=("Diagram: a 30 day AI pilot for a marketing team in four weekly steps.",steps("30 day AI pilot","Two tasks, measured, then a decision",[("Week 1: Audit and baseline","Time two tasks for two weeks; pick the two"),("Week 2: Rules and prompts","Data rules, saved prompts, approvals"),("Week 3: Run in parallel","Old way and new way side by side"),("Week 4: Decide","Adopt if a third faster with no quality drop")],hl_last=True,rowh=62,gap=12))
FIGS['ads-search-terms']=("Diagram: weekly search term review, where the agent proposes and a person applies.",steps("Search term review","20 minutes a week with an agent",[("Pull 7 days of terms","Cost, clicks, conversions, keyword"),("Filter waste","Spend over a limit, zero conversions"),("Agent groups by reason","Jobs, free, wrong product, competitor"),("Person removes real buyers","Check brand and long phrases"),("Apply and record","Log the waste found")],rowh=60,gap=12))
FIGS['ads-angle-test']=("Comparison: testing random wording versus testing angles.",compare("Test angles, not words","What you learn is reusable","Random wording","Angle testing",[("Change a few words, see a click rate","Test price, speed, trust, proof, urgency"),("Lesson: variant B won","Lesson: speed beat price for this audience"),("Judged by clicks","Judged by cost per qualified lead"),("Starts over next time","Next cycle begins from the best angle")],rowh=76))
FIGS['ads-health']=("Checklist: eight checks in a monthly ad account health review.",checklist("Monthly account check","Tracking first, everything else after",["Test conversion recorded once per platform","Platform numbers compared with the CRM","Campaigns merged where goals match","Budgets moved toward cost per qualified lead","Locations, languages and exclusions correct","No disapproved ads or silent ads","Landing pages checked on a phone","Top three fixes written with owners"]))
FIGS['lp-anatomy']=("Diagram: the order of blocks on a lead page, each with one job.",steps("Lead page anatomy","One job per block",[("Headline and main action","Repeat the ad promise; one button"),("Proof strip","Real logos, ratings with source"),("Three benefits","Outcome first, feature second"),("How it works","Three steps in plain words"),("Proof, FAQ, final action","Answer last doubts; repeat the button")],hl_last=True,numbered=False,rowh=60,gap=12))
FIGS['lp-launch']=("Diagram: the launch path for a landing page, from soft launch to scale.",steps("Landing page launch","Test the whole path before spending",[("Build and review the code","Forms, links, tracking, no extras"),("Track once","Conversion fires on the thank you page only"),("Test devices and lead path","Phone, form, CRM, reply, sales alert"),("Soft launch","Small budget; watch 24 hours"),("Scale","Raise spend after the path works")],rowh=60,gap=12))
FIGS['lp-speed']=("Checklist: eight fixes that make a landing page load faster on mobile.",checklist("Landing page speed","Fix images, scripts and fonts first",["Images resized to the size they display","Images compressed and in a modern format","Image width and height set in the page","Only the scripts the page needs","Tracking scripts loaded without blocking","One or two fonts, with a system fallback","Nothing large above the first screen except the headline","Tested on a mid range phone over mobile data"]))
FIGS['cons-select']=("Diagram: the steps to choose an agentic AI consultant, ending in a short paid pilot.",steps("Choosing a consultant","From problem to a short paid pilot",[("Write the problem and number","Not the tool; the result"),("Shortlist three types","Independent, studio, other"),("Same brief, same questions","Nine questions, notes in one sheet"),("Live demo and written proposal","Real data, real errors"),("Score, check references","Evidence over charm"),("Sign a 2 to 4 week pilot","Decide after the numbers")],hl_last=True,rowh=56,gap=10))
FIGS['cons-pilot']=("Timeline: a four week pilot, from access to a written decision.",stages("Four week pilot","One task, one number, one decision",["Week 1","Week 2","Week 3","Week 4"],[["Map the process. Design on paper","Build read-only. Test on old data","Draft mode with approvals. Log edits","Review numbers. Keep, widen or stop"],["You review the design","You compare with manual results","You approve drafts","You receive documents and training"]],rowh=96))
FIGS['dm-audit']=("Diagram: the order of a paid marketing audit, tracking first.",steps("A paid marketing audit","Tracking first, then the rest",[("Kickoff and access","Goals, margins, view access in your name"),("Tracking audit","Test conversions; compare with the CRM"),("Funnel, campaigns, pages","Find the biggest drop and the biggest waste"),("Follow up review","Reply time, scripts, CRM stages"),("Report and 30 day plan","Evidence, impact, effort, owner")],hl_last=True,rowh=60,gap=12))
FIGS['dm-review']=("Checklist: seven steps for a monthly review meeting with your consultant.",checklist("Monthly review","Forty five minutes, decisions in writing",["Read the one page summary before the call","Check cost per qualified lead against target","Ask for the cause in the data, not a guess","Review last month's actions and results","Pick one to three tests with a decision date","Agree budget changes with reasons","Send written notes the same day"]))
FIGS['dm-own']=("Checklist: what you should own when a consultant finishes.",checklist("What you should own","Good consultants leave you in control",["Ad accounts, analytics and domains in your name","All logins listed, shared securely","Reports, audits and the 90 day plan","Creative files and landing page code","Tracking setup notes and tag manager access","A recorded walkthrough and training session"]))
