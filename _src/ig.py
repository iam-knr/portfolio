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
