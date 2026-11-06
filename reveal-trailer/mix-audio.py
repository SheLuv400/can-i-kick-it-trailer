"""Mix supplied recordings only. Run from the project root after editing the manifest."""
import json, pathlib, subprocess
root=pathlib.Path(__file__).resolve().parent
cues=json.loads((root/'audio-manifest.json').read_text())
missing=sorted({c['file'] for c in cues if not (root/'public/audio'/c['file']).is_file()})
if missing:
    raise SystemExit('Supply original audio or edit audio-manifest.json. Missing: '+', '.join(missing))
if not cues:
    raise SystemExit('The audio manifest is empty.')
args=['ffmpeg','-y','-v','error']; filters=[]
voices=[c for c in cues if c['kind']=='voice']
for i,c in enumerate(cues):
    args+=['-i',str(root/'public/audio'/c['file'])]
    duration=c['duration']; start=c['start']; gain=c['gain']
    duck=''
    if c['kind']=='music':
        intervals=[f'between(t,{max(0,v["start"]-start)},{min(duration,v["start"]+v["duration"]-start)})' for v in voices if v['start']<start+duration and v['start']+v['duration']>start]
        if intervals: duck=",volume='if("+'+'.join(intervals)+",0.45,1)':eval=frame"
    filters.append(f'[{i}:a]atrim=start={c["source"]}:duration={duration},asetpts=PTS-STARTPTS,aformat=sample_rates=48000:channel_layouts=stereo,volume={gain}{duck},afade=t=in:d=0.02,afade=t=out:st={max(0,duration-.12)}:d=0.12,adelay={round(start*1000)}:all=1[a{i}]')
filters.append(''.join(f'[a{i}]' for i in range(len(cues)))+f'amix=inputs={len(cues)}:normalize=0,alimiter=limit=0.89:level=0,apad,atrim=duration=90[out]')
args+=['-filter_complex',';'.join(filters),'-map','[out]','-c:a','pcm_s24le',str(root/'public/audio/trailer-mix.wav')]
subprocess.run(args,check=True)
print('Created public/audio/trailer-mix.wav. Audition the mix and set assets.soundtrack.')
