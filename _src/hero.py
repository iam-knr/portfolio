import html,math
INK="#151210";RED="#d81e16";PAPER="#ebe7df";YEL="#ffd84a"
F="font-family=\"Arial,Helvetica,'Liberation Sans',sans-serif\""
def e(s):return html.escape(s)
CFG={
'what-is-agentic-ai':(["What is","agentic AI?"],"A goal, a plan, tools and a loop.","Agent",["Goal","Plan","Tools","Memory","Check"],("You set the goal","It runs the steps"),"An AI agent in the centre with goal, plan, tools, memory and check orbiting it."),
'agentic-ai-in-marketing':(["Agentic AI","in marketing"],"Agents do the repeat work. You approve.","Agent",["Ads","CRM","SEO","Email","Reports"],("Agent proposes","You approve"),"An AI agent in the centre with ads, CRM, SEO, email and reports tools orbiting it."),
'what-is-mcp-model-context-protocol':(["What is MCP?"],"One standard for AI to reach your tools.","MCP",["Ads","CRM","Files","Analytics","Docs"],("Client asks","Server answers"),"An MCP hub in the centre connecting ads, CRM, files, analytics and docs."),
'n8n-ai-agents-marketing-automation':(["n8n AI agents","for marketing"],"Workflows that think. Steps you can see.","n8n",["Trigger","Agent","CRM","WhatsApp","Sheet"],("Self-host it","See every step"),"An n8n workflow hub connecting trigger, agent, CRM, WhatsApp and sheet nodes."),
'ai-in-marketing':(["AI in","marketing"],"Predict. Create. Act.","AI",["Predict","Create","Act","Test","Report"],("Check every claim","Keep the taste human"),"AI at the centre with predict, create, act, test and report around it."),
'ai-in-advertising-meta-google-ads':(["AI in","advertising"],"Meta and Google Ads, with limits.","Ads",["Meta","Google","Audit","Creative","Reports"],("Agent drafts","You approve spend"),"An ads hub with Meta, Google, audit, creative and reports around it."),
'ai-landing-page-development':(["AI landing","pages"],"Build fast. Test one thing at a time.","Page",["Offer","Proof","Speed","Form","Tracking"],("Match the ad","Test on a phone"),"A landing page hub with offer, proof, speed, form and tracking around it."),
'best-agentic-ai-consultant-in-india':(["Best agentic AI","consultant","in India"],"Six checks before you hire.","Hire",["Live demo","Limits","Pilot","Data","Ownership"],("Ask for proof","Start small"),"A hire decision hub with live demo, limits, pilot, data and ownership checks."),
'best-digital-marketing-consultant-in-india':(["Best digital","marketing consultant","in India"],"What to ask and what to expect.","Fit",["Audit","Tracking","Ads","Funnel","Reports"],("Verify results","Paid trial first"),"A consultant fit hub with audit, tracking, ads, funnel and reports around it."),
}
CFG['agentic-ai-vs-ai-agents-vs-generative-ai']=(["Agentic AI vs","AI agents vs","generative AI"],"Which one does your business need first?","AI",["Generate","Agent","Agentic","Rules","Approve"],("Start small","Add limits"),"A hub comparing generative AI, AI agents and agentic AI, with rules and approvals.")
CFG['agentic-ai-for-indian-smes-automation-guide']=(["Agentic AI for","Indian SMEs"],"One workflow. 30 days. Real numbers.","SME",["Leads","Reports","Quotes","Support","Payments"],("Draft mode first","Measure payback"),"An SME hub with leads, reports, quotes, support and payments workflows around it.")

CFG['shika-ai-desktop-buddy-hobby-project']=(["Shika AI,","the desktop","buddy"],"Voice typing that stays on your machine.","Buddy",["Talk","Remind","Tasks","Notes","Focus"],("Free and open source","Runs locally"),"A desktop buddy hub with talk, remind, tasks, notes and focus around it.")
CFG['adcheck-meta-ad-rejection-checker-chrome-extension']=(["AdCheck for","Meta ads"],"Catch the rejection before you publish.","Check",["Copy","Creative","Policy","Fix","India"],("Hover for the reason","A person publishes"),"An ad check hub with copy, creative, policy, fix and India rules around it.")
CFG['programmatic-seo-wordpress-plugin-big-seo-programmatic']=(["Programmatic SEO","on WordPress"],"Many pages. Each one worth reading.","pSEO",["Data","Template","Unique","Links","Launch"],("40% unique text","Launch in batches"),"A programmatic SEO hub with data, template, unique text, links and launch around it.")
CFG['safestep-updates-wordpress-plugin-rollback']=(["SafeStep","Updates"],"Snapshot. Check. Roll back if it breaks.","Safe",["Snapshot","Install","Check","Roll back","Alert"],("Free plugin","Plugins only"),"A plugin update safety hub with snapshot, install, check, roll back and alert around it.")

def pill(x,y,t,fill="#fff",tc=INK):
    w=len(t)*13+34
    return f'<rect x="{x-w/2:.0f}" y="{y-20}" width="{w}" height="40" rx="20" fill="{fill}" stroke="{INK}" stroke-width="2"/><text x="{x}" y="{y+6}" font-size="18" font-weight="700" fill="{tc}" text-anchor="middle" {F}>{e(t)}</text>'
def svg(slug):
    lines,sub,hub,sats,cards,alt=CFG[slug]
    o=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 630" width="1200" height="630" role="img" aria-label="{e(alt)}">'
    o+=f'<defs><pattern id="g" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M40 0H0V40" fill="none" stroke="#fff" stroke-opacity=".06"/></pattern></defs>'
    o+=f'<rect width="1200" height="630" fill="{INK}"/><rect width="1200" height="630" fill="url(#g)"/>'
    o+=f'<circle cx="1130" cy="40" r="170" fill="{RED}" opacity=".9"/>'
    o+=f'<rect x="60" y="54" width="128" height="44" fill="#fff"/><text x="76" y="86" font-size="28" font-weight="900" fill="{INK}" {F}>K</text><rect x="101" y="60" width="34" height="32" fill="{RED}"/><text x="108" y="86" font-size="26" font-weight="900" fill="#fff" {F}>N</text><text x="143" y="86" font-size="28" font-weight="900" fill="{INK}" {F}>R</text>'
    o+=f'<text x="206" y="82" font-size="15" font-weight="700" letter-spacing="2" fill="#bdb6aa" {F}>AGENTIC AI CONSULTANT, INDIA</text>'
    n=len(lines);size=66 if max(len(l) for l in lines)<=16 else 58
    y0=290-(n-1)*size*0.5
    for i,l in enumerate(lines):
        o+=f'<text x="60" y="{y0+i*size*1.08:.0f}" font-size="{size}" font-weight="900" fill="#fff" {F}>{e(l)}</text>'
    yb=y0+(n-1)*size*1.08
    o+=f'<rect x="60" y="{yb+22:.0f}" width="70" height="7" fill="{RED}"/>'
    # sub wrap
    words=sub.split();ln=[];cur=''
    for w in words:
        if len(cur+' '+w)>34 and cur:ln.append(cur);cur=w
        else:cur=(cur+' '+w).strip()
    ln.append(cur)
    for i,l in enumerate(ln):
        o+=f'<text x="60" y="{yb+68+i*34:.0f}" font-size="26" fill="{YEL}" {F}>{e(l)}</text>'
    # diagram
    cx,cy,r=900,300,175
    o+=f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="#fff" stroke-opacity=".35" stroke-width="2" stroke-dasharray="3 9" stroke-linecap="round"/>'
    pts=[]
    for i in range(5):
        a=math.radians(-90+i*72);pts.append((cx+r*math.cos(a),cy+r*math.sin(a)))
    for x,y in pts:o+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="#fff" stroke-opacity=".25" stroke-width="2"/>'
    o+=f'<circle cx="{cx}" cy="{cy}" r="64" fill="{RED}" stroke="#fff" stroke-width="4"/><text x="{cx}" y="{cy+11}" font-size="{34 if len(hub)<6 else 24}" font-weight="900" fill="#fff" text-anchor="middle" {F}>{e(hub)}</text>'
    for (x,y),t in zip(pts,sats):o+=pill(round(x),round(y),t,YEL if t==sats[0] else "#fff")
    # cards
    o+=f'<rect x="640" y="534" width="250" height="56" fill="#fff" stroke="{INK}" stroke-width="2"/><text x="765" y="568" font-size="19" font-weight="800" fill="{INK}" text-anchor="middle" {F}>{e(cards[0])}</text>'
    o+=f'<rect x="920" y="534" width="250" height="56" fill="{RED}" stroke="#fff" stroke-width="2"/><text x="1045" y="568" font-size="19" font-weight="800" fill="#fff" text-anchor="middle" {F}>{e(cards[1])}</text>'
    o+=f'<text x="60" y="590" font-size="16" fill="#8f877a" {F}>iamknr.in/blog</text>'
    return o+'</svg>',alt
