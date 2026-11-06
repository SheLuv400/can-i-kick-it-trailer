import {Sequence,useVideoConfig} from 'remotion';
import {Base,Plate,Atmosphere,Title,Insert,Flash} from '../design';
import {assets} from '../assets';
export const Comeback=()=>{const {fps}=useVideoConfig();return <Base><Sequence durationInFrames={120} premountFor={fps}><Plate src="crate.png" zoom={.18}/><Title size={108} top={160}>DIG DEEP.</Title><Atmosphere/><Flash/></Sequence><Sequence from={120} durationInFrames={360} premountFor={fps}><Insert src={assets.comeback} name="THE COMEBACK" range="00:42–00:54" cue="Mystery card → Backstage knockout → dramatic revival"/></Sequence></Base>};
