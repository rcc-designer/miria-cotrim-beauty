from pathlib import Path
import sys,subprocess
sys.path.insert(0,str(Path(__file__).parent/'.tools'))
import imageio_ffmpeg
ff=imageio_ffmpeg.get_ffmpeg_exe();root=Path(__file__).parent
for variant,crf,rate in [('desktop','26','3200k'),('mobile','27','1600k')]:
    source=root/'dist/video'/f'hero-{variant}.mp4';target=source.with_name(f'optimized-{variant}.mp4')
    p=subprocess.run([ff,'-hide_banner','-loglevel','error','-y','-i',str(source),'-an','-c:v','libx264','-preset','medium','-crf',crf,'-maxrate',rate,'-bufsize','6400k','-movflags','+faststart',str(target)],capture_output=True,text=True)
    if p.returncode:raise RuntimeError(p.stderr)
    target.replace(source);print(variant,source.stat().st_size,flush=True)
from PIL import Image,ImageDraw
sheet=Image.new('RGB',(1000,600))
for i,sec in enumerate([1,6,10,14,18]):
    frame=root/'video-source'/f'final-{i}.jpg'
    subprocess.run([ff,'-hide_banner','-loglevel','error','-y','-ss',str(sec),'-i',str(root/'dist/video/hero-desktop.mp4'),'-frames:v','1','-vf','scale=500:-1',str(frame)],check=True)
    im=Image.open(frame);sheet.paste(im,((i%2)*500,(i//2)*200));ImageDraw.Draw(sheet).text(((i%2)*500+10,(i//2)*200+10),str(sec)+'s',fill='white')
sheet.save(root/'video-source/montage-check.jpg')
