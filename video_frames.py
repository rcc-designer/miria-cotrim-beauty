from pathlib import Path
import sys,subprocess
sys.path.insert(0,str(Path(__file__).parent/'.tools'))
import imageio_ffmpeg
ff=imageio_ffmpeg.get_ffmpeg_exe()
root=Path(__file__).parent
for name in ['bride','quinceanera','birthday','waterfront']:
    subprocess.run([ff,'-y','-ss','1','-i',str(root/'video-source'/f'{name}.mp4'),'-frames:v','1','-vf','scale=600:-1',str(root/'video-source'/f'{name}.jpg')],capture_output=True,check=True)
print('Four representative frames extracted')
