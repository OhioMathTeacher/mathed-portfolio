#!/usr/bin/env python3
"""Build the site into docs/ (GitHub Pages-ready) and the decks into decks/.

  python3 build.py            # relative links between pages (for docs/ and Pages)
  python3 build.py --artifacts  # links point at the published claude.ai artifacts

Sources live in src/. Sample portfolios and template pages are generated;
src/index.html is the hand-authored program page.
"""
import os, sys, subprocess, shutil
ROOT=os.path.dirname(os.path.abspath(__file__)); SRC=os.path.join(ROOT,'src'); DOCS=os.path.join(ROOT,'docs')

ARTIFACTS={
  'index.html':'https://claude.ai/code/artifact/791b0115-1cad-48e7-8b23-456719abe06a',
  'samples/priya.html':'https://claude.ai/code/artifact/9cb26d5b-a1c0-4d7f-b6f3-07187fe283bf',
  'samples/marcus.html':'https://claude.ai/code/artifact/77dd8875-afb8-49b8-a0c6-9ca71961b753',
  'samples/jordan.html':'https://claude.ai/code/artifact/d52ab32e-ad4d-4dad-a26a-bc303a4f60a5',
  'templates/four-year-build.html':'https://claude.ai/code/artifact/fa41ad12-1e2e-4e5b-bdc1-caaca8ff354d',
  'templates/late-start.html':'https://claude.ai/code/artifact/238bda41-bd6d-4874-9ba0-9e0098110710',
  'templates/course-pilot.html':'https://claude.ai/code/artifact/d9afe63b-eebc-4eec-a2a3-f3f86d63fbad',
}
artifacts='--artifacts' in sys.argv
os.makedirs(os.path.join(DOCS,'samples'),exist_ok=True); os.makedirs(os.path.join(DOCS,'templates'),exist_ok=True)

env=dict(os.environ, PORTFOLIO_HOME=ARTIFACTS['index.html'] if artifacts else '../index.html')
for f in ('site_priya.py','site_marcus.py','site_jordan.py'):
    subprocess.run([sys.executable, os.path.join(SRC,f)], check=True, env=env, cwd=SRC, stdout=subprocess.DEVNULL)
subprocess.run([sys.executable, os.path.join(SRC,'render.py'), env['PORTFOLIO_HOME']], check=True, cwd=SRC)

# program page: swap artifact URLs for relative paths unless building for artifacts
html=open(os.path.join(SRC,'index.html')).read()
if not artifacts:
    for rel,url in ARTIFACTS.items():
        if rel!='index.html': html=html.replace(url, rel)
    html=html.replace('PowerPoint versions in Desktop/Portfolio','PowerPoint versions in decks/')
open(os.path.join(DOCS,'index.html'),'w').write(html)
print('built docs/ with', 'artifact' if artifacts else 'relative', 'links')
