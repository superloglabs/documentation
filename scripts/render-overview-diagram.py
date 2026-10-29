"""Generate the overview's editable SVG diagrams (standard library only)."""
from pathlib import Path
from html import escape
from base64 import b64encode

ROOT = Path(__file__).resolve().parents[1]
ICONS = {
 'web': '<rect x="3" y="4" width="22" height="18" rx="3"/><path d="M3 10h22M8 7h.1M12 7h.1"/>',
 'server': '<rect x="4" y="3" width="20" height="9" rx="2"/><rect x="4" y="16" width="20" height="9" rx="2"/><path d="M8 7.5h.1M8 20.5h.1M14 7.5h6M14 20.5h6"/>',
 'cloud': '<path d="M8 22a6 6 0 0 1-1-12 8 8 0 0 1 15-1 6.5 6.5 0 0 1 0 13Z"/>',
 'chart': '<path d="M4 4v20h21M9 19v-6M15 19V7M21 19V11"/>',
 'bell': '<path d="M7 11a7 7 0 0 1 14 0c0 8 3 8 3 10H4c0-2 3-2 3-10ZM11 25h6"/>',
 'error': '<path d="m14 3 11 6v12l-11 6-11-6V9Z M14 9v8M14 21h.1"/>',
 'pulse': '<path d="M2 14h6l4-9 5 18 4-9h5"/>',
 'agent': '<path d="m10 7-7 7 7 7M18 7l7 7-7 7M16 4l-4 20"/>',
 'message': '<path d="M5 4h18a2 2 0 0 1 2 2v13a2 2 0 0 1-2 2H12l-7 5v-5a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2ZM8 10h12M8 15h8"/>',
}

def render(dark=False):
 c = dict(bg='#090909',card='#171717',text='#f2f2f0',muted='#b7b7b2',border='#292929',line='#796ba9',dot='#292929',accent='#d2d2d0',tint='#202020',white='#202020',soft='#111111') if dark else dict(bg='#fcfcfc',card='#ffffff',text='#202020',muted='#767676',border='#eeeeee',line='#b5a9df',dot='#eeeeee',accent='#646464',tint='#f5f5f5',white='#ffffff',soft='#f9f9f9')
 p = ['<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="840" viewBox="0 0 1200 840" role="img" aria-labelledby="title desc">', '<title id="title">How Superlog works</title>', '<desc id="desc">Web apps send logs and traces through the browser SDK. Backend services send logs, traces and metrics through OpenTelemetry. Cloud integrations send logs and metrics. Superlog stores telemetry for dashboards, alerts, error issues and agent access. Synthetic checks send requests to web apps and backend services. Alerts, errors and failing checks notify Slack.</desc>', f'''<defs>
 <pattern id="dots" width="12" height="12" patternUnits="userSpaceOnUse"><circle cx="6" cy="6" r="0.7" fill="{c['dot']}"/></pattern>
 <radialGradient id="fade"><stop offset="0" stop-color="white"/><stop offset="0.7" stop-color="white" stop-opacity=".65"/><stop offset="1" stop-color="white" stop-opacity="0"/></radialGradient>
 <mask id="grid-fade"><rect width="1200" height="840" fill="url(#fade)"/></mask>
 <linearGradient id="surface" x2="0" y2="1"><stop stop-color="{c['white']}"/><stop offset="1" stop-color="{c['soft']}"/></linearGradient>
 <linearGradient id="icon" x2="0" y2="1"><stop stop-color="{c['white']}"/><stop offset="1" stop-color="{c['tint']}"/></linearGradient>
 <filter id="shadow" x="-40%" y="-40%" width="180%" height="220%"><feDropShadow dx="0" dy="6" stdDeviation="8" flood-color="#000000" flood-opacity=".025"/><feDropShadow dx="0" dy="3" stdDeviation="3" flood-color="#000000" flood-opacity=".04"/></filter>
 <filter id="icon-shadow" x="-50%" y="-50%" width="200%" height="220%"><feDropShadow dx="0" dy="3" stdDeviation="3" flood-color="#000000" flood-opacity=".06"/></filter>
 </defs>''',f'<rect width="1200" height="840" fill="{c["bg"]}"/>',f'<g fill="none" stroke="{c["line"]}" stroke-width="1.2" opacity=".22"><circle cx="600" cy="400" r="200"/><circle cx="600" cy="400" r="246"/><circle cx="600" cy="400" r="292" opacity=".5"/></g>','<g font-family="Inter, -apple-system, BlinkMacSystemFont, Segoe UI, Arial, sans-serif">']
 def text(x,y,s,size=18,color='text',weight=400,anchor='start'):
  p.append(f'<text x="{x}" y="{y}" fill="{c[color]}" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}">{escape(s)}</text>')
 def line(d,dashed=False):
  p.append(f'<path d="{d}" fill="none" stroke="{c["line"]}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"'+(' stroke-dasharray="4 6"' if dashed else '')+'/>')
 def port(x,y):
  p.append(f'<circle cx="{x}" cy="{y}" r="6" fill="{c["bg"]}"/><circle cx="{x}" cy="{y}" r="3.5" fill="{c["line"]}"/>')
 def icon(x,y,key,size=44):
  p.append(f'<rect x="{x}" y="{y}" width="{size}" height="{size}" rx="{size/2}" fill="{c["card"]}" stroke="{c["border"]}" filter="url(#icon-shadow)"/><g transform="translate({x+(size-28)/2} {y+(size-28)/2})" fill="none" stroke="{c["accent"]}" stroke-width="1.55" stroke-linecap="round" stroke-linejoin="round">{ICONS[key]}</g>')
 def card(x,y,title,subtitle,key):
  p.append(f'<rect x="{x}" y="{y}" width="288" height="96" rx="13" fill="{c["card"]}" stroke="{c["border"]}" filter="url(#shadow)"/>')
  icon(x+17,y+23,key);text(x+76,y+40,title,20);text(x+76,y+65,subtitle,14,'muted')
 # Fine shared rails, with visible ports rather than a tangle of arrows.
 line('M344 232 H374 Q400 232 400 258 V358 Q400 384 426 384 H456')
 line('M344 384 H456')
 line('M344 536 H374 Q400 536 400 510 V410 Q400 384 426 384 H456')
 line('M744 384 H774 Q800 384 800 358 V258 Q800 232 826 232 H856')
 line('M744 384 H856')
 line('M744 384 H774 Q800 384 800 410 V510 Q800 536 826 536 H856')
 line('M600 548 V680')
 line('M56 728 H48 Q28 728 28 708 V252 Q28 232 48 232 H56',True)
 line('M28 404 Q28 384 48 384 H56',True)
 line('M1144 384 H1152 Q1172 384 1172 404 V708 Q1172 728 1152 728 H1144')
 line('M1144 536 H1172')
 line('M200 776 V790 Q200 812 222 812 H978 Q1000 812 1000 790 V776',True)
 # Quiet column labels align with the cards.
 text(200,139,'Your stack',17,'muted',anchor='middle')
 text(600,139,'Collect & connect',17,'muted',anchor='middle')
 text(1000,139,'Understand & act',17,'muted',anchor='middle')
 card(56,184,'Web app','Superlog browser SDK','web')
 card(56,336,'Backend services','OpenTelemetry SDKs','server')
 card(56,488,'Cloud infrastructure','Vercel · AWS · Google Cloud','cloud')
 card(856,184,'Dashboards','Explore logs, traces & metrics','chart')
 card(856,336,'Alerts','Detect threshold crossings','bell')
 card(856,488,'Error issues','Group matching exceptions','error')
 # A subtly layered central tile is the visual anchor.
 p.append(f'<rect x="466" y="264" width="268" height="292" rx="27" fill="{c["soft"]}" stroke="{c["border"]}"/>')
 p.append(f'<rect x="456" y="252" width="288" height="296" rx="25" fill="url(#surface)" stroke="{c["border"]}" filter="url(#shadow)"/>')
 p.append(f'<rect x="464" y="260" width="272" height="280" rx="19" fill="none" stroke="{c["white"]}"/>')
 p.append(f'<circle cx="600" cy="310" r="33" fill="{c["card"]}" stroke="{c["border"]}" filter="url(#icon-shadow)"/><g transform="translate(580 290) scale(0.1142857)" fill="{c["text"]}"><rect x="172.464" y="172.464" width="96.3768" height="96.3768"/><rect y="81.1594" width="81.1594" height="187.681"/><rect x="268.841" y="81.1594" width="81.1594" height="187.681"/><rect x="81.16" width="187.681" height="81.1594"/><rect x="81.16" y="268.841" width="187.681" height="81.1594"/></g>')
 text(600,377,'Superlog',28,'text',500,'middle')
 text(600,405,'Your telemetry, together',16,'muted',anchor='middle')
 for x,label,key in [(508,'Logs','server'),(578,'Traces','pulse'),(648,'Metrics','chart')]:
  icon(x,433,key,44);text(x+22,502,label,14,'muted',anchor='middle')
 card(56,680,'Synthetic checks','Check endpoint availability','pulse')
 card(456,680,'Agents','MCP server & automations','agent')
 card(856,680,'Slack','Notifications & recoveries','message')
 for x,y in [(344,232),(344,384),(344,536),(456,384),(744,384),(856,232),(856,384),(856,536),(600,548),(600,680),(56,232),(56,384),(56,728),(1144,384),(1144,536),(1144,728),(200,776),(1000,776)]: port(x,y)
 p.append(f'<rect x="501" y="600" width="198" height="28" rx="14" fill="{c["bg"]}" stroke="{c["border"]}"/>');text(600,619,'Read the same telemetry',13,'muted',anchor='middle')
 p.append(f'<rect x="493" y="799" width="214" height="27" rx="13" fill="{c["bg"]}"/>');text(600,818,'Failing check notifications',13,'muted',anchor='middle')
 fonts = []
 for weight in [400, 500]:
  data = b64encode((ROOT/'images'/'fonts'/f'inter-latin-{weight}-normal.woff2').read_bytes()).decode()
  fonts.append(f"@font-face{{font-family:Inter;font-style:normal;font-weight:{weight};src:url(data:font/woff2;base64,{data}) format('woff2');}}")
 p.insert(1, '<style>'+''.join(fonts)+'</style>')
 p.append('</g></svg>')
 return '\n'.join(p)+'\n'

for dark in [False,True]:
 (ROOT/'images'/f'how-superlog-works{"-dark" if dark else ""}.svg').write_text(render(dark))
