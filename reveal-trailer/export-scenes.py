"""Split the rendered assembly into seven frame-accurate editable scene clips."""
from pathlib import Path
import subprocess,json
root=Path(__file__).resolve().parent
src=root/'out/can-i-kick-it-90s-assembly.mp4'
scenes=[('01-opening',0,8),('02-artists',8,14),('03-battle-insert',22,16),('04-crate-comeback',38,16),('05-mixtape-menus',54,14),('06-encore-victory',68,14),('07-endcard',82,8)]
output=root/'out/scenes';output.mkdir(exist_ok=True)
for name,start,duration in scenes:
    target=output/(name+'.mp4')
    subprocess.run(['ffmpeg','-hide_banner','-loglevel','error','-y','-ss',str(start),'-i',str(src),'-t',str(duration),'-an','-c:v','libx264','-preset','fast','-crf','18','-pix_fmt','yuv420p','-threads','2','-movflags','+faststart',str(target)],check=True)
    meta=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_entries','stream=width,height,r_frame_rate,nb_frames:format=duration','-of','json',str(target)]))
    assert abs(float(meta['format']['duration'])-duration)<.04,meta
    assert int(meta['streams'][0]['nb_frames'])==duration*30,meta
    print(name,meta,flush=True)
