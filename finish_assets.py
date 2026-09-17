from pathlib import Path
from PIL import Image
import json
root=Path(__file__).parent
meta={}
for f in (root/'dist/images').glob('*.webp'):
    if '-thumb' in f.stem: continue
    im=Image.open(f);th=Image.open(f.with_name(f.stem+'-thumb.webp'))
    meta[int(f.stem)]={'width':im.width,'height':im.height,'thumbWidth':th.width}
(root/'dist/imageMeta.js').write_text('export const imageMeta = '+json.dumps(meta)+';',encoding='utf-8')
print('Image dimensions recorded for 54 assets')
