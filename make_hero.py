from pathlib import Path
import sys,subprocess,json
sys.path.insert(0,str(Path(__file__).parent/'.tools'))
import imageio_ffmpeg
ff=imageio_ffmpeg.get_ffmpeg_exe()
root=Path(__file__).parent
out=root/'dist/video';out.mkdir(exist_ok=True)
clips=[('hallway',0,5),('bride',1,4),('quinceanera',0,5),('birthday',1,4),('waterfront',0,4)]
def run(args):
    p=subprocess.run([ff,'-hide_banner','-loglevel','error','-y',*args],capture_output=True,text=True)
    if p.returncode: raise RuntimeError(p.stderr)
for variant,w,h in [('desktop',1920,1080),('mobile',720,960)]:
    files=[]
    for i,(name,start,dur) in enumerate(clips):
        path=root/'video-source'/f'edit-{variant}-{i}.mp4';files.append(path)
        # The portrait birthday shot is cropped slightly above centre to retain hair and cake.
        y='(ih-oh)*0.30' if name=='birthday' else '(ih-oh)/2'
        vf=f'scale={w}:{h}:force_original_aspect_ratio=increase,crop={w}:{h}:(iw-ow)/2:{y},setsar=1,fps=24,eq=saturation=0.88:contrast=1.02,format=yuv420p'
        run(['-ss',str(start),'-i',str(root/'video-source'/f'{name}.mp4'),'-t',str(dur),'-an','-vf',vf,'-c:v','libx264','-preset','fast','-crf','21',str(path)])
    inputs=[]
    for f in files: inputs+=['-i',str(f)]
    filters=[];prev='0:v';offset=clips[0][2]-.6
    for i in range(1,len(clips)):
        target=f'v{i}';filters.append(f'[{prev}][{i}:v]xfade=transition=fade:duration=0.6:offset={offset:.1f}[{target}]');prev=target;offset+=clips[i][2]-.6
    run([*inputs,'-filter_complex',';'.join(filters),'-map',f'[{prev}]','-an','-c:v','libx264','-preset','fast','-crf','22','-pix_fmt','yuv420p','-movflags','+faststart',str(out/f'hero-{variant}.mp4')])
    print(variant,(out/f'hero-{variant}.mp4').stat().st_size,flush=True)
run(['-ss','1','-i',str(out/'hero-desktop.mp4'),'-frames:v','1','-q:v','3',str(out/'hero-poster.jpg')])
print('Hero compilation finished: 19.6 seconds, silent, H.264, 24fps')

