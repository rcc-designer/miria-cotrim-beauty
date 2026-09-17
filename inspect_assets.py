from PIL import Image, ImageOps, ImageDraw
from pathlib import Path
import zipfile,json
root=Path(__file__).parent
source=Path(r'C:\Users\romir\OneDrive\Documentos\Miria Bridal Beauty')
with zipfile.ZipFile(next(source.glob('*.zip'))) as z:
    names=[n for n in z.namelist() if n.lower().endswith(('.jpg','.jpeg','.png','.webp'))]
    images=[]
    for i,n in enumerate(names):
        import io
        im=ImageOps.exif_transpose(Image.open(io.BytesIO(z.read(n)))).convert('RGB')
        images.append((i,n,im.copy()))
        im.thumbnail((1600,1800));im.save(root/'dist/images'/f'{i:02}.webp',quality=86)
        im.thumbnail((620,820));im.save(root/'dist/images'/f'{i:02}-thumb.webp',quality=82)
    for batch in range((len(images)+19)//20):
        sheet=Image.new('RGB',(1000,1200),'#eee8e0');draw=ImageDraw.Draw(sheet)
        for k,(i,n,im) in enumerate(images[batch*20:batch*20+20]):
            im.thumbnail((190,255));x=(k%5)*200;y=(k//5)*300
            sheet.paste(im,(x+(200-im.width)//2,y));draw.text((x+8,y+266),f'{i:02}  {images[i][2].size}',fill='black')
        sheet.save(root/f'contact-sheet-{batch}.jpg')
    (root/'asset-manifest.json').write_text(json.dumps([{'id':i,'source':n,'size':im.size} for i,n,im in images],indent=2))
    print(f'{len(images)} images extracted, optimized and indexed')
