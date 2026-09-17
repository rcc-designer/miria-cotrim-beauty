import urllib.request,sys
from pathlib import Path
root=Path(__file__).parent/'video-source'
root.mkdir(exist_ok=True)
url,name=sys.argv[1:3]
target=root/name
with urllib.request.urlopen(url,timeout=60) as r, target.open('wb') as f:
    while block:=r.read(1024*1024): f.write(block)
print(name, target.stat().st_size)
